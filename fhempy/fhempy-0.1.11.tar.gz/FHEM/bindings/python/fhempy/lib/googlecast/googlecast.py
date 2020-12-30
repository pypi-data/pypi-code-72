import asyncio
import aiohttp
import time
import functools
import concurrent.futures
import logging
import threading
import urllib.request
from urllib.parse import urlparse
from urllib.parse import parse_qs
from .. import utils
from .. import fhem


# PyChromecast
import pychromecast
from pychromecast.error import ChromecastConnectionError

# YouTube
from pychromecast.controllers.youtube import YouTubeController

# DashCast
import pychromecast.controllers.dashcast as dashcast

# Spotify
from pychromecast.controllers.spotify import SpotifyController
import spotipy
import spotify_token as st

# youtube_dl
import youtube_dl

from ..generic import FhemModule

connection_update_lock = threading.Lock()


class googlecast(FhemModule):
    def __init__(self, logger):
        super().__init__(logger)
        # do only error logging for pychromecast library
        logging.getLogger("pychromecast").setLevel(logging.ERROR)
        self.cast = None
        self.loop = asyncio.get_running_loop()
        self.hash = None
        self.currPosTask = None
        self.connectionStateCache = ""
        self.browser = None
        attr_conf = {
            "favorite_1": {"default": ""},
            "favorite_2": {"default": ""},
            "favorite_3": {"default": ""},
            "favorite_4": {"default": ""},
            "favorite_5": {"default": ""},
            "spotify_sp_dc": {
                "default": "",
                "help": "Go to chrome://settings/cookies/detail?site=spotify.com and copy the content of sp_dc",
                "function": "set_attr_spotify_cookie",
            },
            "spotify_sp_key": {
                "default": "",
                "help": "Go to chrome://settings/cookies/detail?site=spotify.com and copy the content of sp_key",
                "function": "set_attr_spotify_cookie",
            },
        }
        self.set_attr_config(attr_conf)

        set_conf = {
            "stop": {},
            "pause": {},
            "rewind": {},
            "skip": {},
            "quitApp": {},
            "play": {
                "args": ["url"],
                "argsh": ["url"],
                "params": {"url": {"optional": True, "default": ""}},
            },
            "addToQueue": {
                "args": ["url"],
                "argsh": ["url"],
                "params": {"url": {"default": ""}},
            },
            "playFavorite": {"args": ["id"], "options": "1,2,3,4,5"},
            "volume": {
                "args": ["vol"],
                "params": {"vol": {"format": "int"}},
                "options": "slider,0,1,100",
            },
            "seek": {"args": ["pos"]},
            "next": {},
            "prev": {},
            "subtitles": {"args": ["onoff"], "options": "on,off"},
            "displayWebsite": {
                "args": ["url"],
                "argsh": ["url"],
                "params": {"url": {"optional": True, "default": "https://www.fhem.de"}},
            },
            "speak": {
                "args": ["text"],
                "help": "Please provide text with quotes.",
            },
            "startApp": {"args": ["appid"]},
            "startSpotify": {},
            "volUp": {},
            "volDown": {},
        }
        self.set_set_config(set_conf)

    # FHEM FUNCTION
    async def Define(self, hash, args, argsh):
        await super().Define(hash, args, argsh)
        if len(args) > 3:
            hash["CASTNAME"] = args[3]
        self.hash = hash

        if self.browser:
            pychromecast.stop_discovery(self.browser)
        if self.cast:
            self.cast.disconnect()

        await fhem.readingsBeginUpdate(hash)
        await fhem.readingsBulkUpdateIfChanged(hash, "state", "offline")
        await fhem.readingsBulkUpdateIfChanged(hash, "connection", "disconnected")
        await fhem.readingsEndUpdate(hash, 1)

        self.startDiscovery()

        return ""

    # FHEM FUNCTION
    async def Undefine(self, hash):
        await super().Undefine(hash)
        try:
            pychromecast.stop_discovery(self.browser)
            if self.cast:
                self.cast.disconnect()
        except:
            pass

    # FHEM FUNCTION
    async def Set(self, hash, args, argsh):
        if self.connectionStateCache != "CONNECTED":
            return "Please wait until connected..."
        return await super().Set(hash, args, argsh)

    async def set_play(self, hash, params):
        url = params["url"]
        if url != "":
            self.playUrl(url)
        else:
            self.cast.media_controller.play()

    async def set_addToQueue(self, hash, params):
        url = params["url"]
        if url != "":
            self.queueUrl(url)

    async def set_playFavorite(self, hash, params):
        fav = params["id"]
        url = await fhem.AttrVal(self.hash["NAME"], "favorite_" + str(id), "")
        if len(url) == 0:
            return "Please set favorite before usage"
        self.playUrl(url)

    async def set_stop(self, hash):
        self.cast.media_controller.stop()

    async def set_pause(self, hash):
        self.cast.media_controller.pause()

    async def set_quitApp(self, hash):
        self.cast.quit_app()

    async def set_startApp(self, hash, params):
        appId = params["appid"]
        self.cast.start_app(appId)

    async def set_skip(self, hash):
        self.cast.media_controller.skip()

    async def set_rewind(self, hash):
        self.cast.media_controller.rewind()

    async def set_seek(self, hash, params):
        position = params["pos"]
        self.cast.media_controller.seek(position)

    async def set_next(self, hash):
        self.cast.media_controller.queue_next()

    async def set_prev(self, hash):
        self.cast.media_controller.queue_prev()

    async def set_volUp(self, hash):
        self.cast.volume_up()

    async def set_volDown(self, hash):
        self.cast.volume_down()

    async def set_subtitles(self, hash, params):
        onoff = params["onoff"]
        if onoff == "on":
            self.cast.media_controller.enable_subtitle(1)
        else:
            self.cast.media_controller.disable_subtitle()

    async def set_volume(self, hash, params):
        vol = params["vol"]
        self.cast.set_volume(vol / 100)

    async def set_speak(self, hash, params):
        txt = params["text"]
        ttsUrl = (
            "http://translate.google.com/translate_tts?tl=de&client=tw-ob&q="
            + urllib.parse.quote(txt)
        )
        self.cast.play_media(ttsUrl, "audio/mpeg")

    async def set_displayWebsite(self, hash, params):
        dashUrl = params["url"]
        self.create_async_task(self.displayWebsite(dashUrl))

    async def set_startSpotify(self, hash):
        self.create_async_task(self.launchSpotify())

    def playUrl(self, url):
        videoid = self.extract_video_id(url)
        if videoid == None:
            if url.find("spotify") >= 0:
                self.create_async_task(self.playSpotify(url))
            else:
                self.create_async_task(self.playDefaultMedia(url))
        else:
            if self.cast.cast_type == "audio":
                self.create_async_task(self.playYoutubeAudio(url))
            else:
                playlistid = self.extract_playlist_id(url)
                self.create_async_task(self.playYoutube(videoid, playlistid))

    def queueUrl(self, url):
        self.create_async_task(self.playDefaultMedia(url, enqueue=True))

    async def playDefaultMedia(self, uri, enqueue=False):
        try:
            session = aiohttp.ClientSession()
            res = await session.get(uri)
            mime = res.headers["Content-Type"]
            self.cast.play_media(uri, mime, enqueue=enqueue)
        except:
            self.logger.exception(f"Failed to play: {uri}")

    async def set_attr_spotify_cookie(self, hash):
        if self._attr_spotify_sp_dc != "" and self._attr_spotify_sp_key != "":
            data = st.start_session(self._attr_spotify_sp_dc, self._attr_spotify_sp_key)
            self.spotify_access_token = data[0]
            self.spotify_expires = data[1] - int(time.time())
            self.spotify = spotipy.Spotify(auth=self.spotify_access_token)

            user = await utils.run_blocking(
                functools.partial(self.spotify.current_user)
            )
            if user is not None:
                await fhem.readingsSingleUpdate(
                    self.hash,
                    "spotify_user",
                    user["display_name"] + " (" + user["email"] + ")",
                    1,
                )
            else:
                await fhem.readingsSingleUpdate(
                    self.hash, "spotify_user", "login failed", 1
                )
        else:
            await fhem.readingsSingleUpdate(
                self.hash, "spotify_user", "attr spotify_sp... required", 1
            )

    async def launchSpotify(self):
        if self.spotify_access_token is None:
            await fhem.readingsSingleUpdate(
                self.hash, "spotify_user", "attr spotify sp... required", 1
            )
            return

        # Launch the spotify app on the cast we want to cast to
        sp = SpotifyController(self.spotify_access_token, self.spotify_expires)
        self.cast.register_handler(sp)
        await utils.run_blocking(functools.partial(sp.launch_app))

    async def playSpotify(self, uri):
        if self.spotify_access_token is None:
            await fhem.readingsSingleUpdate(
                self.hash, "spotify_user", "attr spotify sp... required", 1
            )
            return

        try:
            # Launch the spotify app on the cast we want to cast to
            sp = SpotifyController(self.spotify_access_token, self.spotify_expires)
            self.cast.register_handler(sp)
            await utils.run_blocking(functools.partial(sp.launch_app))

            if not sp.is_launched and not sp.credential_error:
                self.logger.error("Failed to launch spotify controller due to timeout")
                return
            if not sp.is_launched and sp.credential_error:
                self.logger.error(
                    "Failed to launch spotify controller due to credential error"
                )
                return

            # Query spotify for active devices
            devices_available = await utils.run_blocking(
                functools.partial(self.spotify.devices)
            )

            # Match active spotify devices with the spotify controller's device id
            spotify_device_id = None
            for device in devices_available["devices"]:
                if device["id"] == sp.device:
                    spotify_device_id = device["id"]
                    break

            if not spotify_device_id:
                self.logger.error(
                    'No device with id "{}" known by Spotify'.format(sp.device)
                )
                self.logger.error(
                    "Known devices: {}".format(devices_available["devices"])
                )
                return

            # Start playback
            if uri.find("track") > 0:
                await utils.run_blocking(
                    functools.partial(
                        self.spotify.start_playback,
                        device_id=spotify_device_id,
                        uris=[uri],
                    )
                )
            else:
                await utils.run_blocking(
                    functools.partial(
                        self.spotify.start_playback,
                        device_id=spotify_device_id,
                        context_uri=uri,
                    )
                )
        except:
            self.logger.exception("Failed to play spotify track")

    async def displayWebsite(self, url):
        d = dashcast.DashCastController()
        self.cast.register_handler(d)
        d.load_url(url, force=True, reload_seconds=30)

    async def playYoutubeAudio(self, uri):
        with concurrent.futures.ThreadPoolExecutor() as pool:
            video_url = await self.loop.run_in_executor(
                pool, functools.partial(self.getYoutubeAudioUrl, uri)
            )
            self.cast.play_media(video_url, "audio/mp4")

    def getYoutubeAudioUrl(self, uri):
        ydl = youtube_dl.YoutubeDL(
            {
                "forceurl": True,
                "simulate": True,
                "quiet": "1",
                "no_warnings": "1",
                "skip_download": True,
                "format": "bestaudio/best",
                "youtube_include_dash_manifest": True,
            }
        )
        result = ydl.extract_info(uri, download=False)
        if "entries" in result:
            # Can be a playlist or a list of videos
            video = result["entries"][0]
        else:
            # Just a video
            video = result
        video_url = video["url"]
        return video_url

    async def playYoutube(self, videoid, playlistid):
        yt = YouTubeController()
        self.cast.register_handler(yt)
        await utils.run_blocking(functools.partial(yt.play_video, videoid, playlistid))

    def extract_video_id(self, url):
        # Examples:
        # - http://youtu.be/SA2iWivDJiE
        # - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        # - http://www.youtube.com/embed/SA2iWivDJiE
        # - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        query = urlparse(url)
        if query.hostname == "youtu.be":
            return query.path[1:]
        if query.hostname in ("www.youtube.com", "youtube.com"):
            if query.path == "/watch":
                return parse_qs(query.query)["v"][0]
            if query.path[:7] == "/embed/":
                return query.path.split("/")[2]
            if query.path[:3] == "/v/":
                return query.path.split("/")[2]
        # fail?
        return None

    def extract_playlist_id(self, url):
        query = urlparse(url)
        if "list" in parse_qs(query.query):
            return parse_qs(query.query)["list"]
        return None

    def startDiscovery(self):
        def castFound(chromecast):
            if chromecast.name == self.hash["CASTNAME"] and self.cast is None:
                self.logger.info("Discovered cast: " + chromecast.name)
                self.cast = chromecast
                # add status listener
                self.cast.register_connection_listener(self)
                self.cast.register_status_listener(self)
                # add media controller listener
                self.cast.media_controller.register_status_listener(self)
                self.logger.debug("wait for chromecast")
                # timeout 0.001 just waits for status to be ready
                # but we just need the thread to start by calling wait()
                self.cast.wait(0.001)
                self.logger.debug("wait finished")

        self.logger.debug("Start discovery")
        self.browser = pychromecast.get_chromecasts(
            blocking=False, tries=None, retry_wait=5, timeout=5, callback=castFound
        )

    # THREADING: this function is called by run_once pychromecast thread
    def new_connection_status(self, status):
        # connection update might come from different threads
        connection_update_lock.acquire()
        self.logger.debug("new_connection_status: " + status.status)

        # prevent to many disconnect events
        if status.status != self.connectionStateCache:
            self.connectionStateCache = status.status
            # run reading updates in main thread
            res = asyncio.run_coroutine_threadsafe(
                self.updateConnectionReadings(self.hash, status), self.loop
            )
            res.result()

        if status.status == "CONNECTED":
            # run reading updates in main thread
            res = asyncio.run_coroutine_threadsafe(
                self.updateDeviceReadings(self.hash), self.loop
            )
            res.result()
        connection_update_lock.release()

    # THREADING: this function is called by run_once pychromecast thread
    def new_cast_status(self, status):
        self.logger.debug("new_cast_status")
        # run reading updates in main thread
        res = asyncio.run_coroutine_threadsafe(
            self.updateStatusReadings(self.hash, status), self.loop
        )
        res.result()

    # THREADING: this function is called by run_once pychromecast thread
    def new_media_status(self, status):
        asyncio.run_coroutine_threadsafe(
            self.stop_updateCurrentPosition(), self.loop
        ).result()
        if (
            status.player_state == "PLAYING"
            and self.currPosTask == None
            and status.duration
            and status.duration > 0
        ):
            asyncio.run_coroutine_threadsafe(
                self.run_updateCurrentPosition(), self.loop
            ).result()
        self.logger.debug("new_media_status")
        # run reading updates in main thread
        res = asyncio.run_coroutine_threadsafe(
            self.updateMediaStatusReadings(self.hash, status), self.loop
        )
        res.result()

    async def run_updateCurrentPosition(self):
        self.currPosTask = self.create_async_task(self.updateCurrentPosition())

    async def stop_updateCurrentPosition(self):
        if self.currPosTask:
            self.cancel_async_task(self.currPosTask)
            self.currPosTask = None

    async def updateCurrentPosition(self):
        try:
            while True:
                await asyncio.sleep(30)
                self.cast.media_controller.update_status()
        except concurrent.futures.CancelledError:
            # task was cancelled, nothing playing
            pass
        except Exception:
            self.logger.error("Update media status failed", exc_info=True)

    async def updateConnectionReadings(self, hash, status):
        self.logger.debug("updateConnectionReading")
        await fhem.readingsBeginUpdate(hash)
        await fhem.readingsBulkUpdateIfChanged(
            hash, "connection", status.status.lower()
        )
        if status.status == "CONNECTED":
            await fhem.readingsBulkUpdateIfChanged(hash, "state", "online")
        else:
            await fhem.readingsBulkUpdateIfChanged(hash, "state", "offline")
        await fhem.readingsEndUpdate(hash, 1)

    async def updateStatusReadings(self, hash, status):
        self.logger.debug("updateStatusReadings")
        await fhem.readingsBeginUpdate(hash)
        await fhem.readingsBulkUpdateIfChanged(
            hash, "volume", round(status.volume_level * 100)
        )
        await fhem.readingsBulkUpdateIfChanged(
            hash, "is_active_input", status.is_active_input
        )
        await fhem.readingsBulkUpdateIfChanged(hash, "is_stand_by", status.is_stand_by)
        await fhem.readingsBulkUpdateIfChanged(hash, "mute", status.volume_muted)
        await fhem.readingsBulkUpdateIfChanged(
            hash, "display_name", status.display_name
        )
        # await fhem.readingsBulkUpdateIfChanged(hash, "namespaces", status.namespaces)
        await fhem.readingsBulkUpdateIfChanged(hash, "session_id", status.session_id)
        await fhem.readingsBulkUpdateIfChanged(
            hash, "transport_id", status.transport_id
        )
        await fhem.readingsBulkUpdateIfChanged(hash, "status_text", status.status_text)
        await fhem.readingsBulkUpdateIfChanged(hash, "icon_url", status.icon_url)
        await fhem.readingsBulkUpdateIfChanged(hash, "app_id", status.app_id)
        await fhem.readingsEndUpdate(hash, 1)

    async def updateMediaStatusReadings(self, hash, status):
        self.logger.debug("updateMediaStatusReadings")
        await fhem.readingsBeginUpdate(hash)
        await fhem.readingsBulkUpdateIfChanged(
            hash, "mediaPlayerState", status.player_state
        )
        await fhem.readingsBulkUpdateIfChanged(
            hash, "mediaContentId", status.content_id
        )
        await fhem.readingsBulkUpdateIfChanged(
            hash, "mediaContentType", status.content_type
        )
        await fhem.readingsBulkUpdateIfChanged(hash, "mediaDuration", status.duration)
        if status.current_time:
            await fhem.readingsBulkUpdateIfChanged(
                hash, "mediaCurrentPosition", round(status.current_time)
            )
        else:
            await fhem.readingsBulkUpdateIfChanged(hash, "mediaCurrentPosition", "")
        if status.duration and status.current_time:
            await fhem.readingsBulkUpdateIfChanged(
                hash,
                "mediaCurrentPosPercent",
                round(status.current_time / status.duration * 100),
            )
        else:
            await fhem.readingsBulkUpdateIfChanged(hash, "mediaCurrentPosPercent", "")
        await fhem.readingsBulkUpdateIfChanged(
            hash, "mediaStreamType", status.stream_type
        )
        await fhem.readingsBulkUpdateIfChanged(hash, "mediaTitle", status.title)
        await fhem.readingsBulkUpdateIfChanged(
            hash, "mediaSeriesTitle", status.series_title
        )
        await fhem.readingsBulkUpdateIfChanged(hash, "mediaSeason", status.season)
        await fhem.readingsBulkUpdateIfChanged(hash, "mediaEpisode", status.episode)
        await fhem.readingsBulkUpdateIfChanged(hash, "mediaArtist", status.artist)
        await fhem.readingsBulkUpdateIfChanged(hash, "mediaAlbum", status.album_name)
        await fhem.readingsBulkUpdateIfChanged(
            hash, "mediaAlbumArtist", status.album_artist
        )
        await fhem.readingsBulkUpdateIfChanged(hash, "mediaTrack", status.track)
        if len(status.images) > 0:
            await fhem.readingsBulkUpdateIfChanged(
                hash, "mediaImageUrl", status.images[0].url
            )
            await fhem.readingsBulkUpdateIfChanged(
                hash, "mediaImageHeight", status.images[0].height
            )
            await fhem.readingsBulkUpdateIfChanged(
                hash, "mediaImageWidth", status.images[0].width
            )
        else:
            await fhem.readingsBulkUpdateIfChanged(hash, "mediaImageUrl", "")
            await fhem.readingsBulkUpdateIfChanged(hash, "mediaImageHeight", "")
            await fhem.readingsBulkUpdateIfChanged(hash, "mediaImageWidth", "")

        if status.player_state == "PLAYING":
            await fhem.readingsBulkUpdateIfChanged(hash, "state", "playing")
        elif status.player_state == "BUFFERING":
            await fhem.readingsBulkUpdateIfChanged(hash, "state", "buffering")
        elif status.player_state == "PAUSED":
            await fhem.readingsBulkUpdateIfChanged(hash, "state", "paused")
        else:
            if (
                await fhem.ReadingsVal(hash["NAME"], "connection", "failed")
                == "connected"
            ):
                await fhem.readingsBulkUpdateIfChanged(hash, "state", "online")
            else:
                await fhem.readingsBulkUpdateIfChanged(hash, "state", "offline")
        await fhem.readingsEndUpdate(hash, 1)

    async def updateDeviceReadings(self, hash):
        self.logger.debug("updateDeviceReadings")
        await fhem.readingsBeginUpdate(hash)
        await fhem.readingsBulkUpdateIfChanged(hash, "name", self.cast.name)
        await fhem.readingsBulkUpdateIfChanged(hash, "model_name", self.cast.model_name)
        await fhem.readingsBulkUpdateIfChanged(hash, "uuid", self.cast.uuid)
        await fhem.readingsBulkUpdateIfChanged(hash, "cast_type", self.cast.cast_type)
        # await fhem.readingsBulkUpdateIfChanged(hash, "uri", self.cast.uri)
        await fhem.readingsBulkUpdateIfChanged(hash, "ignore_cec", self.cast.ignore_cec)
        await fhem.readingsEndUpdate(hash, 1)

        if await fhem.AttrVal(hash["NAME"], "icon", "") == "":
            if await fhem.ReadingsVal(hash["NAME"], "cast_type", "cast") == "cast":
                await fhem.CommandAttr(
                    self.hash, self.hash["NAME"] + " icon scene_scene"
                )
            else:
                await fhem.CommandAttr(
                    self.hash, self.hash["NAME"] + " icon gassistant"
                )
            await fhem.CommandAttr(
                hash, self.hash["NAME"] + " cmdIcon pause:rc_PAUSE play:rc_PLAY"
            )
            await fhem.CommandAttr(
                hash, self.hash["NAME"] + " webCmd volume:play:pause"
            )

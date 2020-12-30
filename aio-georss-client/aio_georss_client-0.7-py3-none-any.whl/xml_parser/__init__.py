"""XML Parser."""
import logging
from typing import Dict, Optional

import dateparser as dateparser
import xmltodict

from aio_georss_client.consts import (
    XML_TAG_CHANNEL,
    XML_TAG_DC_DATE,
    XML_TAG_FEED,
    XML_TAG_GDACS_BBOX,
    XML_TAG_GEO_LAT,
    XML_TAG_GEO_LONG,
    XML_TAG_GEORSS_POINT,
    XML_TAG_GEORSS_POLYGON,
    XML_TAG_GML_POS,
    XML_TAG_GML_POS_LIST,
    XML_TAG_HEIGHT,
    XML_TAG_LAST_BUILD_DATE,
    XML_TAG_PUB_DATE,
    XML_TAG_PUBLISHED,
    XML_TAG_RSS,
    XML_TAG_TTL,
    XML_TAG_UPDATED,
    XML_TAG_WIDTH,
)
from aio_georss_client.xml_parser.feed import Feed

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAMESPACES = {
    "http://www.w3.org/2005/Atom": None,
    "http://purl.org/dc/elements/1.1/": "dc",
    "http://www.georss.org/georss": "georss",
    "http://www.w3.org/2003/01/geo/wgs84_pos#": "geo",
    "http://www.w3.org/2003/01/geo/": "geo",
    "http://www.opengis.net/gml": "gml",
    "http://www.gdacs.org": "gdacs",
}
KEYS_DATE = [
    XML_TAG_DC_DATE,
    XML_TAG_LAST_BUILD_DATE,
    XML_TAG_PUB_DATE,
    XML_TAG_PUBLISHED,
    XML_TAG_UPDATED,
]
KEYS_FLOAT = [XML_TAG_GEO_LAT, XML_TAG_GEO_LONG]
KEYS_FLOAT_LIST = [
    XML_TAG_GEORSS_POLYGON,
    XML_TAG_GML_POS_LIST,
    XML_TAG_GML_POS,
    XML_TAG_GEORSS_POINT,
    XML_TAG_GDACS_BBOX,
]
KEYS_INT = [XML_TAG_HEIGHT, XML_TAG_TTL, XML_TAG_WIDTH]


class XmlParser:
    """Built-in XML parser."""

    def __init__(self, additional_namespaces=None):
        """Initialise the XML parser."""
        self._namespaces = DEFAULT_NAMESPACES
        if additional_namespaces:
            self._namespaces.update(additional_namespaces)

    @staticmethod
    def postprocessor(path, key, value):
        """Conduct type conversion for selected keys."""
        try:
            if key in KEYS_DATE and value:
                return key, dateparser.parse(value)
            if key in KEYS_FLOAT and value:
                return key, float(value)
            if key in KEYS_FLOAT_LIST and value:
                point_coordinates = XmlParser._process_coordinates(value)
                # Return tuple of coordinates to make this conversion
                # compatible with parsing multiple tags of the same type and
                # combining all values into a single array.
                # If we just returned an array here, coordinates would be mixed
                # up like: [lat1, lon1, [lat2, lon2], [lat3, lon3]]
                return key, tuple(point_coordinates)
            if key in KEYS_INT and value:
                return key, int(value)
        except (ValueError, TypeError) as error:
            _LOGGER.warning("Unable to process (%s/%s): %s", key, value, error)
        return key, value

    @staticmethod
    def _process_coordinates(value):
        """Turn white-space separated list of numbers into list of floats."""
        coordinate_values = value.split()
        point_coordinates = []
        for i in range(0, len(coordinate_values)):
            point_coordinates.append(float(coordinate_values[i]))
        return point_coordinates

    def parse(self, xml) -> Optional[Feed]:
        """Parse the provided xml."""
        if xml:
            parsed_dict = xmltodict.parse(
                xml,
                process_namespaces=True,
                namespaces=self._namespaces,
                postprocessor=XmlParser.postprocessor,
            )
            if XML_TAG_RSS in parsed_dict:
                return XmlParser._create_feed_from_rss(parsed_dict)
            if XML_TAG_FEED in parsed_dict:
                return XmlParser._create_feed_from_feed(parsed_dict)
        return None

    @staticmethod
    def _create_feed_from_rss(parsed_dict: Dict) -> Optional[Feed]:
        """Create feed from provided RSS data."""
        rss = parsed_dict.get(XML_TAG_RSS)
        if XML_TAG_CHANNEL in rss:
            channel = rss.get(XML_TAG_CHANNEL)
            return Feed(channel)
        else:
            _LOGGER.warning(
                "Invalid structure: %s not followed by %s", XML_TAG_RSS, XML_TAG_CHANNEL
            )
            return None

    @staticmethod
    def _create_feed_from_feed(parsed_dict: Dict) -> Feed:
        """Create feed from provided Feed data."""
        feed_data = parsed_dict.get(XML_TAG_FEED)
        return Feed(feed_data)

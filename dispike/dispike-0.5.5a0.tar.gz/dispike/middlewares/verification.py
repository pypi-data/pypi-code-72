from loguru import logger
from fastapi.responses import JSONResponse, Response
from fastapi import HTTPException
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

import typing

if typing.TYPE_CHECKING:
    from fastapi import FastAPI


class DiscordVerificationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: "FastAPI", *, client_public_key: str):
        super().__init__(app)
        self._client_public_key = client_public_key
        logger.info(f"pub: {self._client_public_key}")
        self._verification_key = VerifyKey(bytes.fromhex(self._client_public_key))

    def verify_request(self, passed_signature: str, timestamp: str, body):
        try:
            message = timestamp.encode() + body
            self._verification_key.verify(message, bytes.fromhex(passed_signature))
            return True, 200
        except BadSignatureError:
            logger.error("bad signature")
            return False, 401
        except Exception:
            logger.exception("exception on verifying request")
            return False, 500

    async def dispatch(
        self,
        request: Request,
        call_next: typing.Callable[[Request], typing.Awaitable[Response]],
    ) -> Response:
        logger.debug("intercepting request.")
        try:
            get_signature = request.headers["X-Signature-Ed25519"]
            get_timestamp = request.headers["X-Signature-Timestamp"]

            # https://github.com/encode/starlette/issues/495
            # this is bugged. calling request body will cause a timeout when the next endpoint tries to .body too
            get_body = await request.body()

            # so we need to store the body in the request state.
            request.state._cached_body = get_body
        except Exception:
            # logger.exception("error getting needed data for verification")
            return JSONResponse(
                status_code=400, content={"error_message": "Incorrect request."}
            )

        _status_bool, _status_code = self.verify_request(
            passed_signature=get_signature, timestamp=get_timestamp, body=get_body
        )
        if _status_bool == True:
            logger.info("approved request. forwarding call")
            _dispatch_request = await call_next(request)
            return _dispatch_request

        return JSONResponse(status_code=_status_code)

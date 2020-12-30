import logging
from typing import *
from .scpi_resource import ScpiResource
from .scpi_type_base import ScpiTypes
from .scpi_types import ScpiEvent
from .scpi_exceptions import ScpiErrorException

logger = logging.getLogger(__name__)


class ScpiDevice(object):
    def __init__(self, resource: ScpiResource, **kwargs) -> None:
        self.resource = resource
        self.transport = resource.transport(resource.address)
        logger.info(f'open [{resource.transport.transport_name}]: {resource.address}')

    def is_open(self):
        return self.transport.is_open

    def close(self) -> None:
        self.transport.close()

    def reset(self) -> None:
        self.transport.reset()

    def execute(self, header: str, param: Optional[ScpiTypes] = None,
                result: Optional[Type[ScpiTypes]] = type(None)) -> ScpiTypes:
        command = header
        resp = None
        response = None

        if param is not None:
            command = ' '.join([header, param.compose()])

        self.transport.writeline(command)

        if result is not type(None):
            response = result.parse(self.transport)
            resp = str(response)

        logger.info(f'exec [{type(param).__name__}] -> [{result.__name__ }]: <{command}> -> ({resp})')
        return response

    def check_error(self) -> Optional[ScpiEvent]:
        """Checks if an error is available in the device's SCPI error queue and returns it. Returns None otherwise"""
        scpi_error = self.execute('SYST:ERR:NEXT?', result=ScpiEvent)
        if scpi_error.code != 0:
            return scpi_error
        return None

    def raise_error(self) -> None:
        """Raise a ScpiErrorException when an scpi error is in the device's SCPI error queue"""
        scpi_error = self.check_error()
        if scpi_error is not None:
            raise ScpiErrorException(scpi_error)

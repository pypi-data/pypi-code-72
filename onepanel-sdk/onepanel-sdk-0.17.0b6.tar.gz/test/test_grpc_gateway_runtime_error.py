# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.grpc_gateway_runtime_error import GrpcGatewayRuntimeError  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestGrpcGatewayRuntimeError(unittest.TestCase):
    """GrpcGatewayRuntimeError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GrpcGatewayRuntimeError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.grpc_gateway_runtime_error.GrpcGatewayRuntimeError()  # noqa: E501
        if include_optional :
            return GrpcGatewayRuntimeError(
                error = '0', 
                code = 56, 
                message = '0', 
                details = [
                    onepanel.core.api.models.google/protobuf/any.google.protobuf.Any(
                        type_url = '0', 
                        value = 'YQ==', )
                    ]
            )
        else :
            return GrpcGatewayRuntimeError(
        )

    def testGrpcGatewayRuntimeError(self):
        """Test GrpcGatewayRuntimeError"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.google_rpc_status import GoogleRpcStatus  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestGoogleRpcStatus(unittest.TestCase):
    """GoogleRpcStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GoogleRpcStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.google_rpc_status.GoogleRpcStatus()  # noqa: E501
        if include_optional :
            return GoogleRpcStatus(
                code = 56, 
                message = '0', 
                details = [
                    onepanel.core.api.models.google/protobuf/any.google.protobuf.Any(
                        type_url = '0', 
                        value = 'YQ==', )
                    ]
            )
        else :
            return GoogleRpcStatus(
        )

    def testGoogleRpcStatus(self):
        """Test GoogleRpcStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

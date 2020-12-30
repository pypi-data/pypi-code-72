# coding: utf-8

"""
    bmlx api-server.

    Documentation of bmlx api-server apis. To find more info about generating spec from source, please refer to https://goswagger.io/use/spec.html  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.get_execution_events_response import GetExecutionEventsResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestGetExecutionEventsResponse(unittest.TestCase):
    """GetExecutionEventsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetExecutionEventsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.get_execution_events_response.GetExecutionEventsResponse()  # noqa: E501
        if include_optional :
            return GetExecutionEventsResponse(
                events = [
                    openapi_client.models.execution_event.ExecutionEvent(
                        artifact_id = 56, 
                        component_run_id = 56, 
                        event_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        execution_type = '0', 
                        id = 56, )
                    ], 
                next_page_token = '0'
            )
        else :
            return GetExecutionEventsResponse(
        )

    def testGetExecutionEventsResponse(self):
        """Test GetExecutionEventsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

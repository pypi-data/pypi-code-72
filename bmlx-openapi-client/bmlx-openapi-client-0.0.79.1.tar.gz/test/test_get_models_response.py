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
from openapi_client.models.get_models_response import GetModelsResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestGetModelsResponse(unittest.TestCase):
    """GetModelsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetModelsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.get_models_response.GetModelsResponse()  # noqa: E501
        if include_optional :
            return GetModelsResponse(
                models = [
                    openapi_client.models.model.Model(
                        artifact_id = 56, 
                        create_time = 56, 
                        experiment_id = 56, 
                        experiment_name = '0', 
                        experiment_run_id = 56, 
                        id = 56, 
                        name = '0', 
                        pipeline_id = 56, 
                        pipeline_name = '0', 
                        pipeline_version_id = 56, 
                        producer_component = '0', 
                        status = 'Unknown', 
                        uri = '0', )
                    ], 
                next_page_token = '0'
            )
        else :
            return GetModelsResponse(
        )

    def testGetModelsResponse(self):
        """Test GetModelsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

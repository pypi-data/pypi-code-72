# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class DescribeProductTopicsRequest(JDCloudRequest):
    """
    查看产品自定义Topic列表
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(DescribeProductTopicsRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/products/{productKey}/topics', 'GET', header, version)
        self.parameters = parameters


class DescribeProductTopicsParameters(object):

    def __init__(self, regionId, instanceId, productKey, ):
        """
        :param regionId: 地域ID
        :param instanceId: IoTCore实例ID信息
        :param productKey: 产品Key
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.productKey = productKey
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞)
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为10，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) topicShortName-topic名称，模糊匹配，支持单个

        """
        self.filters = filters


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


class DescribeBriefInstancesRequest(JDCloudRequest):
    """
    批量查询云主机信息的轻量接口，不返回云盘、网络、计费、标签等信息。如果不需要关联资源属性，尽量选择使用该接口。<br>
此接口支持分页查询，默认每页20条。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeBriefInstancesRequest, self).__init__(
            '/regions/{regionId}/instances:describeBriefInstances', 'POST', header, version)
        self.parameters = parameters


class DescribeBriefInstancesParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.tags = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码；默认为1
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小；默认为20；取值范围[10, 100]
        """
        self.pageSize = pageSize

    def setTags(self, tags):
        """
        :param tags: (Optional) Tag筛选条件
        """
        self.tags = tags

    def setFilters(self, filters):
        """
        :param filters: (Optional) instanceId - 云主机ID，精确匹配，支持多个
privateIpAddress - 主网卡内网主IP地址，模糊匹配，支持多个
az - 可用区，精确匹配，支持多个
vpcId - 私有网络ID，精确匹配，支持多个
status - 云主机状态，精确匹配，支持多个，<a href="http://docs.jdcloud.com/virtual-machines/api/vm_status">参考云主机状态</a>
name - 云主机名称，模糊匹配，支持单个
imageId - 镜像ID，精确匹配，支持多个
networkInterfaceId - 弹性网卡ID，精确匹配，支持多个
subnetId - 子网ID，精确匹配，支持多个
agId - 使用可用组id，支持单个
faultDomain - 错误域，支持多个
dedicatedHostId - 专有宿主机ID，精确匹配，支持多个
dedicatedPoolId - 专有宿主机池ID，精确匹配，支持多个
instanceType - 实例规格，精确匹配，支持多个
elasticIpAddress - 公网IP地址，精确匹配，支持单个

        """
        self.filters = filters


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


class UpdateBackendConfigRequest(JDCloudRequest):
    """
    修改后端配置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateBackendConfigRequest, self).__init__(
            '/regions/{regionId}/apiGroups/{apiGroupId}/backendConfig/{backendConfigId}', 'PATCH', header, version)
        self.parameters = parameters


class UpdateBackendConfigParameters(object):

    def __init__(self, regionId, apiGroupId, backendConfigId, environment, backendServiceType, sort, ):
        """
        :param regionId: 地域ID
        :param apiGroupId: 分组ID
        :param backendConfigId: backendConfigId
        :param environment: 环境：test、preview、online
        :param backendServiceType: 后端服务类型：mock、HTTP/HTTPS
        :param sort: 排序，赋值0时为默认的后端配置
        """

        self.regionId = regionId
        self.apiGroupId = apiGroupId
        self.backendConfigId = backendConfigId
        self.baseGroupId = None
        self.environment = environment
        self.backendUrl = None
        self.backendServiceType = backendServiceType
        self.headerParams = None
        self.queryParams = None
        self.description = None
        self.createTime = None
        self.sort = sort
        self.userSort = None
        self.jdsfId = None
        self.jdsfParam = None
        self.jdsfRegion = None
        self.jdsfPin = None

    def setBaseGroupId(self, baseGroupId):
        """
        :param baseGroupId: (Optional) 分组ID
        """
        self.baseGroupId = baseGroupId

    def setBackendUrl(self, backendUrl):
        """
        :param backendUrl: (Optional) 后端地址
        """
        self.backendUrl = backendUrl

    def setHeaderParams(self, headerParams):
        """
        :param headerParams: (Optional) header参数列表
        """
        self.headerParams = headerParams

    def setQueryParams(self, queryParams):
        """
        :param queryParams: (Optional) query参数列表
        """
        self.queryParams = queryParams

    def setDescription(self, description):
        """
        :param description: (Optional) 描述
        """
        self.description = description

    def setCreateTime(self, createTime):
        """
        :param createTime: (Optional) 发布日期，格式为毫秒级时间戳
        """
        self.createTime = createTime

    def setUserSort(self, userSort):
        """
        :param userSort: (Optional) 排序，用于展示使用
        """
        self.userSort = userSort

    def setJdsfId(self, jdsfId):
        """
        :param jdsfId: (Optional) vpc网关id
        """
        self.jdsfId = jdsfId

    def setJdsfParam(self, jdsfParam):
        """
        :param jdsfParam: (Optional) vpc后端地址
        """
        self.jdsfParam = jdsfParam

    def setJdsfRegion(self, jdsfRegion):
        """
        :param jdsfRegion: (Optional) vpc网关所属region
        """
        self.jdsfRegion = jdsfRegion

    def setJdsfPin(self, jdsfPin):
        """
        :param jdsfPin: (Optional) vpc网关创建者的pin
        """
        self.jdsfPin = jdsfPin


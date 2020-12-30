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


class CreateLogsetRequest(JDCloudRequest):
    """
    创建日志集。名称不可重复。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateLogsetRequest, self).__init__(
            '/regions/{regionId}/logsets', 'POST', header, version)
        self.parameters = parameters


class CreateLogsetParameters(object):

    def __init__(self, regionId, name, lifeCycle):
        """
        :param regionId: 地域 Id
        :param name: 日志集名称
        :param lifeCycle: 保存周期，只能是 7， 15， 30
        """

        self.regionId = regionId
        self.name = name
        self.description = None
        self.lifeCycle = lifeCycle

    def setDescription(self, description):
        """
        :param description: (Optional) 日志集描述
        """
        self.description = description


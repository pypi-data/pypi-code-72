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


class ReplyRequest(JDCloudRequest):
    """
    短信回复接口。 接口调用需要使用京东云统一鉴权的SDK方式接入，以下文档仅是接口出参、入参描述，并不是最终程序实现逻辑的范例，具体接口实现请查看SDK参考：https://docs.jdcloud.com/cn/text-message/java
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ReplyRequest, self).__init__(
            '/regions/{regionId}/reply', 'POST', header, version)
        self.parameters = parameters


class ReplyParameters(object):

    def __init__(self, regionId, appId, dataDate, ):
        """
        :param regionId: Region ID
        :param appId: 应用Id
        :param dataDate: 查询时间
        """

        self.regionId = regionId
        self.appId = appId
        self.dataDate = dataDate
        self.phoneList = None

    def setPhoneList(self, phoneList):
        """
        :param phoneList: (Optional) 手机号列表（选填）
        """
        self.phoneList = phoneList


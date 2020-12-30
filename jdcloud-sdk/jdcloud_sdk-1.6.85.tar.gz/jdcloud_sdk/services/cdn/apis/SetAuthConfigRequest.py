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


class SetAuthConfigRequest(JDCloudRequest):
    """
    dash鉴权设置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(SetAuthConfigRequest, self).__init__(
            '/domain/{domain}/setAuthConfig', 'POST', header, version)
        self.parameters = parameters


class SetAuthConfigParameters(object):

    def __init__(self, domain, ):
        """
        :param domain: 用户域名
        """

        self.domain = domain
        self.enableUrlAuth = None
        self.authKey = None
        self.age = None
        self.encAlgorithm = None
        self.timeFormat = None
        self.uriType = None
        self.rule = None

    def setEnableUrlAuth(self, enableUrlAuth):
        """
        :param enableUrlAuth: (Optional) 是否开启鉴权[on,off]
        """
        self.enableUrlAuth = enableUrlAuth

    def setAuthKey(self, authKey):
        """
        :param authKey: (Optional) 鉴权key
        """
        self.authKey = authKey

    def setAge(self, age):
        """
        :param age: (Optional) 鉴权时间戳过期时间，默认为0
        """
        self.age = age

    def setEncAlgorithm(self, encAlgorithm):
        """
        :param encAlgorithm: (Optional) 鉴权参数加密算法，默认为md5且只支持md5
        """
        self.encAlgorithm = encAlgorithm

    def setTimeFormat(self, timeFormat):
        """
        :param timeFormat: (Optional) 时间戳格式[hex,dec]
        """
        self.timeFormat = timeFormat

    def setUriType(self, uriType):
        """
        :param uriType: (Optional) 加密算法版本[dash,dashv2,video],默认dashv2
        """
        self.uriType = uriType

    def setRule(self, rule):
        """
        :param rule: (Optional) 鉴权key生成顺序
        """
        self.rule = rule


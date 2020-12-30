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


class RiskRuleCfg(object):

    def __init__(self, id=None, wafInstanceId=None, domain=None, name=None, uri=None, action=None, disable=None, updateTime=None):
        """
        :param id: (Optional) 规则id
        :param wafInstanceId: (Optional) WAF实例id
        :param domain: (Optional) 域名
        :param name: (Optional) 规则名称
        :param uri: (Optional) uri 以/开头
        :param action: (Optional) 动作 支持notice / verify@captcha
        :param disable: (Optional) 0-使用中 1-禁用
        :param updateTime: (Optional) 更新时间，s
        """

        self.id = id
        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.name = name
        self.uri = uri
        self.action = action
        self.disable = disable
        self.updateTime = updateTime

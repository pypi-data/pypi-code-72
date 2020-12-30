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


class UpdateCmAlarmSpec(object):

    def __init__(self, aggrType, dimensions, namespace, region, ruleName, ruleOption, baseContact=None, enabled=None, noticeOption=None, webHookOption=None):
        """
        :param aggrType:  聚合方式，多个维度聚合成1个维度时，多维度值之间的聚合方式。可选值:sum、avg、min、max
        :param baseContact: (Optional) 告警通知联系人
        :param dimensions:  资源维度，指定监控数据实例的维度标签,如resourceId=id。(请确认资源的监控数据带有该标签，否则规则会报数据不足)，至少指定一个
        :param enabled: (Optional) 是否启用, 1表示启用规则，0表示禁用规则，默认为1
        :param namespace:  命名空间
        :param noticeOption: (Optional) 通知策略
        :param region:  规则绑定资源所在地域
        :param ruleName:  规则名称，规则名称，最大长度42个字符，只允许中英文、数字、''-''和"_"
        :param ruleOption:  规则的触发条件设置选项
        :param webHookOption: (Optional) 
        """

        self.aggrType = aggrType
        self.baseContact = baseContact
        self.dimensions = dimensions
        self.enabled = enabled
        self.namespace = namespace
        self.noticeOption = noticeOption
        self.region = region
        self.ruleName = ruleName
        self.ruleOption = ruleOption
        self.webHookOption = webHookOption

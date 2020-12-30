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


class DescribeCustomAlarmDetail(object):

    def __init__(self, aggrType=None, alarmId=None, alarmStatus=None, createTime=None, dimensions=None, dimensionsText=None, enabled=None, namespace=None, namespaceName=None, region=None, ruleName=None, ruleOption=None, ruleVersion=None):
        """
        :param aggrType: (Optional) 聚合方式，多个维度聚合成1个维度时，多维度值之间的聚合方式。可选值:sum、avg、min、max
        :param alarmId: (Optional) 报警规则ID
        :param alarmStatus: (Optional) 规则状态，当一个规则下同时存在报警、数据不足、正常的资源时，规则状态按 报警>数据不足>正常的优先级展示
监控项状态：-1 未启用 1正常，2告警，4数据不足
        :param createTime: (Optional) 创建时间
        :param dimensions: (Optional) 资源维度，指定监控数据实例的维度标签,如resourceId=id。(请确认资源的监控数据带有该标签，否则规则会报数据不足)，至少指定一个
        :param dimensionsText: (Optional) 拼接好的资源维度信息
        :param enabled: (Optional) 是否启用, 1表示启用规则，0表示禁用规则，默认为1
        :param namespace: (Optional) 命名空间
        :param namespaceName: (Optional) 命名空间名称
        :param region: (Optional) 规则绑定资源所在地域
        :param ruleName: (Optional) 规则名称
        :param ruleOption: (Optional) 规则的触发条件设置选项
        :param ruleVersion: (Optional) 规则版本  v1  v2
        """

        self.aggrType = aggrType
        self.alarmId = alarmId
        self.alarmStatus = alarmStatus
        self.createTime = createTime
        self.dimensions = dimensions
        self.dimensionsText = dimensionsText
        self.enabled = enabled
        self.namespace = namespace
        self.namespaceName = namespaceName
        self.region = region
        self.ruleName = ruleName
        self.ruleOption = ruleOption
        self.ruleVersion = ruleVersion

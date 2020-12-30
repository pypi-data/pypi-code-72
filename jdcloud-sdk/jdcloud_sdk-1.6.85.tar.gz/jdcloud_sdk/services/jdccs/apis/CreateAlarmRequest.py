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


class CreateAlarmRequest(JDCloudRequest):
    """
    创建报警
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateAlarmRequest, self).__init__(
            '/alarms', 'POST', header, version)
        self.parameters = parameters


class CreateAlarmParameters(object):

    def __init__(self, ):
        """
        """

        self.idc = None
        self.resourceType = None
        self.resourceId = None
        self.name = None
        self.metric = None
        self.period = None
        self.statisticMethod = None
        self.operator = None
        self.threshold = None
        self.times = None
        self.noticePeriod = None
        self.status = None
        self.noticeMethod = None
        self.noticeObj = None
        self.userId = None

    def setIdc(self, idc):
        """
        :param idc: (Optional) idc机房实例ID
        """
        self.idc = idc

    def setResourceType(self, resourceType):
        """
        :param resourceType: (Optional) 资源类型，bandwidth:带宽
        """
        self.resourceType = resourceType

    def setResourceId(self, resourceId):
        """
        :param resourceId: (Optional) 带宽实例ID
        """
        self.resourceId = resourceId

    def setName(self, name):
        """
        :param name: (Optional) 规则名称
        """
        self.name = name

    def setMetric(self, metric):
        """
        :param metric: (Optional) 监控项，bandwidthTrafficIn:上行实时流量 bandwidthTrafficOut:下行实时流量
        """
        self.metric = metric

    def setPeriod(self, period):
        """
        :param period: (Optional) 统计周期（单位：分钟）
        """
        self.period = period

    def setStatisticMethod(self, statisticMethod):
        """
        :param statisticMethod: (Optional) 统计方法：平均值=avg、最大值=max、最小值=min
        """
        self.statisticMethod = statisticMethod

    def setOperator(self, operator):
        """
        :param operator: (Optional) 计算方式 >=、>、<、<=、=、！=
        """
        self.operator = operator

    def setThreshold(self, threshold):
        """
        :param threshold: (Optional) 阈值
        """
        self.threshold = threshold

    def setTimes(self, times):
        """
        :param times: (Optional) 连续多少次后报警
        """
        self.times = times

    def setNoticePeriod(self, noticePeriod):
        """
        :param noticePeriod: (Optional) 通知周期 单位：小时
        """
        self.noticePeriod = noticePeriod

    def setStatus(self, status):
        """
        :param status: (Optional) 规则状态 disabled:禁用 enabled:启用
        """
        self.status = status

    def setNoticeMethod(self, noticeMethod):
        """
        :param noticeMethod: (Optional) 通知方式 all:全部 sms：短信 email:邮件
        """
        self.noticeMethod = noticeMethod

    def setNoticeObj(self, noticeObj):
        """
        :param noticeObj: (Optional) 通知对象 all:全部 persons：个人 groups:角色组
        """
        self.noticeObj = noticeObj

    def setUserId(self, userId):
        """
        :param userId: (Optional) 通知对象用户ID,若多个用逗号分隔
        """
        self.userId = userId


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


class EbsSeperateBillVo(object):

    def __init__(self, pin=None, dataSourceId=None, appCode=None, chargeTime=None, totalFee=None, seperateFee=None, org=None, userGroup=None, traderName=None, orderType=None, costFee=None, taxRate=None, deptNo=None, sourceId=None, code=None, message=None):
        """
        :param pin: (Optional) 用户pin
        :param dataSourceId: (Optional) 数据源ID
        :param appCode: (Optional) 业务线
        :param chargeTime: (Optional) 费用时间
        :param totalFee: (Optional) 总金额
        :param seperateFee: (Optional) 分摊金额
        :param org: (Optional) 核算组织
        :param userGroup: (Optional) 用户分组
        :param traderName: (Optional) 交易方名称
        :param orderType: (Optional) 订单类型
        :param costFee: (Optional) 成本金额
        :param taxRate: (Optional) 税率
        :param deptNo: (Optional) 部门
        :param sourceId: (Optional) 部门
        :param code: (Optional) 返回编码0成功
        :param message: (Optional) 返回消息
        """

        self.pin = pin
        self.dataSourceId = dataSourceId
        self.appCode = appCode
        self.chargeTime = chargeTime
        self.totalFee = totalFee
        self.seperateFee = seperateFee
        self.org = org
        self.userGroup = userGroup
        self.traderName = traderName
        self.orderType = orderType
        self.costFee = costFee
        self.taxRate = taxRate
        self.deptNo = deptNo
        self.sourceId = sourceId
        self.code = code
        self.message = message

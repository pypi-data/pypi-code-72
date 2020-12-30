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


class OffLineRemittanceBillInfo(object):

    def __init__(self, id=None, pin=None, remittorAccount=None, remittorBankAccount=None, remitAmount=None, remitBankName=None, remitTime=None, contactsPhone=None, status=None, remitPicture=None, createTime=None, updateTime=None, claId=None, erpOrderId=None, createBeginTime=None, createEndTime=None):
        """
        :param id: (Optional) 当前id
        :param pin: (Optional) 用户pin
        :param remittorAccount: (Optional) 汇款人账号名称
        :param remittorBankAccount: (Optional) 汇款人银行账号
        :param remitAmount: (Optional) 汇款金额
        :param remitBankName: (Optional) 汇款银行名称
        :param remitTime: (Optional) 汇款时间
        :param contactsPhone: (Optional) 联系人手机
        :param status: (Optional) 状态
        :param remitPicture: (Optional) 汇款底单扫描件
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param claId: (Optional) 备查id
        :param erpOrderId: (Optional) 充值单号
        :param createBeginTime: (Optional) 提交起始时间
        :param createEndTime: (Optional) 提交截止时间
        """

        self.id = id
        self.pin = pin
        self.remittorAccount = remittorAccount
        self.remittorBankAccount = remittorBankAccount
        self.remitAmount = remitAmount
        self.remitBankName = remitBankName
        self.remitTime = remitTime
        self.contactsPhone = contactsPhone
        self.status = status
        self.remitPicture = remitPicture
        self.createTime = createTime
        self.updateTime = updateTime
        self.claId = claId
        self.erpOrderId = erpOrderId
        self.createBeginTime = createBeginTime
        self.createEndTime = createEndTime

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


class NatGatewaySpec(object):

    def __init__(self, natGatewayName, vpcId, subnetId, azIpSpecs, natGatewaySpec=None, natGatewayCharge=None, description=None):
        """
        :param natGatewayName:  NAT网关名称
        :param natGatewaySpec: (Optional) NAT网关规格，取值small（100万并发连接数），medium（300万并发连接数），large（1000万并发连接数），默认small
        :param vpcId:  私有网络ID
        :param subnetId:  子网ID
        :param azIpSpecs:  NAT网关的可用区属性，目前仅支持一个
        :param natGatewayCharge: (Optional) 计费配置，仅支持按配置，默认按配置
        :param description: (Optional) 描述,​ 允许输入UTF-8编码下的全部字符，不超过256字符
        """

        self.natGatewayName = natGatewayName
        self.natGatewaySpec = natGatewaySpec
        self.vpcId = vpcId
        self.subnetId = subnetId
        self.azIpSpecs = azIpSpecs
        self.natGatewayCharge = natGatewayCharge
        self.description = description

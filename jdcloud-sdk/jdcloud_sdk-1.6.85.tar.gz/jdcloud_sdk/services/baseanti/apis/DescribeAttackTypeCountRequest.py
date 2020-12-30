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


class DescribeAttackTypeCountRequest(JDCloudRequest):
    """
    查询各类型攻击次数
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAttackTypeCountRequest, self).__init__(
            '/describeAttackTypeCount', 'GET', header, version)
        self.parameters = parameters


class DescribeAttackTypeCountParameters(object):

    def __init__(self, startTime, endTime, ):
        """
        :param startTime: 开始时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ
        :param endTime: 结束时间, UTC 时间, 格式: yyyy-MM-dd'T'HH:mm:ssZ
        """

        self.startTime = startTime
        self.endTime = endTime
        self.ip = None

    def setIp(self, ip):
        """
        :param ip: (Optional) 基础防护已防护的公网 IP, ip 不为空时, 查询 ip 对应的各类型攻击次数, ip 为空时, 查询用户所有公网 IP 的各类型攻击次数. <br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources'>describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP. <br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources'>describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网IP 和 弹性公网 IP. <br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeccsipresources'>describeCcsIpResources</a> 接口查询基础防护已防护的托管区公网 IP
        """
        self.ip = ip


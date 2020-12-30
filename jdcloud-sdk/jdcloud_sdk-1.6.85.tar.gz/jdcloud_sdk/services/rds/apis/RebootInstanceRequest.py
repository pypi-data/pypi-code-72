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


class RebootInstanceRequest(JDCloudRequest):
    """
    重启RDS实例，例如修改了一些配置参数后，需要重启实例才能生效。可以结合主备切换的功能，轮流重启备机，降低对业务的影响<br>**注意：如果实例正在进行备份，那么重启主实例将会终止备份操作。** 可以查看备份策略中的备份开始时间确认是否有备份正在运行。如果确实需要在实例备份时重启主实例，建议重启后，手工进行一次实例的全备。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(RebootInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:rebootInstance', 'POST', header, version)
        self.parameters = parameters


class RebootInstanceParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.rebootMaster = None
        self.rebootSlave = None

    def setRebootMaster(self, rebootMaster):
        """
        :param rebootMaster: (Optional) 是否重启主节点。<br> - 仅SQL Server 支持该参数
        """
        self.rebootMaster = rebootMaster

    def setRebootSlave(self, rebootSlave):
        """
        :param rebootSlave: (Optional) 是否重启备节点。<br> - 仅SQL Server 支持该参数
        """
        self.rebootSlave = rebootSlave


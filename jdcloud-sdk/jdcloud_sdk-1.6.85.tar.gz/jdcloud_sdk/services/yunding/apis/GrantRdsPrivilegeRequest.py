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


class GrantRdsPrivilegeRequest(JDCloudRequest):
    """
    授予账号的数据库访问权限，即该账号对数据库拥有什么权限。一个账号可以对多个数据库具有访问权限。<br>为便于管理，RDS对权限进行了归类，目前提供以下两种权限<br>- ro：只读权限，用户只能读取数据库中的数据，不能进行创建、插入、删除、更改等操作。<br>- rw：读写权限，用户可以对数据库进行增删改查等操作
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(GrantRdsPrivilegeRequest, self).__init__(
            '/regions/{regionId}/ydRdsInstances/{instanceId}/accounts/{accountName}:grantPrivilege', 'POST', header, version)
        self.parameters = parameters


class GrantRdsPrivilegeParameters(object):

    def __init__(self, regionId, instanceId, accountName, accountPrivileges):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param accountName: 账号名，在同一个实例中账号名不能重复
        :param accountPrivileges: 账号的访问权限
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.accountName = accountName
        self.accountPrivileges = accountPrivileges


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


class EdgePageVo(object):

    def __init__(self, edgeId=None, edgeName=None, edgeState=None, omName=None, lastOnlineTime=None):
        """
        :param edgeId: (Optional) Edge编号
        :param edgeName: (Optional) Edge显示名称
        :param edgeState: (Optional) Edge状态
        :param omName: (Optional) 物模型名称
        :param lastOnlineTime: (Optional) 最后在线时间
        """

        self.edgeId = edgeId
        self.edgeName = edgeName
        self.edgeState = edgeState
        self.omName = omName
        self.lastOnlineTime = lastOnlineTime

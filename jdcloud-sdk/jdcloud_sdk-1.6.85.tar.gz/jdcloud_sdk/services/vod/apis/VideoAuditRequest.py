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


class VideoAuditRequest(JDCloudRequest):
    """
    视频审核
视频在上传中或者转码中不允许更改视频审核状态，即视频只有在正常或屏蔽状态下才可以调用此接口设置审核状态

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(VideoAuditRequest, self).__init__(
            '/videos/{videoId}:audit', 'POST', header, version)
        self.parameters = parameters


class VideoAuditParameters(object):

    def __init__(self, videoId, auditResult):
        """
        :param videoId: 视频ID
        :param auditResult: 审核结果，取值范围:
 block(封禁)
 unblock(解封)

        """

        self.videoId = videoId
        self.auditResult = auditResult


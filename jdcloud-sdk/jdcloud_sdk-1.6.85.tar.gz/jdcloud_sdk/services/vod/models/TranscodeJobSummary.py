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


class TranscodeJobSummary(object):

    def __init__(self, jobId=None, videoId=None, templateIds=None, createTime=None, completeTime=None, tasks=None):
        """
        :param jobId: (Optional) 作业ID
        :param videoId: (Optional) 视频ID
        :param templateIds: (Optional) 模板ID列表
        :param createTime: (Optional) 创建时间
        :param completeTime: (Optional) 完成时间
        :param tasks: (Optional) 
        """

        self.jobId = jobId
        self.videoId = videoId
        self.templateIds = templateIds
        self.createTime = createTime
        self.completeTime = completeTime
        self.tasks = tasks

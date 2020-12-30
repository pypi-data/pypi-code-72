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


class ContainerStateTerminated(object):

    def __init__(self, signal=None, exitCode=None, reason=None, message=None, finishedAt=None, startedAt=None):
        """
        :param signal: (Optional) 容器被终止的信号。
        :param exitCode: (Optional) 容器被终止的退出码。
        :param reason: (Optional) （简要）容器被终止的原因。
        :param message: (Optional) 容器被终止的详细信息。
        :param finishedAt: (Optional) 容器被终止的时间。
        :param startedAt: (Optional) 容器开始执行的时间。
        """

        self.signal = signal
        self.exitCode = exitCode
        self.reason = reason
        self.message = message
        self.finishedAt = finishedAt
        self.startedAt = startedAt

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


class UpdateQualityDetectionTemplateRequestObject(object):

    def __init__(self, name=None, detections=None):
        """
        :param name: (Optional) 模板名称。长度不超过128个字符。UTF-8编码。

        :param detections: (Optional) 检测项列表。取值范围：
  blackScreen - 黑场
  pureColor - 纯色
  colorCast - 偏色
  frozenFrame - 静帧
  brightness - 亮度
  contrast - 对比度

        """

        self.name = name
        self.detections = detections

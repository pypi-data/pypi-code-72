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


class ImageInstanceTypeConstraint(object):

    def __init__(self, constraintsType=None, instanceTypes=None):
        """
        :param constraintsType: (Optional) 限制类型。取值：excludes：不支持的实例类型；includes：支持的实例类型。
        :param instanceTypes: (Optional) 实例规格列表
        """

        self.constraintsType = constraintsType
        self.instanceTypes = instanceTypes

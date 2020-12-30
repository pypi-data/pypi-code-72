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


class ImportImageRequest(JDCloudRequest):
    """
    导入镜像，将外部镜像导入到京东云中

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ImportImageRequest, self).__init__(
            '/regions/{regionId}/images:import', 'POST', header, version)
        self.parameters = parameters


class ImportImageParameters(object):

    def __init__(self, regionId, architecture, osType, platform, diskFormat, systemDiskSizeGB, imageUrl, imageName, ):
        """
        :param regionId: 地域ID
        :param architecture: 系统架构，可选值：x86_64,i386
        :param osType: 操作系统，可选值：windows,linux
        :param platform: 平台名称，可选值：CentOS,Ubuntu,Windows Server,Other Linux,Other Windows
        :param diskFormat: 磁盘格式，可选值：qcow2,vhd,vmdk,raw
        :param systemDiskSizeGB: 以此镜像需要制作的系统盘的默认大小，单位GB。最小值40，最大值500，要求值是10的整数倍
        :param imageUrl: 要导入镜像的对象存储外链地址
        :param imageName: 导入镜像的自定义名称
        """

        self.regionId = regionId
        self.architecture = architecture
        self.osType = osType
        self.platform = platform
        self.diskFormat = diskFormat
        self.systemDiskSizeGB = systemDiskSizeGB
        self.imageUrl = imageUrl
        self.osVersion = None
        self.imageName = imageName
        self.description = None
        self.forceImport = None
        self.clientToken = None

    def setOsVersion(self, osVersion):
        """
        :param osVersion: (Optional) 镜像的操作系统版本
        """
        self.osVersion = osVersion

    def setDescription(self, description):
        """
        :param description: (Optional) 导入镜像的描述信息
        """
        self.description = description

    def setForceImport(self, forceImport):
        """
        :param forceImport: (Optional) 是否强制导入。强制导入则忽略镜像的合规性检测
        """
        self.forceImport = forceImport

    def setClientToken(self, clientToken):
        """
        :param clientToken: (Optional) 用户导入镜像的幂等性保证。每次创建请传入不同的值，如果传值与某次的clientToken相同，则返还该次的请求结果
        """
        self.clientToken = clientToken


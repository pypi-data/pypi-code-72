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


class CreateSmsSignUsingPOSTRequest(JDCloudRequest):
    """
    创建短信签名
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateSmsSignUsingPOSTRequest, self).__init__(
            '/smsSigns', 'POST', header, version)
        self.parameters = parameters


class CreateSmsSignUsingPOSTParameters(object):

    def __init__(self, appId, signCertificateUrl, signContent, signPurpose, signTypeId):
        """
        :param appId: 应用id
        :param signCertificateUrl: 证明材料下载地址，上传至 oss
        :param signContent: 若签名内容侵犯到第三方权益必须获得第三方真实授权，长度为 2~12 个字符无须添加【】、()、[] 符号，签名发送会自带【】符号，避免重复
        :param signPurpose: 签名用途，0自用 1他用
        :param signTypeId: 签名类型id，调用listSmsSignTypesUsingGET 接口获取
        """

        self.appId = appId
        self.applyExplanation = None
        self.signAttorneyUrl = None
        self.signCertificateUrl = signCertificateUrl
        self.signContent = signContent
        self.signOtherCertificateUrl = None
        self.signPurpose = signPurpose
        self.signTypeId = signTypeId

    def setApplyExplanation(self, applyExplanation):
        """
        :param applyExplanation: (Optional) 申请说明
        """
        self.applyExplanation = applyExplanation

    def setSignAttorneyUrl(self, signAttorneyUrl):
        """
        :param signAttorneyUrl: (Optional) 授权委托下载地址，若短信签名用途为他用，涉及第三方权益需上传，上传至 oss
        """
        self.signAttorneyUrl = signAttorneyUrl

    def setSignOtherCertificateUrl(self, signOtherCertificateUrl):
        """
        :param signOtherCertificateUrl: (Optional) 其他证明材料下载地址 上传至 oss
        """
        self.signOtherCertificateUrl = signOtherCertificateUrl


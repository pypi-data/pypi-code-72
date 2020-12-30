# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpdateChildAccountStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'transactional_email': 'bool',
        'transactional_sms': 'bool',
        'marketing_automation': 'bool',
        'sms_campaign': 'bool'
    }

    attribute_map = {
        'transactional_email': 'transactionalEmail',
        'transactional_sms': 'transactionalSms',
        'marketing_automation': 'marketingAutomation',
        'sms_campaign': 'smsCampaign'
    }

    def __init__(self, transactional_email=None, transactional_sms=None, marketing_automation=None, sms_campaign=None):  # noqa: E501
        """UpdateChildAccountStatus - a model defined in Swagger"""  # noqa: E501

        self._transactional_email = None
        self._transactional_sms = None
        self._marketing_automation = None
        self._sms_campaign = None
        self.discriminator = None

        if transactional_email is not None:
            self.transactional_email = transactional_email
        if transactional_sms is not None:
            self.transactional_sms = transactional_sms
        if marketing_automation is not None:
            self.marketing_automation = marketing_automation
        if sms_campaign is not None:
            self.sms_campaign = sms_campaign

    @property
    def transactional_email(self):
        """Gets the transactional_email of this UpdateChildAccountStatus.  # noqa: E501

        Status of Transactional Email Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :return: The transactional_email of this UpdateChildAccountStatus.  # noqa: E501
        :rtype: bool
        """
        return self._transactional_email

    @transactional_email.setter
    def transactional_email(self, transactional_email):
        """Sets the transactional_email of this UpdateChildAccountStatus.

        Status of Transactional Email Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :param transactional_email: The transactional_email of this UpdateChildAccountStatus.  # noqa: E501
        :type: bool
        """

        self._transactional_email = transactional_email

    @property
    def transactional_sms(self):
        """Gets the transactional_sms of this UpdateChildAccountStatus.  # noqa: E501

        Status of Transactional SMS Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :return: The transactional_sms of this UpdateChildAccountStatus.  # noqa: E501
        :rtype: bool
        """
        return self._transactional_sms

    @transactional_sms.setter
    def transactional_sms(self, transactional_sms):
        """Sets the transactional_sms of this UpdateChildAccountStatus.

        Status of Transactional SMS Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :param transactional_sms: The transactional_sms of this UpdateChildAccountStatus.  # noqa: E501
        :type: bool
        """

        self._transactional_sms = transactional_sms

    @property
    def marketing_automation(self):
        """Gets the marketing_automation of this UpdateChildAccountStatus.  # noqa: E501

        Status of Marketing Automation Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :return: The marketing_automation of this UpdateChildAccountStatus.  # noqa: E501
        :rtype: bool
        """
        return self._marketing_automation

    @marketing_automation.setter
    def marketing_automation(self, marketing_automation):
        """Sets the marketing_automation of this UpdateChildAccountStatus.

        Status of Marketing Automation Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :param marketing_automation: The marketing_automation of this UpdateChildAccountStatus.  # noqa: E501
        :type: bool
        """

        self._marketing_automation = marketing_automation

    @property
    def sms_campaign(self):
        """Gets the sms_campaign of this UpdateChildAccountStatus.  # noqa: E501

        Status of SMS Campaign Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :return: The sms_campaign of this UpdateChildAccountStatus.  # noqa: E501
        :rtype: bool
        """
        return self._sms_campaign

    @sms_campaign.setter
    def sms_campaign(self, sms_campaign):
        """Sets the sms_campaign of this UpdateChildAccountStatus.

        Status of SMS Campaign Platform activation for your account (true=enabled, false=disabled)  # noqa: E501

        :param sms_campaign: The sms_campaign of this UpdateChildAccountStatus.  # noqa: E501
        :type: bool
        """

        self._sms_campaign = sms_campaign

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateChildAccountStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateChildAccountStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

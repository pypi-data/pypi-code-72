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


class RequestContactExportCustomContactFilter(object):
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
        'action_for_contacts': 'str',
        'action_for_email_campaigns': 'str',
        'action_for_sms_campaigns': 'str',
        'list_id': 'int',
        'email_campaign_id': 'int',
        'sms_campaign_id': 'int'
    }

    attribute_map = {
        'action_for_contacts': 'actionForContacts',
        'action_for_email_campaigns': 'actionForEmailCampaigns',
        'action_for_sms_campaigns': 'actionForSmsCampaigns',
        'list_id': 'listId',
        'email_campaign_id': 'emailCampaignId',
        'sms_campaign_id': 'smsCampaignId'
    }

    def __init__(self, action_for_contacts=None, action_for_email_campaigns=None, action_for_sms_campaigns=None, list_id=None, email_campaign_id=None, sms_campaign_id=None):  # noqa: E501
        """RequestContactExportCustomContactFilter - a model defined in Swagger"""  # noqa: E501

        self._action_for_contacts = None
        self._action_for_email_campaigns = None
        self._action_for_sms_campaigns = None
        self._list_id = None
        self._email_campaign_id = None
        self._sms_campaign_id = None
        self.discriminator = None

        if action_for_contacts is not None:
            self.action_for_contacts = action_for_contacts
        if action_for_email_campaigns is not None:
            self.action_for_email_campaigns = action_for_email_campaigns
        if action_for_sms_campaigns is not None:
            self.action_for_sms_campaigns = action_for_sms_campaigns
        if list_id is not None:
            self.list_id = list_id
        if email_campaign_id is not None:
            self.email_campaign_id = email_campaign_id
        if sms_campaign_id is not None:
            self.sms_campaign_id = sms_campaign_id

    @property
    def action_for_contacts(self):
        """Gets the action_for_contacts of this RequestContactExportCustomContactFilter.  # noqa: E501

        Mandatory if neither actionForEmailCampaigns nor actionForSmsCampaigns is passed. This will export the contacts on the basis of provided action applied on contacts as per the list id. * allContacts - Fetch the list of all contacts for a particular list. * subscribed & unsubscribed - Fetch the list of subscribed / unsubscribed (blacklisted via any means) contacts for a particular list. * unsubscribedPerList - Fetch the list of contacts that are unsubscribed from a particular list only.   # noqa: E501

        :return: The action_for_contacts of this RequestContactExportCustomContactFilter.  # noqa: E501
        :rtype: str
        """
        return self._action_for_contacts

    @action_for_contacts.setter
    def action_for_contacts(self, action_for_contacts):
        """Sets the action_for_contacts of this RequestContactExportCustomContactFilter.

        Mandatory if neither actionForEmailCampaigns nor actionForSmsCampaigns is passed. This will export the contacts on the basis of provided action applied on contacts as per the list id. * allContacts - Fetch the list of all contacts for a particular list. * subscribed & unsubscribed - Fetch the list of subscribed / unsubscribed (blacklisted via any means) contacts for a particular list. * unsubscribedPerList - Fetch the list of contacts that are unsubscribed from a particular list only.   # noqa: E501

        :param action_for_contacts: The action_for_contacts of this RequestContactExportCustomContactFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["allContacts", "subscribed", "unsubscribed", "unsubscribedPerList"]  # noqa: E501
        if action_for_contacts not in allowed_values:
            raise ValueError(
                "Invalid value for `action_for_contacts` ({0}), must be one of {1}"  # noqa: E501
                .format(action_for_contacts, allowed_values)
            )

        self._action_for_contacts = action_for_contacts

    @property
    def action_for_email_campaigns(self):
        """Gets the action_for_email_campaigns of this RequestContactExportCustomContactFilter.  # noqa: E501

        Mandatory if neither actionForContacts nor actionForSmsCampaigns is passed. This will export the contacts on the basis of provided action applied on email campaigns. * openers & nonOpeners - emailCampaignId is mandatory. Fetch the list of readers / non-readers for a particular email campaign. * clickers & nonClickers - emailCampaignId is mandatory. Fetch the list of clickers / non-clickers for a particular email campaign. * unsubscribed - emailCampaignId is mandatory. Fetch the list of all unsubscribed (blacklisted via any means) contacts for a particular email campaign. * hardBounces & softBounces - emailCampaignId is optional. Fetch the list of hard bounces / soft bounces for a particular / all email campaign(s).   # noqa: E501

        :return: The action_for_email_campaigns of this RequestContactExportCustomContactFilter.  # noqa: E501
        :rtype: str
        """
        return self._action_for_email_campaigns

    @action_for_email_campaigns.setter
    def action_for_email_campaigns(self, action_for_email_campaigns):
        """Sets the action_for_email_campaigns of this RequestContactExportCustomContactFilter.

        Mandatory if neither actionForContacts nor actionForSmsCampaigns is passed. This will export the contacts on the basis of provided action applied on email campaigns. * openers & nonOpeners - emailCampaignId is mandatory. Fetch the list of readers / non-readers for a particular email campaign. * clickers & nonClickers - emailCampaignId is mandatory. Fetch the list of clickers / non-clickers for a particular email campaign. * unsubscribed - emailCampaignId is mandatory. Fetch the list of all unsubscribed (blacklisted via any means) contacts for a particular email campaign. * hardBounces & softBounces - emailCampaignId is optional. Fetch the list of hard bounces / soft bounces for a particular / all email campaign(s).   # noqa: E501

        :param action_for_email_campaigns: The action_for_email_campaigns of this RequestContactExportCustomContactFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["openers", "nonOpeners", "clickers", "nonClickers", "unsubscribed", "hardBounces", "softBounces"]  # noqa: E501
        if action_for_email_campaigns not in allowed_values:
            raise ValueError(
                "Invalid value for `action_for_email_campaigns` ({0}), must be one of {1}"  # noqa: E501
                .format(action_for_email_campaigns, allowed_values)
            )

        self._action_for_email_campaigns = action_for_email_campaigns

    @property
    def action_for_sms_campaigns(self):
        """Gets the action_for_sms_campaigns of this RequestContactExportCustomContactFilter.  # noqa: E501

        Mandatory if neither actionForContacts nor actionForEmailCampaigns is passed. This will export the contacts on the basis of provided action applied on sms campaigns. * unsubscribed - Fetch the list of all unsubscribed (blacklisted via any means) contacts for all / particular sms campaigns. * hardBounces & softBounces - Fetch the list of hard bounces / soft bounces for all / particular sms campaigns.   # noqa: E501

        :return: The action_for_sms_campaigns of this RequestContactExportCustomContactFilter.  # noqa: E501
        :rtype: str
        """
        return self._action_for_sms_campaigns

    @action_for_sms_campaigns.setter
    def action_for_sms_campaigns(self, action_for_sms_campaigns):
        """Sets the action_for_sms_campaigns of this RequestContactExportCustomContactFilter.

        Mandatory if neither actionForContacts nor actionForEmailCampaigns is passed. This will export the contacts on the basis of provided action applied on sms campaigns. * unsubscribed - Fetch the list of all unsubscribed (blacklisted via any means) contacts for all / particular sms campaigns. * hardBounces & softBounces - Fetch the list of hard bounces / soft bounces for all / particular sms campaigns.   # noqa: E501

        :param action_for_sms_campaigns: The action_for_sms_campaigns of this RequestContactExportCustomContactFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["hardBounces", "softBounces", "unsubscribed"]  # noqa: E501
        if action_for_sms_campaigns not in allowed_values:
            raise ValueError(
                "Invalid value for `action_for_sms_campaigns` ({0}), must be one of {1}"  # noqa: E501
                .format(action_for_sms_campaigns, allowed_values)
            )

        self._action_for_sms_campaigns = action_for_sms_campaigns

    @property
    def list_id(self):
        """Gets the list_id of this RequestContactExportCustomContactFilter.  # noqa: E501

        Mandatory if actionForContacts is passed, ignored otherwise. Id of the list for which the corresponding action shall be applied in the filter.  # noqa: E501

        :return: The list_id of this RequestContactExportCustomContactFilter.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this RequestContactExportCustomContactFilter.

        Mandatory if actionForContacts is passed, ignored otherwise. Id of the list for which the corresponding action shall be applied in the filter.  # noqa: E501

        :param list_id: The list_id of this RequestContactExportCustomContactFilter.  # noqa: E501
        :type: int
        """

        self._list_id = list_id

    @property
    def email_campaign_id(self):
        """Gets the email_campaign_id of this RequestContactExportCustomContactFilter.  # noqa: E501

        Considered only if actionForEmailCampaigns is passed, ignored otherwise. Mandatory if action is one of the following - openers, nonOpeners, clickers, nonClickers, unsubscribed. The id of the email campaign for which the corresponding action shall be applied in the filter.  # noqa: E501

        :return: The email_campaign_id of this RequestContactExportCustomContactFilter.  # noqa: E501
        :rtype: int
        """
        return self._email_campaign_id

    @email_campaign_id.setter
    def email_campaign_id(self, email_campaign_id):
        """Sets the email_campaign_id of this RequestContactExportCustomContactFilter.

        Considered only if actionForEmailCampaigns is passed, ignored otherwise. Mandatory if action is one of the following - openers, nonOpeners, clickers, nonClickers, unsubscribed. The id of the email campaign for which the corresponding action shall be applied in the filter.  # noqa: E501

        :param email_campaign_id: The email_campaign_id of this RequestContactExportCustomContactFilter.  # noqa: E501
        :type: int
        """

        self._email_campaign_id = email_campaign_id

    @property
    def sms_campaign_id(self):
        """Gets the sms_campaign_id of this RequestContactExportCustomContactFilter.  # noqa: E501

        Considered only if actionForSmsCampaigns is passed, ignored otherwise. The id of sms campaign for which the corresponding action shall be applied in the filter.  # noqa: E501

        :return: The sms_campaign_id of this RequestContactExportCustomContactFilter.  # noqa: E501
        :rtype: int
        """
        return self._sms_campaign_id

    @sms_campaign_id.setter
    def sms_campaign_id(self, sms_campaign_id):
        """Sets the sms_campaign_id of this RequestContactExportCustomContactFilter.

        Considered only if actionForSmsCampaigns is passed, ignored otherwise. The id of sms campaign for which the corresponding action shall be applied in the filter.  # noqa: E501

        :param sms_campaign_id: The sms_campaign_id of this RequestContactExportCustomContactFilter.  # noqa: E501
        :type: int
        """

        self._sms_campaign_id = sms_campaign_id

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
        if issubclass(RequestContactExportCustomContactFilter, dict):
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
        if not isinstance(other, RequestContactExportCustomContactFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class RequestContactExport(object):
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
        'export_attributes': 'list[str]',
        'contact_filter': 'object',
        'custom_contact_filter': 'RequestContactExportCustomContactFilter',
        'notify_url': 'str'
    }

    attribute_map = {
        'export_attributes': 'exportAttributes',
        'contact_filter': 'contactFilter',
        'custom_contact_filter': 'customContactFilter',
        'notify_url': 'notifyUrl'
    }

    def __init__(self, export_attributes=None, contact_filter=None, custom_contact_filter=None, notify_url=None):  # noqa: E501
        """RequestContactExport - a model defined in Swagger"""  # noqa: E501

        self._export_attributes = None
        self._contact_filter = None
        self._custom_contact_filter = None
        self._notify_url = None
        self.discriminator = None

        if export_attributes is not None:
            self.export_attributes = export_attributes
        if contact_filter is not None:
            self.contact_filter = contact_filter
        if custom_contact_filter is not None:
            self.custom_contact_filter = custom_contact_filter
        if notify_url is not None:
            self.notify_url = notify_url

    @property
    def export_attributes(self):
        """Gets the export_attributes of this RequestContactExport.  # noqa: E501

        List of all the attributes that you want to export. These attributes must be present in your contact database. For example, ['fname', 'lname', 'email'].  # noqa: E501

        :return: The export_attributes of this RequestContactExport.  # noqa: E501
        :rtype: list[str]
        """
        return self._export_attributes

    @export_attributes.setter
    def export_attributes(self, export_attributes):
        """Sets the export_attributes of this RequestContactExport.

        List of all the attributes that you want to export. These attributes must be present in your contact database. For example, ['fname', 'lname', 'email'].  # noqa: E501

        :param export_attributes: The export_attributes of this RequestContactExport.  # noqa: E501
        :type: list[str]
        """

        self._export_attributes = export_attributes

    @property
    def contact_filter(self):
        """Gets the contact_filter of this RequestContactExport.  # noqa: E501

        This attribute has been deprecated and will be removed by January 1st, 2021. Only one of the two filter options (contactFilter or customContactFilter) can be passed in the request. Set the filter for the contacts to be exported. For example, {\"blacklisted\":true} will export all the blacklisted contacts.   # noqa: E501

        :return: The contact_filter of this RequestContactExport.  # noqa: E501
        :rtype: object
        """
        return self._contact_filter

    @contact_filter.setter
    def contact_filter(self, contact_filter):
        """Sets the contact_filter of this RequestContactExport.

        This attribute has been deprecated and will be removed by January 1st, 2021. Only one of the two filter options (contactFilter or customContactFilter) can be passed in the request. Set the filter for the contacts to be exported. For example, {\"blacklisted\":true} will export all the blacklisted contacts.   # noqa: E501

        :param contact_filter: The contact_filter of this RequestContactExport.  # noqa: E501
        :type: object
        """

        self._contact_filter = contact_filter

    @property
    def custom_contact_filter(self):
        """Gets the custom_contact_filter of this RequestContactExport.  # noqa: E501


        :return: The custom_contact_filter of this RequestContactExport.  # noqa: E501
        :rtype: RequestContactExportCustomContactFilter
        """
        return self._custom_contact_filter

    @custom_contact_filter.setter
    def custom_contact_filter(self, custom_contact_filter):
        """Sets the custom_contact_filter of this RequestContactExport.


        :param custom_contact_filter: The custom_contact_filter of this RequestContactExport.  # noqa: E501
        :type: RequestContactExportCustomContactFilter
        """

        self._custom_contact_filter = custom_contact_filter

    @property
    def notify_url(self):
        """Gets the notify_url of this RequestContactExport.  # noqa: E501

        Webhook that will be called once the export process is finished. For reference, https://help.sendinblue.com/hc/en-us/articles/360007666479  # noqa: E501

        :return: The notify_url of this RequestContactExport.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this RequestContactExport.

        Webhook that will be called once the export process is finished. For reference, https://help.sendinblue.com/hc/en-us/articles/360007666479  # noqa: E501

        :param notify_url: The notify_url of this RequestContactExport.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

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
        if issubclass(RequestContactExport, dict):
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
        if not isinstance(other, RequestContactExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

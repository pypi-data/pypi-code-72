# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.17.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class ListCronWorkflowsResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'count': 'int',
        'cron_workflows': 'list[CronWorkflow]',
        'page': 'int',
        'pages': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'count': 'count',
        'cron_workflows': 'cronWorkflows',
        'page': 'page',
        'pages': 'pages',
        'total_count': 'totalCount'
    }

    def __init__(self, count=None, cron_workflows=None, page=None, pages=None, total_count=None, local_vars_configuration=None):  # noqa: E501
        """ListCronWorkflowsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._cron_workflows = None
        self._page = None
        self._pages = None
        self._total_count = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if cron_workflows is not None:
            self.cron_workflows = cron_workflows
        if page is not None:
            self.page = page
        if pages is not None:
            self.pages = pages
        if total_count is not None:
            self.total_count = total_count

    @property
    def count(self):
        """Gets the count of this ListCronWorkflowsResponse.  # noqa: E501


        :return: The count of this ListCronWorkflowsResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCronWorkflowsResponse.


        :param count: The count of this ListCronWorkflowsResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def cron_workflows(self):
        """Gets the cron_workflows of this ListCronWorkflowsResponse.  # noqa: E501


        :return: The cron_workflows of this ListCronWorkflowsResponse.  # noqa: E501
        :rtype: list[CronWorkflow]
        """
        return self._cron_workflows

    @cron_workflows.setter
    def cron_workflows(self, cron_workflows):
        """Sets the cron_workflows of this ListCronWorkflowsResponse.


        :param cron_workflows: The cron_workflows of this ListCronWorkflowsResponse.  # noqa: E501
        :type: list[CronWorkflow]
        """

        self._cron_workflows = cron_workflows

    @property
    def page(self):
        """Gets the page of this ListCronWorkflowsResponse.  # noqa: E501


        :return: The page of this ListCronWorkflowsResponse.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListCronWorkflowsResponse.


        :param page: The page of this ListCronWorkflowsResponse.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def pages(self):
        """Gets the pages of this ListCronWorkflowsResponse.  # noqa: E501


        :return: The pages of this ListCronWorkflowsResponse.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this ListCronWorkflowsResponse.


        :param pages: The pages of this ListCronWorkflowsResponse.  # noqa: E501
        :type: int
        """

        self._pages = pages

    @property
    def total_count(self):
        """Gets the total_count of this ListCronWorkflowsResponse.  # noqa: E501


        :return: The total_count of this ListCronWorkflowsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCronWorkflowsResponse.


        :param total_count: The total_count of this ListCronWorkflowsResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCronWorkflowsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListCronWorkflowsResponse):
            return True

        return self.to_dict() != other.to_dict()

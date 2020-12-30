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


class StreamResultOfWorkflowExecution(object):
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
        'result': 'WorkflowExecution',
        'error': 'GoogleRpcStatus'
    }

    attribute_map = {
        'result': 'result',
        'error': 'error'
    }

    def __init__(self, result=None, error=None, local_vars_configuration=None):  # noqa: E501
        """StreamResultOfWorkflowExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._error = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if error is not None:
            self.error = error

    @property
    def result(self):
        """Gets the result of this StreamResultOfWorkflowExecution.  # noqa: E501


        :return: The result of this StreamResultOfWorkflowExecution.  # noqa: E501
        :rtype: WorkflowExecution
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this StreamResultOfWorkflowExecution.


        :param result: The result of this StreamResultOfWorkflowExecution.  # noqa: E501
        :type: WorkflowExecution
        """

        self._result = result

    @property
    def error(self):
        """Gets the error of this StreamResultOfWorkflowExecution.  # noqa: E501


        :return: The error of this StreamResultOfWorkflowExecution.  # noqa: E501
        :rtype: GoogleRpcStatus
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this StreamResultOfWorkflowExecution.


        :param error: The error of this StreamResultOfWorkflowExecution.  # noqa: E501
        :type: GoogleRpcStatus
        """

        self._error = error

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
        if not isinstance(other, StreamResultOfWorkflowExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StreamResultOfWorkflowExecution):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    Anyscale API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from anyscale_client.configuration import Configuration


class SessionStateUpdate(object):
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
        'session_id': 'str',
        'completed_session_state': 'SessionState'
    }

    attribute_map = {
        'session_id': 'session_id',
        'completed_session_state': 'completed_session_state'
    }

    def __init__(self, session_id=None, completed_session_state=None, local_vars_configuration=None):  # noqa: E501
        """SessionStateUpdate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._session_id = None
        self._completed_session_state = None
        self.discriminator = None

        self.session_id = session_id
        self.completed_session_state = completed_session_state

    @property
    def session_id(self):
        """Gets the session_id of this SessionStateUpdate.  # noqa: E501

        ID of the Session that is being updated.  # noqa: E501

        :return: The session_id of this SessionStateUpdate.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this SessionStateUpdate.

        ID of the Session that is being updated.  # noqa: E501

        :param session_id: The session_id of this SessionStateUpdate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and session_id is None:  # noqa: E501
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def completed_session_state(self):
        """Gets the completed_session_state of this SessionStateUpdate.  # noqa: E501


        :return: The completed_session_state of this SessionStateUpdate.  # noqa: E501
        :rtype: SessionState
        """
        return self._completed_session_state

    @completed_session_state.setter
    def completed_session_state(self, completed_session_state):
        """Sets the completed_session_state of this SessionStateUpdate.


        :param completed_session_state: The completed_session_state of this SessionStateUpdate.  # noqa: E501
        :type: SessionState
        """
        if self.local_vars_configuration.client_side_validation and completed_session_state is None:  # noqa: E501
            raise ValueError("Invalid value for `completed_session_state`, must not be `None`")  # noqa: E501

        self._completed_session_state = completed_session_state

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
        if not isinstance(other, SessionStateUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SessionStateUpdate):
            return True

        return self.to_dict() != other.to_dict()

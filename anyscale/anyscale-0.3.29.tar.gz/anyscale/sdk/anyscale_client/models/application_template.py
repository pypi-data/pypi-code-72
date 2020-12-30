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


class ApplicationTemplate(object):
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
        'name': 'str',
        'config_json': 'str',
        'project_id': 'str',
        'id': 'str',
        'creator_id': 'str',
        'created_at': 'datetime',
        'last_modified_at': 'datetime',
        'deleted_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'config_json': 'config_json',
        'project_id': 'project_id',
        'id': 'id',
        'creator_id': 'creator_id',
        'created_at': 'created_at',
        'last_modified_at': 'last_modified_at',
        'deleted_at': 'deleted_at'
    }

    def __init__(self, name=None, config_json=None, project_id=None, id=None, creator_id=None, created_at=None, last_modified_at=None, deleted_at=None, local_vars_configuration=None):  # noqa: E501
        """ApplicationTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._config_json = None
        self._project_id = None
        self._id = None
        self._creator_id = None
        self._created_at = None
        self._last_modified_at = None
        self._deleted_at = None
        self.discriminator = None

        self.name = name
        self.config_json = config_json
        self.project_id = project_id
        self.id = id
        self.creator_id = creator_id
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        if deleted_at is not None:
            self.deleted_at = deleted_at

    @property
    def name(self):
        """Gets the name of this ApplicationTemplate.  # noqa: E501

        Name of the Application Template.  # noqa: E501

        :return: The name of this ApplicationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationTemplate.

        Name of the Application Template.  # noqa: E501

        :param name: The name of this ApplicationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def config_json(self):
        """Gets the config_json of this ApplicationTemplate.  # noqa: E501

        Config JSON string for the Application Template.  # noqa: E501

        :return: The config_json of this ApplicationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._config_json

    @config_json.setter
    def config_json(self, config_json):
        """Sets the config_json of this ApplicationTemplate.

        Config JSON string for the Application Template.  # noqa: E501

        :param config_json: The config_json of this ApplicationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and config_json is None:  # noqa: E501
            raise ValueError("Invalid value for `config_json`, must not be `None`")  # noqa: E501

        self._config_json = config_json

    @property
    def project_id(self):
        """Gets the project_id of this ApplicationTemplate.  # noqa: E501

        ID of the Project this Application Template is for.  # noqa: E501

        :return: The project_id of this ApplicationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ApplicationTemplate.

        ID of the Project this Application Template is for.  # noqa: E501

        :param project_id: The project_id of this ApplicationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def id(self):
        """Gets the id of this ApplicationTemplate.  # noqa: E501

        Server assigned unique identifier.  # noqa: E501

        :return: The id of this ApplicationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationTemplate.

        Server assigned unique identifier.  # noqa: E501

        :param id: The id of this ApplicationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def creator_id(self):
        """Gets the creator_id of this ApplicationTemplate.  # noqa: E501

        ID of the User that created this record.  # noqa: E501

        :return: The creator_id of this ApplicationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ApplicationTemplate.

        ID of the User that created this record.  # noqa: E501

        :param creator_id: The creator_id of this ApplicationTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and creator_id is None:  # noqa: E501
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def created_at(self):
        """Gets the created_at of this ApplicationTemplate.  # noqa: E501

        Timestamp of when this record was created.  # noqa: E501

        :return: The created_at of this ApplicationTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApplicationTemplate.

        Timestamp of when this record was created.  # noqa: E501

        :param created_at: The created_at of this ApplicationTemplate.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this ApplicationTemplate.  # noqa: E501

        Timestamp of when this record was last updated.  # noqa: E501

        :return: The last_modified_at of this ApplicationTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this ApplicationTemplate.

        Timestamp of when this record was last updated.  # noqa: E501

        :param last_modified_at: The last_modified_at of this ApplicationTemplate.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def deleted_at(self):
        """Gets the deleted_at of this ApplicationTemplate.  # noqa: E501

        Timestamp of when this record was deleted.  # noqa: E501

        :return: The deleted_at of this ApplicationTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this ApplicationTemplate.

        Timestamp of when this record was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this ApplicationTemplate.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

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
        if not isinstance(other, ApplicationTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationTemplate):
            return True

        return self.to_dict() != other.to_dict()

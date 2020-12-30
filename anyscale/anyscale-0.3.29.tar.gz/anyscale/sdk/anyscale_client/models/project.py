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


class Project(object):
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
        'cluster_config': 'str',
        'description': 'str',
        'id': 'str',
        'creator_id': 'str',
        'created_at': 'datetime',
        'organization_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cluster_config': 'cluster_config',
        'description': 'description',
        'id': 'id',
        'creator_id': 'creator_id',
        'created_at': 'created_at',
        'organization_id': 'organization_id'
    }

    def __init__(self, name=None, cluster_config=None, description=None, id=None, creator_id=None, created_at=None, organization_id=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._cluster_config = None
        self._description = None
        self._id = None
        self._creator_id = None
        self._created_at = None
        self._organization_id = None
        self.discriminator = None

        self.name = name
        self.cluster_config = cluster_config
        if description is not None:
            self.description = description
        self.id = id
        self.creator_id = creator_id
        self.created_at = created_at
        self.organization_id = organization_id

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501

        Name of the Project to be created.  # noqa: E501

        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.

        Name of the Project to be created.  # noqa: E501

        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cluster_config(self):
        """Gets the cluster_config of this Project.  # noqa: E501

        Cluster config associated with the Project. This can later be used to start a Session.  # noqa: E501

        :return: The cluster_config of this Project.  # noqa: E501
        :rtype: str
        """
        return self._cluster_config

    @cluster_config.setter
    def cluster_config(self, cluster_config):
        """Sets the cluster_config of this Project.

        Cluster config associated with the Project. This can later be used to start a Session.  # noqa: E501

        :param cluster_config: The cluster_config of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cluster_config is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_config`, must not be `None`")  # noqa: E501

        self._cluster_config = cluster_config

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501

        Description of Project.  # noqa: E501

        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.

        Description of Project.  # noqa: E501

        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501

        Server assigned unique identifier of the Project.  # noqa: E501

        :return: The id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.

        Server assigned unique identifier of the Project.  # noqa: E501

        :param id: The id of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def creator_id(self):
        """Gets the creator_id of this Project.  # noqa: E501

        Identifier of user who created the Project.  # noqa: E501

        :return: The creator_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this Project.

        Identifier of user who created the Project.  # noqa: E501

        :param creator_id: The creator_id of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and creator_id is None:  # noqa: E501
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501

        Time at which Project was created.  # noqa: E501

        :return: The created_at of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.

        Time at which Project was created.  # noqa: E501

        :param created_at: The created_at of this Project.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def organization_id(self):
        """Gets the organization_id of this Project.  # noqa: E501

        Organization that the Project is associated with.  # noqa: E501

        :return: The organization_id of this Project.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Project.

        Organization that the Project is associated with.  # noqa: E501

        :param organization_id: The organization_id of this Project.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organization_id is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()

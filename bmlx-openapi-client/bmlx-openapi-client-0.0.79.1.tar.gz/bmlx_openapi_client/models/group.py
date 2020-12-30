# coding: utf-8

"""
    bmlx api-server.

    Documentation of bmlx api-server apis. To find more info about generating spec from source, please refer to https://goswagger.io/use/spec.html  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from bmlx_openapi_client.configuration import Configuration


class Group(object):
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
        'users': 'list[User]',
        'admin': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'users': 'Users',
        'admin': 'admin',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, users=None, admin=None, id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """Group - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._users = None
        self._admin = None
        self._id = None
        self._name = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if admin is not None:
            self.admin = admin
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def users(self):
        """Gets the users of this Group.  # noqa: E501


        :return: The users of this Group.  # noqa: E501
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Group.


        :param users: The users of this Group.  # noqa: E501
        :type users: list[User]
        """

        self._users = users

    @property
    def admin(self):
        """Gets the admin of this Group.  # noqa: E501


        :return: The admin of this Group.  # noqa: E501
        :rtype: str
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this Group.


        :param admin: The admin of this Group.  # noqa: E501
        :type admin: str
        """

        self._admin = admin

    @property
    def id(self):
        """Gets the id of this Group.  # noqa: E501


        :return: The id of this Group.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Group.


        :param id: The id of this Group.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501


        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.


        :param name: The name of this Group.  # noqa: E501
        :type name: str
        """

        self._name = name

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                elif len(args) == 2:
                    return x.to_dict(serialize)
                else:
                    raise ValueError("Invalid argument size of to_dict")
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Group):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Group):
            return True

        return self.to_dict() != other.to_dict()

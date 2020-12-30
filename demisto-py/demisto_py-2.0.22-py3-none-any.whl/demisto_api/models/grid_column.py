# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GridColumn(object):
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
        'display_name': 'str',
        'field_calc_script': 'str',
        'is_default': 'bool',
        'is_read_only': 'bool',
        'key': 'str',
        'required': 'bool',
        'script': 'str',
        'select_values': 'list[str]',
        'type': 'str',
        'width': 'int'
    }

    attribute_map = {
        'display_name': 'displayName',
        'field_calc_script': 'fieldCalcScript',
        'is_default': 'isDefault',
        'is_read_only': 'isReadOnly',
        'key': 'key',
        'required': 'required',
        'script': 'script',
        'select_values': 'selectValues',
        'type': 'type',
        'width': 'width'
    }

    def __init__(self, display_name=None, field_calc_script=None, is_default=None, is_read_only=None, key=None, required=None, script=None, select_values=None, type=None, width=None):  # noqa: E501
        """GridColumn - a model defined in Swagger"""  # noqa: E501

        self._display_name = None
        self._field_calc_script = None
        self._is_default = None
        self._is_read_only = None
        self._key = None
        self._required = None
        self._script = None
        self._select_values = None
        self._type = None
        self._width = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if field_calc_script is not None:
            self.field_calc_script = field_calc_script
        if is_default is not None:
            self.is_default = is_default
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if key is not None:
            self.key = key
        if required is not None:
            self.required = required
        if script is not None:
            self.script = script
        if select_values is not None:
            self.select_values = select_values
        if type is not None:
            self.type = type
        if width is not None:
            self.width = width

    @property
    def display_name(self):
        """Gets the display_name of this GridColumn.  # noqa: E501


        :return: The display_name of this GridColumn.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GridColumn.


        :param display_name: The display_name of this GridColumn.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def field_calc_script(self):
        """Gets the field_calc_script of this GridColumn.  # noqa: E501


        :return: The field_calc_script of this GridColumn.  # noqa: E501
        :rtype: str
        """
        return self._field_calc_script

    @field_calc_script.setter
    def field_calc_script(self, field_calc_script):
        """Sets the field_calc_script of this GridColumn.


        :param field_calc_script: The field_calc_script of this GridColumn.  # noqa: E501
        :type: str
        """

        self._field_calc_script = field_calc_script

    @property
    def is_default(self):
        """Gets the is_default of this GridColumn.  # noqa: E501


        :return: The is_default of this GridColumn.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this GridColumn.


        :param is_default: The is_default of this GridColumn.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_read_only(self):
        """Gets the is_read_only of this GridColumn.  # noqa: E501


        :return: The is_read_only of this GridColumn.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this GridColumn.


        :param is_read_only: The is_read_only of this GridColumn.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def key(self):
        """Gets the key of this GridColumn.  # noqa: E501


        :return: The key of this GridColumn.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this GridColumn.


        :param key: The key of this GridColumn.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def required(self):
        """Gets the required of this GridColumn.  # noqa: E501


        :return: The required of this GridColumn.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this GridColumn.


        :param required: The required of this GridColumn.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def script(self):
        """Gets the script of this GridColumn.  # noqa: E501


        :return: The script of this GridColumn.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this GridColumn.


        :param script: The script of this GridColumn.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def select_values(self):
        """Gets the select_values of this GridColumn.  # noqa: E501


        :return: The select_values of this GridColumn.  # noqa: E501
        :rtype: list[str]
        """
        return self._select_values

    @select_values.setter
    def select_values(self, select_values):
        """Sets the select_values of this GridColumn.


        :param select_values: The select_values of this GridColumn.  # noqa: E501
        :type: list[str]
        """

        self._select_values = select_values

    @property
    def type(self):
        """Gets the type of this GridColumn.  # noqa: E501


        :return: The type of this GridColumn.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GridColumn.


        :param type: The type of this GridColumn.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def width(self):
        """Gets the width of this GridColumn.  # noqa: E501


        :return: The width of this GridColumn.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this GridColumn.


        :param width: The width of this GridColumn.  # noqa: E501
        :type: int
        """

        self._width = width

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
        if issubclass(GridColumn, dict):
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
        if not isinstance(other, GridColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

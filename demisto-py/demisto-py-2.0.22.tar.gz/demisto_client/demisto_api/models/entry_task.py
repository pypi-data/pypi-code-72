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


class EntryTask(object):
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
        'playbook_name': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'playbook_name': 'playbookName',
        'task_id': 'taskId',
        'task_name': 'taskName',
        'task_status': 'taskStatus'
    }

    def __init__(self, playbook_name=None, task_id=None, task_name=None, task_status=None):  # noqa: E501
        """EntryTask - a model defined in Swagger"""  # noqa: E501

        self._playbook_name = None
        self._task_id = None
        self._task_name = None
        self._task_status = None
        self.discriminator = None

        if playbook_name is not None:
            self.playbook_name = playbook_name
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_status is not None:
            self.task_status = task_status

    @property
    def playbook_name(self):
        """Gets the playbook_name of this EntryTask.  # noqa: E501


        :return: The playbook_name of this EntryTask.  # noqa: E501
        :rtype: str
        """
        return self._playbook_name

    @playbook_name.setter
    def playbook_name(self, playbook_name):
        """Sets the playbook_name of this EntryTask.


        :param playbook_name: The playbook_name of this EntryTask.  # noqa: E501
        :type: str
        """

        self._playbook_name = playbook_name

    @property
    def task_id(self):
        """Gets the task_id of this EntryTask.  # noqa: E501


        :return: The task_id of this EntryTask.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this EntryTask.


        :param task_id: The task_id of this EntryTask.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this EntryTask.  # noqa: E501


        :return: The task_name of this EntryTask.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this EntryTask.


        :param task_name: The task_name of this EntryTask.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def task_status(self):
        """Gets the task_status of this EntryTask.  # noqa: E501


        :return: The task_status of this EntryTask.  # noqa: E501
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this EntryTask.


        :param task_status: The task_status of this EntryTask.  # noqa: E501
        :type: str
        """

        self._task_status = task_status

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
        if issubclass(EntryTask, dict):
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
        if not isinstance(other, EntryTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

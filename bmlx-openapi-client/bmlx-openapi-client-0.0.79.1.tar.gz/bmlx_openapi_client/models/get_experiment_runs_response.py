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


class GetExperimentRunsResponse(object):
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
        'experiment_runs': 'list[ExperimentRun]',
        'next_page_token': 'str'
    }

    attribute_map = {
        'experiment_runs': 'experiment_runs',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, experiment_runs=None, next_page_token=None, local_vars_configuration=None):  # noqa: E501
        """GetExperimentRunsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._experiment_runs = None
        self._next_page_token = None
        self.discriminator = None

        if experiment_runs is not None:
            self.experiment_runs = experiment_runs
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def experiment_runs(self):
        """Gets the experiment_runs of this GetExperimentRunsResponse.  # noqa: E501


        :return: The experiment_runs of this GetExperimentRunsResponse.  # noqa: E501
        :rtype: list[ExperimentRun]
        """
        return self._experiment_runs

    @experiment_runs.setter
    def experiment_runs(self, experiment_runs):
        """Sets the experiment_runs of this GetExperimentRunsResponse.


        :param experiment_runs: The experiment_runs of this GetExperimentRunsResponse.  # noqa: E501
        :type experiment_runs: list[ExperimentRun]
        """

        self._experiment_runs = experiment_runs

    @property
    def next_page_token(self):
        """Gets the next_page_token of this GetExperimentRunsResponse.  # noqa: E501


        :return: The next_page_token of this GetExperimentRunsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this GetExperimentRunsResponse.


        :param next_page_token: The next_page_token of this GetExperimentRunsResponse.  # noqa: E501
        :type next_page_token: str
        """

        self._next_page_token = next_page_token

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
        if not isinstance(other, GetExperimentRunsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetExperimentRunsResponse):
            return True

        return self.to_dict() != other.to_dict()

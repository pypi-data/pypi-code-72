# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ExternalServiceStatusResponse(object):
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
        'metrics_dashboard_status': 'ExternalServiceStatus',
        'jupyter_noteboook_status': 'ExternalServiceStatus',
        'service_proxy_status': 'ExternalServiceStatus',
        'ray_dashboard_status': 'ExternalServiceStatus'
    }

    attribute_map = {
        'metrics_dashboard_status': 'metrics_dashboard_status',
        'jupyter_noteboook_status': 'jupyter_noteboook_status',
        'service_proxy_status': 'service_proxy_status',
        'ray_dashboard_status': 'ray_dashboard_status'
    }

    def __init__(self, metrics_dashboard_status=None, jupyter_noteboook_status=None, service_proxy_status=None, ray_dashboard_status=None, local_vars_configuration=None):  # noqa: E501
        """ExternalServiceStatusResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metrics_dashboard_status = None
        self._jupyter_noteboook_status = None
        self._service_proxy_status = None
        self._ray_dashboard_status = None
        self.discriminator = None

        if metrics_dashboard_status is not None:
            self.metrics_dashboard_status = metrics_dashboard_status
        if jupyter_noteboook_status is not None:
            self.jupyter_noteboook_status = jupyter_noteboook_status
        if service_proxy_status is not None:
            self.service_proxy_status = service_proxy_status
        if ray_dashboard_status is not None:
            self.ray_dashboard_status = ray_dashboard_status

    @property
    def metrics_dashboard_status(self):
        """Gets the metrics_dashboard_status of this ExternalServiceStatusResponse.  # noqa: E501


        :return: The metrics_dashboard_status of this ExternalServiceStatusResponse.  # noqa: E501
        :rtype: ExternalServiceStatus
        """
        return self._metrics_dashboard_status

    @metrics_dashboard_status.setter
    def metrics_dashboard_status(self, metrics_dashboard_status):
        """Sets the metrics_dashboard_status of this ExternalServiceStatusResponse.


        :param metrics_dashboard_status: The metrics_dashboard_status of this ExternalServiceStatusResponse.  # noqa: E501
        :type: ExternalServiceStatus
        """

        self._metrics_dashboard_status = metrics_dashboard_status

    @property
    def jupyter_noteboook_status(self):
        """Gets the jupyter_noteboook_status of this ExternalServiceStatusResponse.  # noqa: E501


        :return: The jupyter_noteboook_status of this ExternalServiceStatusResponse.  # noqa: E501
        :rtype: ExternalServiceStatus
        """
        return self._jupyter_noteboook_status

    @jupyter_noteboook_status.setter
    def jupyter_noteboook_status(self, jupyter_noteboook_status):
        """Sets the jupyter_noteboook_status of this ExternalServiceStatusResponse.


        :param jupyter_noteboook_status: The jupyter_noteboook_status of this ExternalServiceStatusResponse.  # noqa: E501
        :type: ExternalServiceStatus
        """

        self._jupyter_noteboook_status = jupyter_noteboook_status

    @property
    def service_proxy_status(self):
        """Gets the service_proxy_status of this ExternalServiceStatusResponse.  # noqa: E501


        :return: The service_proxy_status of this ExternalServiceStatusResponse.  # noqa: E501
        :rtype: ExternalServiceStatus
        """
        return self._service_proxy_status

    @service_proxy_status.setter
    def service_proxy_status(self, service_proxy_status):
        """Sets the service_proxy_status of this ExternalServiceStatusResponse.


        :param service_proxy_status: The service_proxy_status of this ExternalServiceStatusResponse.  # noqa: E501
        :type: ExternalServiceStatus
        """

        self._service_proxy_status = service_proxy_status

    @property
    def ray_dashboard_status(self):
        """Gets the ray_dashboard_status of this ExternalServiceStatusResponse.  # noqa: E501


        :return: The ray_dashboard_status of this ExternalServiceStatusResponse.  # noqa: E501
        :rtype: ExternalServiceStatus
        """
        return self._ray_dashboard_status

    @ray_dashboard_status.setter
    def ray_dashboard_status(self, ray_dashboard_status):
        """Sets the ray_dashboard_status of this ExternalServiceStatusResponse.


        :param ray_dashboard_status: The ray_dashboard_status of this ExternalServiceStatusResponse.  # noqa: E501
        :type: ExternalServiceStatus
        """

        self._ray_dashboard_status = ray_dashboard_status

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
        if not isinstance(other, ExternalServiceStatusResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalServiceStatusResponse):
            return True

        return self.to_dict() != other.to_dict()

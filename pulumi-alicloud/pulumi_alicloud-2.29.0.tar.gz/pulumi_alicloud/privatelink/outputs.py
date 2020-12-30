# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'VpcEndpointZone',
    'GetVpcEndpointConnectionsConnectionResult',
    'GetVpcEndpointServiceResourcesResourceResult',
    'GetVpcEndpointServiceUsersUserResult',
    'GetVpcEndpointServicesServiceResult',
    'GetVpcEndpointsEndpointResult',
    'GetVpcEndpointsEndpointZoneResult',
]

@pulumi.output_type
class VpcEndpointZone(dict):
    def __init__(__self__, *,
                 vswitch_id: Optional[str] = None,
                 zone_id: Optional[str] = None):
        """
        :param str vswitch_id: To create the vswitch of the terminal node network card in the available zone.
        :param str zone_id: Availability zone corresponding to terminal node service.
        """
        if vswitch_id is not None:
            pulumi.set(__self__, "vswitch_id", vswitch_id)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> Optional[str]:
        """
        To create the vswitch of the terminal node network card in the available zone.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[str]:
        """
        Availability zone corresponding to terminal node service.
        """
        return pulumi.get(self, "zone_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetVpcEndpointConnectionsConnectionResult(dict):
    def __init__(__self__, *,
                 bandwidth: int,
                 endpoint_id: str,
                 id: str,
                 status: str):
        """
        :param int bandwidth: The Bandwidth.
        :param str endpoint_id: The ID of the Vpc Endpoint.
        :param str id: The ID of the Vpc Endpoint Connection.
        :param str status: The status of Vpc Endpoint Connection.
        """
        pulumi.set(__self__, "bandwidth", bandwidth)
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def bandwidth(self) -> int:
        """
        The Bandwidth.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> str:
        """
        The ID of the Vpc Endpoint.
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Vpc Endpoint Connection.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of Vpc Endpoint Connection.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetVpcEndpointServiceResourcesResourceResult(dict):
    def __init__(__self__, *,
                 id: str,
                 resource_id: str,
                 resource_type: str):
        """
        :param str id: The ID of the Vpc Endpoint Service Resource.
        :param str resource_id: The ID of Resource.
        :param str resource_type: The type of Resource.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Vpc Endpoint Service Resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The ID of Resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> str:
        """
        The type of Resource.
        """
        return pulumi.get(self, "resource_type")


@pulumi.output_type
class GetVpcEndpointServiceUsersUserResult(dict):
    def __init__(__self__, *,
                 id: str,
                 user_id: str):
        """
        :param str id: The ID of the Vpc Endpoint Service User.
        :param str user_id: The Id of Ram User.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Vpc Endpoint Service User.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        The Id of Ram User.
        """
        return pulumi.get(self, "user_id")


@pulumi.output_type
class GetVpcEndpointServicesServiceResult(dict):
    def __init__(__self__, *,
                 auto_accept_connection: bool,
                 connect_bandwidth: int,
                 id: str,
                 service_business_status: str,
                 service_description: str,
                 service_domain: str,
                 service_id: str,
                 status: str,
                 vpc_endpoint_service_name: str):
        """
        :param bool auto_accept_connection: Whether to automatically accept terminal node connections..
        :param int connect_bandwidth: The connection bandwidth.
        :param str id: The ID of the Vpc Endpoint Service.
        :param str service_business_status: The business status of the terminal node service..
        :param str service_description: The description of the terminal node service.
        :param str service_domain: The domain of service.
        :param str service_id: The ID of the Vpc Endpoint Service.
        :param str status: The Status of Vpc Endpoint Service.
        :param str vpc_endpoint_service_name: The name of Vpc Endpoint Service.
        """
        pulumi.set(__self__, "auto_accept_connection", auto_accept_connection)
        pulumi.set(__self__, "connect_bandwidth", connect_bandwidth)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "service_business_status", service_business_status)
        pulumi.set(__self__, "service_description", service_description)
        pulumi.set(__self__, "service_domain", service_domain)
        pulumi.set(__self__, "service_id", service_id)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "vpc_endpoint_service_name", vpc_endpoint_service_name)

    @property
    @pulumi.getter(name="autoAcceptConnection")
    def auto_accept_connection(self) -> bool:
        """
        Whether to automatically accept terminal node connections..
        """
        return pulumi.get(self, "auto_accept_connection")

    @property
    @pulumi.getter(name="connectBandwidth")
    def connect_bandwidth(self) -> int:
        """
        The connection bandwidth.
        """
        return pulumi.get(self, "connect_bandwidth")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Vpc Endpoint Service.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="serviceBusinessStatus")
    def service_business_status(self) -> str:
        """
        The business status of the terminal node service..
        """
        return pulumi.get(self, "service_business_status")

    @property
    @pulumi.getter(name="serviceDescription")
    def service_description(self) -> str:
        """
        The description of the terminal node service.
        """
        return pulumi.get(self, "service_description")

    @property
    @pulumi.getter(name="serviceDomain")
    def service_domain(self) -> str:
        """
        The domain of service.
        """
        return pulumi.get(self, "service_domain")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        """
        The ID of the Vpc Endpoint Service.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The Status of Vpc Endpoint Service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcEndpointServiceName")
    def vpc_endpoint_service_name(self) -> str:
        """
        The name of Vpc Endpoint Service.
        """
        return pulumi.get(self, "vpc_endpoint_service_name")


@pulumi.output_type
class GetVpcEndpointsEndpointResult(dict):
    def __init__(__self__, *,
                 bandwidth: int,
                 connection_status: str,
                 endpoint_business_status: str,
                 endpoint_description: str,
                 endpoint_domain: str,
                 endpoint_id: str,
                 id: str,
                 security_group_ids: Sequence[str],
                 service_id: str,
                 service_name: str,
                 status: str,
                 vpc_endpoint_name: str,
                 vpc_id: str,
                 zones: Sequence['outputs.GetVpcEndpointsEndpointZoneResult']):
        """
        :param int bandwidth: The Bandwidth.
        :param str connection_status: The status of Connection.
        :param str endpoint_business_status: The status of Endpoint Business.
        :param str endpoint_description: The description of Vpc Endpoint.
        :param str endpoint_domain: The Endpoint Domain.
        :param str endpoint_id: The ID of the Vpc Endpoint.
        :param str id: The ID of the Vpc Endpoint.
        :param Sequence[str] security_group_ids: The security group associated with the terminal node network card.
        :param str service_id: The terminal node service associated with the terminal node.
        :param str service_name: The name of the terminal node service associated with the terminal node.
        :param str status: The status of Vpc Endpoint.
        :param str vpc_endpoint_name: The name of Vpc Endpoint.
        :param str vpc_id: The private network to which the terminal node belongs.
        :param Sequence['GetVpcEndpointsEndpointZoneArgs'] zones: Availability zone.
        """
        pulumi.set(__self__, "bandwidth", bandwidth)
        pulumi.set(__self__, "connection_status", connection_status)
        pulumi.set(__self__, "endpoint_business_status", endpoint_business_status)
        pulumi.set(__self__, "endpoint_description", endpoint_description)
        pulumi.set(__self__, "endpoint_domain", endpoint_domain)
        pulumi.set(__self__, "endpoint_id", endpoint_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "service_id", service_id)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "vpc_endpoint_name", vpc_endpoint_name)
        pulumi.set(__self__, "vpc_id", vpc_id)
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def bandwidth(self) -> int:
        """
        The Bandwidth.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> str:
        """
        The status of Connection.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter(name="endpointBusinessStatus")
    def endpoint_business_status(self) -> str:
        """
        The status of Endpoint Business.
        """
        return pulumi.get(self, "endpoint_business_status")

    @property
    @pulumi.getter(name="endpointDescription")
    def endpoint_description(self) -> str:
        """
        The description of Vpc Endpoint.
        """
        return pulumi.get(self, "endpoint_description")

    @property
    @pulumi.getter(name="endpointDomain")
    def endpoint_domain(self) -> str:
        """
        The Endpoint Domain.
        """
        return pulumi.get(self, "endpoint_domain")

    @property
    @pulumi.getter(name="endpointId")
    def endpoint_id(self) -> str:
        """
        The ID of the Vpc Endpoint.
        """
        return pulumi.get(self, "endpoint_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Vpc Endpoint.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Sequence[str]:
        """
        The security group associated with the terminal node network card.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> str:
        """
        The terminal node service associated with the terminal node.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        The name of the terminal node service associated with the terminal node.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of Vpc Endpoint.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcEndpointName")
    def vpc_endpoint_name(self) -> str:
        """
        The name of Vpc Endpoint.
        """
        return pulumi.get(self, "vpc_endpoint_name")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        The private network to which the terminal node belongs.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter
    def zones(self) -> Sequence['outputs.GetVpcEndpointsEndpointZoneResult']:
        """
        Availability zone.
        """
        return pulumi.get(self, "zones")


@pulumi.output_type
class GetVpcEndpointsEndpointZoneResult(dict):
    def __init__(__self__, *,
                 vswitch_id: str,
                 zone_id: str):
        """
        :param str vswitch_id: To create the vswitch of the terminal node network card in the available zone.
        :param str zone_id: Availability zone corresponding to terminal node service.
        """
        pulumi.set(__self__, "vswitch_id", vswitch_id)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> str:
        """
        To create the vswitch of the terminal node network card in the available zone.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        """
        Availability zone corresponding to terminal node service.
        """
        return pulumi.get(self, "zone_id")



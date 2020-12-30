# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['VpcEndpoint']


class VpcEndpoint(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 endpoint_description: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 vpc_endpoint_name: Optional[pulumi.Input[str]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcEndpointZoneArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Private Link Vpc Endpoint resource.

        For information about Private Link Vpc Endpoint and how to use it, see [What is Vpc Endpoint](https://help.aliyun.com/document_detail/120479.html).

        > **NOTE:** Available in v1.109.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.privatelink.VpcEndpoint("example",
            security_group_ids=["sg-ercx1234"],
            service_id="YourServiceId",
            vpc_id="YourVpcId")
        ```

        ## Import

        Private Link Vpc Endpoint can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:privatelink/vpcEndpoint:VpcEndpoint example <endpoint_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] dry_run: The dry run. Default to: `false`.
        :param pulumi.Input[str] endpoint_description: The description of Vpc Endpoint. The length is 2~256 characters and cannot start with `http://` and `https://`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The security group associated with the terminal node network card.
        :param pulumi.Input[str] service_id: The terminal node service associated with the terminal node.
        :param pulumi.Input[str] service_name: The name of the terminal node service associated with the terminal node.
        :param pulumi.Input[str] vpc_endpoint_name: The name of Vpc Endpoint. The length is between 2 and 128 characters, starting with English letters or Chinese, and can include numbers, hyphens (-) and underscores (_).
        :param pulumi.Input[str] vpc_id: The private network to which the terminal node belongs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcEndpointZoneArgs']]]] zones: Availability zone.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['dry_run'] = dry_run
            __props__['endpoint_description'] = endpoint_description
            if security_group_ids is None:
                raise TypeError("Missing required property 'security_group_ids'")
            __props__['security_group_ids'] = security_group_ids
            __props__['service_id'] = service_id
            __props__['service_name'] = service_name
            __props__['vpc_endpoint_name'] = vpc_endpoint_name
            if vpc_id is None:
                raise TypeError("Missing required property 'vpc_id'")
            __props__['vpc_id'] = vpc_id
            __props__['zones'] = zones
            __props__['bandwidth'] = None
            __props__['connection_status'] = None
            __props__['endpoint_business_status'] = None
            __props__['endpoint_domain'] = None
            __props__['status'] = None
        super(VpcEndpoint, __self__).__init__(
            'alicloud:privatelink/vpcEndpoint:VpcEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bandwidth: Optional[pulumi.Input[int]] = None,
            connection_status: Optional[pulumi.Input[str]] = None,
            dry_run: Optional[pulumi.Input[bool]] = None,
            endpoint_business_status: Optional[pulumi.Input[str]] = None,
            endpoint_description: Optional[pulumi.Input[str]] = None,
            endpoint_domain: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            service_id: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            vpc_endpoint_name: Optional[pulumi.Input[str]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None,
            zones: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcEndpointZoneArgs']]]]] = None) -> 'VpcEndpoint':
        """
        Get an existing VpcEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] bandwidth: The Bandwidth.
        :param pulumi.Input[str] connection_status: The status of Connection.
        :param pulumi.Input[bool] dry_run: The dry run. Default to: `false`.
        :param pulumi.Input[str] endpoint_business_status: The status of Endpoint Business.
        :param pulumi.Input[str] endpoint_description: The description of Vpc Endpoint. The length is 2~256 characters and cannot start with `http://` and `https://`.
        :param pulumi.Input[str] endpoint_domain: The Endpoint Domain.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The security group associated with the terminal node network card.
        :param pulumi.Input[str] service_id: The terminal node service associated with the terminal node.
        :param pulumi.Input[str] service_name: The name of the terminal node service associated with the terminal node.
        :param pulumi.Input[str] status: The status of Vpc Endpoint.
        :param pulumi.Input[str] vpc_endpoint_name: The name of Vpc Endpoint. The length is between 2 and 128 characters, starting with English letters or Chinese, and can include numbers, hyphens (-) and underscores (_).
        :param pulumi.Input[str] vpc_id: The private network to which the terminal node belongs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpcEndpointZoneArgs']]]] zones: Availability zone.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bandwidth"] = bandwidth
        __props__["connection_status"] = connection_status
        __props__["dry_run"] = dry_run
        __props__["endpoint_business_status"] = endpoint_business_status
        __props__["endpoint_description"] = endpoint_description
        __props__["endpoint_domain"] = endpoint_domain
        __props__["security_group_ids"] = security_group_ids
        __props__["service_id"] = service_id
        __props__["service_name"] = service_name
        __props__["status"] = status
        __props__["vpc_endpoint_name"] = vpc_endpoint_name
        __props__["vpc_id"] = vpc_id
        __props__["zones"] = zones
        return VpcEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Output[int]:
        """
        The Bandwidth.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> pulumi.Output[str]:
        """
        The status of Connection.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> pulumi.Output[Optional[bool]]:
        """
        The dry run. Default to: `false`.
        """
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter(name="endpointBusinessStatus")
    def endpoint_business_status(self) -> pulumi.Output[str]:
        """
        The status of Endpoint Business.
        """
        return pulumi.get(self, "endpoint_business_status")

    @property
    @pulumi.getter(name="endpointDescription")
    def endpoint_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of Vpc Endpoint. The length is 2~256 characters and cannot start with `http://` and `https://`.
        """
        return pulumi.get(self, "endpoint_description")

    @property
    @pulumi.getter(name="endpointDomain")
    def endpoint_domain(self) -> pulumi.Output[str]:
        """
        The Endpoint Domain.
        """
        return pulumi.get(self, "endpoint_domain")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The security group associated with the terminal node network card.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[Optional[str]]:
        """
        The terminal node service associated with the terminal node.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The name of the terminal node service associated with the terminal node.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of Vpc Endpoint.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcEndpointName")
    def vpc_endpoint_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of Vpc Endpoint. The length is between 2 and 128 characters, starting with English letters or Chinese, and can include numbers, hyphens (-) and underscores (_).
        """
        return pulumi.get(self, "vpc_endpoint_name")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The private network to which the terminal node belongs.
        """
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence['outputs.VpcEndpointZone']]]:
        """
        Availability zone.
        """
        return pulumi.get(self, "zones")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


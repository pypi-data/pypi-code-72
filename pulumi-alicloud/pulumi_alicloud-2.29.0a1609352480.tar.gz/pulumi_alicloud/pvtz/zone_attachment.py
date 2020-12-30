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

__all__ = ['ZoneAttachment']


class ZoneAttachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 user_client_ip: Optional[pulumi.Input[str]] = None,
                 vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneAttachmentVpcArgs']]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Private Zone attachment can be imported using the id(same with `zone_id`), e.g.

        ```sh
         $ pulumi import alicloud:pvtz/zoneAttachment:ZoneAttachment example abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] lang: The language of code.
        :param pulumi.Input[str] user_client_ip: The user custom IP address.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_ids: The id List of the VPC with the same region, for example:["vpc-1","vpc-2"].
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneAttachmentVpcArgs']]]] vpcs: The List of the VPC:
        :param pulumi.Input[str] zone_id: The name of the Private Zone Record.
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

            __props__['lang'] = lang
            __props__['user_client_ip'] = user_client_ip
            __props__['vpc_ids'] = vpc_ids
            __props__['vpcs'] = vpcs
            if zone_id is None:
                raise TypeError("Missing required property 'zone_id'")
            __props__['zone_id'] = zone_id
        super(ZoneAttachment, __self__).__init__(
            'alicloud:pvtz/zoneAttachment:ZoneAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            lang: Optional[pulumi.Input[str]] = None,
            user_client_ip: Optional[pulumi.Input[str]] = None,
            vpc_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            vpcs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneAttachmentVpcArgs']]]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ZoneAttachment':
        """
        Get an existing ZoneAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] lang: The language of code.
        :param pulumi.Input[str] user_client_ip: The user custom IP address.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] vpc_ids: The id List of the VPC with the same region, for example:["vpc-1","vpc-2"].
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ZoneAttachmentVpcArgs']]]] vpcs: The List of the VPC:
        :param pulumi.Input[str] zone_id: The name of the Private Zone Record.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["lang"] = lang
        __props__["user_client_ip"] = user_client_ip
        __props__["vpc_ids"] = vpc_ids
        __props__["vpcs"] = vpcs
        __props__["zone_id"] = zone_id
        return ZoneAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def lang(self) -> pulumi.Output[Optional[str]]:
        """
        The language of code.
        """
        return pulumi.get(self, "lang")

    @property
    @pulumi.getter(name="userClientIp")
    def user_client_ip(self) -> pulumi.Output[Optional[str]]:
        """
        The user custom IP address.
        """
        return pulumi.get(self, "user_client_ip")

    @property
    @pulumi.getter(name="vpcIds")
    def vpc_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The id List of the VPC with the same region, for example:["vpc-1","vpc-2"].
        """
        return pulumi.get(self, "vpc_ids")

    @property
    @pulumi.getter
    def vpcs(self) -> pulumi.Output[Sequence['outputs.ZoneAttachmentVpc']]:
        """
        The List of the VPC:
        """
        return pulumi.get(self, "vpcs")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The name of the Private Zone Record.
        """
        return pulumi.get(self, "zone_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


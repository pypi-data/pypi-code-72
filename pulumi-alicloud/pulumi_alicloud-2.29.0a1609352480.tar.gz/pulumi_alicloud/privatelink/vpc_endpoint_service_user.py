# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['VpcEndpointServiceUser']


class VpcEndpointServiceUser(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 service_id: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Private Link Vpc Endpoint Service User resource.

        For information about Private Link Vpc Endpoint Service User and how to use it, see [What is Vpc Endpoint Service User](https://help.aliyun.com/document_detail/183545.html).

        > **NOTE:** Available in v1.110.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.privatelink.VpcEndpointServiceUser("example",
            service_id="epsrv-gw81c6xxxxxx",
            user_id="YourRamUserId")
        ```

        ## Import

        Private Link Vpc Endpoint Service User can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:privatelink/vpcEndpointServiceUser:VpcEndpointServiceUser example <service_id>:<user_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] service_id: The Id of Vpc Endpoint Service.
        :param pulumi.Input[str] user_id: The Id of Ram User.
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
            if service_id is None:
                raise TypeError("Missing required property 'service_id'")
            __props__['service_id'] = service_id
            if user_id is None:
                raise TypeError("Missing required property 'user_id'")
            __props__['user_id'] = user_id
        super(VpcEndpointServiceUser, __self__).__init__(
            'alicloud:privatelink/vpcEndpointServiceUser:VpcEndpointServiceUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dry_run: Optional[pulumi.Input[bool]] = None,
            service_id: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'VpcEndpointServiceUser':
        """
        Get an existing VpcEndpointServiceUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] dry_run: The dry run.
        :param pulumi.Input[str] service_id: The Id of Vpc Endpoint Service.
        :param pulumi.Input[str] user_id: The Id of Ram User.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["dry_run"] = dry_run
        __props__["service_id"] = service_id
        __props__["user_id"] = user_id
        return VpcEndpointServiceUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> pulumi.Output[Optional[bool]]:
        """
        The dry run.
        """
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter(name="serviceId")
    def service_id(self) -> pulumi.Output[str]:
        """
        The Id of Vpc Endpoint Service.
        """
        return pulumi.get(self, "service_id")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The Id of Ram User.
        """
        return pulumi.get(self, "user_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Instance']


class Instance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_security: Optional[pulumi.Input[str]] = None,
                 domain_numbers: Optional[pulumi.Input[str]] = None,
                 payment_type: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 renew_period: Optional[pulumi.Input[int]] = None,
                 renewal_status: Optional[pulumi.Input[str]] = None,
                 version_code: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        DNS instance be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:dns/instance:Instance example dns-cn-v0h1ldjhfff
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_security: DNS security level. Valid values: `no`, `basic`, `advanced`.
        :param pulumi.Input[str] domain_numbers: Number of domain names bound.
        :param pulumi.Input[int] period: Creating a pre-paid instance, it must be set, the unit is month, please enter an integer multiple of 12 for annually paid products.
        :param pulumi.Input[int] renew_period: Automatic renewal period, the unit is month. When setting RenewalStatus to AutoRenewal, it must be set.
        :param pulumi.Input[str] renewal_status: Automatic renewal status. Valid values: `AutoRenewal`, `ManualRenewal`, default to `ManualRenewal`.
        :param pulumi.Input[str] version_code: Paid package version. Valid values: `version_personal`, `version_enterprise_basic`, `version_enterprise_advanced`.
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

            if dns_security is None:
                raise TypeError("Missing required property 'dns_security'")
            __props__['dns_security'] = dns_security
            if domain_numbers is None:
                raise TypeError("Missing required property 'domain_numbers'")
            __props__['domain_numbers'] = domain_numbers
            __props__['payment_type'] = payment_type
            __props__['period'] = period
            __props__['renew_period'] = renew_period
            __props__['renewal_status'] = renewal_status
            if version_code is None:
                raise TypeError("Missing required property 'version_code'")
            __props__['version_code'] = version_code
            __props__['version_name'] = None
        super(Instance, __self__).__init__(
            'alicloud:dns/instance:Instance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dns_security: Optional[pulumi.Input[str]] = None,
            domain_numbers: Optional[pulumi.Input[str]] = None,
            payment_type: Optional[pulumi.Input[str]] = None,
            period: Optional[pulumi.Input[int]] = None,
            renew_period: Optional[pulumi.Input[int]] = None,
            renewal_status: Optional[pulumi.Input[str]] = None,
            version_code: Optional[pulumi.Input[str]] = None,
            version_name: Optional[pulumi.Input[str]] = None) -> 'Instance':
        """
        Get an existing Instance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_security: DNS security level. Valid values: `no`, `basic`, `advanced`.
        :param pulumi.Input[str] domain_numbers: Number of domain names bound.
        :param pulumi.Input[int] period: Creating a pre-paid instance, it must be set, the unit is month, please enter an integer multiple of 12 for annually paid products.
        :param pulumi.Input[int] renew_period: Automatic renewal period, the unit is month. When setting RenewalStatus to AutoRenewal, it must be set.
        :param pulumi.Input[str] renewal_status: Automatic renewal status. Valid values: `AutoRenewal`, `ManualRenewal`, default to `ManualRenewal`.
        :param pulumi.Input[str] version_code: Paid package version. Valid values: `version_personal`, `version_enterprise_basic`, `version_enterprise_advanced`.
        :param pulumi.Input[str] version_name: Paid package version name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["dns_security"] = dns_security
        __props__["domain_numbers"] = domain_numbers
        __props__["payment_type"] = payment_type
        __props__["period"] = period
        __props__["renew_period"] = renew_period
        __props__["renewal_status"] = renewal_status
        __props__["version_code"] = version_code
        __props__["version_name"] = version_name
        return Instance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dnsSecurity")
    def dns_security(self) -> pulumi.Output[str]:
        """
        DNS security level. Valid values: `no`, `basic`, `advanced`.
        """
        return pulumi.get(self, "dns_security")

    @property
    @pulumi.getter(name="domainNumbers")
    def domain_numbers(self) -> pulumi.Output[str]:
        """
        Number of domain names bound.
        """
        return pulumi.get(self, "domain_numbers")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[int]]:
        """
        Creating a pre-paid instance, it must be set, the unit is month, please enter an integer multiple of 12 for annually paid products.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="renewPeriod")
    def renew_period(self) -> pulumi.Output[Optional[int]]:
        """
        Automatic renewal period, the unit is month. When setting RenewalStatus to AutoRenewal, it must be set.
        """
        return pulumi.get(self, "renew_period")

    @property
    @pulumi.getter(name="renewalStatus")
    def renewal_status(self) -> pulumi.Output[Optional[str]]:
        """
        Automatic renewal status. Valid values: `AutoRenewal`, `ManualRenewal`, default to `ManualRenewal`.
        """
        return pulumi.get(self, "renewal_status")

    @property
    @pulumi.getter(name="versionCode")
    def version_code(self) -> pulumi.Output[str]:
        """
        Paid package version. Valid values: `version_personal`, `version_enterprise_basic`, `version_enterprise_advanced`.
        """
        return pulumi.get(self, "version_code")

    @property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Output[str]:
        """
        Paid package version name.
        """
        return pulumi.get(self, "version_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


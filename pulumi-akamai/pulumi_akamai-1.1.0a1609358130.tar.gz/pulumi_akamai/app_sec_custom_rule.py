# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['AppSecCustomRule']


class AppSecCustomRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_id: Optional[pulumi.Input[int]] = None,
                 rules: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The `AppSecCustomRule` resource allows you to create or modify a custom rule associated with a given security configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] config_id: The ID of the security configuration to use.
        :param pulumi.Input[str] rules: The name of a JSON file containing a custom rule definition ([format](https://developer.akamai.com/api/cloud_security/application_security/v1.html#postcustomrules)).
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

            if config_id is None and not opts.urn:
                raise TypeError("Missing required property 'config_id'")
            __props__['config_id'] = config_id
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__['rules'] = rules
            __props__['custom_rule_id'] = None
        super(AppSecCustomRule, __self__).__init__(
            'akamai:index/appSecCustomRule:AppSecCustomRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config_id: Optional[pulumi.Input[int]] = None,
            custom_rule_id: Optional[pulumi.Input[int]] = None,
            rules: Optional[pulumi.Input[str]] = None) -> 'AppSecCustomRule':
        """
        Get an existing AppSecCustomRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] config_id: The ID of the security configuration to use.
        :param pulumi.Input[int] custom_rule_id: The ID of the custom rule.
        :param pulumi.Input[str] rules: The name of a JSON file containing a custom rule definition ([format](https://developer.akamai.com/api/cloud_security/application_security/v1.html#postcustomrules)).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["config_id"] = config_id
        __props__["custom_rule_id"] = custom_rule_id
        __props__["rules"] = rules
        return AppSecCustomRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Output[int]:
        """
        The ID of the security configuration to use.
        """
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter(name="customRuleId")
    def custom_rule_id(self) -> pulumi.Output[int]:
        """
        The ID of the custom rule.
        """
        return pulumi.get(self, "custom_rule_id")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[str]:
        """
        The name of a JSON file containing a custom rule definition ([format](https://developer.akamai.com/api/cloud_security/application_security/v1.html#postcustomrules)).
        """
        return pulumi.get(self, "rules")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


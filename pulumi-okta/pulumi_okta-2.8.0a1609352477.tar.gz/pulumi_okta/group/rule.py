# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Rule']


class Rule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expression_type: Optional[pulumi.Input[str]] = None,
                 expression_value: Optional[pulumi.Input[str]] = None,
                 group_assignments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an Okta Group Rule.

        This resource allows you to create and configure an Okta Group Rule.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.group.Rule("example",
            expression_type="urn:okta:expression:1.0",
            expression_value="String.startsWith(user.firstName,\"andy\")",
            group_assignments=["<group id>"],
            status="ACTIVE")
        ```

        ## Import

        An Okta Group Rule can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:group/rule:Rule example <group rule id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] expression_type: The expression type to use to invoke the rule. The default is `"urn:okta:expression:1.0"`.
        :param pulumi.Input[str] expression_value: The expression value.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_assignments: The list of group ids to assign the users to.
        :param pulumi.Input[str] name: The name of the Group Rule.
        :param pulumi.Input[str] status: The status of the group rule.
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

            __props__['expression_type'] = expression_type
            if expression_value is None and not opts.urn:
                raise TypeError("Missing required property 'expression_value'")
            __props__['expression_value'] = expression_value
            if group_assignments is None and not opts.urn:
                raise TypeError("Missing required property 'group_assignments'")
            __props__['group_assignments'] = group_assignments
            __props__['name'] = name
            __props__['status'] = status
        super(Rule, __self__).__init__(
            'okta:group/rule:Rule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            expression_type: Optional[pulumi.Input[str]] = None,
            expression_value: Optional[pulumi.Input[str]] = None,
            group_assignments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'Rule':
        """
        Get an existing Rule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] expression_type: The expression type to use to invoke the rule. The default is `"urn:okta:expression:1.0"`.
        :param pulumi.Input[str] expression_value: The expression value.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_assignments: The list of group ids to assign the users to.
        :param pulumi.Input[str] name: The name of the Group Rule.
        :param pulumi.Input[str] status: The status of the group rule.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["expression_type"] = expression_type
        __props__["expression_value"] = expression_value
        __props__["group_assignments"] = group_assignments
        __props__["name"] = name
        __props__["status"] = status
        return Rule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="expressionType")
    def expression_type(self) -> pulumi.Output[Optional[str]]:
        """
        The expression type to use to invoke the rule. The default is `"urn:okta:expression:1.0"`.
        """
        return pulumi.get(self, "expression_type")

    @property
    @pulumi.getter(name="expressionValue")
    def expression_value(self) -> pulumi.Output[str]:
        """
        The expression value.
        """
        return pulumi.get(self, "expression_value")

    @property
    @pulumi.getter(name="groupAssignments")
    def group_assignments(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of group ids to assign the users to.
        """
        return pulumi.get(self, "group_assignments")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Group Rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the group rule.
        """
        return pulumi.get(self, "status")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


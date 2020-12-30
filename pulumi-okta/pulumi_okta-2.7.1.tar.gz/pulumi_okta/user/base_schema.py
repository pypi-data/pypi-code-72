# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['BaseSchema']


class BaseSchema(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 index: Optional[pulumi.Input[str]] = None,
                 master: Optional[pulumi.Input[str]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[str]] = None,
                 required: Optional[pulumi.Input[bool]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a User Base Schema property.

        This resource allows you to configure a base user schema property.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.user.BaseSchema("example",
            index="customPropertyName",
            master="OKTA",
            title="customPropertyName",
            type="string",
            user_type=data["okta_user_type"]["example"]["id"])
        ```

        ## Import

        User schema property of default user type can be imported via the property index.

        ```sh
         $ pulumi import okta:user/baseSchema:BaseSchema example <property name>
        ```

         User schema property of custom user type can be imported via user type id and property index

        ```sh
         $ pulumi import okta:user/baseSchema:BaseSchema example <user type id>.<property name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] index: The property name.
        :param pulumi.Input[str] master: Master priority for the user schema property. It can be set to `"PROFILE_MASTER"` or `"OKTA"`.
        :param pulumi.Input[str] pattern: The validation pattern to use for the subschema, only available for `login` property. Must be in form of `.+`, or `[<pattern>]+`.
        :param pulumi.Input[str] permissions: Access control permissions for the property. It can be set to `"READ_WRITE"`, `"READ_ONLY"`, `"HIDE"`.
        :param pulumi.Input[bool] required: Whether the property is required for this application's users.
        :param pulumi.Input[str] title: The property display name.
        :param pulumi.Input[str] type: The type of the schema property. It can be `"string"`, `"boolean"`, `"number"`, `"integer"`, `"array"`, or `"object"`.
        :param pulumi.Input[str] user_type: User type ID
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

            if index is None and not opts.urn:
                raise TypeError("Missing required property 'index'")
            __props__['index'] = index
            __props__['master'] = master
            __props__['pattern'] = pattern
            __props__['permissions'] = permissions
            __props__['required'] = required
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__['title'] = title
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['user_type'] = user_type
        super(BaseSchema, __self__).__init__(
            'okta:user/baseSchema:BaseSchema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            index: Optional[pulumi.Input[str]] = None,
            master: Optional[pulumi.Input[str]] = None,
            pattern: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[str]] = None,
            required: Optional[pulumi.Input[bool]] = None,
            title: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            user_type: Optional[pulumi.Input[str]] = None) -> 'BaseSchema':
        """
        Get an existing BaseSchema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] index: The property name.
        :param pulumi.Input[str] master: Master priority for the user schema property. It can be set to `"PROFILE_MASTER"` or `"OKTA"`.
        :param pulumi.Input[str] pattern: The validation pattern to use for the subschema, only available for `login` property. Must be in form of `.+`, or `[<pattern>]+`.
        :param pulumi.Input[str] permissions: Access control permissions for the property. It can be set to `"READ_WRITE"`, `"READ_ONLY"`, `"HIDE"`.
        :param pulumi.Input[bool] required: Whether the property is required for this application's users.
        :param pulumi.Input[str] title: The property display name.
        :param pulumi.Input[str] type: The type of the schema property. It can be `"string"`, `"boolean"`, `"number"`, `"integer"`, `"array"`, or `"object"`.
        :param pulumi.Input[str] user_type: User type ID
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["index"] = index
        __props__["master"] = master
        __props__["pattern"] = pattern
        __props__["permissions"] = permissions
        __props__["required"] = required
        __props__["title"] = title
        __props__["type"] = type
        __props__["user_type"] = user_type
        return BaseSchema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def index(self) -> pulumi.Output[str]:
        """
        The property name.
        """
        return pulumi.get(self, "index")

    @property
    @pulumi.getter
    def master(self) -> pulumi.Output[Optional[str]]:
        """
        Master priority for the user schema property. It can be set to `"PROFILE_MASTER"` or `"OKTA"`.
        """
        return pulumi.get(self, "master")

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Output[Optional[str]]:
        """
        The validation pattern to use for the subschema, only available for `login` property. Must be in form of `.+`, or `[<pattern>]+`.
        """
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[str]]:
        """
        Access control permissions for the property. It can be set to `"READ_WRITE"`, `"READ_ONLY"`, `"HIDE"`.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def required(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the property is required for this application's users.
        """
        return pulumi.get(self, "required")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The property display name.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the schema property. It can be `"string"`, `"boolean"`, `"number"`, `"integer"`, `"array"`, or `"object"`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userType")
    def user_type(self) -> pulumi.Output[Optional[str]]:
        """
        User type ID
        """
        return pulumi.get(self, "user_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


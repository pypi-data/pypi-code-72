# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['ClientGrant']


class ClientGrant(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audience: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Auth0 uses various grant types, or methods by which you grant limited access to your resources to another entity without exposing credentials. The OAuth 2.0 protocol supports several types of grants, which allow different types of access. This resource allows you to create and manage client grants used with configured Auth0 clients.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_auth0 as auth0

        my_client = auth0.Client("myClient")
        my_resource_server = auth0.ResourceServer("myResourceServer",
            identifier="https://api.example.com/client-grant",
            scopes=[
                auth0.ResourceServerScopeArgs(
                    description="Create foos",
                    value="create:foo",
                ),
                auth0.ResourceServerScopeArgs(
                    description="Create bars",
                    value="create:bar",
                ),
            ])
        my_client_grant = auth0.ClientGrant("myClientGrant",
            audience=my_resource_server.identifier,
            client_id=my_client.id,
            scopes=["create:foo"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audience: String. Audience or API Identifier for this grant.
        :param pulumi.Input[str] client_id: String. ID of the client for this grant.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: List(String). Permissions (scopes) included in this grant.
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

            if audience is None:
                raise TypeError("Missing required property 'audience'")
            __props__['audience'] = audience
            if client_id is None:
                raise TypeError("Missing required property 'client_id'")
            __props__['client_id'] = client_id
            if scopes is None:
                raise TypeError("Missing required property 'scopes'")
            __props__['scopes'] = scopes
        super(ClientGrant, __self__).__init__(
            'auth0:index/clientGrant:ClientGrant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            audience: Optional[pulumi.Input[str]] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'ClientGrant':
        """
        Get an existing ClientGrant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audience: String. Audience or API Identifier for this grant.
        :param pulumi.Input[str] client_id: String. ID of the client for this grant.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: List(String). Permissions (scopes) included in this grant.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["audience"] = audience
        __props__["client_id"] = client_id
        __props__["scopes"] = scopes
        return ClientGrant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def audience(self) -> pulumi.Output[str]:
        """
        String. Audience or API Identifier for this grant.
        """
        return pulumi.get(self, "audience")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        String. ID of the client for this grant.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        List(String). Permissions (scopes) included in this grant.
        """
        return pulumi.get(self, "scopes")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


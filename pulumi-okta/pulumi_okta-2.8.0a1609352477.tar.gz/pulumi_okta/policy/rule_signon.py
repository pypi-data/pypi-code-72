# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['RuleSignon']


class RuleSignon(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access: Optional[pulumi.Input[str]] = None,
                 authtype: Optional[pulumi.Input[str]] = None,
                 mfa_lifetime: Optional[pulumi.Input[int]] = None,
                 mfa_prompt: Optional[pulumi.Input[str]] = None,
                 mfa_remember_device: Optional[pulumi.Input[bool]] = None,
                 mfa_required: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_connection: Optional[pulumi.Input[str]] = None,
                 network_excludes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 network_includes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 policyid: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 session_idle: Optional[pulumi.Input[int]] = None,
                 session_lifetime: Optional[pulumi.Input[int]] = None,
                 session_persistent: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 users_excludeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a Sign On Policy Rule.

        ## Import

        A Policy Rule can be imported via the Policy and Rule ID.

        ```sh
         $ pulumi import okta:policy/ruleSignon:RuleSignon example <policy id>/<rule id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access: Allow or deny access based on the rule conditions: `"ALLOW"` or `"DENY"`. The default is `"ALLOW"`.
        :param pulumi.Input[str] authtype: Authentication entrypoint: `"ANY"` or `"RADIUS"`.
        :param pulumi.Input[int] mfa_lifetime: Elapsed time before the next MFA challenge.
        :param pulumi.Input[str] mfa_prompt: Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: `"DEVICE"`, `"SESSION"` or `"ALWAYS"`.
        :param pulumi.Input[bool] mfa_remember_device: Remember MFA device. The default `false`.
        :param pulumi.Input[bool] mfa_required: Require MFA. By default is `false`.
        :param pulumi.Input[str] name: Policy Rule Name.
        :param pulumi.Input[str] network_connection: Network selection mode: `"ANYWHERE"`, `"ZONE"`, `"ON_NETWORK"`, or `"OFF_NETWORK"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] network_excludes: The network zones to exclude. Conflicts with `network_includes`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] network_includes: The network zones to include. Conflicts with `network_excludes`.
        :param pulumi.Input[str] policyid: Policy ID.
        :param pulumi.Input[int] priority: Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.
        :param pulumi.Input[int] session_idle: Max minutes a session can be idle.",
        :param pulumi.Input[int] session_lifetime: Max minutes a session is active: Disable = 0.
        :param pulumi.Input[bool] session_persistent: Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session cookies.
        :param pulumi.Input[str] status: Policy Rule Status: `"ACTIVE"` or `"INACTIVE"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] users_excludeds: Set of User IDs to Exclude
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

            __props__['access'] = access
            __props__['authtype'] = authtype
            __props__['mfa_lifetime'] = mfa_lifetime
            __props__['mfa_prompt'] = mfa_prompt
            __props__['mfa_remember_device'] = mfa_remember_device
            __props__['mfa_required'] = mfa_required
            __props__['name'] = name
            __props__['network_connection'] = network_connection
            __props__['network_excludes'] = network_excludes
            __props__['network_includes'] = network_includes
            if policyid is None and not opts.urn:
                raise TypeError("Missing required property 'policyid'")
            __props__['policyid'] = policyid
            __props__['priority'] = priority
            __props__['session_idle'] = session_idle
            __props__['session_lifetime'] = session_lifetime
            __props__['session_persistent'] = session_persistent
            __props__['status'] = status
            __props__['users_excludeds'] = users_excludeds
        super(RuleSignon, __self__).__init__(
            'okta:policy/ruleSignon:RuleSignon',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access: Optional[pulumi.Input[str]] = None,
            authtype: Optional[pulumi.Input[str]] = None,
            mfa_lifetime: Optional[pulumi.Input[int]] = None,
            mfa_prompt: Optional[pulumi.Input[str]] = None,
            mfa_remember_device: Optional[pulumi.Input[bool]] = None,
            mfa_required: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_connection: Optional[pulumi.Input[str]] = None,
            network_excludes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            network_includes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            policyid: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            session_idle: Optional[pulumi.Input[int]] = None,
            session_lifetime: Optional[pulumi.Input[int]] = None,
            session_persistent: Optional[pulumi.Input[bool]] = None,
            status: Optional[pulumi.Input[str]] = None,
            users_excludeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'RuleSignon':
        """
        Get an existing RuleSignon resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access: Allow or deny access based on the rule conditions: `"ALLOW"` or `"DENY"`. The default is `"ALLOW"`.
        :param pulumi.Input[str] authtype: Authentication entrypoint: `"ANY"` or `"RADIUS"`.
        :param pulumi.Input[int] mfa_lifetime: Elapsed time before the next MFA challenge.
        :param pulumi.Input[str] mfa_prompt: Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: `"DEVICE"`, `"SESSION"` or `"ALWAYS"`.
        :param pulumi.Input[bool] mfa_remember_device: Remember MFA device. The default `false`.
        :param pulumi.Input[bool] mfa_required: Require MFA. By default is `false`.
        :param pulumi.Input[str] name: Policy Rule Name.
        :param pulumi.Input[str] network_connection: Network selection mode: `"ANYWHERE"`, `"ZONE"`, `"ON_NETWORK"`, or `"OFF_NETWORK"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] network_excludes: The network zones to exclude. Conflicts with `network_includes`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] network_includes: The network zones to include. Conflicts with `network_excludes`.
        :param pulumi.Input[str] policyid: Policy ID.
        :param pulumi.Input[int] priority: Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.
        :param pulumi.Input[int] session_idle: Max minutes a session can be idle.",
        :param pulumi.Input[int] session_lifetime: Max minutes a session is active: Disable = 0.
        :param pulumi.Input[bool] session_persistent: Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session cookies.
        :param pulumi.Input[str] status: Policy Rule Status: `"ACTIVE"` or `"INACTIVE"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] users_excludeds: Set of User IDs to Exclude
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access"] = access
        __props__["authtype"] = authtype
        __props__["mfa_lifetime"] = mfa_lifetime
        __props__["mfa_prompt"] = mfa_prompt
        __props__["mfa_remember_device"] = mfa_remember_device
        __props__["mfa_required"] = mfa_required
        __props__["name"] = name
        __props__["network_connection"] = network_connection
        __props__["network_excludes"] = network_excludes
        __props__["network_includes"] = network_includes
        __props__["policyid"] = policyid
        __props__["priority"] = priority
        __props__["session_idle"] = session_idle
        __props__["session_lifetime"] = session_lifetime
        __props__["session_persistent"] = session_persistent
        __props__["status"] = status
        __props__["users_excludeds"] = users_excludeds
        return RuleSignon(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def access(self) -> pulumi.Output[Optional[str]]:
        """
        Allow or deny access based on the rule conditions: `"ALLOW"` or `"DENY"`. The default is `"ALLOW"`.
        """
        return pulumi.get(self, "access")

    @property
    @pulumi.getter
    def authtype(self) -> pulumi.Output[Optional[str]]:
        """
        Authentication entrypoint: `"ANY"` or `"RADIUS"`.
        """
        return pulumi.get(self, "authtype")

    @property
    @pulumi.getter(name="mfaLifetime")
    def mfa_lifetime(self) -> pulumi.Output[Optional[int]]:
        """
        Elapsed time before the next MFA challenge.
        """
        return pulumi.get(self, "mfa_lifetime")

    @property
    @pulumi.getter(name="mfaPrompt")
    def mfa_prompt(self) -> pulumi.Output[Optional[str]]:
        """
        Prompt for MFA based on the device used, a factor session lifetime, or every sign on attempt: `"DEVICE"`, `"SESSION"` or `"ALWAYS"`.
        """
        return pulumi.get(self, "mfa_prompt")

    @property
    @pulumi.getter(name="mfaRememberDevice")
    def mfa_remember_device(self) -> pulumi.Output[Optional[bool]]:
        """
        Remember MFA device. The default `false`.
        """
        return pulumi.get(self, "mfa_remember_device")

    @property
    @pulumi.getter(name="mfaRequired")
    def mfa_required(self) -> pulumi.Output[Optional[bool]]:
        """
        Require MFA. By default is `false`.
        """
        return pulumi.get(self, "mfa_required")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Policy Rule Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkConnection")
    def network_connection(self) -> pulumi.Output[Optional[str]]:
        """
        Network selection mode: `"ANYWHERE"`, `"ZONE"`, `"ON_NETWORK"`, or `"OFF_NETWORK"`.
        """
        return pulumi.get(self, "network_connection")

    @property
    @pulumi.getter(name="networkExcludes")
    def network_excludes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The network zones to exclude. Conflicts with `network_includes`.
        """
        return pulumi.get(self, "network_excludes")

    @property
    @pulumi.getter(name="networkIncludes")
    def network_includes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The network zones to include. Conflicts with `network_excludes`.
        """
        return pulumi.get(self, "network_includes")

    @property
    @pulumi.getter
    def policyid(self) -> pulumi.Output[str]:
        """
        Policy ID.
        """
        return pulumi.get(self, "policyid")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Policy Rule Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid priority is provided. API defaults it to the last/lowest if not there.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="sessionIdle")
    def session_idle(self) -> pulumi.Output[Optional[int]]:
        """
        Max minutes a session can be idle.",
        """
        return pulumi.get(self, "session_idle")

    @property
    @pulumi.getter(name="sessionLifetime")
    def session_lifetime(self) -> pulumi.Output[Optional[int]]:
        """
        Max minutes a session is active: Disable = 0.
        """
        return pulumi.get(self, "session_lifetime")

    @property
    @pulumi.getter(name="sessionPersistent")
    def session_persistent(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether session cookies will last across browser sessions. Okta Administrators can never have persistent session cookies.
        """
        return pulumi.get(self, "session_persistent")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Policy Rule Status: `"ACTIVE"` or `"INACTIVE"`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="usersExcludeds")
    def users_excludeds(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Set of User IDs to Exclude
        """
        return pulumi.get(self, "users_excludeds")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


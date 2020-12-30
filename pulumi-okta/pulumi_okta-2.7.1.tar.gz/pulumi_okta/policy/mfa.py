# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Mfa']


class Mfa(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duo: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_u2f: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_webauthn: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 google_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 groups_includeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okta_call: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_password: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_push: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_question: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_sms: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rsa_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 symantec_vip: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 yubikey_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an MFA Policy.

        This resource allows you to create and configure an MFA Policy.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.policy.Mfa("example",
            description="Example",
            groups_includeds=[data["okta_group"]["everyone"]["id"]],
            okta_otp={
                "enroll": "REQUIRED",
            },
            status="ACTIVE")
        ```

        ## Import

        An MFA Policy can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:policy/mfa:Mfa example <policy id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Policy Description.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] duo: DUO MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fido_u2f: Fido U2F MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fido_webauthn: Fido Web Authn MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] google_otp: Google OTP MFA policy settings.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups_includeds: List of Group IDs to Include.
        :param pulumi.Input[str] name: Policy Name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_call: Okta Call MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_otp: Okta OTP MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_password: Okta Password MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_push: Okta Push MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_question: Okta Question MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_sms: Okta SMS MFA policy settings.
        :param pulumi.Input[int] priority: Priority of the policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] rsa_token: RSA Token MFA policy settings.
        :param pulumi.Input[str] status: Policy Status: `"ACTIVE"` or `"INACTIVE"`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] symantec_vip: Symantec VIP MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] yubikey_token: Yubikey Token MFA policy settings.
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

            __props__['description'] = description
            __props__['duo'] = duo
            __props__['fido_u2f'] = fido_u2f
            __props__['fido_webauthn'] = fido_webauthn
            __props__['google_otp'] = google_otp
            __props__['groups_includeds'] = groups_includeds
            __props__['name'] = name
            __props__['okta_call'] = okta_call
            __props__['okta_otp'] = okta_otp
            __props__['okta_password'] = okta_password
            __props__['okta_push'] = okta_push
            __props__['okta_question'] = okta_question
            __props__['okta_sms'] = okta_sms
            __props__['priority'] = priority
            __props__['rsa_token'] = rsa_token
            __props__['status'] = status
            __props__['symantec_vip'] = symantec_vip
            __props__['yubikey_token'] = yubikey_token
        super(Mfa, __self__).__init__(
            'okta:policy/mfa:Mfa',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            duo: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            fido_u2f: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            fido_webauthn: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            google_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            groups_includeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            okta_call: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_password: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_push: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_question: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_sms: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            rsa_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            symantec_vip: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            yubikey_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Mfa':
        """
        Get an existing Mfa resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Policy Description.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] duo: DUO MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fido_u2f: Fido U2F MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] fido_webauthn: Fido Web Authn MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] google_otp: Google OTP MFA policy settings.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups_includeds: List of Group IDs to Include.
        :param pulumi.Input[str] name: Policy Name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_call: Okta Call MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_otp: Okta OTP MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_password: Okta Password MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_push: Okta Push MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_question: Okta Question MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] okta_sms: Okta SMS MFA policy settings.
        :param pulumi.Input[int] priority: Priority of the policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] rsa_token: RSA Token MFA policy settings.
        :param pulumi.Input[str] status: Policy Status: `"ACTIVE"` or `"INACTIVE"`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] symantec_vip: Symantec VIP MFA policy settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] yubikey_token: Yubikey Token MFA policy settings.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["duo"] = duo
        __props__["fido_u2f"] = fido_u2f
        __props__["fido_webauthn"] = fido_webauthn
        __props__["google_otp"] = google_otp
        __props__["groups_includeds"] = groups_includeds
        __props__["name"] = name
        __props__["okta_call"] = okta_call
        __props__["okta_otp"] = okta_otp
        __props__["okta_password"] = okta_password
        __props__["okta_push"] = okta_push
        __props__["okta_question"] = okta_question
        __props__["okta_sms"] = okta_sms
        __props__["priority"] = priority
        __props__["rsa_token"] = rsa_token
        __props__["status"] = status
        __props__["symantec_vip"] = symantec_vip
        __props__["yubikey_token"] = yubikey_token
        return Mfa(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Policy Description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duo(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        DUO MFA policy settings.
        """
        return pulumi.get(self, "duo")

    @property
    @pulumi.getter(name="fidoU2f")
    def fido_u2f(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Fido U2F MFA policy settings.
        """
        return pulumi.get(self, "fido_u2f")

    @property
    @pulumi.getter(name="fidoWebauthn")
    def fido_webauthn(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Fido Web Authn MFA policy settings.
        """
        return pulumi.get(self, "fido_webauthn")

    @property
    @pulumi.getter(name="googleOtp")
    def google_otp(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Google OTP MFA policy settings.
        """
        return pulumi.get(self, "google_otp")

    @property
    @pulumi.getter(name="groupsIncludeds")
    def groups_includeds(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Group IDs to Include.
        """
        return pulumi.get(self, "groups_includeds")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Policy Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oktaCall")
    def okta_call(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Okta Call MFA policy settings.
        """
        return pulumi.get(self, "okta_call")

    @property
    @pulumi.getter(name="oktaOtp")
    def okta_otp(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Okta OTP MFA policy settings.
        """
        return pulumi.get(self, "okta_otp")

    @property
    @pulumi.getter(name="oktaPassword")
    def okta_password(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Okta Password MFA policy settings.
        """
        return pulumi.get(self, "okta_password")

    @property
    @pulumi.getter(name="oktaPush")
    def okta_push(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Okta Push MFA policy settings.
        """
        return pulumi.get(self, "okta_push")

    @property
    @pulumi.getter(name="oktaQuestion")
    def okta_question(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Okta Question MFA policy settings.
        """
        return pulumi.get(self, "okta_question")

    @property
    @pulumi.getter(name="oktaSms")
    def okta_sms(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Okta SMS MFA policy settings.
        """
        return pulumi.get(self, "okta_sms")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of the policy.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="rsaToken")
    def rsa_token(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        RSA Token MFA policy settings.
        """
        return pulumi.get(self, "rsa_token")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Policy Status: `"ACTIVE"` or `"INACTIVE"`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="symantecVip")
    def symantec_vip(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Symantec VIP MFA policy settings.
        """
        return pulumi.get(self, "symantec_vip")

    @property
    @pulumi.getter(name="yubikeyToken")
    def yubikey_token(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Yubikey Token MFA policy settings.
        """
        return pulumi.get(self, "yubikey_token")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


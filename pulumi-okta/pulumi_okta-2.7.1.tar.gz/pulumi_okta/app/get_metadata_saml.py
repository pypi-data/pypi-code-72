# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetMetadataSamlResult',
    'AwaitableGetMetadataSamlResult',
    'get_metadata_saml',
]

@pulumi.output_type
class GetMetadataSamlResult:
    """
    A collection of values returned by getMetadataSaml.
    """
    def __init__(__self__, app_id=None, certificate=None, entity_id=None, http_post_binding=None, http_redirect_binding=None, id=None, key_id=None, metadata=None, want_authn_requests_signed=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)
        if entity_id and not isinstance(entity_id, str):
            raise TypeError("Expected argument 'entity_id' to be a str")
        pulumi.set(__self__, "entity_id", entity_id)
        if http_post_binding and not isinstance(http_post_binding, str):
            raise TypeError("Expected argument 'http_post_binding' to be a str")
        pulumi.set(__self__, "http_post_binding", http_post_binding)
        if http_redirect_binding and not isinstance(http_redirect_binding, str):
            raise TypeError("Expected argument 'http_redirect_binding' to be a str")
        pulumi.set(__self__, "http_redirect_binding", http_redirect_binding)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_id and not isinstance(key_id, str):
            raise TypeError("Expected argument 'key_id' to be a str")
        pulumi.set(__self__, "key_id", key_id)
        if metadata and not isinstance(metadata, str):
            raise TypeError("Expected argument 'metadata' to be a str")
        pulumi.set(__self__, "metadata", metadata)
        if want_authn_requests_signed and not isinstance(want_authn_requests_signed, bool):
            raise TypeError("Expected argument 'want_authn_requests_signed' to be a bool")
        pulumi.set(__self__, "want_authn_requests_signed", want_authn_requests_signed)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> str:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def certificate(self) -> str:
        """
        public certificate from application metadata.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> str:
        """
        Entity URL for instance `https://www.okta.com/saml2/service-provider/sposcfdmlybtwkdcgtuf`.
        """
        return pulumi.get(self, "entity_id")

    @property
    @pulumi.getter(name="httpPostBinding")
    def http_post_binding(self) -> str:
        """
        urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Post location from the SAML metadata.
        """
        return pulumi.get(self, "http_post_binding")

    @property
    @pulumi.getter(name="httpRedirectBinding")
    def http_redirect_binding(self) -> str:
        """
        urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect location from the SAML metadata.
        """
        return pulumi.get(self, "http_redirect_binding")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> str:
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def metadata(self) -> str:
        """
        raw metadata of application.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter(name="wantAuthnRequestsSigned")
    def want_authn_requests_signed(self) -> bool:
        """
        Whether authn requests are signed.
        """
        return pulumi.get(self, "want_authn_requests_signed")


class AwaitableGetMetadataSamlResult(GetMetadataSamlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetadataSamlResult(
            app_id=self.app_id,
            certificate=self.certificate,
            entity_id=self.entity_id,
            http_post_binding=self.http_post_binding,
            http_redirect_binding=self.http_redirect_binding,
            id=self.id,
            key_id=self.key_id,
            metadata=self.metadata,
            want_authn_requests_signed=self.want_authn_requests_signed)


def get_metadata_saml(app_id: Optional[str] = None,
                      key_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetadataSamlResult:
    """
    Use this data source to retrieve the collaborators for a given repository.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.app.get_metadata_saml(app_id="<app id>",
        key_id="<cert key id>")
    ```


    :param str app_id: The application ID.
    :param str key_id: Certificate Key ID.
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['keyId'] = key_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('okta:app/getMetadataSaml:getMetadataSaml', __args__, opts=opts, typ=GetMetadataSamlResult).value

    return AwaitableGetMetadataSamlResult(
        app_id=__ret__.app_id,
        certificate=__ret__.certificate,
        entity_id=__ret__.entity_id,
        http_post_binding=__ret__.http_post_binding,
        http_redirect_binding=__ret__.http_redirect_binding,
        id=__ret__.id,
        key_id=__ret__.key_id,
        metadata=__ret__.metadata,
        want_authn_requests_signed=__ret__.want_authn_requests_signed)

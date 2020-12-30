# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetAccountAliasResult',
    'AwaitableGetAccountAliasResult',
    'get_account_alias',
]

@pulumi.output_type
class GetAccountAliasResult:
    """
    A collection of values returned by getAccountAlias.
    """
    def __init__(__self__, account_alias=None, id=None, output_file=None):
        if account_alias and not isinstance(account_alias, str):
            raise TypeError("Expected argument 'account_alias' to be a str")
        pulumi.set(__self__, "account_alias", account_alias)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)

    @property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> str:
        return pulumi.get(self, "account_alias")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")


class AwaitableGetAccountAliasResult(GetAccountAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountAliasResult(
            account_alias=self.account_alias,
            id=self.id,
            output_file=self.output_file)


def get_account_alias(output_file: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountAliasResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['outputFile'] = output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:ram/getAccountAlias:getAccountAlias', __args__, opts=opts, typ=GetAccountAliasResult).value

    return AwaitableGetAccountAliasResult(
        account_alias=__ret__.account_alias,
        id=__ret__.id,
        output_file=__ret__.output_file)

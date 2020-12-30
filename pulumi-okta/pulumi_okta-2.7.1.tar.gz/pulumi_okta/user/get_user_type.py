# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetUserTypeResult',
    'AwaitableGetUserTypeResult',
    'get_user_type',
]

@pulumi.output_type
class GetUserTypeResult:
    """
    A collection of values returned by getUserType.
    """
    def __init__(__self__, description=None, display_name=None, id=None, name=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        description of user type.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        display name of user type.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        id of user type.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        name of user type.
        """
        return pulumi.get(self, "name")


class AwaitableGetUserTypeResult(GetUserTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserTypeResult(
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            name=self.name)


def get_user_type(description: Optional[str] = None,
                  display_name: Optional[str] = None,
                  name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserTypeResult:
    """
    Use this data source to retrieve a user type from Okta.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_okta as okta

    example = okta.user.get_user_type(name="example")
    ```


    :param str description: description of user type.
    :param str display_name: display name of user type.
    :param str name: name of user type to retrieve.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['displayName'] = display_name
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('okta:user/getUserType:getUserType', __args__, opts=opts, typ=GetUserTypeResult).value

    return AwaitableGetUserTypeResult(
        description=__ret__.description,
        display_name=__ret__.display_name,
        id=__ret__.id,
        name=__ret__.name)

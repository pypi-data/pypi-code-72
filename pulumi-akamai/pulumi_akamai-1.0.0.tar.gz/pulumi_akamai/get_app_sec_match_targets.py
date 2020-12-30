# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetAppSecMatchTargetsResult',
    'AwaitableGetAppSecMatchTargetsResult',
    'get_app_sec_match_targets',
]

@pulumi.output_type
class GetAppSecMatchTargetsResult:
    """
    A collection of values returned by getAppSecMatchTargets.
    """
    def __init__(__self__, config_id=None, id=None, output_text=None, version=None):
        if config_id and not isinstance(config_id, int):
            raise TypeError("Expected argument 'config_id' to be a int")
        pulumi.set(__self__, "config_id", config_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if output_text and not isinstance(output_text, str):
            raise TypeError("Expected argument 'output_text' to be a str")
        pulumi.set(__self__, "output_text", output_text)
        if version and not isinstance(version, int):
            raise TypeError("Expected argument 'version' to be a int")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> int:
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="outputText")
    def output_text(self) -> str:
        """
        A tabular display showing the ID and Policy ID of all match targets associated with the specified security configuration and version.
        """
        return pulumi.get(self, "output_text")

    @property
    @pulumi.getter
    def version(self) -> int:
        return pulumi.get(self, "version")


class AwaitableGetAppSecMatchTargetsResult(GetAppSecMatchTargetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppSecMatchTargetsResult(
            config_id=self.config_id,
            id=self.id,
            output_text=self.output_text,
            version=self.version)


def get_app_sec_match_targets(config_id: Optional[int] = None,
                              version: Optional[int] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppSecMatchTargetsResult:
    """
    Use the `getAppSecMatchTargets` data source to retrieve information about the match targets associated with a given configuration version.

    ## Example Usage

    Basic usage:

    ```python
    import pulumi
    import pulumi_akamai as akamai

    configuration = akamai.get_app_sec_configuration(name="Akamai Tools")
    match_targets_app_sec_match_targets = akamai.get_app_sec_match_targets(config_id=configuration.config_id,
        version=configuration.latest_version)
    pulumi.export("matchTargets", match_targets_app_sec_match_targets.output_text)
    ```


    :param int config_id: The ID of the security configuration to use.
    :param int version: The version number of the security configuration to use.
    """
    __args__ = dict()
    __args__['configId'] = config_id
    __args__['version'] = version
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('akamai:index/getAppSecMatchTargets:getAppSecMatchTargets', __args__, opts=opts, typ=GetAppSecMatchTargetsResult).value

    return AwaitableGetAppSecMatchTargetsResult(
        config_id=__ret__.config_id,
        id=__ret__.id,
        output_text=__ret__.output_text,
        version=__ret__.version)

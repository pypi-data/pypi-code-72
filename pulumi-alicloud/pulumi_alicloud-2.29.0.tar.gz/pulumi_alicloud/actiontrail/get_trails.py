# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetTrailsResult',
    'AwaitableGetTrailsResult',
    'get_trails',
]

@pulumi.output_type
class GetTrailsResult:
    """
    A collection of values returned by getTrails.
    """
    def __init__(__self__, actiontrails=None, id=None, ids=None, include_shadow_trails=None, name_regex=None, names=None, output_file=None, status=None, trails=None):
        if actiontrails and not isinstance(actiontrails, list):
            raise TypeError("Expected argument 'actiontrails' to be a list")
        if actiontrails is not None:
            warnings.warn("""Field 'actiontrails' has been deprecated from version 1.95.0. Use 'trails' instead.""", DeprecationWarning)
            pulumi.log.warn("actiontrails is deprecated: Field 'actiontrails' has been deprecated from version 1.95.0. Use 'trails' instead.")

        pulumi.set(__self__, "actiontrails", actiontrails)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if include_shadow_trails and not isinstance(include_shadow_trails, bool):
            raise TypeError("Expected argument 'include_shadow_trails' to be a bool")
        pulumi.set(__self__, "include_shadow_trails", include_shadow_trails)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if trails and not isinstance(trails, list):
            raise TypeError("Expected argument 'trails' to be a list")
        pulumi.set(__self__, "trails", trails)

    @property
    @pulumi.getter
    def actiontrails(self) -> Sequence['outputs.GetTrailsActiontrailResult']:
        """
        Field `actiontrails` has been deprecated from version 1.95.0. Use `trails` instead."
        """
        return pulumi.get(self, "actiontrails")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of ActionTrail Trail ids. It is the same as trail name.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="includeShadowTrails")
    def include_shadow_trails(self) -> Optional[bool]:
        return pulumi.get(self, "include_shadow_trails")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of trail names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the ActionTrail Trail.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def trails(self) -> Sequence['outputs.GetTrailsTrailResult']:
        """
        A list of ActionTrail Trails. Each element contains the following attributes:
        """
        return pulumi.get(self, "trails")


class AwaitableGetTrailsResult(GetTrailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrailsResult(
            actiontrails=self.actiontrails,
            id=self.id,
            ids=self.ids,
            include_shadow_trails=self.include_shadow_trails,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status,
            trails=self.trails)


def get_trails(ids: Optional[Sequence[str]] = None,
               include_shadow_trails: Optional[bool] = None,
               name_regex: Optional[str] = None,
               output_file: Optional[str] = None,
               status: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrailsResult:
    """
    This data source provides a list of ActionTrail Trails in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in 1.95.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.actiontrail.get_trails(name_regex="tf-testacc-actiontrail")
    pulumi.export("trailName", default.trails[0].id)
    ```


    :param Sequence[str] ids: A list of ActionTrail Trail IDs. It is the same as trail name.
    :param bool include_shadow_trails: Whether to show shadow tracking. Default to `false`.
    :param str name_regex: A regex string to filter results by trail name.
    :param str status: Filter the results by status of the ActionTrail Trail. Valid values: `Disable`, `Enable`, `Fresh`.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['includeShadowTrails'] = include_shadow_trails
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:actiontrail/getTrails:getTrails', __args__, opts=opts, typ=GetTrailsResult).value

    return AwaitableGetTrailsResult(
        actiontrails=__ret__.actiontrails,
        id=__ret__.id,
        ids=__ret__.ids,
        include_shadow_trails=__ret__.include_shadow_trails,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        status=__ret__.status,
        trails=__ret__.trails)

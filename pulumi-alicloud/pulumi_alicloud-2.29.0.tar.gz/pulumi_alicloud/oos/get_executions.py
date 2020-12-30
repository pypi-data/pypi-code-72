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
    'GetExecutionsResult',
    'AwaitableGetExecutionsResult',
    'get_executions',
]

@pulumi.output_type
class GetExecutionsResult:
    """
    A collection of values returned by getExecutions.
    """
    def __init__(__self__, category=None, end_date=None, end_date_after=None, executed_by=None, executions=None, id=None, ids=None, include_child_execution=None, mode=None, output_file=None, parent_execution_id=None, ram_role=None, sort_field=None, sort_order=None, start_date_after=None, start_date_before=None, status=None, tags=None, template_name=None):
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if end_date and not isinstance(end_date, str):
            raise TypeError("Expected argument 'end_date' to be a str")
        pulumi.set(__self__, "end_date", end_date)
        if end_date_after and not isinstance(end_date_after, str):
            raise TypeError("Expected argument 'end_date_after' to be a str")
        pulumi.set(__self__, "end_date_after", end_date_after)
        if executed_by and not isinstance(executed_by, str):
            raise TypeError("Expected argument 'executed_by' to be a str")
        pulumi.set(__self__, "executed_by", executed_by)
        if executions and not isinstance(executions, list):
            raise TypeError("Expected argument 'executions' to be a list")
        pulumi.set(__self__, "executions", executions)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if include_child_execution and not isinstance(include_child_execution, bool):
            raise TypeError("Expected argument 'include_child_execution' to be a bool")
        pulumi.set(__self__, "include_child_execution", include_child_execution)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if parent_execution_id and not isinstance(parent_execution_id, str):
            raise TypeError("Expected argument 'parent_execution_id' to be a str")
        pulumi.set(__self__, "parent_execution_id", parent_execution_id)
        if ram_role and not isinstance(ram_role, str):
            raise TypeError("Expected argument 'ram_role' to be a str")
        pulumi.set(__self__, "ram_role", ram_role)
        if sort_field and not isinstance(sort_field, str):
            raise TypeError("Expected argument 'sort_field' to be a str")
        pulumi.set(__self__, "sort_field", sort_field)
        if sort_order and not isinstance(sort_order, str):
            raise TypeError("Expected argument 'sort_order' to be a str")
        pulumi.set(__self__, "sort_order", sort_order)
        if start_date_after and not isinstance(start_date_after, str):
            raise TypeError("Expected argument 'start_date_after' to be a str")
        pulumi.set(__self__, "start_date_after", start_date_after)
        if start_date_before and not isinstance(start_date_before, str):
            raise TypeError("Expected argument 'start_date_before' to be a str")
        pulumi.set(__self__, "start_date_before", start_date_before)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template_name and not isinstance(template_name, str):
            raise TypeError("Expected argument 'template_name' to be a str")
        pulumi.set(__self__, "template_name", template_name)

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[str]:
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="endDateAfter")
    def end_date_after(self) -> Optional[str]:
        return pulumi.get(self, "end_date_after")

    @property
    @pulumi.getter(name="executedBy")
    def executed_by(self) -> Optional[str]:
        return pulumi.get(self, "executed_by")

    @property
    @pulumi.getter
    def executions(self) -> Sequence['outputs.GetExecutionsExecutionResult']:
        """
        A list of OOS Executions. Each element contains the following attributes:
        """
        return pulumi.get(self, "executions")

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
        A list of OOS Execution ids.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="includeChildExecution")
    def include_child_execution(self) -> Optional[bool]:
        return pulumi.get(self, "include_child_execution")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="parentExecutionId")
    def parent_execution_id(self) -> Optional[str]:
        return pulumi.get(self, "parent_execution_id")

    @property
    @pulumi.getter(name="ramRole")
    def ram_role(self) -> Optional[str]:
        return pulumi.get(self, "ram_role")

    @property
    @pulumi.getter(name="sortField")
    def sort_field(self) -> Optional[str]:
        return pulumi.get(self, "sort_field")

    @property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[str]:
        return pulumi.get(self, "sort_order")

    @property
    @pulumi.getter(name="startDateAfter")
    def start_date_after(self) -> Optional[str]:
        return pulumi.get(self, "start_date_after")

    @property
    @pulumi.getter(name="startDateBefore")
    def start_date_before(self) -> Optional[str]:
        return pulumi.get(self, "start_date_before")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[str]:
        return pulumi.get(self, "template_name")


class AwaitableGetExecutionsResult(GetExecutionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExecutionsResult(
            category=self.category,
            end_date=self.end_date,
            end_date_after=self.end_date_after,
            executed_by=self.executed_by,
            executions=self.executions,
            id=self.id,
            ids=self.ids,
            include_child_execution=self.include_child_execution,
            mode=self.mode,
            output_file=self.output_file,
            parent_execution_id=self.parent_execution_id,
            ram_role=self.ram_role,
            sort_field=self.sort_field,
            sort_order=self.sort_order,
            start_date_after=self.start_date_after,
            start_date_before=self.start_date_before,
            status=self.status,
            tags=self.tags,
            template_name=self.template_name)


def get_executions(category: Optional[str] = None,
                   end_date: Optional[str] = None,
                   end_date_after: Optional[str] = None,
                   executed_by: Optional[str] = None,
                   ids: Optional[Sequence[str]] = None,
                   include_child_execution: Optional[bool] = None,
                   mode: Optional[str] = None,
                   output_file: Optional[str] = None,
                   parent_execution_id: Optional[str] = None,
                   ram_role: Optional[str] = None,
                   sort_field: Optional[str] = None,
                   sort_order: Optional[str] = None,
                   start_date_after: Optional[str] = None,
                   start_date_before: Optional[str] = None,
                   status: Optional[str] = None,
                   tags: Optional[Mapping[str, Any]] = None,
                   template_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExecutionsResult:
    """
    This data source provides a list of OOS Executions in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in v1.93.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.oos.get_executions(ids=["execution_id"],
        status="Success",
        template_name="name")
    pulumi.export("firstExecutionId", example.executions[0].id)
    ```


    :param str category: The category of template. Valid: `AlarmTrigger`, `EventTrigger`, `Other` and `TimerTrigger`.
    :param str end_date: The time when the execution was ended.
    :param str end_date_after: Execution whose end time is less than or equal to the specified time.
    :param str executed_by: The user who execute the template.
    :param Sequence[str] ids: A list of OOS Execution ids.
    :param bool include_child_execution: Whether to include sub-execution.
    :param str mode: The mode of OOS Execution. Valid: `Automatic`, `Debug`.
    :param str parent_execution_id: The id of parent OOS Execution.
    :param str ram_role: The role that executes the current template.
    :param str sort_field: The sort field.
    :param str sort_order: The sort order.
    :param str start_date_after: The execution whose start time is greater than or equal to the specified time.
    :param str start_date_before: The execution with start time less than or equal to the specified time.
    :param str status: The Status of OOS Execution. Valid: `Cancelled`, `Failed`, `Queued`, `Running`, `Started`, `Success`, `Waiting`.
    :param Mapping[str, Any] tags: A mapping of tags to assign to the resource.
    :param str template_name: The name of execution template.
    """
    __args__ = dict()
    __args__['category'] = category
    __args__['endDate'] = end_date
    __args__['endDateAfter'] = end_date_after
    __args__['executedBy'] = executed_by
    __args__['ids'] = ids
    __args__['includeChildExecution'] = include_child_execution
    __args__['mode'] = mode
    __args__['outputFile'] = output_file
    __args__['parentExecutionId'] = parent_execution_id
    __args__['ramRole'] = ram_role
    __args__['sortField'] = sort_field
    __args__['sortOrder'] = sort_order
    __args__['startDateAfter'] = start_date_after
    __args__['startDateBefore'] = start_date_before
    __args__['status'] = status
    __args__['tags'] = tags
    __args__['templateName'] = template_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:oos/getExecutions:getExecutions', __args__, opts=opts, typ=GetExecutionsResult).value

    return AwaitableGetExecutionsResult(
        category=__ret__.category,
        end_date=__ret__.end_date,
        end_date_after=__ret__.end_date_after,
        executed_by=__ret__.executed_by,
        executions=__ret__.executions,
        id=__ret__.id,
        ids=__ret__.ids,
        include_child_execution=__ret__.include_child_execution,
        mode=__ret__.mode,
        output_file=__ret__.output_file,
        parent_execution_id=__ret__.parent_execution_id,
        ram_role=__ret__.ram_role,
        sort_field=__ret__.sort_field,
        sort_order=__ret__.sort_order,
        start_date_after=__ret__.start_date_after,
        start_date_before=__ret__.start_date_before,
        status=__ret__.status,
        tags=__ret__.tags,
        template_name=__ret__.template_name)

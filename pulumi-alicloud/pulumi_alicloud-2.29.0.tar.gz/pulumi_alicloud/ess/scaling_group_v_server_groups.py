# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['ScalingGroupVServerGroups']


class ScalingGroupVServerGroups(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 vserver_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingGroupVServerGroupsVserverGroupArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Attaches/Detaches vserver groups to a specified scaling group.

        > **NOTE:** The load balancer of which vserver groups belongs to must be in `active` status.

        > **NOTE:** If scaling group's network type is `VPC`, the vserver groups must be in the same `VPC`.

        > **NOTE:** A scaling group can have at most 5 vserver groups attached by default.

        > **NOTE:** Vserver groups and the default group of loadbalancer share the same backend server quota.

        > **NOTE:** When attach vserver groups to scaling group, existing ECS instances will be added to vserver groups; Instead, ECS instances will be removed from vserver group when detach.

        > **NOTE:** Detach action will be executed before attach action.

        > **NOTE:** Vserver group is defined uniquely by `loadbalancer_id`, `vserver_group_id`, `port`.

        > **NOTE:** Modifing `weight` attribute means detach vserver group first and then, attach with new weight parameter.

        > **NOTE:** Resource `ess.ScalingGroupVServerGroups` is available in 1.53.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "testAccEssVserverGroupsAttachment"
        default_zones = alicloud.get_zones(available_disk_category="cloud_efficiency",
            available_resource_creation="VSwitch")
        default_network = alicloud.vpc.Network("defaultNetwork", cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            availability_zone=default_zones.zones[0].id)
        default_load_balancer = alicloud.slb.LoadBalancer("defaultLoadBalancer", vswitch_id=default_switch.id)
        default_server_group = alicloud.slb.ServerGroup("defaultServerGroup", load_balancer_id=default_load_balancer.id)
        default_listener = []
        for range in [{"value": i} for i in range(0, 2)]:
            default_listener.append(alicloud.slb.Listener(f"defaultListener-{range['value']}",
                load_balancer_id=[__item.id for __item in [default_load_balancer]][range["value"]],
                backend_port=22,
                frontend_port=22,
                protocol="tcp",
                bandwidth=10,
                health_check_type="tcp"))
        default_scaling_group = alicloud.ess.ScalingGroup("defaultScalingGroup",
            min_size=2,
            max_size=2,
            scaling_group_name=name,
            vswitch_ids=[default_switch.id])
        default_scaling_group_v_server_groups = alicloud.ess.ScalingGroupVServerGroups("defaultScalingGroupVServerGroups",
            scaling_group_id=default_scaling_group.id,
            vserver_groups=[alicloud.ess.ScalingGroupVServerGroupsVserverGroupArgs(
                loadbalancer_id=default_load_balancer.id,
                vserver_attributes=[alicloud.ess.ScalingGroupVServerGroupsVserverGroupVserverAttributeArgs(
                    vserver_group_id=default_server_group.id,
                    port=100,
                    weight=60,
                )],
            )])
        ```
        ## Block vserver_group

        the vserver_group supports the following:

        * `loadbalancer_id` - (Required) Loadbalancer server ID of VServer Group.
        * `vserver_attributes` - (Required) A list of VServer Group attributes. See Block vserver_attribute below for details.

        ## Block vserver_attribute

        * `vserver_group_id` - (Required) ID of VServer Group.
        * `port` - (Required) - The port will be used for VServer Group backend server.
        * `weight` - (Required) The weight of an ECS instance attached to the VServer Group.

        ## Import

        ESS vserver groups can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ess/scalingGroupVServerGroups:ScalingGroupVServerGroups example abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] force: If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingGroupVServerGroupsVserverGroupArgs']]]] vserver_groups: A list of vserver groups attached on scaling group. See Block vserver_group below for details.
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

            __props__['force'] = force
            if scaling_group_id is None:
                raise TypeError("Missing required property 'scaling_group_id'")
            __props__['scaling_group_id'] = scaling_group_id
            if vserver_groups is None:
                raise TypeError("Missing required property 'vserver_groups'")
            __props__['vserver_groups'] = vserver_groups
        super(ScalingGroupVServerGroups, __self__).__init__(
            'alicloud:ess/scalingGroupVServerGroups:ScalingGroupVServerGroups',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            force: Optional[pulumi.Input[bool]] = None,
            scaling_group_id: Optional[pulumi.Input[str]] = None,
            vserver_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingGroupVServerGroupsVserverGroupArgs']]]]] = None) -> 'ScalingGroupVServerGroups':
        """
        Get an existing ScalingGroupVServerGroups resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] force: If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingGroupVServerGroupsVserverGroupArgs']]]] vserver_groups: A list of vserver groups attached on scaling group. See Block vserver_group below for details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["force"] = force
        __props__["scaling_group_id"] = scaling_group_id
        __props__["vserver_groups"] = vserver_groups
        return ScalingGroupVServerGroups(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def force(self) -> pulumi.Output[Optional[bool]]:
        """
        If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.
        """
        return pulumi.get(self, "force")

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> pulumi.Output[str]:
        """
        ID of the scaling group.
        """
        return pulumi.get(self, "scaling_group_id")

    @property
    @pulumi.getter(name="vserverGroups")
    def vserver_groups(self) -> pulumi.Output[Sequence['outputs.ScalingGroupVServerGroupsVserverGroup']]:
        """
        A list of vserver groups attached on scaling group. See Block vserver_group below for details.
        """
        return pulumi.get(self, "vserver_groups")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


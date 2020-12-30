# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Cluster']


class Cluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_type: Optional[pulumi.Input[int]] = None,
                 logical_region_id: Optional[pulumi.Input[str]] = None,
                 network_mode: Optional[pulumi.Input[int]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an EDAS cluster resource.

        > **NOTE:** Available in 1.82.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.edas.Cluster("default",
            cluster_name=var["cluster_name"],
            cluster_type=var["cluster_type"],
            network_mode=var["network_mode"],
            logical_region_id=var["logical_region_id"],
            vpc_id=var["vpc_id"])
        ```

        ## Import

        EDAS cluster can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:edas/cluster:Cluster cluster cluster_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster that you want to create.
        :param pulumi.Input[int] cluster_type: The type of the cluster that you want to create. Valid values only: 2: ECS cluster.
        :param pulumi.Input[str] logical_region_id: The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.
        :param pulumi.Input[int] network_mode: The network type of the cluster that you want to create. Valid values: 1: classic network. 2: VPC.
        :param pulumi.Input[str] vpc_id: The ID of the Virtual Private Cloud (VPC) for the cluster.
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

            if cluster_name is None:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            if cluster_type is None:
                raise TypeError("Missing required property 'cluster_type'")
            __props__['cluster_type'] = cluster_type
            __props__['logical_region_id'] = logical_region_id
            if network_mode is None:
                raise TypeError("Missing required property 'network_mode'")
            __props__['network_mode'] = network_mode
            __props__['vpc_id'] = vpc_id
        super(Cluster, __self__).__init__(
            'alicloud:edas/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            cluster_type: Optional[pulumi.Input[int]] = None,
            logical_region_id: Optional[pulumi.Input[str]] = None,
            network_mode: Optional[pulumi.Input[int]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the cluster that you want to create.
        :param pulumi.Input[int] cluster_type: The type of the cluster that you want to create. Valid values only: 2: ECS cluster.
        :param pulumi.Input[str] logical_region_id: The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.
        :param pulumi.Input[int] network_mode: The network type of the cluster that you want to create. Valid values: 1: classic network. 2: VPC.
        :param pulumi.Input[str] vpc_id: The ID of the Virtual Private Cloud (VPC) for the cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_name"] = cluster_name
        __props__["cluster_type"] = cluster_type
        __props__["logical_region_id"] = logical_region_id
        __props__["network_mode"] = network_mode
        __props__["vpc_id"] = vpc_id
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        The name of the cluster that you want to create.
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[int]:
        """
        The type of the cluster that you want to create. Valid values only: 2: ECS cluster.
        """
        return pulumi.get(self, "cluster_type")

    @property
    @pulumi.getter(name="logicalRegionId")
    def logical_region_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the namespace where you want to create the application. You can call the ListUserDefineRegion operation to query the namespace ID.
        """
        return pulumi.get(self, "logical_region_id")

    @property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> pulumi.Output[int]:
        """
        The network type of the cluster that you want to create. Valid values: 1: classic network. 2: VPC.
        """
        return pulumi.get(self, "network_mode")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Virtual Private Cloud (VPC) for the cluster.
        """
        return pulumi.get(self, "vpc_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


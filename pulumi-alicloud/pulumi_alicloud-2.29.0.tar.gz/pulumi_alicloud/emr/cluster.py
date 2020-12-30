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

__all__ = ['Cluster']


class Cluster(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bootstrap_actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterBootstrapActionArgs']]]]] = None,
                 charge_type: Optional[pulumi.Input[str]] = None,
                 cluster_type: Optional[pulumi.Input[str]] = None,
                 deposit_type: Optional[pulumi.Input[str]] = None,
                 eas_enable: Optional[pulumi.Input[bool]] = None,
                 emr_ver: Optional[pulumi.Input[str]] = None,
                 high_availability_enable: Optional[pulumi.Input[bool]] = None,
                 host_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterHostGroupArgs']]]]] = None,
                 is_open_public_ip: Optional[pulumi.Input[bool]] = None,
                 key_pair_name: Optional[pulumi.Input[str]] = None,
                 master_pwd: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 option_software_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 related_cluster_id: Optional[pulumi.Input[str]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 ssh_enable: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 use_local_metadb: Optional[pulumi.Input[bool]] = None,
                 user_defined_emr_ecs_role: Optional[pulumi.Input[str]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a EMR Cluster resource. With this you can create, read, and release  EMR Cluster.

        > **NOTE:** Available in 1.57.0+.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] charge_type: Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.
        :param pulumi.Input[str] cluster_type: EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported 'GATEWAY' available in 1.61.0+.
        :param pulumi.Input[str] deposit_type: Cluster deposit type, HALF_MANAGED or FULL_MANAGED.
        :param pulumi.Input[bool] eas_enable: High security cluster (true) or not. Default value is false.
        :param pulumi.Input[str] emr_ver: EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.
        :param pulumi.Input[bool] high_availability_enable: High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterHostGroupArgs']]]] host_groups: Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).
        :param pulumi.Input[str] key_pair_name: Ssh key pair.
        :param pulumi.Input[str] master_pwd: Master ssh password.
        :param pulumi.Input[str] name: bootstrap action name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] option_software_lists: Optional software list.
        :param pulumi.Input[int] period: If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.
        :param pulumi.Input[str] related_cluster_id: This specify the related cluster id, if this cluster is a Gateway.
        :param pulumi.Input[str] security_group_id: Security Group ID for Cluster, you can also specify this key for each host group.
        :param pulumi.Input[bool] ssh_enable: If this is set true, we can ssh into cluster. Default value is false.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] use_local_metadb: Use local metadb. Default is false.
        :param pulumi.Input[str] user_defined_emr_ecs_role: Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.
        :param pulumi.Input[str] vswitch_id: Global vswitch id, you can also specify it in host group.
        :param pulumi.Input[str] zone_id: Zone ID, e.g. cn-huhehaote-a
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

            __props__['bootstrap_actions'] = bootstrap_actions
            __props__['charge_type'] = charge_type
            if cluster_type is None:
                raise TypeError("Missing required property 'cluster_type'")
            __props__['cluster_type'] = cluster_type
            __props__['deposit_type'] = deposit_type
            __props__['eas_enable'] = eas_enable
            if emr_ver is None:
                raise TypeError("Missing required property 'emr_ver'")
            __props__['emr_ver'] = emr_ver
            __props__['high_availability_enable'] = high_availability_enable
            __props__['host_groups'] = host_groups
            __props__['is_open_public_ip'] = is_open_public_ip
            __props__['key_pair_name'] = key_pair_name
            __props__['master_pwd'] = master_pwd
            __props__['name'] = name
            __props__['option_software_lists'] = option_software_lists
            __props__['period'] = period
            __props__['related_cluster_id'] = related_cluster_id
            __props__['security_group_id'] = security_group_id
            __props__['ssh_enable'] = ssh_enable
            __props__['tags'] = tags
            __props__['use_local_metadb'] = use_local_metadb
            __props__['user_defined_emr_ecs_role'] = user_defined_emr_ecs_role
            __props__['vswitch_id'] = vswitch_id
            if zone_id is None:
                raise TypeError("Missing required property 'zone_id'")
            __props__['zone_id'] = zone_id
        super(Cluster, __self__).__init__(
            'alicloud:emr/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bootstrap_actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterBootstrapActionArgs']]]]] = None,
            charge_type: Optional[pulumi.Input[str]] = None,
            cluster_type: Optional[pulumi.Input[str]] = None,
            deposit_type: Optional[pulumi.Input[str]] = None,
            eas_enable: Optional[pulumi.Input[bool]] = None,
            emr_ver: Optional[pulumi.Input[str]] = None,
            high_availability_enable: Optional[pulumi.Input[bool]] = None,
            host_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterHostGroupArgs']]]]] = None,
            is_open_public_ip: Optional[pulumi.Input[bool]] = None,
            key_pair_name: Optional[pulumi.Input[str]] = None,
            master_pwd: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            option_software_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            period: Optional[pulumi.Input[int]] = None,
            related_cluster_id: Optional[pulumi.Input[str]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None,
            ssh_enable: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            use_local_metadb: Optional[pulumi.Input[bool]] = None,
            user_defined_emr_ecs_role: Optional[pulumi.Input[str]] = None,
            vswitch_id: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] charge_type: Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.
        :param pulumi.Input[str] cluster_type: EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported 'GATEWAY' available in 1.61.0+.
        :param pulumi.Input[str] deposit_type: Cluster deposit type, HALF_MANAGED or FULL_MANAGED.
        :param pulumi.Input[bool] eas_enable: High security cluster (true) or not. Default value is false.
        :param pulumi.Input[str] emr_ver: EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.
        :param pulumi.Input[bool] high_availability_enable: High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterHostGroupArgs']]]] host_groups: Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).
        :param pulumi.Input[str] key_pair_name: Ssh key pair.
        :param pulumi.Input[str] master_pwd: Master ssh password.
        :param pulumi.Input[str] name: bootstrap action name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] option_software_lists: Optional software list.
        :param pulumi.Input[int] period: If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.
        :param pulumi.Input[str] related_cluster_id: This specify the related cluster id, if this cluster is a Gateway.
        :param pulumi.Input[str] security_group_id: Security Group ID for Cluster, you can also specify this key for each host group.
        :param pulumi.Input[bool] ssh_enable: If this is set true, we can ssh into cluster. Default value is false.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[bool] use_local_metadb: Use local metadb. Default is false.
        :param pulumi.Input[str] user_defined_emr_ecs_role: Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.
        :param pulumi.Input[str] vswitch_id: Global vswitch id, you can also specify it in host group.
        :param pulumi.Input[str] zone_id: Zone ID, e.g. cn-huhehaote-a
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bootstrap_actions"] = bootstrap_actions
        __props__["charge_type"] = charge_type
        __props__["cluster_type"] = cluster_type
        __props__["deposit_type"] = deposit_type
        __props__["eas_enable"] = eas_enable
        __props__["emr_ver"] = emr_ver
        __props__["high_availability_enable"] = high_availability_enable
        __props__["host_groups"] = host_groups
        __props__["is_open_public_ip"] = is_open_public_ip
        __props__["key_pair_name"] = key_pair_name
        __props__["master_pwd"] = master_pwd
        __props__["name"] = name
        __props__["option_software_lists"] = option_software_lists
        __props__["period"] = period
        __props__["related_cluster_id"] = related_cluster_id
        __props__["security_group_id"] = security_group_id
        __props__["ssh_enable"] = ssh_enable
        __props__["tags"] = tags
        __props__["use_local_metadb"] = use_local_metadb
        __props__["user_defined_emr_ecs_role"] = user_defined_emr_ecs_role
        __props__["vswitch_id"] = vswitch_id
        __props__["zone_id"] = zone_id
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bootstrapActions")
    def bootstrap_actions(self) -> pulumi.Output[Optional[Sequence['outputs.ClusterBootstrapAction']]]:
        return pulumi.get(self, "bootstrap_actions")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> pulumi.Output[Optional[str]]:
        """
        Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.
        """
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[str]:
        """
        EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported 'GATEWAY' available in 1.61.0+.
        """
        return pulumi.get(self, "cluster_type")

    @property
    @pulumi.getter(name="depositType")
    def deposit_type(self) -> pulumi.Output[Optional[str]]:
        """
        Cluster deposit type, HALF_MANAGED or FULL_MANAGED.
        """
        return pulumi.get(self, "deposit_type")

    @property
    @pulumi.getter(name="easEnable")
    def eas_enable(self) -> pulumi.Output[Optional[bool]]:
        """
        High security cluster (true) or not. Default value is false.
        """
        return pulumi.get(self, "eas_enable")

    @property
    @pulumi.getter(name="emrVer")
    def emr_ver(self) -> pulumi.Output[str]:
        """
        EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.
        """
        return pulumi.get(self, "emr_ver")

    @property
    @pulumi.getter(name="highAvailabilityEnable")
    def high_availability_enable(self) -> pulumi.Output[Optional[bool]]:
        """
        High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.
        """
        return pulumi.get(self, "high_availability_enable")

    @property
    @pulumi.getter(name="hostGroups")
    def host_groups(self) -> pulumi.Output[Optional[Sequence['outputs.ClusterHostGroup']]]:
        """
        Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).
        """
        return pulumi.get(self, "host_groups")

    @property
    @pulumi.getter(name="isOpenPublicIp")
    def is_open_public_ip(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "is_open_public_ip")

    @property
    @pulumi.getter(name="keyPairName")
    def key_pair_name(self) -> pulumi.Output[Optional[str]]:
        """
        Ssh key pair.
        """
        return pulumi.get(self, "key_pair_name")

    @property
    @pulumi.getter(name="masterPwd")
    def master_pwd(self) -> pulumi.Output[Optional[str]]:
        """
        Master ssh password.
        """
        return pulumi.get(self, "master_pwd")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        bootstrap action name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="optionSoftwareLists")
    def option_software_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Optional software list.
        """
        return pulumi.get(self, "option_software_lists")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[int]]:
        """
        If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="relatedClusterId")
    def related_cluster_id(self) -> pulumi.Output[Optional[str]]:
        """
        This specify the related cluster id, if this cluster is a Gateway.
        """
        return pulumi.get(self, "related_cluster_id")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        Security Group ID for Cluster, you can also specify this key for each host group.
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter(name="sshEnable")
    def ssh_enable(self) -> pulumi.Output[Optional[bool]]:
        """
        If this is set true, we can ssh into cluster. Default value is false.
        """
        return pulumi.get(self, "ssh_enable")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useLocalMetadb")
    def use_local_metadb(self) -> pulumi.Output[Optional[bool]]:
        """
        Use local metadb. Default is false.
        """
        return pulumi.get(self, "use_local_metadb")

    @property
    @pulumi.getter(name="userDefinedEmrEcsRole")
    def user_defined_emr_ecs_role(self) -> pulumi.Output[Optional[str]]:
        """
        Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.
        """
        return pulumi.get(self, "user_defined_emr_ecs_role")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> pulumi.Output[Optional[str]]:
        """
        Global vswitch id, you can also specify it in host group.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        Zone ID, e.g. cn-huhehaote-a
        """
        return pulumi.get(self, "zone_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


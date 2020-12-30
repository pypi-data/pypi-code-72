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

__all__ = ['ScalingConfiguration']


class ScalingConfiguration(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 credit_specification: Optional[pulumi.Input[str]] = None,
                 data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingConfigurationDataDiskArgs']]]]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 force_delete: Optional[pulumi.Input[bool]] = None,
                 image_id: Optional[pulumi.Input[str]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 instance_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 internet_charge_type: Optional[pulumi.Input[str]] = None,
                 internet_max_bandwidth_in: Optional[pulumi.Input[int]] = None,
                 internet_max_bandwidth_out: Optional[pulumi.Input[int]] = None,
                 io_optimized: Optional[pulumi.Input[str]] = None,
                 is_outdated: Optional[pulumi.Input[bool]] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 kms_encrypted_password: Optional[pulumi.Input[str]] = None,
                 kms_encryption_context: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 override: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 password_inherit: Optional[pulumi.Input[bool]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 scaling_configuration_name: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 substitute: Optional[pulumi.Input[str]] = None,
                 system_disk_auto_snapshot_policy_id: Optional[pulumi.Input[str]] = None,
                 system_disk_category: Optional[pulumi.Input[str]] = None,
                 system_disk_description: Optional[pulumi.Input[str]] = None,
                 system_disk_name: Optional[pulumi.Input[str]] = None,
                 system_disk_size: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        ESS scaling configuration can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ess/scalingConfiguration:ScalingConfiguration example asg-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Whether active current scaling configuration in the specified scaling group. Default to `false`.
        :param pulumi.Input[str] credit_specification: Performance mode of the t5 burstable instance. Valid values: 'Standard', 'Unlimited'.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingConfigurationDataDiskArgs']]]] data_disks: DataDisk mappings to attach to ecs instance. See Block datadisk below for details.
        :param pulumi.Input[bool] enable: Whether enable the specified scaling group(make it active) to which the current scaling configuration belongs.
        :param pulumi.Input[bool] force_delete: The last scaling configuration will be deleted forcibly with deleting its scaling group. Default to false.
        :param pulumi.Input[str] image_id: ID of an image file, indicating the image resource selected when an instance is enabled.
        :param pulumi.Input[str] image_name: Name of an image file, indicating the image resource selected when an instance is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_ids: It has been deprecated from version 1.6.0. New resource `ess.Attachment` replaces it.
        :param pulumi.Input[str] instance_name: Name of an ECS instance. Default to "ESS-Instance". It is valid from version 1.7.1.
        :param pulumi.Input[str] instance_type: Resource type of an ECS instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_types: Resource types of an ECS instance.
        :param pulumi.Input[str] internet_charge_type: Network billing type, Values: PayByBandwidth or PayByTraffic. Default to `PayByBandwidth`.
        :param pulumi.Input[int] internet_max_bandwidth_in: Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). The value range is [1,200].
        :param pulumi.Input[int] internet_max_bandwidth_out: Maximum outgoing bandwidth from the public network, measured in Mbps (Mega bit per second). The value range for PayByBandwidth is [0,100].
        :param pulumi.Input[str] io_optimized: It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.
        :param pulumi.Input[bool] is_outdated: Whether to use outdated instance type. Default to false.
        :param pulumi.Input[str] key_name: The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.
        :param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a db account. If the `password` is filled in, this field will be ignored.
        :param pulumi.Input[Mapping[str, Any]] kms_encryption_context: An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a db account with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
        :param pulumi.Input[bool] override: Indicates whether to overwrite the existing data. Default to false.
        :param pulumi.Input[str] password: The password of the ECS instance. The password must be 8 to 30 characters in length. It must contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `() ~!@#$%^&*-_+=\|{}[]:;'<>,.?/`, The password of Windows-based instances cannot start with a forward slash (/).
        :param pulumi.Input[bool] password_inherit: Specifies whether to use the password that is predefined in the image. If the PasswordInherit parameter is set to true, the `password` and `kms_encrypted_password` will be ignored. You must ensure that the selected image has a password configured.
        :param pulumi.Input[str] role_name: Instance RAM role name. The name is provided and maintained by RAM. You can use `ram.Role` to create a new one.
        :param pulumi.Input[str] scaling_configuration_name: Name shown for the scheduled task. which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores `_`, hypens `-`, and decimal point `.`. If this parameter value is not specified, the default value is ScalingConfigurationId.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group of a scaling configuration.
        :param pulumi.Input[str] security_group_id: ID of the security group used to create new instance. It is conflict with `security_group_ids`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: List IDs of the security group used to create new instances. It is conflict with `security_group_id`.
        :param pulumi.Input[str] substitute: The another scaling configuration which will be active automatically and replace current configuration when setting `active` to 'false'. It is invalid when `active` is 'true'.
        :param pulumi.Input[str] system_disk_auto_snapshot_policy_id: The id of auto snapshot policy for system disk.
        :param pulumi.Input[str] system_disk_category: Category of the system disk. The parameter value options are `ephemeral_ssd`, `cloud_efficiency`, `cloud_ssd`, `cloud_essd` and `cloud`. `cloud` only is used to some no I/O optimized instance. Default to `cloud_efficiency`.
        :param pulumi.Input[str] system_disk_description: The description of the system disk. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        :param pulumi.Input[str] system_disk_name: The name of the system disk. It must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-). Default value: null.
        :param pulumi.Input[int] system_disk_size: Size of system disk, in GiB. Optional values: cloud: 20-500, cloud_efficiency: 20-500, cloud_ssd: 20-500, ephemeral_ssd: 20-500 The default value is max{40, ImageSize}. If this parameter is set, the system disk size must be greater than or equal to max{40, ImageSize}.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource. It will be applied for ECS instances finally.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "http://", or "https://" It can be a null string.
        :param pulumi.Input[str] user_data: User-defined data to customize the startup behaviors of the ECS instance and to pass data into the ECS instance.
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

            __props__['active'] = active
            __props__['credit_specification'] = credit_specification
            __props__['data_disks'] = data_disks
            __props__['enable'] = enable
            __props__['force_delete'] = force_delete
            __props__['image_id'] = image_id
            __props__['image_name'] = image_name
            if instance_ids is not None:
                warnings.warn("""Field 'instance_ids' has been deprecated from provider version 1.6.0. New resource 'alicloud_ess_attachment' replaces it.""", DeprecationWarning)
                pulumi.log.warn("instance_ids is deprecated: Field 'instance_ids' has been deprecated from provider version 1.6.0. New resource 'alicloud_ess_attachment' replaces it.")
            __props__['instance_ids'] = instance_ids
            __props__['instance_name'] = instance_name
            __props__['instance_type'] = instance_type
            __props__['instance_types'] = instance_types
            __props__['internet_charge_type'] = internet_charge_type
            __props__['internet_max_bandwidth_in'] = internet_max_bandwidth_in
            __props__['internet_max_bandwidth_out'] = internet_max_bandwidth_out
            if io_optimized is not None:
                warnings.warn("""Attribute io_optimized has been deprecated on instance resource. All the launched alicloud instances will be IO optimized. Suggest to remove it from your template.""", DeprecationWarning)
                pulumi.log.warn("io_optimized is deprecated: Attribute io_optimized has been deprecated on instance resource. All the launched alicloud instances will be IO optimized. Suggest to remove it from your template.")
            __props__['io_optimized'] = io_optimized
            __props__['is_outdated'] = is_outdated
            __props__['key_name'] = key_name
            __props__['kms_encrypted_password'] = kms_encrypted_password
            __props__['kms_encryption_context'] = kms_encryption_context
            __props__['override'] = override
            __props__['password'] = password
            __props__['password_inherit'] = password_inherit
            __props__['role_name'] = role_name
            __props__['scaling_configuration_name'] = scaling_configuration_name
            if scaling_group_id is None:
                raise TypeError("Missing required property 'scaling_group_id'")
            __props__['scaling_group_id'] = scaling_group_id
            __props__['security_group_id'] = security_group_id
            __props__['security_group_ids'] = security_group_ids
            __props__['substitute'] = substitute
            __props__['system_disk_auto_snapshot_policy_id'] = system_disk_auto_snapshot_policy_id
            __props__['system_disk_category'] = system_disk_category
            __props__['system_disk_description'] = system_disk_description
            __props__['system_disk_name'] = system_disk_name
            __props__['system_disk_size'] = system_disk_size
            __props__['tags'] = tags
            __props__['user_data'] = user_data
        super(ScalingConfiguration, __self__).__init__(
            'alicloud:ess/scalingConfiguration:ScalingConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            credit_specification: Optional[pulumi.Input[str]] = None,
            data_disks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingConfigurationDataDiskArgs']]]]] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            force_delete: Optional[pulumi.Input[bool]] = None,
            image_id: Optional[pulumi.Input[str]] = None,
            image_name: Optional[pulumi.Input[str]] = None,
            instance_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            instance_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            internet_charge_type: Optional[pulumi.Input[str]] = None,
            internet_max_bandwidth_in: Optional[pulumi.Input[int]] = None,
            internet_max_bandwidth_out: Optional[pulumi.Input[int]] = None,
            io_optimized: Optional[pulumi.Input[str]] = None,
            is_outdated: Optional[pulumi.Input[bool]] = None,
            key_name: Optional[pulumi.Input[str]] = None,
            kms_encrypted_password: Optional[pulumi.Input[str]] = None,
            kms_encryption_context: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            override: Optional[pulumi.Input[bool]] = None,
            password: Optional[pulumi.Input[str]] = None,
            password_inherit: Optional[pulumi.Input[bool]] = None,
            role_name: Optional[pulumi.Input[str]] = None,
            scaling_configuration_name: Optional[pulumi.Input[str]] = None,
            scaling_group_id: Optional[pulumi.Input[str]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            substitute: Optional[pulumi.Input[str]] = None,
            system_disk_auto_snapshot_policy_id: Optional[pulumi.Input[str]] = None,
            system_disk_category: Optional[pulumi.Input[str]] = None,
            system_disk_description: Optional[pulumi.Input[str]] = None,
            system_disk_name: Optional[pulumi.Input[str]] = None,
            system_disk_size: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            user_data: Optional[pulumi.Input[str]] = None) -> 'ScalingConfiguration':
        """
        Get an existing ScalingConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Whether active current scaling configuration in the specified scaling group. Default to `false`.
        :param pulumi.Input[str] credit_specification: Performance mode of the t5 burstable instance. Valid values: 'Standard', 'Unlimited'.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScalingConfigurationDataDiskArgs']]]] data_disks: DataDisk mappings to attach to ecs instance. See Block datadisk below for details.
        :param pulumi.Input[bool] enable: Whether enable the specified scaling group(make it active) to which the current scaling configuration belongs.
        :param pulumi.Input[bool] force_delete: The last scaling configuration will be deleted forcibly with deleting its scaling group. Default to false.
        :param pulumi.Input[str] image_id: ID of an image file, indicating the image resource selected when an instance is enabled.
        :param pulumi.Input[str] image_name: Name of an image file, indicating the image resource selected when an instance is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_ids: It has been deprecated from version 1.6.0. New resource `ess.Attachment` replaces it.
        :param pulumi.Input[str] instance_name: Name of an ECS instance. Default to "ESS-Instance". It is valid from version 1.7.1.
        :param pulumi.Input[str] instance_type: Resource type of an ECS instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] instance_types: Resource types of an ECS instance.
        :param pulumi.Input[str] internet_charge_type: Network billing type, Values: PayByBandwidth or PayByTraffic. Default to `PayByBandwidth`.
        :param pulumi.Input[int] internet_max_bandwidth_in: Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). The value range is [1,200].
        :param pulumi.Input[int] internet_max_bandwidth_out: Maximum outgoing bandwidth from the public network, measured in Mbps (Mega bit per second). The value range for PayByBandwidth is [0,100].
        :param pulumi.Input[str] io_optimized: It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.
        :param pulumi.Input[bool] is_outdated: Whether to use outdated instance type. Default to false.
        :param pulumi.Input[str] key_name: The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.
        :param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a db account. If the `password` is filled in, this field will be ignored.
        :param pulumi.Input[Mapping[str, Any]] kms_encryption_context: An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a db account with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
        :param pulumi.Input[bool] override: Indicates whether to overwrite the existing data. Default to false.
        :param pulumi.Input[str] password: The password of the ECS instance. The password must be 8 to 30 characters in length. It must contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `() ~!@#$%^&*-_+=\|{}[]:;'<>,.?/`, The password of Windows-based instances cannot start with a forward slash (/).
        :param pulumi.Input[bool] password_inherit: Specifies whether to use the password that is predefined in the image. If the PasswordInherit parameter is set to true, the `password` and `kms_encrypted_password` will be ignored. You must ensure that the selected image has a password configured.
        :param pulumi.Input[str] role_name: Instance RAM role name. The name is provided and maintained by RAM. You can use `ram.Role` to create a new one.
        :param pulumi.Input[str] scaling_configuration_name: Name shown for the scheduled task. which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores `_`, hypens `-`, and decimal point `.`. If this parameter value is not specified, the default value is ScalingConfigurationId.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group of a scaling configuration.
        :param pulumi.Input[str] security_group_id: ID of the security group used to create new instance. It is conflict with `security_group_ids`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: List IDs of the security group used to create new instances. It is conflict with `security_group_id`.
        :param pulumi.Input[str] substitute: The another scaling configuration which will be active automatically and replace current configuration when setting `active` to 'false'. It is invalid when `active` is 'true'.
        :param pulumi.Input[str] system_disk_auto_snapshot_policy_id: The id of auto snapshot policy for system disk.
        :param pulumi.Input[str] system_disk_category: Category of the system disk. The parameter value options are `ephemeral_ssd`, `cloud_efficiency`, `cloud_ssd`, `cloud_essd` and `cloud`. `cloud` only is used to some no I/O optimized instance. Default to `cloud_efficiency`.
        :param pulumi.Input[str] system_disk_description: The description of the system disk. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        :param pulumi.Input[str] system_disk_name: The name of the system disk. It must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-). Default value: null.
        :param pulumi.Input[int] system_disk_size: Size of system disk, in GiB. Optional values: cloud: 20-500, cloud_efficiency: 20-500, cloud_ssd: 20-500, ephemeral_ssd: 20-500 The default value is max{40, ImageSize}. If this parameter is set, the system disk size must be greater than or equal to max{40, ImageSize}.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource. It will be applied for ECS instances finally.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "http://", or "https://" It can be a null string.
        :param pulumi.Input[str] user_data: User-defined data to customize the startup behaviors of the ECS instance and to pass data into the ECS instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["active"] = active
        __props__["credit_specification"] = credit_specification
        __props__["data_disks"] = data_disks
        __props__["enable"] = enable
        __props__["force_delete"] = force_delete
        __props__["image_id"] = image_id
        __props__["image_name"] = image_name
        __props__["instance_ids"] = instance_ids
        __props__["instance_name"] = instance_name
        __props__["instance_type"] = instance_type
        __props__["instance_types"] = instance_types
        __props__["internet_charge_type"] = internet_charge_type
        __props__["internet_max_bandwidth_in"] = internet_max_bandwidth_in
        __props__["internet_max_bandwidth_out"] = internet_max_bandwidth_out
        __props__["io_optimized"] = io_optimized
        __props__["is_outdated"] = is_outdated
        __props__["key_name"] = key_name
        __props__["kms_encrypted_password"] = kms_encrypted_password
        __props__["kms_encryption_context"] = kms_encryption_context
        __props__["override"] = override
        __props__["password"] = password
        __props__["password_inherit"] = password_inherit
        __props__["role_name"] = role_name
        __props__["scaling_configuration_name"] = scaling_configuration_name
        __props__["scaling_group_id"] = scaling_group_id
        __props__["security_group_id"] = security_group_id
        __props__["security_group_ids"] = security_group_ids
        __props__["substitute"] = substitute
        __props__["system_disk_auto_snapshot_policy_id"] = system_disk_auto_snapshot_policy_id
        __props__["system_disk_category"] = system_disk_category
        __props__["system_disk_description"] = system_disk_description
        __props__["system_disk_name"] = system_disk_name
        __props__["system_disk_size"] = system_disk_size
        __props__["tags"] = tags
        __props__["user_data"] = user_data
        return ScalingConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[bool]:
        """
        Whether active current scaling configuration in the specified scaling group. Default to `false`.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter(name="creditSpecification")
    def credit_specification(self) -> pulumi.Output[Optional[str]]:
        """
        Performance mode of the t5 burstable instance. Valid values: 'Standard', 'Unlimited'.
        """
        return pulumi.get(self, "credit_specification")

    @property
    @pulumi.getter(name="dataDisks")
    def data_disks(self) -> pulumi.Output[Optional[Sequence['outputs.ScalingConfigurationDataDisk']]]:
        """
        DataDisk mappings to attach to ecs instance. See Block datadisk below for details.
        """
        return pulumi.get(self, "data_disks")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether enable the specified scaling group(make it active) to which the current scaling configuration belongs.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter(name="forceDelete")
    def force_delete(self) -> pulumi.Output[Optional[bool]]:
        """
        The last scaling configuration will be deleted forcibly with deleting its scaling group. Default to false.
        """
        return pulumi.get(self, "force_delete")

    @property
    @pulumi.getter(name="imageId")
    def image_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of an image file, indicating the image resource selected when an instance is enabled.
        """
        return pulumi.get(self, "image_id")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of an image file, indicating the image resource selected when an instance is enabled.
        """
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        It has been deprecated from version 1.6.0. New resource `ess.Attachment` replaces it.
        """
        return pulumi.get(self, "instance_ids")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of an ECS instance. Default to "ESS-Instance". It is valid from version 1.7.1.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type of an ECS instance.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="instanceTypes")
    def instance_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Resource types of an ECS instance.
        """
        return pulumi.get(self, "instance_types")

    @property
    @pulumi.getter(name="internetChargeType")
    def internet_charge_type(self) -> pulumi.Output[Optional[str]]:
        """
        Network billing type, Values: PayByBandwidth or PayByTraffic. Default to `PayByBandwidth`.
        """
        return pulumi.get(self, "internet_charge_type")

    @property
    @pulumi.getter(name="internetMaxBandwidthIn")
    def internet_max_bandwidth_in(self) -> pulumi.Output[int]:
        """
        Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). The value range is [1,200].
        """
        return pulumi.get(self, "internet_max_bandwidth_in")

    @property
    @pulumi.getter(name="internetMaxBandwidthOut")
    def internet_max_bandwidth_out(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum outgoing bandwidth from the public network, measured in Mbps (Mega bit per second). The value range for PayByBandwidth is [0,100].
        """
        return pulumi.get(self, "internet_max_bandwidth_out")

    @property
    @pulumi.getter(name="ioOptimized")
    def io_optimized(self) -> pulumi.Output[Optional[str]]:
        """
        It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.
        """
        return pulumi.get(self, "io_optimized")

    @property
    @pulumi.getter(name="isOutdated")
    def is_outdated(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to use outdated instance type. Default to false.
        """
        return pulumi.get(self, "is_outdated")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="kmsEncryptedPassword")
    def kms_encrypted_password(self) -> pulumi.Output[Optional[str]]:
        """
        An KMS encrypts password used to a db account. If the `password` is filled in, this field will be ignored.
        """
        return pulumi.get(self, "kms_encrypted_password")

    @property
    @pulumi.getter(name="kmsEncryptionContext")
    def kms_encryption_context(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a db account with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
        """
        return pulumi.get(self, "kms_encryption_context")

    @property
    @pulumi.getter
    def override(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to overwrite the existing data. Default to false.
        """
        return pulumi.get(self, "override")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password of the ECS instance. The password must be 8 to 30 characters in length. It must contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `() ~!@#$%^&*-_+=\|{}[]:;'<>,.?/`, The password of Windows-based instances cannot start with a forward slash (/).
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="passwordInherit")
    def password_inherit(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to use the password that is predefined in the image. If the PasswordInherit parameter is set to true, the `password` and `kms_encrypted_password` will be ignored. You must ensure that the selected image has a password configured.
        """
        return pulumi.get(self, "password_inherit")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[Optional[str]]:
        """
        Instance RAM role name. The name is provided and maintained by RAM. You can use `ram.Role` to create a new one.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter(name="scalingConfigurationName")
    def scaling_configuration_name(self) -> pulumi.Output[str]:
        """
        Name shown for the scheduled task. which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores `_`, hypens `-`, and decimal point `.`. If this parameter value is not specified, the default value is ScalingConfigurationId.
        """
        return pulumi.get(self, "scaling_configuration_name")

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> pulumi.Output[str]:
        """
        ID of the scaling group of a scaling configuration.
        """
        return pulumi.get(self, "scaling_group_id")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the security group used to create new instance. It is conflict with `security_group_ids`.
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List IDs of the security group used to create new instances. It is conflict with `security_group_id`.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter
    def substitute(self) -> pulumi.Output[str]:
        """
        The another scaling configuration which will be active automatically and replace current configuration when setting `active` to 'false'. It is invalid when `active` is 'true'.
        """
        return pulumi.get(self, "substitute")

    @property
    @pulumi.getter(name="systemDiskAutoSnapshotPolicyId")
    def system_disk_auto_snapshot_policy_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id of auto snapshot policy for system disk.
        """
        return pulumi.get(self, "system_disk_auto_snapshot_policy_id")

    @property
    @pulumi.getter(name="systemDiskCategory")
    def system_disk_category(self) -> pulumi.Output[Optional[str]]:
        """
        Category of the system disk. The parameter value options are `ephemeral_ssd`, `cloud_efficiency`, `cloud_ssd`, `cloud_essd` and `cloud`. `cloud` only is used to some no I/O optimized instance. Default to `cloud_efficiency`.
        """
        return pulumi.get(self, "system_disk_category")

    @property
    @pulumi.getter(name="systemDiskDescription")
    def system_disk_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the system disk. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        """
        return pulumi.get(self, "system_disk_description")

    @property
    @pulumi.getter(name="systemDiskName")
    def system_disk_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the system disk. It must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-). Default value: null.
        """
        return pulumi.get(self, "system_disk_name")

    @property
    @pulumi.getter(name="systemDiskSize")
    def system_disk_size(self) -> pulumi.Output[Optional[int]]:
        """
        Size of system disk, in GiB. Optional values: cloud: 20-500, cloud_efficiency: 20-500, cloud_ssd: 20-500, ephemeral_ssd: 20-500 The default value is max{40, ImageSize}. If this parameter is set, the system disk size must be greater than or equal to max{40, ImageSize}.
        """
        return pulumi.get(self, "system_disk_size")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource. It will be applied for ECS instances finally.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "http://", or "https://" It can be a null string.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[str]]:
        """
        User-defined data to customize the startup behaviors of the ECS instance and to pass data into the ECS instance.
        """
        return pulumi.get(self, "user_data")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


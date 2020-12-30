# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Secret']


class Secret(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encryption_key_id: Optional[pulumi.Input[str]] = None,
                 force_delete_without_recovery: Optional[pulumi.Input[bool]] = None,
                 recovery_window_in_days: Optional[pulumi.Input[int]] = None,
                 secret_data: Optional[pulumi.Input[str]] = None,
                 secret_data_type: Optional[pulumi.Input[str]] = None,
                 secret_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 version_id: Optional[pulumi.Input[str]] = None,
                 version_stages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resouce used to create a secret and store its initial version.

        > **NOTE:** Available in 1.76.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.kms.Secret("default",
            description="from terraform",
            force_delete_without_recovery=True,
            secret_data="Secret data.",
            secret_name="secret-foo",
            version_id="000000000001")
        ```

        ## Import

        KMS secret can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:kms/secret:Secret default secret-foo
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the secret.
        :param pulumi.Input[str] encryption_key_id: The ID of the KMS CMK that is used to encrypt the secret value. If you do not specify this parameter, Secrets Manager automatically creates an encryption key to encrypt the secret.
        :param pulumi.Input[bool] force_delete_without_recovery: Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered. Valid values: true, false. Default to: false.
        :param pulumi.Input[int] recovery_window_in_days: Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. It will be ignored when `force_delete_without_recovery` is true.
        :param pulumi.Input[str] secret_data: The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores it in the initial version.
        :param pulumi.Input[str] secret_data_type: The type of the secret value. Valid values: text, binary. Default to "text".
        :param pulumi.Input[str] secret_name: The name of the secret.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] version_id: The version number of the initial version. Version numbers are unique in each secret object.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] version_stages: ) The stage labels that mark the new secret version. If you do not specify this parameter, Secrets Manager marks it with "ACSCurrent".
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

            __props__['description'] = description
            __props__['encryption_key_id'] = encryption_key_id
            __props__['force_delete_without_recovery'] = force_delete_without_recovery
            __props__['recovery_window_in_days'] = recovery_window_in_days
            if secret_data is None:
                raise TypeError("Missing required property 'secret_data'")
            __props__['secret_data'] = secret_data
            __props__['secret_data_type'] = secret_data_type
            if secret_name is None:
                raise TypeError("Missing required property 'secret_name'")
            __props__['secret_name'] = secret_name
            __props__['tags'] = tags
            if version_id is None:
                raise TypeError("Missing required property 'version_id'")
            __props__['version_id'] = version_id
            __props__['version_stages'] = version_stages
            __props__['arn'] = None
            __props__['planned_delete_time'] = None
        super(Secret, __self__).__init__(
            'alicloud:kms/secret:Secret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            encryption_key_id: Optional[pulumi.Input[str]] = None,
            force_delete_without_recovery: Optional[pulumi.Input[bool]] = None,
            planned_delete_time: Optional[pulumi.Input[str]] = None,
            recovery_window_in_days: Optional[pulumi.Input[int]] = None,
            secret_data: Optional[pulumi.Input[str]] = None,
            secret_data_type: Optional[pulumi.Input[str]] = None,
            secret_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            version_id: Optional[pulumi.Input[str]] = None,
            version_stages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Secret':
        """
        Get an existing Secret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Alicloud Resource Name (ARN) of the secret.
        :param pulumi.Input[str] description: The description of the secret.
        :param pulumi.Input[str] encryption_key_id: The ID of the KMS CMK that is used to encrypt the secret value. If you do not specify this parameter, Secrets Manager automatically creates an encryption key to encrypt the secret.
        :param pulumi.Input[bool] force_delete_without_recovery: Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered. Valid values: true, false. Default to: false.
        :param pulumi.Input[str] planned_delete_time: The time when the secret is scheduled to be deleted.
        :param pulumi.Input[int] recovery_window_in_days: Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. It will be ignored when `force_delete_without_recovery` is true.
        :param pulumi.Input[str] secret_data: The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores it in the initial version.
        :param pulumi.Input[str] secret_data_type: The type of the secret value. Valid values: text, binary. Default to "text".
        :param pulumi.Input[str] secret_name: The name of the secret.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] version_id: The version number of the initial version. Version numbers are unique in each secret object.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] version_stages: ) The stage labels that mark the new secret version. If you do not specify this parameter, Secrets Manager marks it with "ACSCurrent".
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["encryption_key_id"] = encryption_key_id
        __props__["force_delete_without_recovery"] = force_delete_without_recovery
        __props__["planned_delete_time"] = planned_delete_time
        __props__["recovery_window_in_days"] = recovery_window_in_days
        __props__["secret_data"] = secret_data
        __props__["secret_data_type"] = secret_data_type
        __props__["secret_name"] = secret_name
        __props__["tags"] = tags
        __props__["version_id"] = version_id
        __props__["version_stages"] = version_stages
        return Secret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Alicloud Resource Name (ARN) of the secret.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the secret.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptionKeyId")
    def encryption_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the KMS CMK that is used to encrypt the secret value. If you do not specify this parameter, Secrets Manager automatically creates an encryption key to encrypt the secret.
        """
        return pulumi.get(self, "encryption_key_id")

    @property
    @pulumi.getter(name="forceDeleteWithoutRecovery")
    def force_delete_without_recovery(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered. Valid values: true, false. Default to: false.
        """
        return pulumi.get(self, "force_delete_without_recovery")

    @property
    @pulumi.getter(name="plannedDeleteTime")
    def planned_delete_time(self) -> pulumi.Output[str]:
        """
        The time when the secret is scheduled to be deleted.
        """
        return pulumi.get(self, "planned_delete_time")

    @property
    @pulumi.getter(name="recoveryWindowInDays")
    def recovery_window_in_days(self) -> pulumi.Output[Optional[int]]:
        """
        Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. It will be ignored when `force_delete_without_recovery` is true.
        """
        return pulumi.get(self, "recovery_window_in_days")

    @property
    @pulumi.getter(name="secretData")
    def secret_data(self) -> pulumi.Output[str]:
        """
        The value of the secret that you want to create. Secrets Manager encrypts the secret value and stores it in the initial version.
        """
        return pulumi.get(self, "secret_data")

    @property
    @pulumi.getter(name="secretDataType")
    def secret_data_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the secret value. Valid values: text, binary. Default to "text".
        """
        return pulumi.get(self, "secret_data_type")

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Output[str]:
        """
        The name of the secret.
        """
        return pulumi.get(self, "secret_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> pulumi.Output[str]:
        """
        The version number of the initial version. Version numbers are unique in each secret object.
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter(name="versionStages")
    def version_stages(self) -> pulumi.Output[Sequence[str]]:
        """
        ) The stage labels that mark the new secret version. If you do not specify this parameter, Secrets Manager marks it with "ACSCurrent".
        """
        return pulumi.get(self, "version_stages")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


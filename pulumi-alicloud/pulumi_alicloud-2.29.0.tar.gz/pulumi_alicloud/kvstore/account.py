# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Account']


class Account(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_password: Optional[pulumi.Input[str]] = None,
                 account_privilege: Optional[pulumi.Input[str]] = None,
                 account_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 kms_encrypted_password: Optional[pulumi.Input[str]] = None,
                 kms_encryption_context: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a KVStore Account resource.

        For information about KVStore Account and how to use it, see [What is Account](https://www.alibabacloud.com/help/doc-detail/95973.htm).

        > **NOTE:** Available in 1.66.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        creation = config.get("creation")
        if creation is None:
            creation = "KVStore"
        name = config.get("name")
        if name is None:
            name = "kvstoreinstancevpc"
        default_zones = alicloud.get_zones(available_resource_creation=creation)
        default_network = alicloud.vpc.Network("defaultNetwork", cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            availability_zone=default_zones.zones[0].id)
        default_instance = alicloud.kvstore.Instance("defaultInstance",
            instance_class="redis.master.small.default",
            instance_name=name,
            vswitch_id=default_switch.id,
            private_ip="172.16.0.10",
            security_ips=["10.0.0.1"],
            instance_type="Redis",
            engine_version="4.0")
        example = alicloud.kvstore.Account("example",
            account_name="tftestnormal",
            account_password="YourPassword_123",
            instance_id=default_instance.id)
        ```

        ## Import

        KVStore account can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:kvstore/account:Account example <instance_id>:<account_name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the account. The name must be 1 to 16 characters in length and contain lowercase letters, digits, and underscores (_). It must start with a lowercase letter.
        :param pulumi.Input[str] account_password: Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters. You have to specify one of `account_password` and `kms_encrypted_password` fields.
        :param pulumi.Input[str] account_privilege: The privilege of account access database. Valid values: 
               - RoleReadOnly: This value is only for Redis and Memcache
               - RoleReadWrite: This value is only for Redis and Memcache
               - RoleRepl: This value supports instance to read, write, and open SYNC / PSYNC commands.
               Only for Redis which engine version is 4.0 and architecture type is standard
        :param pulumi.Input[str] account_type: Privilege type of account.
               - Normal: Common privilege.
               Default to Normal.
        :param pulumi.Input[str] description: Database description. It cannot begin with https://. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.
        :param pulumi.Input[str] instance_id: The Id of instance in which account belongs (The engine version of instance must be 4.0 or 4.0+).
        :param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a KVStore account. If the `account_password` is filled in, this field will be ignored.
        :param pulumi.Input[Mapping[str, Any]] kms_encryption_context: An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a KVStore account with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
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

            if account_name is None:
                raise TypeError("Missing required property 'account_name'")
            __props__['account_name'] = account_name
            __props__['account_password'] = account_password
            __props__['account_privilege'] = account_privilege
            __props__['account_type'] = account_type
            __props__['description'] = description
            if instance_id is None:
                raise TypeError("Missing required property 'instance_id'")
            __props__['instance_id'] = instance_id
            __props__['kms_encrypted_password'] = kms_encrypted_password
            __props__['kms_encryption_context'] = kms_encryption_context
            __props__['status'] = None
        super(Account, __self__).__init__(
            'alicloud:kvstore/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name: Optional[pulumi.Input[str]] = None,
            account_password: Optional[pulumi.Input[str]] = None,
            account_privilege: Optional[pulumi.Input[str]] = None,
            account_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            kms_encrypted_password: Optional[pulumi.Input[str]] = None,
            kms_encryption_context: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the account. The name must be 1 to 16 characters in length and contain lowercase letters, digits, and underscores (_). It must start with a lowercase letter.
        :param pulumi.Input[str] account_password: Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters. You have to specify one of `account_password` and `kms_encrypted_password` fields.
        :param pulumi.Input[str] account_privilege: The privilege of account access database. Valid values: 
               - RoleReadOnly: This value is only for Redis and Memcache
               - RoleReadWrite: This value is only for Redis and Memcache
               - RoleRepl: This value supports instance to read, write, and open SYNC / PSYNC commands.
               Only for Redis which engine version is 4.0 and architecture type is standard
        :param pulumi.Input[str] account_type: Privilege type of account.
               - Normal: Common privilege.
               Default to Normal.
        :param pulumi.Input[str] description: Database description. It cannot begin with https://. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.
        :param pulumi.Input[str] instance_id: The Id of instance in which account belongs (The engine version of instance must be 4.0 or 4.0+).
        :param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a KVStore account. If the `account_password` is filled in, this field will be ignored.
        :param pulumi.Input[Mapping[str, Any]] kms_encryption_context: An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a KVStore account with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
        :param pulumi.Input[str] status: The status of KVStore Account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_name"] = account_name
        __props__["account_password"] = account_password
        __props__["account_privilege"] = account_privilege
        __props__["account_type"] = account_type
        __props__["description"] = description
        __props__["instance_id"] = instance_id
        __props__["kms_encrypted_password"] = kms_encrypted_password
        __props__["kms_encryption_context"] = kms_encryption_context
        __props__["status"] = status
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[str]:
        """
        The name of the account. The name must be 1 to 16 characters in length and contain lowercase letters, digits, and underscores (_). It must start with a lowercase letter.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="accountPassword")
    def account_password(self) -> pulumi.Output[Optional[str]]:
        """
        Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters. You have to specify one of `account_password` and `kms_encrypted_password` fields.
        """
        return pulumi.get(self, "account_password")

    @property
    @pulumi.getter(name="accountPrivilege")
    def account_privilege(self) -> pulumi.Output[Optional[str]]:
        """
        The privilege of account access database. Valid values: 
        - RoleReadOnly: This value is only for Redis and Memcache
        - RoleReadWrite: This value is only for Redis and Memcache
        - RoleRepl: This value supports instance to read, write, and open SYNC / PSYNC commands.
        Only for Redis which engine version is 4.0 and architecture type is standard
        """
        return pulumi.get(self, "account_privilege")

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> pulumi.Output[Optional[str]]:
        """
        Privilege type of account.
        - Normal: Common privilege.
        Default to Normal.
        """
        return pulumi.get(self, "account_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Database description. It cannot begin with https://. It must start with a Chinese character or English letter. It can include Chinese and English characters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The Id of instance in which account belongs (The engine version of instance must be 4.0 or 4.0+).
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="kmsEncryptedPassword")
    def kms_encrypted_password(self) -> pulumi.Output[Optional[str]]:
        """
        An KMS encrypts password used to a KVStore account. If the `account_password` is filled in, this field will be ignored.
        """
        return pulumi.get(self, "kms_encrypted_password")

    @property
    @pulumi.getter(name="kmsEncryptionContext")
    def kms_encryption_context(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        An KMS encryption context used to decrypt `kms_encrypted_password` before creating or updating a KVStore account with `kms_encrypted_password`. See [Encryption Context](https://www.alibabacloud.com/help/doc-detail/42975.htm). It is valid when `kms_encrypted_password` is set.
        """
        return pulumi.get(self, "kms_encryption_context")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of KVStore Account.
        """
        return pulumi.get(self, "status")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


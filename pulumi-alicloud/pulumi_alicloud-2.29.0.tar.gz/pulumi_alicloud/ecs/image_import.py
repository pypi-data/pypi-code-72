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

__all__ = ['ImageImport']


class ImageImport(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disk_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageImportDiskDeviceMappingArgs']]]]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 license_type: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Import a copy of your local on-premise file to ECS, and appear as a custom replacement in the corresponding domain.

        > **NOTE:** You must upload the image file to the object storage OSS in advance.

        > **NOTE:** The region where the image is imported must be the same region as the OSS bucket where the image file is uploaded.

        > **NOTE:** Available in 1.69.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        this = alicloud.ecs.ImageImport("this",
            architecture="x86_64",
            description="test import image",
            disk_device_mappings=[alicloud.ecs.ImageImportDiskDeviceMappingArgs(
                disk_image_size=5,
                oss_bucket="testimportimage",
                oss_object="root.img",
            )],
            image_name="test-import-image",
            license_type="Auto",
            os_type="linux",
            platform="Ubuntu")
        ```
        ## Attributes Reference0

         The following attributes are exported:

        * `id` - ID of the image.

        ## Import

        image can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/imageImport:ImageImport default m-uf66871ape***yg1q***
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture: Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `i386` , Default is `x86_64`.
        :param pulumi.Input[str] description: Description of the image. The length is 2 to 256 English or Chinese characters, and cannot begin with http: // and https: //.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageImportDiskDeviceMappingArgs']]]] disk_device_mappings: Description of the system with disks and snapshots under the image.
        :param pulumi.Input[str] image_name: The image name. The length is 2 ~ 128 English or Chinese characters. Must start with a english letter or Chinese, and cannot start with http: // and https: //. Can contain numbers, colons (:), underscores (_), or hyphens (-).
        :param pulumi.Input[str] license_type: The type of the license used to activate the operating system after the image is imported. Default value: `Auto`. Valid values: `Auto`,`Aliyun`,`BYOL`.
        :param pulumi.Input[str] os_type: Operating system platform type. Valid values: `windows`, Default is `linux`.
        :param pulumi.Input[str] platform: Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `CentOS`, `Ubuntu`, `SUSE`, `OpenSUSE`, `Debian`, `CoreOS`, `Windows Server 2003`, `Windows Server 2008`, `Windows Server 2012`, `Windows 7`, Default is `Others Linux`, `Customized Linux`.
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

            __props__['architecture'] = architecture
            __props__['description'] = description
            if disk_device_mappings is None:
                raise TypeError("Missing required property 'disk_device_mappings'")
            __props__['disk_device_mappings'] = disk_device_mappings
            __props__['image_name'] = image_name
            __props__['license_type'] = license_type
            __props__['os_type'] = os_type
            __props__['platform'] = platform
        super(ImageImport, __self__).__init__(
            'alicloud:ecs/imageImport:ImageImport',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            architecture: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            disk_device_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageImportDiskDeviceMappingArgs']]]]] = None,
            image_name: Optional[pulumi.Input[str]] = None,
            license_type: Optional[pulumi.Input[str]] = None,
            os_type: Optional[pulumi.Input[str]] = None,
            platform: Optional[pulumi.Input[str]] = None) -> 'ImageImport':
        """
        Get an existing ImageImport resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] architecture: Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `i386` , Default is `x86_64`.
        :param pulumi.Input[str] description: Description of the image. The length is 2 to 256 English or Chinese characters, and cannot begin with http: // and https: //.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ImageImportDiskDeviceMappingArgs']]]] disk_device_mappings: Description of the system with disks and snapshots under the image.
        :param pulumi.Input[str] image_name: The image name. The length is 2 ~ 128 English or Chinese characters. Must start with a english letter or Chinese, and cannot start with http: // and https: //. Can contain numbers, colons (:), underscores (_), or hyphens (-).
        :param pulumi.Input[str] license_type: The type of the license used to activate the operating system after the image is imported. Default value: `Auto`. Valid values: `Auto`,`Aliyun`,`BYOL`.
        :param pulumi.Input[str] os_type: Operating system platform type. Valid values: `windows`, Default is `linux`.
        :param pulumi.Input[str] platform: Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `CentOS`, `Ubuntu`, `SUSE`, `OpenSUSE`, `Debian`, `CoreOS`, `Windows Server 2003`, `Windows Server 2008`, `Windows Server 2012`, `Windows 7`, Default is `Others Linux`, `Customized Linux`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["architecture"] = architecture
        __props__["description"] = description
        __props__["disk_device_mappings"] = disk_device_mappings
        __props__["image_name"] = image_name
        __props__["license_type"] = license_type
        __props__["os_type"] = os_type
        __props__["platform"] = platform
        return ImageImport(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the architecture of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `i386` , Default is `x86_64`.
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the image. The length is 2 to 256 English or Chinese characters, and cannot begin with http: // and https: //.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="diskDeviceMappings")
    def disk_device_mappings(self) -> pulumi.Output[Sequence['outputs.ImageImportDiskDeviceMapping']]:
        """
        Description of the system with disks and snapshots under the image.
        """
        return pulumi.get(self, "disk_device_mappings")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[Optional[str]]:
        """
        The image name. The length is 2 ~ 128 English or Chinese characters. Must start with a english letter or Chinese, and cannot start with http: // and https: //. Can contain numbers, colons (:), underscores (_), or hyphens (-).
        """
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the license used to activate the operating system after the image is imported. Default value: `Auto`. Valid values: `Auto`,`Aliyun`,`BYOL`.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[str]]:
        """
        Operating system platform type. Valid values: `windows`, Default is `linux`.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the operating system platform of the system disk after you specify a data disk snapshot as the data source of the system disk for creating an image. Valid values: `CentOS`, `Ubuntu`, `SUSE`, `OpenSUSE`, `Debian`, `CoreOS`, `Windows Server 2003`, `Windows Server 2008`, `Windows Server 2012`, `Windows 7`, Default is `Others Linux`, `Customized Linux`.
        """
        return pulumi.get(self, "platform")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


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

__all__ = ['Domain']


class Domain(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_config: Optional[pulumi.Input[pulumi.InputType['DomainAuthConfigArgs']]] = None,
                 block_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 cache_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainCacheConfigArgs']]]]] = None,
                 cdn_type: Optional[pulumi.Input[str]] = None,
                 certificate_config: Optional[pulumi.Input[pulumi.InputType['DomainCertificateConfigArgs']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 http_header_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainHttpHeaderConfigArgs']]]]] = None,
                 optimize_enable: Optional[pulumi.Input[str]] = None,
                 page404_config: Optional[pulumi.Input[pulumi.InputType['DomainPage404ConfigArgs']]] = None,
                 page_compress_enable: Optional[pulumi.Input[str]] = None,
                 parameter_filter_config: Optional[pulumi.Input[pulumi.InputType['DomainParameterFilterConfigArgs']]] = None,
                 range_enable: Optional[pulumi.Input[str]] = None,
                 refer_config: Optional[pulumi.Input[pulumi.InputType['DomainReferConfigArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 source_port: Optional[pulumi.Input[int]] = None,
                 source_type: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 video_seek_enable: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Domain resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DomainAuthConfigArgs']] auth_config: The auth config of the accelerated domain.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainCacheConfigArgs']]]] cache_configs: The cache configs of the accelerated domain.
        :param pulumi.Input[str] cdn_type: Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
        :param pulumi.Input[str] domain_name: Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainHttpHeaderConfigArgs']]]] http_header_configs: The http header configs of the accelerated domain.
        :param pulumi.Input[str] optimize_enable: Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
        :param pulumi.Input[pulumi.InputType['DomainPage404ConfigArgs']] page404_config: The error page config of the accelerated domain.
        :param pulumi.Input[str] page_compress_enable: Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        :param pulumi.Input[pulumi.InputType['DomainParameterFilterConfigArgs']] parameter_filter_config: The parameter filter config of the accelerated domain.
        :param pulumi.Input[str] range_enable: Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        :param pulumi.Input[pulumi.InputType['DomainReferConfigArgs']] refer_config: The refer config of the accelerated domain.
        :param pulumi.Input[str] scope: Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
        :param pulumi.Input[int] source_port: Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
        :param pulumi.Input[str] source_type: Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sources: Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
        :param pulumi.Input[str] video_seek_enable: Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
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

            if auth_config is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("auth_config is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['auth_config'] = auth_config
            if block_ips is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("block_ips is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['block_ips'] = block_ips
            if cache_configs is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("cache_configs is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['cache_configs'] = cache_configs
            if cdn_type is None:
                raise TypeError("Missing required property 'cdn_type'")
            __props__['cdn_type'] = cdn_type
            if certificate_config is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("certificate_config is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['certificate_config'] = certificate_config
            if domain_name is None:
                raise TypeError("Missing required property 'domain_name'")
            __props__['domain_name'] = domain_name
            if http_header_configs is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("http_header_configs is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['http_header_configs'] = http_header_configs
            if optimize_enable is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("optimize_enable is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['optimize_enable'] = optimize_enable
            if page404_config is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("page404_config is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['page404_config'] = page404_config
            if page_compress_enable is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("page_compress_enable is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['page_compress_enable'] = page_compress_enable
            if parameter_filter_config is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("parameter_filter_config is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['parameter_filter_config'] = parameter_filter_config
            if range_enable is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("range_enable is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['range_enable'] = range_enable
            if refer_config is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("refer_config is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['refer_config'] = refer_config
            __props__['scope'] = scope
            if source_port is not None:
                warnings.warn("""Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.""", DeprecationWarning)
                pulumi.log.warn("source_port is deprecated: Use `alicloud_cdn_domain_new` configuration `sources` block `port` argument instead.")
            __props__['source_port'] = source_port
            if source_type is not None:
                warnings.warn("""Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.""", DeprecationWarning)
                pulumi.log.warn("source_type is deprecated: Use `alicloud_cdn_domain_new` configuration `sources` block `type` argument instead.")
            __props__['source_type'] = source_type
            if sources is not None:
                warnings.warn("""Use `alicloud_cdn_domain_new` configuration `sources` argument instead.""", DeprecationWarning)
                pulumi.log.warn("sources is deprecated: Use `alicloud_cdn_domain_new` configuration `sources` argument instead.")
            __props__['sources'] = sources
            if video_seek_enable is not None:
                warnings.warn("""Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.""", DeprecationWarning)
                pulumi.log.warn("video_seek_enable is deprecated: Use `alicloud_cdn_domain_config` configuration `function_name` and `function_args` arguments instead.")
            __props__['video_seek_enable'] = video_seek_enable
        super(Domain, __self__).__init__(
            'alicloud:cdn/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth_config: Optional[pulumi.Input[pulumi.InputType['DomainAuthConfigArgs']]] = None,
            block_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            cache_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainCacheConfigArgs']]]]] = None,
            cdn_type: Optional[pulumi.Input[str]] = None,
            certificate_config: Optional[pulumi.Input[pulumi.InputType['DomainCertificateConfigArgs']]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            http_header_configs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainHttpHeaderConfigArgs']]]]] = None,
            optimize_enable: Optional[pulumi.Input[str]] = None,
            page404_config: Optional[pulumi.Input[pulumi.InputType['DomainPage404ConfigArgs']]] = None,
            page_compress_enable: Optional[pulumi.Input[str]] = None,
            parameter_filter_config: Optional[pulumi.Input[pulumi.InputType['DomainParameterFilterConfigArgs']]] = None,
            range_enable: Optional[pulumi.Input[str]] = None,
            refer_config: Optional[pulumi.Input[pulumi.InputType['DomainReferConfigArgs']]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            source_port: Optional[pulumi.Input[int]] = None,
            source_type: Optional[pulumi.Input[str]] = None,
            sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            video_seek_enable: Optional[pulumi.Input[str]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DomainAuthConfigArgs']] auth_config: The auth config of the accelerated domain.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainCacheConfigArgs']]]] cache_configs: The cache configs of the accelerated domain.
        :param pulumi.Input[str] cdn_type: Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
        :param pulumi.Input[str] domain_name: Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainHttpHeaderConfigArgs']]]] http_header_configs: The http header configs of the accelerated domain.
        :param pulumi.Input[str] optimize_enable: Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
        :param pulumi.Input[pulumi.InputType['DomainPage404ConfigArgs']] page404_config: The error page config of the accelerated domain.
        :param pulumi.Input[str] page_compress_enable: Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        :param pulumi.Input[pulumi.InputType['DomainParameterFilterConfigArgs']] parameter_filter_config: The parameter filter config of the accelerated domain.
        :param pulumi.Input[str] range_enable: Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        :param pulumi.Input[pulumi.InputType['DomainReferConfigArgs']] refer_config: The refer config of the accelerated domain.
        :param pulumi.Input[str] scope: Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
        :param pulumi.Input[int] source_port: Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
        :param pulumi.Input[str] source_type: Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sources: Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
        :param pulumi.Input[str] video_seek_enable: Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auth_config"] = auth_config
        __props__["block_ips"] = block_ips
        __props__["cache_configs"] = cache_configs
        __props__["cdn_type"] = cdn_type
        __props__["certificate_config"] = certificate_config
        __props__["domain_name"] = domain_name
        __props__["http_header_configs"] = http_header_configs
        __props__["optimize_enable"] = optimize_enable
        __props__["page404_config"] = page404_config
        __props__["page_compress_enable"] = page_compress_enable
        __props__["parameter_filter_config"] = parameter_filter_config
        __props__["range_enable"] = range_enable
        __props__["refer_config"] = refer_config
        __props__["scope"] = scope
        __props__["source_port"] = source_port
        __props__["source_type"] = source_type
        __props__["sources"] = sources
        __props__["video_seek_enable"] = video_seek_enable
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> pulumi.Output[Optional['outputs.DomainAuthConfig']]:
        """
        The auth config of the accelerated domain.
        """
        return pulumi.get(self, "auth_config")

    @property
    @pulumi.getter(name="blockIps")
    def block_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "block_ips")

    @property
    @pulumi.getter(name="cacheConfigs")
    def cache_configs(self) -> pulumi.Output[Optional[Sequence['outputs.DomainCacheConfig']]]:
        """
        The cache configs of the accelerated domain.
        """
        return pulumi.get(self, "cache_configs")

    @property
    @pulumi.getter(name="cdnType")
    def cdn_type(self) -> pulumi.Output[str]:
        """
        Cdn type of the accelerated domain. Valid values are `web`, `download`, `video`, `liveStream`.
        """
        return pulumi.get(self, "cdn_type")

    @property
    @pulumi.getter(name="certificateConfig")
    def certificate_config(self) -> pulumi.Output[Optional['outputs.DomainCertificateConfig']]:
        return pulumi.get(self, "certificate_config")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="httpHeaderConfigs")
    def http_header_configs(self) -> pulumi.Output[Optional[Sequence['outputs.DomainHttpHeaderConfig']]]:
        """
        The http header configs of the accelerated domain.
        """
        return pulumi.get(self, "http_header_configs")

    @property
    @pulumi.getter(name="optimizeEnable")
    def optimize_enable(self) -> pulumi.Output[Optional[str]]:
        """
        Page Optimize config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is `on`.
        """
        return pulumi.get(self, "optimize_enable")

    @property
    @pulumi.getter(name="page404Config")
    def page404_config(self) -> pulumi.Output[Optional['outputs.DomainPage404Config']]:
        """
        The error page config of the accelerated domain.
        """
        return pulumi.get(self, "page404_config")

    @property
    @pulumi.getter(name="pageCompressEnable")
    def page_compress_enable(self) -> pulumi.Output[Optional[str]]:
        """
        Page Compress config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        """
        return pulumi.get(self, "page_compress_enable")

    @property
    @pulumi.getter(name="parameterFilterConfig")
    def parameter_filter_config(self) -> pulumi.Output[Optional['outputs.DomainParameterFilterConfig']]:
        """
        The parameter filter config of the accelerated domain.
        """
        return pulumi.get(self, "parameter_filter_config")

    @property
    @pulumi.getter(name="rangeEnable")
    def range_enable(self) -> pulumi.Output[Optional[str]]:
        """
        Range Source config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        """
        return pulumi.get(self, "range_enable")

    @property
    @pulumi.getter(name="referConfig")
    def refer_config(self) -> pulumi.Output[Optional['outputs.DomainReferConfig']]:
        """
        The refer config of the accelerated domain.
        """
        return pulumi.get(self, "refer_config")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[str]:
        """
        Scope of the accelerated domain. Valid values are `domestic`, `overseas`, `global`. Default value is `domestic`. This parameter's setting is valid Only for the international users and domestic L3 and above users .
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="sourcePort")
    def source_port(self) -> pulumi.Output[Optional[int]]:
        """
        Source port of the accelerated domain. Valid values are `80` and `443`. Default value is `80`. You must use `80` when the `source_type` is `oss`.
        """
        return pulumi.get(self, "source_port")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[Optional[str]]:
        """
        Source type of the accelerated domain. Valid values are `ipaddr`, `domain`, `oss`. You must set this parameter when `cdn_type` value is not `liveStream`.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Sources of the accelerated domain. It's a list of domain names or IP address and consists of at most 20 items. You must set this parameter when `cdn_type` value is not `liveStream`.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="videoSeekEnable")
    def video_seek_enable(self) -> pulumi.Output[Optional[str]]:
        """
        Video Seek config of the accelerated domain. Valid values are `on` and `off`. Default value is `off`.
        """
        return pulumi.get(self, "video_seek_enable")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['QosPolicy']


class QosPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dest_cidr: Optional[pulumi.Input[str]] = None,
                 dest_port_range: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 qos_id: Optional[pulumi.Input[str]] = None,
                 source_cidr: Optional[pulumi.Input[str]] = None,
                 source_port_range: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Sag qos policy resource.
        You need to create a QoS policy to set priorities, rate limits, and quintuple rules for different messages.

        For information about Sag Qos Policy and how to use it, see [What is Qos Policy](https://www.alibabacloud.com/help/doc-detail/140065.htm).

        > **NOTE:** Available in 1.60.0+

        > **NOTE:** Only the following regions support. [`cn-shanghai`, `cn-shanghai-finance-1`, `cn-hongkong`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-5`, `ap-northeast-1`, `eu-central-1`]

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default_qos = alicloud.rocketmq.Qos("defaultQos")
        default_qos_policy = alicloud.rocketmq.QosPolicy("defaultQosPolicy",
            qos_id=default_qos.id,
            description="tf-testSagQosPolicyDescription",
            priority=1,
            ip_protocol="ALL",
            source_cidr="192.168.0.0/24",
            source_port_range="-1/-1",
            dest_cidr="10.10.0.0/24",
            dest_port_range="-1/-1",
            start_time="2019-10-25T16:41:33+0800",
            end_time="2019-10-26T16:41:33+0800")
        ```

        ## Import

        The Sag Qos Policy can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:rocketmq/qosPolicy:QosPolicy example qos-abc123456:qospy-abc123456
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the QoS policy.
        :param pulumi.Input[str] dest_cidr: The destination CIDR block.
        :param pulumi.Input[str] dest_port_range: The destination port range.
        :param pulumi.Input[str] end_time: The expiration time of the quintuple rule.
        :param pulumi.Input[str] ip_protocol: The transport layer protocol.
        :param pulumi.Input[str] name: The name of the QoS policy.
        :param pulumi.Input[int] priority: The priority of the quintuple rule. A smaller value indicates a higher priority. If the priorities of two quintuple rules are the same, the rule created earlier is applied first.Value range: 1 to 7.
        :param pulumi.Input[str] qos_id: The instance ID of the QoS policy to which the quintuple rule is created.
        :param pulumi.Input[str] source_cidr: The source CIDR block.
        :param pulumi.Input[str] source_port_range: The source port range of the transport layer.
        :param pulumi.Input[str] start_time: The time when the quintuple rule takes effect.
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
            if dest_cidr is None:
                raise TypeError("Missing required property 'dest_cidr'")
            __props__['dest_cidr'] = dest_cidr
            if dest_port_range is None:
                raise TypeError("Missing required property 'dest_port_range'")
            __props__['dest_port_range'] = dest_port_range
            __props__['end_time'] = end_time
            if ip_protocol is None:
                raise TypeError("Missing required property 'ip_protocol'")
            __props__['ip_protocol'] = ip_protocol
            __props__['name'] = name
            if priority is None:
                raise TypeError("Missing required property 'priority'")
            __props__['priority'] = priority
            if qos_id is None:
                raise TypeError("Missing required property 'qos_id'")
            __props__['qos_id'] = qos_id
            if source_cidr is None:
                raise TypeError("Missing required property 'source_cidr'")
            __props__['source_cidr'] = source_cidr
            if source_port_range is None:
                raise TypeError("Missing required property 'source_port_range'")
            __props__['source_port_range'] = source_port_range
            __props__['start_time'] = start_time
        super(QosPolicy, __self__).__init__(
            'alicloud:rocketmq/qosPolicy:QosPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            dest_cidr: Optional[pulumi.Input[str]] = None,
            dest_port_range: Optional[pulumi.Input[str]] = None,
            end_time: Optional[pulumi.Input[str]] = None,
            ip_protocol: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            qos_id: Optional[pulumi.Input[str]] = None,
            source_cidr: Optional[pulumi.Input[str]] = None,
            source_port_range: Optional[pulumi.Input[str]] = None,
            start_time: Optional[pulumi.Input[str]] = None) -> 'QosPolicy':
        """
        Get an existing QosPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the QoS policy.
        :param pulumi.Input[str] dest_cidr: The destination CIDR block.
        :param pulumi.Input[str] dest_port_range: The destination port range.
        :param pulumi.Input[str] end_time: The expiration time of the quintuple rule.
        :param pulumi.Input[str] ip_protocol: The transport layer protocol.
        :param pulumi.Input[str] name: The name of the QoS policy.
        :param pulumi.Input[int] priority: The priority of the quintuple rule. A smaller value indicates a higher priority. If the priorities of two quintuple rules are the same, the rule created earlier is applied first.Value range: 1 to 7.
        :param pulumi.Input[str] qos_id: The instance ID of the QoS policy to which the quintuple rule is created.
        :param pulumi.Input[str] source_cidr: The source CIDR block.
        :param pulumi.Input[str] source_port_range: The source port range of the transport layer.
        :param pulumi.Input[str] start_time: The time when the quintuple rule takes effect.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["dest_cidr"] = dest_cidr
        __props__["dest_port_range"] = dest_port_range
        __props__["end_time"] = end_time
        __props__["ip_protocol"] = ip_protocol
        __props__["name"] = name
        __props__["priority"] = priority
        __props__["qos_id"] = qos_id
        __props__["source_cidr"] = source_cidr
        __props__["source_port_range"] = source_port_range
        __props__["start_time"] = start_time
        return QosPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the QoS policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destCidr")
    def dest_cidr(self) -> pulumi.Output[str]:
        """
        The destination CIDR block.
        """
        return pulumi.get(self, "dest_cidr")

    @property
    @pulumi.getter(name="destPortRange")
    def dest_port_range(self) -> pulumi.Output[str]:
        """
        The destination port range.
        """
        return pulumi.get(self, "dest_port_range")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[str]]:
        """
        The expiration time of the quintuple rule.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[str]:
        """
        The transport layer protocol.
        """
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the QoS policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The priority of the quintuple rule. A smaller value indicates a higher priority. If the priorities of two quintuple rules are the same, the rule created earlier is applied first.Value range: 1 to 7.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="qosId")
    def qos_id(self) -> pulumi.Output[str]:
        """
        The instance ID of the QoS policy to which the quintuple rule is created.
        """
        return pulumi.get(self, "qos_id")

    @property
    @pulumi.getter(name="sourceCidr")
    def source_cidr(self) -> pulumi.Output[str]:
        """
        The source CIDR block.
        """
        return pulumi.get(self, "source_cidr")

    @property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> pulumi.Output[str]:
        """
        The source port range of the transport layer.
        """
        return pulumi.get(self, "source_port_range")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The time when the quintuple rule takes effect.
        """
        return pulumi.get(self, "start_time")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


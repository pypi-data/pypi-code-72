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
    'GetMongoInstancesInstanceResult',
    'GetMongoInstancesInstanceMongoResult',
    'GetMongoInstancesInstanceShardResult',
]

@pulumi.output_type
class GetMongoInstancesInstanceResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 charge_type: str,
                 creation_time: str,
                 engine: str,
                 engine_version: str,
                 expiration_time: str,
                 id: str,
                 instance_class: str,
                 instance_type: str,
                 lock_mode: str,
                 mongos: Sequence['outputs.GetMongoInstancesInstanceMongoResult'],
                 name: str,
                 network_type: str,
                 region_id: str,
                 replication: str,
                 shards: Sequence['outputs.GetMongoInstancesInstanceShardResult'],
                 status: str,
                 storage: int,
                 tags: Mapping[str, Any]):
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "creation_time", creation_time)
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "engine_version", engine_version)
        pulumi.set(__self__, "expiration_time", expiration_time)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "instance_class", instance_class)
        pulumi.set(__self__, "instance_type", instance_type)
        pulumi.set(__self__, "lock_mode", lock_mode)
        pulumi.set(__self__, "mongos", mongos)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "network_type", network_type)
        pulumi.set(__self__, "region_id", region_id)
        pulumi.set(__self__, "replication", replication)
        pulumi.set(__self__, "shards", shards)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "storage", storage)
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def engine(self) -> str:
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> str:
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> str:
        return pulumi.get(self, "instance_class")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="lockMode")
    def lock_mode(self) -> str:
        return pulumi.get(self, "lock_mode")

    @property
    @pulumi.getter
    def mongos(self) -> Sequence['outputs.GetMongoInstancesInstanceMongoResult']:
        return pulumi.get(self, "mongos")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> str:
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> str:
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter
    def replication(self) -> str:
        return pulumi.get(self, "replication")

    @property
    @pulumi.getter
    def shards(self) -> Sequence['outputs.GetMongoInstancesInstanceShardResult']:
        return pulumi.get(self, "shards")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def storage(self) -> int:
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, Any]:
        return pulumi.get(self, "tags")


@pulumi.output_type
class GetMongoInstancesInstanceMongoResult(dict):
    def __init__(__self__, *,
                 class_: str,
                 description: str,
                 node_id: str):
        pulumi.set(__self__, "class_", class_)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "node_id", node_id)

    @property
    @pulumi.getter(name="class")
    def class_(self) -> str:
        return pulumi.get(self, "class_")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> str:
        return pulumi.get(self, "node_id")


@pulumi.output_type
class GetMongoInstancesInstanceShardResult(dict):
    def __init__(__self__, *,
                 class_: str,
                 description: str,
                 node_id: str,
                 storage: int):
        pulumi.set(__self__, "class_", class_)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "node_id", node_id)
        pulumi.set(__self__, "storage", storage)

    @property
    @pulumi.getter(name="class")
    def class_(self) -> str:
        return pulumi.get(self, "class_")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> str:
        return pulumi.get(self, "node_id")

    @property
    @pulumi.getter
    def storage(self) -> int:
        return pulumi.get(self, "storage")



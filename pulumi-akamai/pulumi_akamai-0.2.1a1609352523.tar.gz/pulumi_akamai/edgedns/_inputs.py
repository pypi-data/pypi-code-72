# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'DnsZoneTsigKeyArgs',
]

@pulumi.input_type
class DnsZoneTsigKeyArgs:
    def __init__(__self__, *,
                 algorithm: pulumi.Input[str],
                 name: pulumi.Input[str],
                 secret: pulumi.Input[str]):
        pulumi.set(__self__, "algorithm", algorithm)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Input[str]:
        return pulumi.get(self, "algorithm")

    @algorithm.setter
    def algorithm(self, value: pulumi.Input[str]):
        pulumi.set(self, "algorithm", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)



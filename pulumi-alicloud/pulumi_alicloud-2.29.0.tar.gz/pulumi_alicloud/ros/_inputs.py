# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ChangeSetParameterArgs',
    'StackGroupParameterArgs',
    'StackParameterArgs',
]

@pulumi.input_type
class ChangeSetParameterArgs:
    def __init__(__self__, *,
                 parameter_key: pulumi.Input[str],
                 parameter_value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] parameter_key: The parameter key.
        :param pulumi.Input[str] parameter_value: The parameter value.
        """
        pulumi.set(__self__, "parameter_key", parameter_key)
        pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> pulumi.Input[str]:
        """
        The parameter key.
        """
        return pulumi.get(self, "parameter_key")

    @parameter_key.setter
    def parameter_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_key", value)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[str]:
        """
        The parameter value.
        """
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_value", value)


@pulumi.input_type
class StackGroupParameterArgs:
    def __init__(__self__, *,
                 parameter_key: Optional[pulumi.Input[str]] = None,
                 parameter_value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] parameter_key: The parameter key.
        :param pulumi.Input[str] parameter_value: The parameter value.
        """
        if parameter_key is not None:
            pulumi.set(__self__, "parameter_key", parameter_key)
        if parameter_value is not None:
            pulumi.set(__self__, "parameter_value", parameter_value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> Optional[pulumi.Input[str]]:
        """
        The parameter key.
        """
        return pulumi.get(self, "parameter_key")

    @parameter_key.setter
    def parameter_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_key", value)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> Optional[pulumi.Input[str]]:
        """
        The parameter value.
        """
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_value", value)


@pulumi.input_type
class StackParameterArgs:
    def __init__(__self__, *,
                 parameter_value: pulumi.Input[str],
                 parameter_key: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] parameter_value: The parameter value.
        :param pulumi.Input[str] parameter_key: The parameter key.
        """
        pulumi.set(__self__, "parameter_value", parameter_value)
        if parameter_key is not None:
            pulumi.set(__self__, "parameter_key", parameter_key)

    @property
    @pulumi.getter(name="parameterValue")
    def parameter_value(self) -> pulumi.Input[str]:
        """
        The parameter value.
        """
        return pulumi.get(self, "parameter_value")

    @parameter_value.setter
    def parameter_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "parameter_value", value)

    @property
    @pulumi.getter(name="parameterKey")
    def parameter_key(self) -> Optional[pulumi.Input[str]]:
        """
        The parameter key.
        """
        return pulumi.get(self, "parameter_key")

    @parameter_key.setter
    def parameter_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameter_key", value)



# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .get_everyone_group import *
from .get_group import *
from .group import *
from .roles import *
from .rule import *

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "okta:group/group:Group":
                return Group(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "okta:group/roles:Roles":
                return Roles(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "okta:group/rule:Rule":
                return Rule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("okta", "group/group", _module_instance)
    pulumi.runtime.register_resource_module("okta", "group/roles", _module_instance)
    pulumi.runtime.register_resource_module("okta", "group/rule", _module_instance)

_register_module()

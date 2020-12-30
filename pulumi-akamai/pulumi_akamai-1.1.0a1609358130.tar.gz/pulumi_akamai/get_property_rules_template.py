# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetPropertyRulesTemplateResult',
    'AwaitableGetPropertyRulesTemplateResult',
    'get_property_rules_template',
]

@pulumi.output_type
class GetPropertyRulesTemplateResult:
    """
    A collection of values returned by getPropertyRulesTemplate.
    """
    def __init__(__self__, id=None, json=None, template_file=None, var_definition_file=None, var_values_file=None, variables=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if template_file and not isinstance(template_file, str):
            raise TypeError("Expected argument 'template_file' to be a str")
        pulumi.set(__self__, "template_file", template_file)
        if var_definition_file and not isinstance(var_definition_file, str):
            raise TypeError("Expected argument 'var_definition_file' to be a str")
        pulumi.set(__self__, "var_definition_file", var_definition_file)
        if var_values_file and not isinstance(var_values_file, str):
            raise TypeError("Expected argument 'var_values_file' to be a str")
        pulumi.set(__self__, "var_values_file", var_values_file)
        if variables and not isinstance(variables, list):
            raise TypeError("Expected argument 'variables' to be a list")
        pulumi.set(__self__, "variables", variables)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def json(self) -> str:
        return pulumi.get(self, "json")

    @property
    @pulumi.getter(name="templateFile")
    def template_file(self) -> str:
        return pulumi.get(self, "template_file")

    @property
    @pulumi.getter(name="varDefinitionFile")
    def var_definition_file(self) -> Optional[str]:
        return pulumi.get(self, "var_definition_file")

    @property
    @pulumi.getter(name="varValuesFile")
    def var_values_file(self) -> Optional[str]:
        return pulumi.get(self, "var_values_file")

    @property
    @pulumi.getter
    def variables(self) -> Optional[Sequence['outputs.GetPropertyRulesTemplateVariableResult']]:
        return pulumi.get(self, "variables")


class AwaitableGetPropertyRulesTemplateResult(GetPropertyRulesTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPropertyRulesTemplateResult(
            id=self.id,
            json=self.json,
            template_file=self.template_file,
            var_definition_file=self.var_definition_file,
            var_values_file=self.var_values_file,
            variables=self.variables)


def get_property_rules_template(template_file: Optional[str] = None,
                                var_definition_file: Optional[str] = None,
                                var_values_file: Optional[str] = None,
                                variables: Optional[Sequence[pulumi.InputType['GetPropertyRulesTemplateVariableArgs']]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPropertyRulesTemplateResult:
    """
    The `getPropertyRulesTemplate` data source lets you configure a rule tree through the use of JSON template files. A rule tree is a nested block of property
    rules in JSON format that include match criteria and behaviors.

    With this data source you define the location of the JSON template files and provide information about any user-defined variables included within the templates.

    The template format used in this data source matches those used in the [Property Manager CLI](https://learn.akamai.com/en-us/learn_akamai/getting_started_with_akamai_developers/developer_tools/getstartedpmcli.html#addanewsnippet).

    You can pass user-defined variables by supplying either:

    * paths to `variableDefinitions.json` and `variables.json` with syntax used in Property Manager CLI, or
    * a set of provider variables.

    ## Referencing sub-files from a template

    You can split each template out into a series of smaller template files. To add
    them to this data source, you need to include them in the currently loaded file,
    which corresponds to the value in the `template_file` argument.  For example, to
    include `example-file.json` from the `template` directory, use this syntax
    including the quotes: `"#include:example-file.json"`.  All files are resolved in
    relation to the directory that contains the starting template file.

    ## Inserting variables in a template

    You can also add variables to a template by using a string like `“${env.<variableName>}"`. You'll need the quotes here too.\
    These variables follow the format used in the [Property Manager CLI](https://github.com/akamai/cli-property-manager#update-the-variabledefinitions-file).  They differ from the provider variables which should resolve normally.

    ## Example Usage
    ## Argument reference

    * `template_file` - (Required) The absolute path to your top-level JSON template file. The top-level template combines smaller, nested JSON templates to form your property rule tree.
    * `variables` - (Optional) A definition of a variable. Variables aren't required and you can use multiple ones if needed. This argument conflicts with the `variable_definition_file` and `variable_values_file` arguments. A `variables` block includes:
        * `name` - The name of the variable used in template.
        * `type` - The type of variable: `string`, `number`, `bool`, or `jsonBlock`.
        * `value` - The value of the variable passed as a string.
    * `variable_definition_file` - (Optional) The absolute path to the file containing variable definitions and defaults. This file follows the syntax used in the [Property Manager CLI](https://github.com/akamai/cli-property-manager). This argument is required if you set `variable_values_file` and conflicts with `variables`.
    * `variable_values_file` - (Optional) The absolute path to the file containing variable values. This file follows the syntax used in the Property Manager CLI. This argument is required if you set `variable_definition_file` and conflicts with `variables`.

    ## Attributes reference

    This data source returns this attribute:

    * `json` - The fully expanded template with variables and all nested templates resolved.
    """
    __args__ = dict()
    __args__['templateFile'] = template_file
    __args__['varDefinitionFile'] = var_definition_file
    __args__['varValuesFile'] = var_values_file
    __args__['variables'] = variables
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('akamai:index/getPropertyRulesTemplate:getPropertyRulesTemplate', __args__, opts=opts, typ=GetPropertyRulesTemplateResult).value

    return AwaitableGetPropertyRulesTemplateResult(
        id=__ret__.id,
        json=__ret__.json,
        template_file=__ret__.template_file,
        var_definition_file=__ret__.var_definition_file,
        var_values_file=__ret__.var_values_file,
        variables=__ret__.variables)

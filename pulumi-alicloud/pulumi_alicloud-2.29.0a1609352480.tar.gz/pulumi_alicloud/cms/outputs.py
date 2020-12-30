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
    'AlarmEscalationsCritical',
    'AlarmEscalationsInfo',
    'AlarmEscalationsWarn',
    'GroupMetricRuleEscalations',
    'GroupMetricRuleEscalationsCritical',
    'GroupMetricRuleEscalationsInfo',
    'GroupMetricRuleEscalationsWarn',
    'SiteMonitorIspCity',
    'GetAlarmContactGroupsGroupResult',
    'GetAlarmContactsContactResult',
    'GetGroupMetricRulesRuleResult',
    'GetGroupMetricRulesRuleEscalationResult',
    'GetGroupMetricRulesRuleEscalationCriticalResult',
    'GetGroupMetricRulesRuleEscalationInfoResult',
    'GetGroupMetricRulesRuleEscalationWarnResult',
]

@pulumi.output_type
class AlarmEscalationsCritical(dict):
    def __init__(__self__, *,
                 comparison_operator: Optional[str] = None,
                 statistics: Optional[str] = None,
                 threshold: Optional[str] = None,
                 times: Optional[int] = None):
        """
        :param str comparison_operator: Critical level alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".
        :param str statistics: Critical level alarm statistics method.. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".
        :param str threshold: Critical level alarm threshold value, which must be a numeric value currently.
        :param int times: Critical level alarm retry times. Default to 3.
        """
        if comparison_operator is not None:
            pulumi.set(__self__, "comparison_operator", comparison_operator)
        if statistics is not None:
            pulumi.set(__self__, "statistics", statistics)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if times is not None:
            pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[str]:
        """
        Critical level alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> Optional[str]:
        """
        Critical level alarm statistics method.. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> Optional[str]:
        """
        Critical level alarm threshold value, which must be a numeric value currently.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> Optional[int]:
        """
        Critical level alarm retry times. Default to 3.
        """
        return pulumi.get(self, "times")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AlarmEscalationsInfo(dict):
    def __init__(__self__, *,
                 comparison_operator: Optional[str] = None,
                 statistics: Optional[str] = None,
                 threshold: Optional[str] = None,
                 times: Optional[int] = None):
        """
        :param str comparison_operator: Critical level alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".
        :param str statistics: Critical level alarm statistics method.. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".
        :param str threshold: Critical level alarm threshold value, which must be a numeric value currently.
        :param int times: Critical level alarm retry times. Default to 3.
        """
        if comparison_operator is not None:
            pulumi.set(__self__, "comparison_operator", comparison_operator)
        if statistics is not None:
            pulumi.set(__self__, "statistics", statistics)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if times is not None:
            pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[str]:
        """
        Critical level alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> Optional[str]:
        """
        Critical level alarm statistics method.. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> Optional[str]:
        """
        Critical level alarm threshold value, which must be a numeric value currently.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> Optional[int]:
        """
        Critical level alarm retry times. Default to 3.
        """
        return pulumi.get(self, "times")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AlarmEscalationsWarn(dict):
    def __init__(__self__, *,
                 comparison_operator: Optional[str] = None,
                 statistics: Optional[str] = None,
                 threshold: Optional[str] = None,
                 times: Optional[int] = None):
        """
        :param str comparison_operator: Critical level alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".
        :param str statistics: Critical level alarm statistics method.. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".
        :param str threshold: Critical level alarm threshold value, which must be a numeric value currently.
        :param int times: Critical level alarm retry times. Default to 3.
        """
        if comparison_operator is not None:
            pulumi.set(__self__, "comparison_operator", comparison_operator)
        if statistics is not None:
            pulumi.set(__self__, "statistics", statistics)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if times is not None:
            pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[str]:
        """
        Critical level alarm comparison operator. Valid values: ["<=", "<", ">", ">=", "==", "!="]. Default to "==".
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> Optional[str]:
        """
        Critical level alarm statistics method.. It must be consistent with that defined for metrics. Valid values: ["Average", "Minimum", "Maximum"]. Default to "Average".
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> Optional[str]:
        """
        Critical level alarm threshold value, which must be a numeric value currently.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> Optional[int]:
        """
        Critical level alarm retry times. Default to 3.
        """
        return pulumi.get(self, "times")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMetricRuleEscalations(dict):
    def __init__(__self__, *,
                 critical: Optional['outputs.GroupMetricRuleEscalationsCritical'] = None,
                 info: Optional['outputs.GroupMetricRuleEscalationsInfo'] = None,
                 warn: Optional['outputs.GroupMetricRuleEscalationsWarn'] = None):
        """
        :param 'GroupMetricRuleEscalationsCriticalArgs' critical: The critical level.
        :param 'GroupMetricRuleEscalationsInfoArgs' info: The info level.
        :param 'GroupMetricRuleEscalationsWarnArgs' warn: The warn level.
        """
        if critical is not None:
            pulumi.set(__self__, "critical", critical)
        if info is not None:
            pulumi.set(__self__, "info", info)
        if warn is not None:
            pulumi.set(__self__, "warn", warn)

    @property
    @pulumi.getter
    def critical(self) -> Optional['outputs.GroupMetricRuleEscalationsCritical']:
        """
        The critical level.
        """
        return pulumi.get(self, "critical")

    @property
    @pulumi.getter
    def info(self) -> Optional['outputs.GroupMetricRuleEscalationsInfo']:
        """
        The info level.
        """
        return pulumi.get(self, "info")

    @property
    @pulumi.getter
    def warn(self) -> Optional['outputs.GroupMetricRuleEscalationsWarn']:
        """
        The warn level.
        """
        return pulumi.get(self, "warn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMetricRuleEscalationsCritical(dict):
    def __init__(__self__, *,
                 comparison_operator: Optional[str] = None,
                 statistics: Optional[str] = None,
                 threshold: Optional[str] = None,
                 times: Optional[int] = None):
        """
        :param str comparison_operator: The comparison operator of the threshold for warn-level alerts.
        :param str statistics: The statistical aggregation method for warn-level alerts.
        :param str threshold: The threshold for warn-level alerts.
        :param int times: The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        if comparison_operator is not None:
            pulumi.set(__self__, "comparison_operator", comparison_operator)
        if statistics is not None:
            pulumi.set(__self__, "statistics", statistics)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if times is not None:
            pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[str]:
        """
        The comparison operator of the threshold for warn-level alerts.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> Optional[str]:
        """
        The statistical aggregation method for warn-level alerts.
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> Optional[str]:
        """
        The threshold for warn-level alerts.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> Optional[int]:
        """
        The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        return pulumi.get(self, "times")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMetricRuleEscalationsInfo(dict):
    def __init__(__self__, *,
                 comparison_operator: Optional[str] = None,
                 statistics: Optional[str] = None,
                 threshold: Optional[str] = None,
                 times: Optional[int] = None):
        """
        :param str comparison_operator: The comparison operator of the threshold for warn-level alerts.
        :param str statistics: The statistical aggregation method for warn-level alerts.
        :param str threshold: The threshold for warn-level alerts.
        :param int times: The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        if comparison_operator is not None:
            pulumi.set(__self__, "comparison_operator", comparison_operator)
        if statistics is not None:
            pulumi.set(__self__, "statistics", statistics)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if times is not None:
            pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[str]:
        """
        The comparison operator of the threshold for warn-level alerts.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> Optional[str]:
        """
        The statistical aggregation method for warn-level alerts.
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> Optional[str]:
        """
        The threshold for warn-level alerts.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> Optional[int]:
        """
        The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        return pulumi.get(self, "times")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GroupMetricRuleEscalationsWarn(dict):
    def __init__(__self__, *,
                 comparison_operator: Optional[str] = None,
                 statistics: Optional[str] = None,
                 threshold: Optional[str] = None,
                 times: Optional[int] = None):
        """
        :param str comparison_operator: The comparison operator of the threshold for warn-level alerts.
        :param str statistics: The statistical aggregation method for warn-level alerts.
        :param str threshold: The threshold for warn-level alerts.
        :param int times: The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        if comparison_operator is not None:
            pulumi.set(__self__, "comparison_operator", comparison_operator)
        if statistics is not None:
            pulumi.set(__self__, "statistics", statistics)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if times is not None:
            pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> Optional[str]:
        """
        The comparison operator of the threshold for warn-level alerts.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> Optional[str]:
        """
        The statistical aggregation method for warn-level alerts.
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> Optional[str]:
        """
        The threshold for warn-level alerts.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> Optional[int]:
        """
        The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        return pulumi.get(self, "times")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SiteMonitorIspCity(dict):
    def __init__(__self__, *,
                 city: str,
                 isp: str):
        pulumi.set(__self__, "city", city)
        pulumi.set(__self__, "isp", isp)

    @property
    @pulumi.getter
    def city(self) -> str:
        return pulumi.get(self, "city")

    @property
    @pulumi.getter
    def isp(self) -> str:
        return pulumi.get(self, "isp")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class GetAlarmContactGroupsGroupResult(dict):
    def __init__(__self__, *,
                 alarm_contact_group_name: str,
                 contacts: Sequence[str],
                 describe: str,
                 enable_subscribed: bool,
                 id: str):
        """
        :param str alarm_contact_group_name: The name of Alarm Contact Group.
        :param Sequence[str] contacts: The alarm contacts in the alarm group.
        :param str describe: The description of the Alarm Group.
        :param bool enable_subscribed: Indicates whether the alarm group subscribes to weekly reports.
        :param str id: The ID of the CMS.
        """
        pulumi.set(__self__, "alarm_contact_group_name", alarm_contact_group_name)
        pulumi.set(__self__, "contacts", contacts)
        pulumi.set(__self__, "describe", describe)
        pulumi.set(__self__, "enable_subscribed", enable_subscribed)
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="alarmContactGroupName")
    def alarm_contact_group_name(self) -> str:
        """
        The name of Alarm Contact Group.
        """
        return pulumi.get(self, "alarm_contact_group_name")

    @property
    @pulumi.getter
    def contacts(self) -> Sequence[str]:
        """
        The alarm contacts in the alarm group.
        """
        return pulumi.get(self, "contacts")

    @property
    @pulumi.getter
    def describe(self) -> str:
        """
        The description of the Alarm Group.
        """
        return pulumi.get(self, "describe")

    @property
    @pulumi.getter(name="enableSubscribed")
    def enable_subscribed(self) -> bool:
        """
        Indicates whether the alarm group subscribes to weekly reports.
        """
        return pulumi.get(self, "enable_subscribed")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the CMS.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class GetAlarmContactsContactResult(dict):
    def __init__(__self__, *,
                 alarm_contact_name: str,
                 channels_aliim: str,
                 channels_ding_web_hook: str,
                 channels_mail: str,
                 channels_sms: str,
                 channels_state_aliim: str,
                 channels_state_ding_web_hook: str,
                 channels_state_mail: str,
                 channels_status_sms: str,
                 contact_groups: Sequence[str],
                 describe: str,
                 id: str,
                 lang: str):
        """
        :param str alarm_contact_name: The name of the alarm contact.
        :param str channels_aliim: The TradeManager ID of the alarm contact.
        :param str channels_ding_web_hook: The webhook URL of the DingTalk chatbot.
        :param str channels_mail: The email address of the alarm contact.
        :param str channels_sms: The phone number of the alarm contact.
        :param str channels_state_aliim: Indicates whether the TradeManager ID is valid.
        :param str channels_state_ding_web_hook: Indicates whether the DingTalk chatbot is normal.
        :param str channels_state_mail: The status of the email address.
        :param str channels_status_sms: The status of the phone number.
        :param Sequence[str] contact_groups: The alert groups to which the alarm contact is added.
        :param str describe: The description of the alarm contact.
        :param str id: The ID of the alarm contact.
        """
        pulumi.set(__self__, "alarm_contact_name", alarm_contact_name)
        pulumi.set(__self__, "channels_aliim", channels_aliim)
        pulumi.set(__self__, "channels_ding_web_hook", channels_ding_web_hook)
        pulumi.set(__self__, "channels_mail", channels_mail)
        pulumi.set(__self__, "channels_sms", channels_sms)
        pulumi.set(__self__, "channels_state_aliim", channels_state_aliim)
        pulumi.set(__self__, "channels_state_ding_web_hook", channels_state_ding_web_hook)
        pulumi.set(__self__, "channels_state_mail", channels_state_mail)
        pulumi.set(__self__, "channels_status_sms", channels_status_sms)
        pulumi.set(__self__, "contact_groups", contact_groups)
        pulumi.set(__self__, "describe", describe)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "lang", lang)

    @property
    @pulumi.getter(name="alarmContactName")
    def alarm_contact_name(self) -> str:
        """
        The name of the alarm contact.
        """
        return pulumi.get(self, "alarm_contact_name")

    @property
    @pulumi.getter(name="channelsAliim")
    def channels_aliim(self) -> str:
        """
        The TradeManager ID of the alarm contact.
        """
        return pulumi.get(self, "channels_aliim")

    @property
    @pulumi.getter(name="channelsDingWebHook")
    def channels_ding_web_hook(self) -> str:
        """
        The webhook URL of the DingTalk chatbot.
        """
        return pulumi.get(self, "channels_ding_web_hook")

    @property
    @pulumi.getter(name="channelsMail")
    def channels_mail(self) -> str:
        """
        The email address of the alarm contact.
        """
        return pulumi.get(self, "channels_mail")

    @property
    @pulumi.getter(name="channelsSms")
    def channels_sms(self) -> str:
        """
        The phone number of the alarm contact.
        """
        return pulumi.get(self, "channels_sms")

    @property
    @pulumi.getter(name="channelsStateAliim")
    def channels_state_aliim(self) -> str:
        """
        Indicates whether the TradeManager ID is valid.
        """
        return pulumi.get(self, "channels_state_aliim")

    @property
    @pulumi.getter(name="channelsStateDingWebHook")
    def channels_state_ding_web_hook(self) -> str:
        """
        Indicates whether the DingTalk chatbot is normal.
        """
        return pulumi.get(self, "channels_state_ding_web_hook")

    @property
    @pulumi.getter(name="channelsStateMail")
    def channels_state_mail(self) -> str:
        """
        The status of the email address.
        """
        return pulumi.get(self, "channels_state_mail")

    @property
    @pulumi.getter(name="channelsStatusSms")
    def channels_status_sms(self) -> str:
        """
        The status of the phone number.
        """
        return pulumi.get(self, "channels_status_sms")

    @property
    @pulumi.getter(name="contactGroups")
    def contact_groups(self) -> Sequence[str]:
        """
        The alert groups to which the alarm contact is added.
        """
        return pulumi.get(self, "contact_groups")

    @property
    @pulumi.getter
    def describe(self) -> str:
        """
        The description of the alarm contact.
        """
        return pulumi.get(self, "describe")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the alarm contact.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def lang(self) -> str:
        return pulumi.get(self, "lang")


@pulumi.output_type
class GetGroupMetricRulesRuleResult(dict):
    def __init__(__self__, *,
                 contact_groups: str,
                 dimensions: str,
                 effective_interval: str,
                 email_subject: str,
                 enable_state: bool,
                 escalations: Sequence['outputs.GetGroupMetricRulesRuleEscalationResult'],
                 group_id: str,
                 group_metric_rule_name: str,
                 id: str,
                 metric_name: str,
                 namespace: str,
                 no_effective_interval: str,
                 period: int,
                 resources: str,
                 rule_id: str,
                 silence_time: int,
                 source_type: str,
                 status: str,
                 webhook: str):
        """
        :param str contact_groups: Alarm contact group.
        :param str dimensions: The dimensions that specify the resources to be associated with the alert rule.
        :param str effective_interval: The time period during which the alert rule is effective.
        :param str email_subject: The subject of the alert notification email.
        :param bool enable_state: Indicates whether the alert rule is enabled.
        :param Sequence['GetGroupMetricRulesRuleEscalationArgs'] escalations: Alarm level.
        :param str group_id: The ID of the application group.
        :param str group_metric_rule_name: The name of the alert rule.
        :param str id: The ID of the Group Metric Rule.
        :param str metric_name: The name of the metric.
        :param str namespace: The namespace of the service.
        :param str no_effective_interval: The time period during which the alert rule is ineffective.
        :param int period: The aggregation period of the monitoring data. Unit: seconds. The value is an integral multiple of 60. Default value: `300`.
        :param str resources: The resources that are associated with the alert rule.
        :param str rule_id: The ID of the alert rule.
        :param int silence_time: The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: `86400`, which is equivalent to one day.
        :param str source_type: The type of the alert rule. The value is fixed to METRIC, indicating an alert rule for time series metrics.
        :param str status: The status of Group Metric Rule..
        :param str webhook: The callback URL.
        """
        pulumi.set(__self__, "contact_groups", contact_groups)
        pulumi.set(__self__, "dimensions", dimensions)
        pulumi.set(__self__, "effective_interval", effective_interval)
        pulumi.set(__self__, "email_subject", email_subject)
        pulumi.set(__self__, "enable_state", enable_state)
        pulumi.set(__self__, "escalations", escalations)
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "group_metric_rule_name", group_metric_rule_name)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "no_effective_interval", no_effective_interval)
        pulumi.set(__self__, "period", period)
        pulumi.set(__self__, "resources", resources)
        pulumi.set(__self__, "rule_id", rule_id)
        pulumi.set(__self__, "silence_time", silence_time)
        pulumi.set(__self__, "source_type", source_type)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "webhook", webhook)

    @property
    @pulumi.getter(name="contactGroups")
    def contact_groups(self) -> str:
        """
        Alarm contact group.
        """
        return pulumi.get(self, "contact_groups")

    @property
    @pulumi.getter
    def dimensions(self) -> str:
        """
        The dimensions that specify the resources to be associated with the alert rule.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="effectiveInterval")
    def effective_interval(self) -> str:
        """
        The time period during which the alert rule is effective.
        """
        return pulumi.get(self, "effective_interval")

    @property
    @pulumi.getter(name="emailSubject")
    def email_subject(self) -> str:
        """
        The subject of the alert notification email.
        """
        return pulumi.get(self, "email_subject")

    @property
    @pulumi.getter(name="enableState")
    def enable_state(self) -> bool:
        """
        Indicates whether the alert rule is enabled.
        """
        return pulumi.get(self, "enable_state")

    @property
    @pulumi.getter
    def escalations(self) -> Sequence['outputs.GetGroupMetricRulesRuleEscalationResult']:
        """
        Alarm level.
        """
        return pulumi.get(self, "escalations")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> str:
        """
        The ID of the application group.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="groupMetricRuleName")
    def group_metric_rule_name(self) -> str:
        """
        The name of the alert rule.
        """
        return pulumi.get(self, "group_metric_rule_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Group Metric Rule.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> str:
        """
        The name of the metric.
        """
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        """
        The namespace of the service.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="noEffectiveInterval")
    def no_effective_interval(self) -> str:
        """
        The time period during which the alert rule is ineffective.
        """
        return pulumi.get(self, "no_effective_interval")

    @property
    @pulumi.getter
    def period(self) -> int:
        """
        The aggregation period of the monitoring data. Unit: seconds. The value is an integral multiple of 60. Default value: `300`.
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter
    def resources(self) -> str:
        """
        The resources that are associated with the alert rule.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> str:
        """
        The ID of the alert rule.
        """
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter(name="silenceTime")
    def silence_time(self) -> int:
        """
        The mute period during which new alerts are not reported even if the alert trigger conditions are met. Unit: seconds. Default value: `86400`, which is equivalent to one day.
        """
        return pulumi.get(self, "silence_time")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> str:
        """
        The type of the alert rule. The value is fixed to METRIC, indicating an alert rule for time series metrics.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of Group Metric Rule..
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def webhook(self) -> str:
        """
        The callback URL.
        """
        return pulumi.get(self, "webhook")


@pulumi.output_type
class GetGroupMetricRulesRuleEscalationResult(dict):
    def __init__(__self__, *,
                 criticals: Sequence['outputs.GetGroupMetricRulesRuleEscalationCriticalResult'],
                 infos: Sequence['outputs.GetGroupMetricRulesRuleEscalationInfoResult'],
                 warns: Sequence['outputs.GetGroupMetricRulesRuleEscalationWarnResult']):
        """
        :param Sequence['GetGroupMetricRulesRuleEscalationCriticalArgs'] criticals: The critical level.
        :param Sequence['GetGroupMetricRulesRuleEscalationInfoArgs'] infos: The info level.
        :param Sequence['GetGroupMetricRulesRuleEscalationWarnArgs'] warns: The warn level.
        """
        pulumi.set(__self__, "criticals", criticals)
        pulumi.set(__self__, "infos", infos)
        pulumi.set(__self__, "warns", warns)

    @property
    @pulumi.getter
    def criticals(self) -> Sequence['outputs.GetGroupMetricRulesRuleEscalationCriticalResult']:
        """
        The critical level.
        """
        return pulumi.get(self, "criticals")

    @property
    @pulumi.getter
    def infos(self) -> Sequence['outputs.GetGroupMetricRulesRuleEscalationInfoResult']:
        """
        The info level.
        """
        return pulumi.get(self, "infos")

    @property
    @pulumi.getter
    def warns(self) -> Sequence['outputs.GetGroupMetricRulesRuleEscalationWarnResult']:
        """
        The warn level.
        """
        return pulumi.get(self, "warns")


@pulumi.output_type
class GetGroupMetricRulesRuleEscalationCriticalResult(dict):
    def __init__(__self__, *,
                 comparison_operator: str,
                 statistics: str,
                 threshold: str,
                 times: int):
        """
        :param str comparison_operator: The comparison operator of the threshold for warn-level alerts.
        :param str statistics: The statistical aggregation method for warn-level alerts.
        :param str threshold: The threshold for warn-level alerts.
        :param int times: The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        pulumi.set(__self__, "comparison_operator", comparison_operator)
        pulumi.set(__self__, "statistics", statistics)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> str:
        """
        The comparison operator of the threshold for warn-level alerts.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> str:
        """
        The statistical aggregation method for warn-level alerts.
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> str:
        """
        The threshold for warn-level alerts.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> int:
        """
        The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        return pulumi.get(self, "times")


@pulumi.output_type
class GetGroupMetricRulesRuleEscalationInfoResult(dict):
    def __init__(__self__, *,
                 comparison_operator: str,
                 statistics: str,
                 threshold: str,
                 times: int):
        """
        :param str comparison_operator: The comparison operator of the threshold for warn-level alerts.
        :param str statistics: The statistical aggregation method for warn-level alerts.
        :param str threshold: The threshold for warn-level alerts.
        :param int times: The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        pulumi.set(__self__, "comparison_operator", comparison_operator)
        pulumi.set(__self__, "statistics", statistics)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> str:
        """
        The comparison operator of the threshold for warn-level alerts.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> str:
        """
        The statistical aggregation method for warn-level alerts.
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> str:
        """
        The threshold for warn-level alerts.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> int:
        """
        The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        return pulumi.get(self, "times")


@pulumi.output_type
class GetGroupMetricRulesRuleEscalationWarnResult(dict):
    def __init__(__self__, *,
                 comparison_operator: str,
                 statistics: str,
                 threshold: str,
                 times: int):
        """
        :param str comparison_operator: The comparison operator of the threshold for warn-level alerts.
        :param str statistics: The statistical aggregation method for warn-level alerts.
        :param str threshold: The threshold for warn-level alerts.
        :param int times: The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        pulumi.set(__self__, "comparison_operator", comparison_operator)
        pulumi.set(__self__, "statistics", statistics)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "times", times)

    @property
    @pulumi.getter(name="comparisonOperator")
    def comparison_operator(self) -> str:
        """
        The comparison operator of the threshold for warn-level alerts.
        """
        return pulumi.get(self, "comparison_operator")

    @property
    @pulumi.getter
    def statistics(self) -> str:
        """
        The statistical aggregation method for warn-level alerts.
        """
        return pulumi.get(self, "statistics")

    @property
    @pulumi.getter
    def threshold(self) -> str:
        """
        The threshold for warn-level alerts.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter
    def times(self) -> int:
        """
        The consecutive number of times for which the metric value is measured before a warn-level alert is triggered.
        """
        return pulumi.get(self, "times")



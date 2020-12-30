# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'BucketCorsRuleArgs',
    'BucketLifecycleRuleArgs',
    'BucketLifecycleRuleExpirationArgs',
    'BucketLifecycleRuleTransitionArgs',
    'BucketLoggingArgs',
    'BucketRefererConfigArgs',
    'BucketServerSideEncryptionRuleArgs',
    'BucketVersioningArgs',
    'BucketWebsiteArgs',
]

@pulumi.input_type
class BucketCorsRuleArgs:
    def __init__(__self__, *,
                 allowed_methods: pulumi.Input[Sequence[pulumi.Input[str]]],
                 allowed_origins: pulumi.Input[Sequence[pulumi.Input[str]]],
                 allowed_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 expose_headers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 max_age_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_methods: Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_origins: Specifies which origins are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_headers: Specifies which headers are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] expose_headers: Specifies expose header in the response.
        :param pulumi.Input[int] max_age_seconds: Specifies time in seconds that browser can cache the response for a preflight request.
        """
        pulumi.set(__self__, "allowed_methods", allowed_methods)
        pulumi.set(__self__, "allowed_origins", allowed_origins)
        if allowed_headers is not None:
            pulumi.set(__self__, "allowed_headers", allowed_headers)
        if expose_headers is not None:
            pulumi.set(__self__, "expose_headers", expose_headers)
        if max_age_seconds is not None:
            pulumi.set(__self__, "max_age_seconds", max_age_seconds)

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specifies which methods are allowed. Can be GET, PUT, POST, DELETE or HEAD.
        """
        return pulumi.get(self, "allowed_methods")

    @allowed_methods.setter
    def allowed_methods(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_methods", value)

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specifies which origins are allowed.
        """
        return pulumi.get(self, "allowed_origins")

    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_origins", value)

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies which headers are allowed.
        """
        return pulumi.get(self, "allowed_headers")

    @allowed_headers.setter
    def allowed_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_headers", value)

    @property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies expose header in the response.
        """
        return pulumi.get(self, "expose_headers")

    @expose_headers.setter
    def expose_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "expose_headers", value)

    @property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies time in seconds that browser can cache the response for a preflight request.
        """
        return pulumi.get(self, "max_age_seconds")

    @max_age_seconds.setter
    def max_age_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_age_seconds", value)


@pulumi.input_type
class BucketLifecycleRuleArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 expirations: Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleExpirationArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 transitions: Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleTransitionArgs']]]] = None):
        """
        :param pulumi.Input[bool] enabled: Specifies lifecycle rule status.
        :param pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleExpirationArgs']]] expirations: Specifies a period in the object's expire (documented below).
        :param pulumi.Input[str] id: Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.
        :param pulumi.Input[str] prefix: Object key prefix identifying one or more objects to which the rule applies. Default value is null, the rule applies to all objects in a bucket.
        :param pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleTransitionArgs']]] transitions: Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).
        """
        pulumi.set(__self__, "enabled", enabled)
        if expirations is not None:
            pulumi.set(__self__, "expirations", expirations)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)
        if transitions is not None:
            pulumi.set(__self__, "transitions", transitions)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Specifies lifecycle rule status.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def expirations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleExpirationArgs']]]]:
        """
        Specifies a period in the object's expire (documented below).
        """
        return pulumi.get(self, "expirations")

    @expirations.setter
    def expirations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleExpirationArgs']]]]):
        pulumi.set(self, "expirations", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier for the rule. If omitted, OSS bucket will assign a unique name.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Object key prefix identifying one or more objects to which the rule applies. Default value is null, the rule applies to all objects in a bucket.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)

    @property
    @pulumi.getter
    def transitions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleTransitionArgs']]]]:
        """
        Specifies the time when an object is converted to the IA or archive storage class during a valid life cycle. (documented below).
        """
        return pulumi.get(self, "transitions")

    @transitions.setter
    def transitions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BucketLifecycleRuleTransitionArgs']]]]):
        pulumi.set(self, "transitions", value)


@pulumi.input_type
class BucketLifecycleRuleExpirationArgs:
    def __init__(__self__, *,
                 date: Optional[pulumi.Input[str]] = None,
                 days: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] date: Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like `2017-03-09`.
        :param pulumi.Input[int] days: Specifies the number of days after object creation when the specific rule action takes effect.
        """
        if date is not None:
            pulumi.set(__self__, "date", date)
        if days is not None:
            pulumi.set(__self__, "days", days)

    @property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the date after which you want the corresponding action to take effect. The value obeys ISO8601 format like `2017-03-09`.
        """
        return pulumi.get(self, "date")

    @date.setter
    def date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "date", value)

    @property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the number of days after object creation when the specific rule action takes effect.
        """
        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "days", value)


@pulumi.input_type
class BucketLifecycleRuleTransitionArgs:
    def __init__(__self__, *,
                 created_before_date: Optional[pulumi.Input[str]] = None,
                 days: Optional[pulumi.Input[int]] = None,
                 storage_class: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] created_before_date: Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.
        :param pulumi.Input[int] days: Specifies the number of days after object creation when the specific rule action takes effect.
        :param pulumi.Input[str] storage_class: Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`.
        """
        if created_before_date is not None:
            pulumi.set(__self__, "created_before_date", created_before_date)
        if days is not None:
            pulumi.set(__self__, "days", days)
        if storage_class is not None:
            pulumi.set(__self__, "storage_class", storage_class)

    @property
    @pulumi.getter(name="createdBeforeDate")
    def created_before_date(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the time before which the rules take effect. The date must conform to the ISO8601 format and always be UTC 00:00. For example: 2002-10-11T00:00:00.000Z indicates that objects updated before 2002-10-11T00:00:00.000Z are deleted or converted to another storage class, and objects updated after this time (including this time) are not deleted or converted.
        """
        return pulumi.get(self, "created_before_date")

    @created_before_date.setter
    def created_before_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_before_date", value)

    @property
    @pulumi.getter
    def days(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the number of days after object creation when the specific rule action takes effect.
        """
        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "days", value)

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the storage class that objects that conform to the rule are converted into. The storage class of the objects in a bucket of the IA storage class can be converted into Archive but cannot be converted into Standard. Values: `IA`, `Archive`.
        """
        return pulumi.get(self, "storage_class")

    @storage_class.setter
    def storage_class(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_class", value)


@pulumi.input_type
class BucketLoggingArgs:
    def __init__(__self__, *,
                 target_bucket: pulumi.Input[str],
                 target_prefix: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] target_bucket: The name of the bucket that will receive the log objects.
        :param pulumi.Input[str] target_prefix: To specify a key prefix for log objects.
        """
        pulumi.set(__self__, "target_bucket", target_bucket)
        if target_prefix is not None:
            pulumi.set(__self__, "target_prefix", target_prefix)

    @property
    @pulumi.getter(name="targetBucket")
    def target_bucket(self) -> pulumi.Input[str]:
        """
        The name of the bucket that will receive the log objects.
        """
        return pulumi.get(self, "target_bucket")

    @target_bucket.setter
    def target_bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_bucket", value)

    @property
    @pulumi.getter(name="targetPrefix")
    def target_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        To specify a key prefix for log objects.
        """
        return pulumi.get(self, "target_prefix")

    @target_prefix.setter
    def target_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_prefix", value)


@pulumi.input_type
class BucketRefererConfigArgs:
    def __init__(__self__, *,
                 referers: pulumi.Input[Sequence[pulumi.Input[str]]],
                 allow_empty: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] referers: The list of referer.
        :param pulumi.Input[bool] allow_empty: Allows referer to be empty. Defaults false.
        """
        pulumi.set(__self__, "referers", referers)
        if allow_empty is not None:
            pulumi.set(__self__, "allow_empty", allow_empty)

    @property
    @pulumi.getter
    def referers(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of referer.
        """
        return pulumi.get(self, "referers")

    @referers.setter
    def referers(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "referers", value)

    @property
    @pulumi.getter(name="allowEmpty")
    def allow_empty(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows referer to be empty. Defaults false.
        """
        return pulumi.get(self, "allow_empty")

    @allow_empty.setter
    def allow_empty(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_empty", value)


@pulumi.input_type
class BucketServerSideEncryptionRuleArgs:
    def __init__(__self__, *,
                 sse_algorithm: pulumi.Input[str],
                 kms_master_key_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] sse_algorithm: The server-side encryption algorithm to use. Possible values: `AES256` and `KMS`.
        :param pulumi.Input[str] kms_master_key_id: The alibaba cloud KMS master key ID used for the SSE-KMS encryption.
        """
        pulumi.set(__self__, "sse_algorithm", sse_algorithm)
        if kms_master_key_id is not None:
            pulumi.set(__self__, "kms_master_key_id", kms_master_key_id)

    @property
    @pulumi.getter(name="sseAlgorithm")
    def sse_algorithm(self) -> pulumi.Input[str]:
        """
        The server-side encryption algorithm to use. Possible values: `AES256` and `KMS`.
        """
        return pulumi.get(self, "sse_algorithm")

    @sse_algorithm.setter
    def sse_algorithm(self, value: pulumi.Input[str]):
        pulumi.set(self, "sse_algorithm", value)

    @property
    @pulumi.getter(name="kmsMasterKeyId")
    def kms_master_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The alibaba cloud KMS master key ID used for the SSE-KMS encryption.
        """
        return pulumi.get(self, "kms_master_key_id")

    @kms_master_key_id.setter
    def kms_master_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_master_key_id", value)


@pulumi.input_type
class BucketVersioningArgs:
    def __init__(__self__, *,
                 status: pulumi.Input[str]):
        """
        :param pulumi.Input[str] status: Specifies the versioning state of a bucket. Valid values: `Enabled` and `Suspended`.
        """
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        Specifies the versioning state of a bucket. Valid values: `Enabled` and `Suspended`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class BucketWebsiteArgs:
    def __init__(__self__, *,
                 index_document: pulumi.Input[str],
                 error_document: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] index_document: Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.
        :param pulumi.Input[str] error_document: An absolute path to the document to return in case of a 4XX error.
        """
        pulumi.set(__self__, "index_document", index_document)
        if error_document is not None:
            pulumi.set(__self__, "error_document", error_document)

    @property
    @pulumi.getter(name="indexDocument")
    def index_document(self) -> pulumi.Input[str]:
        """
        Alicloud OSS returns this index document when requests are made to the root domain or any of the subfolders.
        """
        return pulumi.get(self, "index_document")

    @index_document.setter
    def index_document(self, value: pulumi.Input[str]):
        pulumi.set(self, "index_document", value)

    @property
    @pulumi.getter(name="errorDocument")
    def error_document(self) -> Optional[pulumi.Input[str]]:
        """
        An absolute path to the document to return in case of a 4XX error.
        """
        return pulumi.get(self, "error_document")

    @error_document.setter
    def error_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error_document", value)



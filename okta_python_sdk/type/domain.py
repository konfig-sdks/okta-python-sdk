# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from okta_python_sdk.type.dns_record import DNSRecord
from okta_python_sdk.type.domain_certificate_metadata import DomainCertificateMetadata
from okta_python_sdk.type.domain_certificate_source_type import DomainCertificateSourceType
from okta_python_sdk.type.domain_validation_status import DomainValidationStatus

class RequiredDomain(TypedDict):
    pass

class OptionalDomain(TypedDict, total=False):
    certificateSourceType: DomainCertificateSourceType

    dnsRecords: typing.List[DNSRecord]

    domain: str

    id: str

    publicCertificate: DomainCertificateMetadata

    validationStatus: DomainValidationStatus

class Domain(RequiredDomain, OptionalDomain):
    pass

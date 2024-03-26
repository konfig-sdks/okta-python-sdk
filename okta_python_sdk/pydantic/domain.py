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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from okta_python_sdk.pydantic.dns_record import DNSRecord
from okta_python_sdk.pydantic.domain_certificate_metadata import DomainCertificateMetadata
from okta_python_sdk.pydantic.domain_certificate_source_type import DomainCertificateSourceType
from okta_python_sdk.pydantic.domain_validation_status import DomainValidationStatus

class Domain(BaseModel):
    certificate_source_type: typing.Optional[DomainCertificateSourceType] = Field(None, alias='certificateSourceType')

    dns_records: typing.Optional[typing.List[DNSRecord]] = Field(None, alias='dnsRecords')

    domain: typing.Optional[str] = Field(None, alias='domain')

    id: typing.Optional[str] = Field(None, alias='id')

    public_certificate: typing.Optional[DomainCertificateMetadata] = Field(None, alias='publicCertificate')

    validation_status: typing.Optional[DomainValidationStatus] = Field(None, alias='validationStatus')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

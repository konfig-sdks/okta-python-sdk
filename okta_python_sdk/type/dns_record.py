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

from okta_python_sdk.type.dns_record_type import DNSRecordType

class RequiredDNSRecord(TypedDict):
    pass

class OptionalDNSRecord(TypedDict, total=False):
    expiration: str

    fqdn: str

    recordType: DNSRecordType

    values: typing.List[str]

class DNSRecord(RequiredDNSRecord, OptionalDNSRecord):
    pass

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


class RequiredOrgSetting(TypedDict):
    pass

class OptionalOrgSetting(TypedDict, total=False):
    _links: typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    address1: str

    address2: str

    city: str

    companyName: str

    country: str

    created: datetime

    endUserSupportHelpURL: str

    expiresAt: datetime

    id: str

    lastUpdated: datetime

    phoneNumber: str

    postalCode: str

    state: str

    status: str

    subdomain: str

    supportPhoneNumber: str

    website: str

class OrgSetting(RequiredOrgSetting, OptionalOrgSetting):
    pass

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

from okta_python_sdk.type.scope import Scope
from okta_python_sdk.type.trusted_origin_links import TrustedOriginLinks

class RequiredTrustedOrigin(TypedDict):
    pass

class OptionalTrustedOrigin(TypedDict, total=False):
    _links: TrustedOriginLinks

    created: datetime

    createdBy: str

    id: str

    lastUpdated: datetime

    lastUpdatedBy: str

    name: str

    origin: str

    scopes: typing.List[Scope]

    status: str

class TrustedOrigin(RequiredTrustedOrigin, OptionalTrustedOrigin):
    pass

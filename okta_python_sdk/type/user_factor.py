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

from okta_python_sdk.type.factor_provider import FactorProvider
from okta_python_sdk.type.factor_status import FactorStatus
from okta_python_sdk.type.factor_type import FactorType
from okta_python_sdk.type.user_factor_embedded import UserFactorEmbedded
from okta_python_sdk.type.user_factor_links import UserFactorLinks
from okta_python_sdk.type.verify_factor_request import VerifyFactorRequest

class RequiredUserFactor(TypedDict):
    pass

class OptionalUserFactor(TypedDict, total=False):
    _embedded: UserFactorEmbedded

    _links: UserFactorLinks

    created: datetime

    factorType: FactorType

    id: str

    lastUpdated: datetime

    provider: FactorProvider

    status: FactorStatus

    verify: VerifyFactorRequest

class UserFactor(RequiredUserFactor, OptionalUserFactor):
    pass

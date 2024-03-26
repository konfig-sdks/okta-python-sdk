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

from okta_python_sdk.type.factor_result_type import FactorResultType
from okta_python_sdk.type.push_user_factor_profile import PushUserFactorProfile

class RequiredPushUserFactor(TypedDict):
    pass

class OptionalPushUserFactor(TypedDict, total=False):
    expiresAt: datetime

    factorResult: FactorResultType

    profile: PushUserFactorProfile

class PushUserFactor(RequiredPushUserFactor, OptionalPushUserFactor):
    pass

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

from okta_python_sdk.type.u2f_user_factor_profile import U2fUserFactorProfile

class RequiredU2fUserFactor(TypedDict):
    pass

class OptionalU2fUserFactor(TypedDict, total=False):
    profile: U2fUserFactorProfile

class U2fUserFactor(RequiredU2fUserFactor, OptionalU2fUserFactor):
    pass

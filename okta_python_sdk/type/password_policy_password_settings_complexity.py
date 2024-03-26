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

from okta_python_sdk.type.password_dictionary import PasswordDictionary
from okta_python_sdk.type.password_policy_password_settings_complexity_exclude_attributes import PasswordPolicyPasswordSettingsComplexityExcludeAttributes

class RequiredPasswordPolicyPasswordSettingsComplexity(TypedDict):
    pass

class OptionalPasswordPolicyPasswordSettingsComplexity(TypedDict, total=False):
    dictionary: PasswordDictionary

    excludeAttributes: PasswordPolicyPasswordSettingsComplexityExcludeAttributes

    excludeUsername: bool

    minLength: int

    minLowerCase: int

    minNumber: int

    minSymbol: int

    minUpperCase: int

class PasswordPolicyPasswordSettingsComplexity(RequiredPasswordPolicyPasswordSettingsComplexity, OptionalPasswordPolicyPasswordSettingsComplexity):
    pass

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

from okta_python_sdk.type.password_policy_password_settings_age import PasswordPolicyPasswordSettingsAge
from okta_python_sdk.type.password_policy_password_settings_complexity import PasswordPolicyPasswordSettingsComplexity
from okta_python_sdk.type.password_policy_password_settings_lockout import PasswordPolicyPasswordSettingsLockout

class RequiredPasswordPolicyPasswordSettings(TypedDict):
    pass

class OptionalPasswordPolicyPasswordSettings(TypedDict, total=False):
    age: PasswordPolicyPasswordSettingsAge

    complexity: PasswordPolicyPasswordSettingsComplexity

    lockout: PasswordPolicyPasswordSettingsLockout

class PasswordPolicyPasswordSettings(RequiredPasswordPolicyPasswordSettings, OptionalPasswordPolicyPasswordSettings):
    pass

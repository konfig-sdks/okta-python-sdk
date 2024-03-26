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

from okta_python_sdk.type.password_policy_delegation_settings import PasswordPolicyDelegationSettings
from okta_python_sdk.type.password_policy_password_settings import PasswordPolicyPasswordSettings
from okta_python_sdk.type.password_policy_recovery_settings import PasswordPolicyRecoverySettings

class RequiredPasswordPolicySettings(TypedDict):
    pass

class OptionalPasswordPolicySettings(TypedDict, total=False):
    delegation: PasswordPolicyDelegationSettings

    password: PasswordPolicyPasswordSettings

    recovery: PasswordPolicyRecoverySettings

class PasswordPolicySettings(RequiredPasswordPolicySettings, OptionalPasswordPolicySettings):
    pass

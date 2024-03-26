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

from okta_python_sdk.type.password_policy_recovery_email import PasswordPolicyRecoveryEmail
from okta_python_sdk.type.password_policy_recovery_factor_settings import PasswordPolicyRecoveryFactorSettings
from okta_python_sdk.type.password_policy_recovery_question import PasswordPolicyRecoveryQuestion

class RequiredPasswordPolicyRecoveryFactors(TypedDict):
    pass

class OptionalPasswordPolicyRecoveryFactors(TypedDict, total=False):
    okta_call: PasswordPolicyRecoveryFactorSettings

    okta_email: PasswordPolicyRecoveryEmail

    okta_sms: PasswordPolicyRecoveryFactorSettings

    recovery_question: PasswordPolicyRecoveryQuestion

class PasswordPolicyRecoveryFactors(RequiredPasswordPolicyRecoveryFactors, OptionalPasswordPolicyRecoveryFactors):
    pass

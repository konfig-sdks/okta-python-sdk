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

from okta_python_sdk.type.multifactor_enrollment_policy_authenticator_settings_constraints import MultifactorEnrollmentPolicyAuthenticatorSettingsConstraints
from okta_python_sdk.type.multifactor_enrollment_policy_authenticator_settings_enroll import MultifactorEnrollmentPolicyAuthenticatorSettingsEnroll
from okta_python_sdk.type.multifactor_enrollment_policy_authenticator_type import MultifactorEnrollmentPolicyAuthenticatorType

class RequiredMultifactorEnrollmentPolicyAuthenticatorSettings(TypedDict):
    pass

class OptionalMultifactorEnrollmentPolicyAuthenticatorSettings(TypedDict, total=False):
    constraints: MultifactorEnrollmentPolicyAuthenticatorSettingsConstraints

    enroll: MultifactorEnrollmentPolicyAuthenticatorSettingsEnroll

    key: MultifactorEnrollmentPolicyAuthenticatorType

class MultifactorEnrollmentPolicyAuthenticatorSettings(RequiredMultifactorEnrollmentPolicyAuthenticatorSettings, OptionalMultifactorEnrollmentPolicyAuthenticatorSettings):
    pass

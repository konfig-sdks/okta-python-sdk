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

from okta_python_sdk.type.multifactor_enrollment_policy_authenticator_settings import MultifactorEnrollmentPolicyAuthenticatorSettings
from okta_python_sdk.type.multifactor_enrollment_policy_settings_type import MultifactorEnrollmentPolicySettingsType

class RequiredMultifactorEnrollmentPolicySettings(TypedDict):
    pass

class OptionalMultifactorEnrollmentPolicySettings(TypedDict, total=False):
    authenticators: typing.List[MultifactorEnrollmentPolicyAuthenticatorSettings]

    type: MultifactorEnrollmentPolicySettingsType

class MultifactorEnrollmentPolicySettings(RequiredMultifactorEnrollmentPolicySettings, OptionalMultifactorEnrollmentPolicySettings):
    pass

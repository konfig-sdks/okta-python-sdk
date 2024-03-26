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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from okta_python_sdk.pydantic.multifactor_enrollment_policy_authenticator_settings_constraints import MultifactorEnrollmentPolicyAuthenticatorSettingsConstraints
from okta_python_sdk.pydantic.multifactor_enrollment_policy_authenticator_settings_enroll import MultifactorEnrollmentPolicyAuthenticatorSettingsEnroll
from okta_python_sdk.pydantic.multifactor_enrollment_policy_authenticator_type import MultifactorEnrollmentPolicyAuthenticatorType

class MultifactorEnrollmentPolicyAuthenticatorSettings(BaseModel):
    constraints: typing.Optional[MultifactorEnrollmentPolicyAuthenticatorSettingsConstraints] = Field(None, alias='constraints')

    enroll: typing.Optional[MultifactorEnrollmentPolicyAuthenticatorSettingsEnroll] = Field(None, alias='enroll')

    key: typing.Optional[MultifactorEnrollmentPolicyAuthenticatorType] = Field(None, alias='key')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

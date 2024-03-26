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

from okta_python_sdk.pydantic.password_policy_recovery_email import PasswordPolicyRecoveryEmail
from okta_python_sdk.pydantic.password_policy_recovery_factor_settings import PasswordPolicyRecoveryFactorSettings
from okta_python_sdk.pydantic.password_policy_recovery_question import PasswordPolicyRecoveryQuestion

class PasswordPolicyRecoveryFactors(BaseModel):
    okta_call: typing.Optional[PasswordPolicyRecoveryFactorSettings] = Field(None, alias='okta_call')

    okta_email: typing.Optional[PasswordPolicyRecoveryEmail] = Field(None, alias='okta_email')

    okta_sms: typing.Optional[PasswordPolicyRecoveryFactorSettings] = Field(None, alias='okta_sms')

    recovery_question: typing.Optional[PasswordPolicyRecoveryQuestion] = Field(None, alias='recovery_question')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

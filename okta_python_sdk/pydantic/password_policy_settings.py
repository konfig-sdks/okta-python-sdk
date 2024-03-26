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

from okta_python_sdk.pydantic.password_policy_delegation_settings import PasswordPolicyDelegationSettings
from okta_python_sdk.pydantic.password_policy_password_settings import PasswordPolicyPasswordSettings
from okta_python_sdk.pydantic.password_policy_recovery_settings import PasswordPolicyRecoverySettings

class PasswordPolicySettings(BaseModel):
    delegation: typing.Optional[PasswordPolicyDelegationSettings] = Field(None, alias='delegation')

    password: typing.Optional[PasswordPolicyPasswordSettings] = Field(None, alias='password')

    recovery: typing.Optional[PasswordPolicyRecoverySettings] = Field(None, alias='recovery')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.password_policy_rule_action import PasswordPolicyRuleAction

class PasswordPolicyRuleActions(BaseModel):
    password_change: typing.Optional[PasswordPolicyRuleAction] = Field(None, alias='passwordChange')

    self_service_password_reset: typing.Optional[PasswordPolicyRuleAction] = Field(None, alias='selfServicePasswordReset')

    self_service_unlock: typing.Optional[PasswordPolicyRuleAction] = Field(None, alias='selfServiceUnlock')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.okta_sign_on_policy_rule_signon_session_actions import OktaSignOnPolicyRuleSignonSessionActions

class OktaSignOnPolicyRuleSignonActions(BaseModel):
    access: typing.Optional[Literal["ALLOW", "DENY"]] = Field(None, alias='access')

    factor_lifetime: typing.Optional[int] = Field(None, alias='factorLifetime')

    factor_prompt_mode: typing.Optional[Literal["ALWAYS", "DEVICE", "SESSION"]] = Field(None, alias='factorPromptMode')

    remember_device_by_default: typing.Optional[bool] = Field(None, alias='rememberDeviceByDefault')

    require_factor: typing.Optional[bool] = Field(None, alias='requireFactor')

    session: typing.Optional[OktaSignOnPolicyRuleSignonSessionActions] = Field(None, alias='session')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.idp_policy_rule_action import IdpPolicyRuleAction
from okta_python_sdk.pydantic.okta_sign_on_policy_rule_signon_actions import OktaSignOnPolicyRuleSignonActions
from okta_python_sdk.pydantic.password_policy_rule_action import PasswordPolicyRuleAction
from okta_python_sdk.pydantic.policy_rule_actions_enroll import PolicyRuleActionsEnroll

class PolicyRuleActions(BaseModel):
    enroll: typing.Optional[PolicyRuleActionsEnroll] = Field(None, alias='enroll')

    idp: typing.Optional[IdpPolicyRuleAction] = Field(None, alias='idp')

    password_change: typing.Optional[PasswordPolicyRuleAction] = Field(None, alias='passwordChange')

    self_service_password_reset: typing.Optional[PasswordPolicyRuleAction] = Field(None, alias='selfServicePasswordReset')

    self_service_unlock: typing.Optional[PasswordPolicyRuleAction] = Field(None, alias='selfServiceUnlock')

    signon: typing.Optional[OktaSignOnPolicyRuleSignonActions] = Field(None, alias='signon')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

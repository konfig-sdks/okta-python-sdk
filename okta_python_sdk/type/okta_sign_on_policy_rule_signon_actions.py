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

from okta_python_sdk.type.okta_sign_on_policy_rule_signon_session_actions import OktaSignOnPolicyRuleSignonSessionActions

class RequiredOktaSignOnPolicyRuleSignonActions(TypedDict):
    pass

class OptionalOktaSignOnPolicyRuleSignonActions(TypedDict, total=False):
    access: str

    factorLifetime: int

    factorPromptMode: str

    rememberDeviceByDefault: bool

    requireFactor: bool

    session: OktaSignOnPolicyRuleSignonSessionActions

class OktaSignOnPolicyRuleSignonActions(RequiredOktaSignOnPolicyRuleSignonActions, OptionalOktaSignOnPolicyRuleSignonActions):
    pass

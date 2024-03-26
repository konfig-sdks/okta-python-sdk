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

from okta_python_sdk.type.idp_policy_rule_action import IdpPolicyRuleAction
from okta_python_sdk.type.okta_sign_on_policy_rule_signon_actions import OktaSignOnPolicyRuleSignonActions
from okta_python_sdk.type.password_policy_rule_action import PasswordPolicyRuleAction
from okta_python_sdk.type.policy_rule_actions_enroll import PolicyRuleActionsEnroll

class RequiredPolicyRuleActions(TypedDict):
    pass

class OptionalPolicyRuleActions(TypedDict, total=False):
    enroll: PolicyRuleActionsEnroll

    idp: IdpPolicyRuleAction

    passwordChange: PasswordPolicyRuleAction

    selfServicePasswordReset: PasswordPolicyRuleAction

    selfServiceUnlock: PasswordPolicyRuleAction

    signon: OktaSignOnPolicyRuleSignonActions

class PolicyRuleActions(RequiredPolicyRuleActions, OptionalPolicyRuleActions):
    pass

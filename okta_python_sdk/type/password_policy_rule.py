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

from okta_python_sdk.type.password_policy_rule_actions import PasswordPolicyRuleActions
from okta_python_sdk.type.password_policy_rule_conditions import PasswordPolicyRuleConditions

class RequiredPasswordPolicyRule(TypedDict):
    pass

class OptionalPasswordPolicyRule(TypedDict, total=False):
    actions: PasswordPolicyRuleActions

    conditions: PasswordPolicyRuleConditions

    name: str

class PasswordPolicyRule(RequiredPasswordPolicyRule, OptionalPasswordPolicyRule):
    pass

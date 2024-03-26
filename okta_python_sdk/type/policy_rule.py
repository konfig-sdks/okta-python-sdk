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

from okta_python_sdk.type.policy_rule_actions import PolicyRuleActions
from okta_python_sdk.type.policy_rule_conditions import PolicyRuleConditions

class RequiredPolicyRule(TypedDict):
    pass

class OptionalPolicyRule(TypedDict, total=False):
    actions: PolicyRuleActions

    conditions: PolicyRuleConditions

    created: datetime

    id: str

    lastUpdated: datetime

    name: str

    priority: int

    status: str

    system: bool

    type: str

class PolicyRule(RequiredPolicyRule, OptionalPolicyRule):
    pass

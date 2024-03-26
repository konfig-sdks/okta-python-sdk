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

from okta_python_sdk.type.authorization_server_policy_rule_actions import AuthorizationServerPolicyRuleActions
from okta_python_sdk.type.authorization_server_policy_rule_conditions import AuthorizationServerPolicyRuleConditions

class RequiredAuthorizationServerPolicyRule(TypedDict):
    pass

class OptionalAuthorizationServerPolicyRule(TypedDict, total=False):
    actions: AuthorizationServerPolicyRuleActions

    conditions: AuthorizationServerPolicyRuleConditions

    created: datetime

    id: str

    lastUpdated: datetime

    name: str

    priority: int

    status: str

    system: bool

    type: str

class AuthorizationServerPolicyRule(RequiredAuthorizationServerPolicyRule, OptionalAuthorizationServerPolicyRule):
    pass

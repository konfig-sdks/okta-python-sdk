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

from okta_python_sdk.type.policy_network_condition import PolicyNetworkCondition
from okta_python_sdk.type.policy_people_condition import PolicyPeopleCondition
from okta_python_sdk.type.policy_rule_auth_context_condition import PolicyRuleAuthContextCondition

class RequiredOktaSignOnPolicyRuleConditions(TypedDict):
    pass

class OptionalOktaSignOnPolicyRuleConditions(TypedDict, total=False):
    authContext: PolicyRuleAuthContextCondition

    network: PolicyNetworkCondition

    people: PolicyPeopleCondition

class OktaSignOnPolicyRuleConditions(RequiredOktaSignOnPolicyRuleConditions, OptionalOktaSignOnPolicyRuleConditions):
    pass

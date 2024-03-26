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

from okta_python_sdk.type.client_policy_condition import ClientPolicyCondition
from okta_python_sdk.type.grant_type_policy_rule_condition import GrantTypePolicyRuleCondition
from okta_python_sdk.type.o_auth2_scopes_mediation_policy_rule_condition import OAuth2ScopesMediationPolicyRuleCondition
from okta_python_sdk.type.policy_people_condition import PolicyPeopleCondition

class RequiredAuthorizationServerPolicyRuleConditions(TypedDict):
    pass

class OptionalAuthorizationServerPolicyRuleConditions(TypedDict, total=False):
    clients: ClientPolicyCondition

    grantTypes: GrantTypePolicyRuleCondition

    people: PolicyPeopleCondition

    scopes: OAuth2ScopesMediationPolicyRuleCondition

class AuthorizationServerPolicyRuleConditions(RequiredAuthorizationServerPolicyRuleConditions, OptionalAuthorizationServerPolicyRuleConditions):
    pass

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

from okta_python_sdk.type.authorization_server_policy_embedded import AuthorizationServerPolicyEmbedded
from okta_python_sdk.type.authorization_server_policy_links import AuthorizationServerPolicyLinks
from okta_python_sdk.type.policy_rule_conditions import PolicyRuleConditions
from okta_python_sdk.type.policy_type import PolicyType

class RequiredAuthorizationServerPolicy(TypedDict):
    pass

class OptionalAuthorizationServerPolicy(TypedDict, total=False):
    description: str

    _embedded: AuthorizationServerPolicyEmbedded

    _links: AuthorizationServerPolicyLinks

    conditions: PolicyRuleConditions

    created: datetime

    id: str

    lastUpdated: datetime

    name: str

    priority: int

    status: str

    system: bool

    type: PolicyType

class AuthorizationServerPolicy(RequiredAuthorizationServerPolicy, OptionalAuthorizationServerPolicy):
    pass

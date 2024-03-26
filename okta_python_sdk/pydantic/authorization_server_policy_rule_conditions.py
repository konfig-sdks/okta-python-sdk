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

from okta_python_sdk.pydantic.client_policy_condition import ClientPolicyCondition
from okta_python_sdk.pydantic.grant_type_policy_rule_condition import GrantTypePolicyRuleCondition
from okta_python_sdk.pydantic.o_auth2_scopes_mediation_policy_rule_condition import OAuth2ScopesMediationPolicyRuleCondition
from okta_python_sdk.pydantic.policy_people_condition import PolicyPeopleCondition

class AuthorizationServerPolicyRuleConditions(BaseModel):
    clients: typing.Optional[ClientPolicyCondition] = Field(None, alias='clients')

    grant_types: typing.Optional[GrantTypePolicyRuleCondition] = Field(None, alias='grantTypes')

    people: typing.Optional[PolicyPeopleCondition] = Field(None, alias='people')

    scopes: typing.Optional[OAuth2ScopesMediationPolicyRuleCondition] = Field(None, alias='scopes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

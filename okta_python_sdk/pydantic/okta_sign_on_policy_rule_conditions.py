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

from okta_python_sdk.pydantic.policy_network_condition import PolicyNetworkCondition
from okta_python_sdk.pydantic.policy_people_condition import PolicyPeopleCondition
from okta_python_sdk.pydantic.policy_rule_auth_context_condition import PolicyRuleAuthContextCondition

class OktaSignOnPolicyRuleConditions(BaseModel):
    auth_context: typing.Optional[PolicyRuleAuthContextCondition] = Field(None, alias='authContext')

    network: typing.Optional[PolicyNetworkCondition] = Field(None, alias='network')

    people: typing.Optional[PolicyPeopleCondition] = Field(None, alias='people')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.identity_provider_policy_rule_condition_idp_ids import IdentityProviderPolicyRuleConditionIdpIds

class IdentityProviderPolicyRuleCondition(BaseModel):
    idp_ids: typing.Optional[IdentityProviderPolicyRuleConditionIdpIds] = Field(None, alias='idpIds')

    provider: typing.Optional[Literal["ANY", "OKTA", "SPECIFIC_IDP"]] = Field(None, alias='provider')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.password_policy_authentication_provider_condition import PasswordPolicyAuthenticationProviderCondition
from okta_python_sdk.pydantic.policy_people_condition import PolicyPeopleCondition

class PasswordPolicyConditions(BaseModel):
    auth_provider: typing.Optional[PasswordPolicyAuthenticationProviderCondition] = Field(None, alias='authProvider')

    people: typing.Optional[PolicyPeopleCondition] = Field(None, alias='people')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

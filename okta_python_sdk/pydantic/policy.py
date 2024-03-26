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

from okta_python_sdk.pydantic.policy_embedded import PolicyEmbedded
from okta_python_sdk.pydantic.policy_links import PolicyLinks
from okta_python_sdk.pydantic.policy_rule_conditions import PolicyRuleConditions
from okta_python_sdk.pydantic.policy_type import PolicyType

class Policy(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    _embedded: typing.Optional[PolicyEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[PolicyLinks] = Field(None, alias='_links')

    conditions: typing.Optional[PolicyRuleConditions] = Field(None, alias='conditions')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    priority: typing.Optional[int] = Field(None, alias='priority')

    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    system: typing.Optional[bool] = Field(None, alias='system')

    type: typing.Optional[PolicyType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

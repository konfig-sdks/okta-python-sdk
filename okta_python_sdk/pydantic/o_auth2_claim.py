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

from okta_python_sdk.pydantic.o_auth2_claim_conditions import OAuth2ClaimConditions
from okta_python_sdk.pydantic.o_auth2_claim_links import OAuth2ClaimLinks

class OAuth2Claim(BaseModel):
    _links: typing.Optional[OAuth2ClaimLinks] = Field(None, alias='_links')

    always_include_in_token: typing.Optional[bool] = Field(None, alias='alwaysIncludeInToken')

    claim_type: typing.Optional[Literal["IDENTITY", "RESOURCE"]] = Field(None, alias='claimType')

    conditions: typing.Optional[OAuth2ClaimConditions] = Field(None, alias='conditions')

    group_filter_type: typing.Optional[Literal["STARTS_WITH", "EQUALS", "CONTAINS", "REGEX"]] = Field(None, alias='group_filter_type')

    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    system: typing.Optional[bool] = Field(None, alias='system')

    value: typing.Optional[str] = Field(None, alias='value')

    value_type: typing.Optional[Literal["EXPRESSION", "GROUPS", "SYSTEM"]] = Field(None, alias='valueType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

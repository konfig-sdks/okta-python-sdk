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

from okta_python_sdk.pydantic.factor_provider import FactorProvider
from okta_python_sdk.pydantic.factor_status import FactorStatus
from okta_python_sdk.pydantic.factor_type import FactorType
from okta_python_sdk.pydantic.user_factor_embedded import UserFactorEmbedded
from okta_python_sdk.pydantic.user_factor_links import UserFactorLinks
from okta_python_sdk.pydantic.verify_factor_request import VerifyFactorRequest

class UserFactor(BaseModel):
    _embedded: typing.Optional[UserFactorEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[UserFactorLinks] = Field(None, alias='_links')

    created: typing.Optional[datetime] = Field(None, alias='created')

    factor_type: typing.Optional[FactorType] = Field(None, alias='factorType')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    provider: typing.Optional[FactorProvider] = Field(None, alias='provider')

    status: typing.Optional[FactorStatus] = Field(None, alias='status')

    verify: typing.Optional[VerifyFactorRequest] = Field(None, alias='verify')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

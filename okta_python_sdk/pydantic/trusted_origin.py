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

from okta_python_sdk.pydantic.scope import Scope
from okta_python_sdk.pydantic.trusted_origin_links import TrustedOriginLinks

class TrustedOrigin(BaseModel):
    _links: typing.Optional[TrustedOriginLinks] = Field(None, alias='_links')

    created: typing.Optional[datetime] = Field(None, alias='created')

    created_by: typing.Optional[str] = Field(None, alias='createdBy')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    last_updated_by: typing.Optional[str] = Field(None, alias='lastUpdatedBy')

    name: typing.Optional[str] = Field(None, alias='name')

    origin: typing.Optional[str] = Field(None, alias='origin')

    scopes: typing.Optional[typing.List[Scope]] = Field(None, alias='scopes')

    status: typing.Optional[str] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

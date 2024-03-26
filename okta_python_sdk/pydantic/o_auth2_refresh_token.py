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

from okta_python_sdk.pydantic.o_auth2_actor import OAuth2Actor
from okta_python_sdk.pydantic.o_auth2_refresh_token_embedded import OAuth2RefreshTokenEmbedded
from okta_python_sdk.pydantic.o_auth2_refresh_token_links import OAuth2RefreshTokenLinks
from okta_python_sdk.pydantic.o_auth2_refresh_token_scopes import OAuth2RefreshTokenScopes

class OAuth2RefreshToken(BaseModel):
    _embedded: typing.Optional[OAuth2RefreshTokenEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[OAuth2RefreshTokenLinks] = Field(None, alias='_links')

    client_id: typing.Optional[str] = Field(None, alias='clientId')

    created: typing.Optional[datetime] = Field(None, alias='created')

    created_by: typing.Optional[OAuth2Actor] = Field(None, alias='createdBy')

    expires_at: typing.Optional[datetime] = Field(None, alias='expiresAt')

    id: typing.Optional[str] = Field(None, alias='id')

    issuer: typing.Optional[str] = Field(None, alias='issuer')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    scopes: typing.Optional[OAuth2RefreshTokenScopes] = Field(None, alias='scopes')

    status: typing.Optional[Literal["ACTIVE", "REVOKED"]] = Field(None, alias='status')

    user_id: typing.Optional[str] = Field(None, alias='userId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.social_auth_token_scopes import SocialAuthTokenScopes

class SocialAuthToken(BaseModel):
    expires_at: typing.Optional[datetime] = Field(None, alias='expiresAt')

    id: typing.Optional[str] = Field(None, alias='id')

    scopes: typing.Optional[SocialAuthTokenScopes] = Field(None, alias='scopes')

    token: typing.Optional[str] = Field(None, alias='token')

    token_auth_scheme: typing.Optional[str] = Field(None, alias='tokenAuthScheme')

    token_type: typing.Optional[str] = Field(None, alias='tokenType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

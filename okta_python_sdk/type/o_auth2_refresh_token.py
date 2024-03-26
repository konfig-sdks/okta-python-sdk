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

from okta_python_sdk.type.o_auth2_actor import OAuth2Actor
from okta_python_sdk.type.o_auth2_refresh_token_embedded import OAuth2RefreshTokenEmbedded
from okta_python_sdk.type.o_auth2_refresh_token_links import OAuth2RefreshTokenLinks
from okta_python_sdk.type.o_auth2_refresh_token_scopes import OAuth2RefreshTokenScopes

class RequiredOAuth2RefreshToken(TypedDict):
    pass

class OptionalOAuth2RefreshToken(TypedDict, total=False):
    _embedded: OAuth2RefreshTokenEmbedded

    _links: OAuth2RefreshTokenLinks

    clientId: str

    created: datetime

    createdBy: OAuth2Actor

    expiresAt: datetime

    id: str

    issuer: str

    lastUpdated: datetime

    scopes: OAuth2RefreshTokenScopes

    status: str

    userId: str

class OAuth2RefreshToken(RequiredOAuth2RefreshToken, OptionalOAuth2RefreshToken):
    pass

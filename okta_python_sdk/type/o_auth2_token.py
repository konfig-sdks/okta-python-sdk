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

from okta_python_sdk.type.o_auth2_token_embedded import OAuth2TokenEmbedded
from okta_python_sdk.type.o_auth2_token_links import OAuth2TokenLinks
from okta_python_sdk.type.o_auth2_token_scopes import OAuth2TokenScopes

class RequiredOAuth2Token(TypedDict):
    pass

class OptionalOAuth2Token(TypedDict, total=False):
    _embedded: OAuth2TokenEmbedded

    _links: OAuth2TokenLinks

    clientId: str

    created: datetime

    expiresAt: datetime

    id: str

    issuer: str

    lastUpdated: datetime

    scopes: OAuth2TokenScopes

    status: str

    userId: str

class OAuth2Token(RequiredOAuth2Token, OptionalOAuth2Token):
    pass

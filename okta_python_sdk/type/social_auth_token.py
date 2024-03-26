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

from okta_python_sdk.type.social_auth_token_scopes import SocialAuthTokenScopes

class RequiredSocialAuthToken(TypedDict):
    pass

class OptionalSocialAuthToken(TypedDict, total=False):
    expiresAt: datetime

    id: str

    scopes: SocialAuthTokenScopes

    token: str

    tokenAuthScheme: str

    tokenType: str

class SocialAuthToken(RequiredSocialAuthToken, OptionalSocialAuthToken):
    pass

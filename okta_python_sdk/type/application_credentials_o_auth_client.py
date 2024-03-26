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

from okta_python_sdk.type.o_auth_endpoint_authentication_method import OAuthEndpointAuthenticationMethod

class RequiredApplicationCredentialsOAuthClient(TypedDict):
    pass

class OptionalApplicationCredentialsOAuthClient(TypedDict, total=False):
    autoKeyRotation: bool

    client_id: str

    client_secret: str

    pkce_required: bool

    token_endpoint_auth_method: OAuthEndpointAuthenticationMethod

class ApplicationCredentialsOAuthClient(RequiredApplicationCredentialsOAuthClient, OptionalApplicationCredentialsOAuthClient):
    pass

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

from okta_python_sdk.pydantic.o_auth_endpoint_authentication_method import OAuthEndpointAuthenticationMethod

class ApplicationCredentialsOAuthClient(BaseModel):
    auto_key_rotation: typing.Optional[bool] = Field(None, alias='autoKeyRotation')

    client_id: typing.Optional[str] = Field(None, alias='client_id')

    client_secret: typing.Optional[str] = Field(None, alias='client_secret')

    pkce_required: typing.Optional[bool] = Field(None, alias='pkce_required')

    token_endpoint_auth_method: typing.Optional[OAuthEndpointAuthenticationMethod] = Field(None, alias='token_endpoint_auth_method')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

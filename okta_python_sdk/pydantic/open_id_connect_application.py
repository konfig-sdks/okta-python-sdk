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

from okta_python_sdk.pydantic.o_auth_application_credentials import OAuthApplicationCredentials
from okta_python_sdk.pydantic.open_id_connect_application_settings import OpenIdConnectApplicationSettings

class OpenIdConnectApplication(BaseModel):
    credentials: typing.Optional[OAuthApplicationCredentials] = Field(None, alias='credentials')

    name: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='name')

    settings: typing.Optional[OpenIdConnectApplicationSettings] = Field(None, alias='settings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

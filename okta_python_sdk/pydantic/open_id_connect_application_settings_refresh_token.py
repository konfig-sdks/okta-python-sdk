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

from okta_python_sdk.pydantic.open_id_connect_refresh_token_rotation_type import OpenIdConnectRefreshTokenRotationType

class OpenIdConnectApplicationSettingsRefreshToken(BaseModel):
    leeway: typing.Optional[int] = Field(None, alias='leeway')

    rotation_type: typing.Optional[OpenIdConnectRefreshTokenRotationType] = Field(None, alias='rotation_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.inline_hook_channel_config_auth_scheme import InlineHookChannelConfigAuthScheme
from okta_python_sdk.pydantic.inline_hook_channel_config_headers import InlineHookChannelConfigHeaders

class InlineHookChannelConfig(BaseModel):
    auth_scheme: typing.Optional[InlineHookChannelConfigAuthScheme] = Field(None, alias='authScheme')

    headers: typing.Optional[typing.List[InlineHookChannelConfigHeaders]] = Field(None, alias='headers')

    method: typing.Optional[str] = Field(None, alias='method')

    uri: typing.Optional[str] = Field(None, alias='uri')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

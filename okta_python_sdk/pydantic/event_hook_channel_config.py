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

from okta_python_sdk.pydantic.event_hook_channel_config_auth_scheme import EventHookChannelConfigAuthScheme
from okta_python_sdk.pydantic.event_hook_channel_config_header import EventHookChannelConfigHeader

class EventHookChannelConfig(BaseModel):
    auth_scheme: typing.Optional[EventHookChannelConfigAuthScheme] = Field(None, alias='authScheme')

    headers: typing.Optional[typing.List[EventHookChannelConfigHeader]] = Field(None, alias='headers')

    uri: typing.Optional[str] = Field(None, alias='uri')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

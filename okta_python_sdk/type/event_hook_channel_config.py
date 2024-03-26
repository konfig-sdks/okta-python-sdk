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

from okta_python_sdk.type.event_hook_channel_config_auth_scheme import EventHookChannelConfigAuthScheme
from okta_python_sdk.type.event_hook_channel_config_header import EventHookChannelConfigHeader

class RequiredEventHookChannelConfig(TypedDict):
    pass

class OptionalEventHookChannelConfig(TypedDict, total=False):
    authScheme: EventHookChannelConfigAuthScheme

    headers: typing.List[EventHookChannelConfigHeader]

    uri: str

class EventHookChannelConfig(RequiredEventHookChannelConfig, OptionalEventHookChannelConfig):
    pass

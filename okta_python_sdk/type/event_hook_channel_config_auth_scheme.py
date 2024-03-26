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

from okta_python_sdk.type.event_hook_channel_config_auth_scheme_type import EventHookChannelConfigAuthSchemeType

class RequiredEventHookChannelConfigAuthScheme(TypedDict):
    pass

class OptionalEventHookChannelConfigAuthScheme(TypedDict, total=False):
    key: str

    type: EventHookChannelConfigAuthSchemeType

    value: str

class EventHookChannelConfigAuthScheme(RequiredEventHookChannelConfigAuthScheme, OptionalEventHookChannelConfigAuthScheme):
    pass

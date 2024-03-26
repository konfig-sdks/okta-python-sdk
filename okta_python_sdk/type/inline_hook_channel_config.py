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

from okta_python_sdk.type.inline_hook_channel_config_auth_scheme import InlineHookChannelConfigAuthScheme
from okta_python_sdk.type.inline_hook_channel_config_headers import InlineHookChannelConfigHeaders

class RequiredInlineHookChannelConfig(TypedDict):
    pass

class OptionalInlineHookChannelConfig(TypedDict, total=False):
    authScheme: InlineHookChannelConfigAuthScheme

    headers: typing.List[InlineHookChannelConfigHeaders]

    method: str

    uri: str

class InlineHookChannelConfig(RequiredInlineHookChannelConfig, OptionalInlineHookChannelConfig):
    pass

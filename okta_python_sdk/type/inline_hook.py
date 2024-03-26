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

from okta_python_sdk.type.inline_hook_channel import InlineHookChannel
from okta_python_sdk.type.inline_hook_links import InlineHookLinks
from okta_python_sdk.type.inline_hook_status import InlineHookStatus
from okta_python_sdk.type.inline_hook_type import InlineHookType

class RequiredInlineHook(TypedDict):
    pass

class OptionalInlineHook(TypedDict, total=False):
    version: str

    _links: InlineHookLinks

    channel: InlineHookChannel

    created: datetime

    id: str

    lastUpdated: datetime

    name: str

    status: InlineHookStatus

    type: InlineHookType

class InlineHook(RequiredInlineHook, OptionalInlineHook):
    pass

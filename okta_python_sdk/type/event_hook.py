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

from okta_python_sdk.type.event_hook_channel import EventHookChannel
from okta_python_sdk.type.event_hook_links import EventHookLinks
from okta_python_sdk.type.event_subscriptions import EventSubscriptions

class RequiredEventHook(TypedDict):
    pass

class OptionalEventHook(TypedDict, total=False):
    _links: EventHookLinks

    channel: EventHookChannel

    created: datetime

    createdBy: str

    events: EventSubscriptions

    id: str

    lastUpdated: datetime

    name: str

    status: str

    verificationStatus: str

class EventHook(RequiredEventHook, OptionalEventHook):
    pass

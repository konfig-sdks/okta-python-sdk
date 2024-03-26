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

from okta_python_sdk.pydantic.event_hook_channel import EventHookChannel
from okta_python_sdk.pydantic.event_hook_links import EventHookLinks
from okta_python_sdk.pydantic.event_subscriptions import EventSubscriptions

class EventHook(BaseModel):
    _links: typing.Optional[EventHookLinks] = Field(None, alias='_links')

    channel: typing.Optional[EventHookChannel] = Field(None, alias='channel')

    created: typing.Optional[datetime] = Field(None, alias='created')

    created_by: typing.Optional[str] = Field(None, alias='createdBy')

    events: typing.Optional[EventSubscriptions] = Field(None, alias='events')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    verification_status: typing.Optional[Literal["UNVERIFIED", "VERIFIED"]] = Field(None, alias='verificationStatus')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

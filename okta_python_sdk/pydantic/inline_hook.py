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

from okta_python_sdk.pydantic.inline_hook_channel import InlineHookChannel
from okta_python_sdk.pydantic.inline_hook_links import InlineHookLinks
from okta_python_sdk.pydantic.inline_hook_status import InlineHookStatus
from okta_python_sdk.pydantic.inline_hook_type import InlineHookType

class InlineHook(BaseModel):
    version: typing.Optional[str] = Field(None, alias='version')

    _links: typing.Optional[InlineHookLinks] = Field(None, alias='_links')

    channel: typing.Optional[InlineHookChannel] = Field(None, alias='channel')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    status: typing.Optional[InlineHookStatus] = Field(None, alias='status')

    type: typing.Optional[InlineHookType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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


class ClientSecret(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='_links')

    client_secret: typing.Optional[str] = Field(None, alias='client_secret')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    secret_hash: typing.Optional[str] = Field(None, alias='secret_hash')

    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

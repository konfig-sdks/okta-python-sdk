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

from okta_python_sdk.pydantic.user_credentials import UserCredentials
from okta_python_sdk.pydantic.user_embedded import UserEmbedded
from okta_python_sdk.pydantic.user_links import UserLinks
from okta_python_sdk.pydantic.user_profile import UserProfile
from okta_python_sdk.pydantic.user_status import UserStatus
from okta_python_sdk.pydantic.user_type import UserType

class User(BaseModel):
    _embedded: typing.Optional[UserEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[UserLinks] = Field(None, alias='_links')

    activated: typing.Optional[datetime] = Field(None, alias='activated')

    created: typing.Optional[datetime] = Field(None, alias='created')

    credentials: typing.Optional[UserCredentials] = Field(None, alias='credentials')

    id: typing.Optional[str] = Field(None, alias='id')

    last_login: typing.Optional[datetime] = Field(None, alias='lastLogin')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    password_changed: typing.Optional[datetime] = Field(None, alias='passwordChanged')

    profile: typing.Optional[UserProfile] = Field(None, alias='profile')

    status: typing.Optional[UserStatus] = Field(None, alias='status')

    status_changed: typing.Optional[datetime] = Field(None, alias='statusChanged')

    transitioning_to_status: typing.Optional[UserStatus] = Field(None, alias='transitioningToStatus')

    type: typing.Optional[UserType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.app_user_credentials import AppUserCredentials
from okta_python_sdk.pydantic.app_user_embedded import AppUserEmbedded
from okta_python_sdk.pydantic.app_user_links import AppUserLinks
from okta_python_sdk.pydantic.app_user_profile import AppUserProfile

class AppUser(BaseModel):
    _embedded: typing.Optional[AppUserEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[AppUserLinks] = Field(None, alias='_links')

    created: typing.Optional[datetime] = Field(None, alias='created')

    credentials: typing.Optional[AppUserCredentials] = Field(None, alias='credentials')

    external_id: typing.Optional[str] = Field(None, alias='externalId')

    id: typing.Optional[str] = Field(None, alias='id')

    last_sync: typing.Optional[datetime] = Field(None, alias='lastSync')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    password_changed: typing.Optional[datetime] = Field(None, alias='passwordChanged')

    profile: typing.Optional[AppUserProfile] = Field(None, alias='profile')

    scope: typing.Optional[str] = Field(None, alias='scope')

    status: typing.Optional[str] = Field(None, alias='status')

    status_changed: typing.Optional[datetime] = Field(None, alias='statusChanged')

    sync_state: typing.Optional[str] = Field(None, alias='syncState')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

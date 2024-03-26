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

from okta_python_sdk.pydantic.identity_provider_application_user_embedded import IdentityProviderApplicationUserEmbedded
from okta_python_sdk.pydantic.identity_provider_application_user_links import IdentityProviderApplicationUserLinks
from okta_python_sdk.pydantic.identity_provider_application_user_profile import IdentityProviderApplicationUserProfile

class IdentityProviderApplicationUser(BaseModel):
    _embedded: typing.Optional[IdentityProviderApplicationUserEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[IdentityProviderApplicationUserLinks] = Field(None, alias='_links')

    created: typing.Optional[str] = Field(None, alias='created')

    external_id: typing.Optional[str] = Field(None, alias='externalId')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[str] = Field(None, alias='lastUpdated')

    profile: typing.Optional[IdentityProviderApplicationUserProfile] = Field(None, alias='profile')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

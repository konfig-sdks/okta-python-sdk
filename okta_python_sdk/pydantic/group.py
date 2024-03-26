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

from okta_python_sdk.pydantic.group_embedded import GroupEmbedded
from okta_python_sdk.pydantic.group_links import GroupLinks
from okta_python_sdk.pydantic.group_object_class import GroupObjectClass
from okta_python_sdk.pydantic.group_profile import GroupProfile
from okta_python_sdk.pydantic.group_type import GroupType

class Group(BaseModel):
    _embedded: typing.Optional[GroupEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[GroupLinks] = Field(None, alias='_links')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    last_membership_updated: typing.Optional[datetime] = Field(None, alias='lastMembershipUpdated')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    object_class: typing.Optional[GroupObjectClass] = Field(None, alias='objectClass')

    profile: typing.Optional[GroupProfile] = Field(None, alias='profile')

    type: typing.Optional[GroupType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

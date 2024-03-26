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

from okta_python_sdk.pydantic.user_type_links import UserTypeLinks

class UserType(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    _links: typing.Optional[UserTypeLinks] = Field(None, alias='_links')

    created: typing.Optional[datetime] = Field(None, alias='created')

    created_by: typing.Optional[str] = Field(None, alias='createdBy')

    default: typing.Optional[bool] = Field(None, alias='default')

    display_name: typing.Optional[str] = Field(None, alias='displayName')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    last_updated_by: typing.Optional[str] = Field(None, alias='lastUpdatedBy')

    name: typing.Optional[str] = Field(None, alias='name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

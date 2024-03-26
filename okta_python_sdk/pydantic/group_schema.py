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

from okta_python_sdk.pydantic.group_schema_definitions import GroupSchemaDefinitions
from okta_python_sdk.pydantic.group_schema_links import GroupSchemaLinks
from okta_python_sdk.pydantic.user_schema_properties import UserSchemaProperties

class GroupSchema(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    $schema_: typing.Optional[str] = Field(None, alias='$schema')

    _links: typing.Optional[GroupSchemaLinks] = Field(None, alias='_links')

    created: typing.Optional[str] = Field(None, alias='created')

    definitions: typing.Optional[GroupSchemaDefinitions] = Field(None, alias='definitions')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[str] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    properties: typing.Optional[UserSchemaProperties] = Field(None, alias='properties')

    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

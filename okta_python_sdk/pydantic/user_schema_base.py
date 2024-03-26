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

from okta_python_sdk.pydantic.user_schema_base_properties import UserSchemaBaseProperties
from okta_python_sdk.pydantic.user_schema_base_required import UserSchemaBaseRequired

class UserSchemaBase(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    properties: typing.Optional[UserSchemaBaseProperties] = Field(None, alias='properties')

    required: typing.Optional[UserSchemaBaseRequired] = Field(None, alias='required')

    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

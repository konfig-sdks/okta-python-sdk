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

from okta_python_sdk.pydantic.user_schema_attribute_enum import UserSchemaAttributeEnum
from okta_python_sdk.pydantic.user_schema_attribute_items import UserSchemaAttributeItems
from okta_python_sdk.pydantic.user_schema_attribute_master import UserSchemaAttributeMaster
from okta_python_sdk.pydantic.user_schema_attribute_permission import UserSchemaAttributePermission
from okta_python_sdk.pydantic.user_schema_attribute_scope import UserSchemaAttributeScope
from okta_python_sdk.pydantic.user_schema_attribute_type import UserSchemaAttributeType
from okta_python_sdk.pydantic.user_schema_attribute_union import UserSchemaAttributeUnion

class UserSchemaAttribute(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    description: typing.Optional[str] = Field(None, alias='description')

    enum: typing.Optional[UserSchemaAttributeEnum] = Field(None, alias='enum')

    external_name: typing.Optional[str] = Field(None, alias='externalName')

    external_namespace: typing.Optional[str] = Field(None, alias='externalNamespace')

    items: typing.Optional[UserSchemaAttributeItems] = Field(None, alias='items')

    master: typing.Optional[UserSchemaAttributeMaster] = Field(None, alias='master')

    max_length: typing.Optional[int] = Field(None, alias='maxLength')

    min_length: typing.Optional[int] = Field(None, alias='minLength')

    mutability: typing.Optional[str] = Field(None, alias='mutability')

    one_of: typing.Optional[typing.List[UserSchemaAttributeEnum]] = Field(None, alias='oneOf')

    pattern: typing.Optional[str] = Field(None, alias='pattern')

    permissions: typing.Optional[typing.List[UserSchemaAttributePermission]] = Field(None, alias='permissions')

    required: typing.Optional[bool] = Field(None, alias='required')

    scope: typing.Optional[UserSchemaAttributeScope] = Field(None, alias='scope')

    type: typing.Optional[UserSchemaAttributeType] = Field(None, alias='type')

    union: typing.Optional[UserSchemaAttributeUnion] = Field(None, alias='union')

    unique: typing.Optional[str] = Field(None, alias='unique')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

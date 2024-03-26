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

from okta_python_sdk.type.group_schema_attribute_enum import GroupSchemaAttributeEnum
from okta_python_sdk.type.user_schema_attribute_enum import UserSchemaAttributeEnum
from okta_python_sdk.type.user_schema_attribute_items import UserSchemaAttributeItems
from okta_python_sdk.type.user_schema_attribute_master import UserSchemaAttributeMaster
from okta_python_sdk.type.user_schema_attribute_permission import UserSchemaAttributePermission
from okta_python_sdk.type.user_schema_attribute_scope import UserSchemaAttributeScope
from okta_python_sdk.type.user_schema_attribute_type import UserSchemaAttributeType
from okta_python_sdk.type.user_schema_attribute_union import UserSchemaAttributeUnion

class RequiredGroupSchemaAttribute(TypedDict):
    pass

class OptionalGroupSchemaAttribute(TypedDict, total=False):
    title: str

    description: str

    enum: GroupSchemaAttributeEnum

    externalName: str

    externalNamespace: str

    items: UserSchemaAttributeItems

    master: UserSchemaAttributeMaster

    maxLength: int

    minLength: int

    mutability: str

    oneOf: typing.List[UserSchemaAttributeEnum]

    permissions: typing.List[UserSchemaAttributePermission]

    required: bool

    scope: UserSchemaAttributeScope

    type: UserSchemaAttributeType

    union: UserSchemaAttributeUnion

    unique: str

class GroupSchemaAttribute(RequiredGroupSchemaAttribute, OptionalGroupSchemaAttribute):
    pass

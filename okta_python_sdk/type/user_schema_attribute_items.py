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

from okta_python_sdk.type.user_schema_attribute_enum import UserSchemaAttributeEnum
from okta_python_sdk.type.user_schema_attribute_items_enum import UserSchemaAttributeItemsEnum

class RequiredUserSchemaAttributeItems(TypedDict):
    pass

class OptionalUserSchemaAttributeItems(TypedDict, total=False):
    enum: UserSchemaAttributeItemsEnum

    oneOf: typing.List[UserSchemaAttributeEnum]

    type: str

class UserSchemaAttributeItems(RequiredUserSchemaAttributeItems, OptionalUserSchemaAttributeItems):
    pass

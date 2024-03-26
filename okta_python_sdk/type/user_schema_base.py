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

from okta_python_sdk.type.user_schema_base_properties import UserSchemaBaseProperties
from okta_python_sdk.type.user_schema_base_required import UserSchemaBaseRequired

class RequiredUserSchemaBase(TypedDict):
    pass

class OptionalUserSchemaBase(TypedDict, total=False):
    id: str

    properties: UserSchemaBaseProperties

    required: UserSchemaBaseRequired

    type: str

class UserSchemaBase(RequiredUserSchemaBase, OptionalUserSchemaBase):
    pass

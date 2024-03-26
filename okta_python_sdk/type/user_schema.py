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

from okta_python_sdk.type.user_schema_definitions import UserSchemaDefinitions
from okta_python_sdk.type.user_schema_links import UserSchemaLinks
from okta_python_sdk.type.user_schema_properties import UserSchemaProperties

RequiredUserSchema = TypedDict("RequiredUserSchema", {
    })

OptionalUserSchema = TypedDict("OptionalUserSchema", {
    "title": str,

    "$schema": str,

    "_links": UserSchemaLinks,

    "created": str,

    "definitions": UserSchemaDefinitions,

    "id": str,

    "lastUpdated": str,

    "name": str,

    "properties": UserSchemaProperties,

    "type": str,
    }, total=False)

class UserSchema(RequiredUserSchema, OptionalUserSchema):
    pass

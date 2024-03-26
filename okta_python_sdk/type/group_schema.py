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

from okta_python_sdk.type.group_schema_definitions import GroupSchemaDefinitions
from okta_python_sdk.type.group_schema_links import GroupSchemaLinks
from okta_python_sdk.type.user_schema_properties import UserSchemaProperties

RequiredGroupSchema = TypedDict("RequiredGroupSchema", {
    })

OptionalGroupSchema = TypedDict("OptionalGroupSchema", {
    "title": str,

    "description": str,

    "$schema": str,

    "_links": GroupSchemaLinks,

    "created": str,

    "definitions": GroupSchemaDefinitions,

    "id": str,

    "lastUpdated": str,

    "name": str,

    "properties": UserSchemaProperties,

    "type": str,
    }, total=False)

class GroupSchema(RequiredGroupSchema, OptionalGroupSchema):
    pass

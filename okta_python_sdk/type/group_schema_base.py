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

from okta_python_sdk.type.group_schema_base_properties import GroupSchemaBaseProperties
from okta_python_sdk.type.group_schema_base_required import GroupSchemaBaseRequired

class RequiredGroupSchemaBase(TypedDict):
    pass

class OptionalGroupSchemaBase(TypedDict, total=False):
    id: str

    properties: GroupSchemaBaseProperties

    required: GroupSchemaBaseRequired

    type: str

class GroupSchemaBase(RequiredGroupSchemaBase, OptionalGroupSchemaBase):
    pass

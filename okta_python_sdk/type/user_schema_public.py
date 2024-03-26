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

from okta_python_sdk.type.user_schema_public_properties import UserSchemaPublicProperties
from okta_python_sdk.type.user_schema_public_required import UserSchemaPublicRequired

class RequiredUserSchemaPublic(TypedDict):
    pass

class OptionalUserSchemaPublic(TypedDict, total=False):
    id: str

    properties: UserSchemaPublicProperties

    required: UserSchemaPublicRequired

    type: str

class UserSchemaPublic(RequiredUserSchemaPublic, OptionalUserSchemaPublic):
    pass

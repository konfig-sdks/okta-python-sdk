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

from okta_python_sdk.type.group_embedded import GroupEmbedded
from okta_python_sdk.type.group_links import GroupLinks
from okta_python_sdk.type.group_object_class import GroupObjectClass
from okta_python_sdk.type.group_profile import GroupProfile
from okta_python_sdk.type.group_type import GroupType

class RequiredGroup(TypedDict):
    pass

class OptionalGroup(TypedDict, total=False):
    _embedded: GroupEmbedded

    _links: GroupLinks

    created: datetime

    id: str

    lastMembershipUpdated: datetime

    lastUpdated: datetime

    objectClass: GroupObjectClass

    profile: GroupProfile

    type: GroupType

class Group(RequiredGroup, OptionalGroup):
    pass

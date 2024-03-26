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

from okta_python_sdk.type.role_assignment_type import RoleAssignmentType
from okta_python_sdk.type.role_embedded import RoleEmbedded
from okta_python_sdk.type.role_links import RoleLinks
from okta_python_sdk.type.role_status import RoleStatus
from okta_python_sdk.type.role_type import RoleType

class RequiredRole(TypedDict):
    pass

class OptionalRole(TypedDict, total=False):
    description: str

    _embedded: RoleEmbedded

    _links: RoleLinks

    assignmentType: RoleAssignmentType

    created: datetime

    id: str

    label: str

    lastUpdated: datetime

    status: RoleStatus

    type: RoleType

class Role(RequiredRole, OptionalRole):
    pass

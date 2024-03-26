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

from okta_python_sdk.type.application_group_assignment_embedded import ApplicationGroupAssignmentEmbedded
from okta_python_sdk.type.application_group_assignment_links import ApplicationGroupAssignmentLinks
from okta_python_sdk.type.application_group_assignment_profile import ApplicationGroupAssignmentProfile

class RequiredApplicationGroupAssignment(TypedDict):
    pass

class OptionalApplicationGroupAssignment(TypedDict, total=False):
    _embedded: ApplicationGroupAssignmentEmbedded

    _links: ApplicationGroupAssignmentLinks

    id: str

    lastUpdated: datetime

    priority: int

    profile: ApplicationGroupAssignmentProfile

class ApplicationGroupAssignment(RequiredApplicationGroupAssignment, OptionalApplicationGroupAssignment):
    pass

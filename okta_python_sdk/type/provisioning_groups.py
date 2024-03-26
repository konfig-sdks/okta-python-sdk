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

from okta_python_sdk.type.provisioning_groups_assignments import ProvisioningGroupsAssignments
from okta_python_sdk.type.provisioning_groups_filter import ProvisioningGroupsFilter

class RequiredProvisioningGroups(TypedDict):
    pass

class OptionalProvisioningGroups(TypedDict, total=False):
    action: str

    assignments: ProvisioningGroupsAssignments

    filter: ProvisioningGroupsFilter

    sourceAttributeName: str

class ProvisioningGroups(RequiredProvisioningGroups, OptionalProvisioningGroups):
    pass

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

from okta_python_sdk.type.provisioning_conditions import ProvisioningConditions
from okta_python_sdk.type.provisioning_groups import ProvisioningGroups

class RequiredProvisioning(TypedDict):
    pass

class OptionalProvisioning(TypedDict, total=False):
    action: str

    conditions: ProvisioningConditions

    groups: ProvisioningGroups

    profileMaster: bool

class Provisioning(RequiredProvisioning, OptionalProvisioning):
    pass

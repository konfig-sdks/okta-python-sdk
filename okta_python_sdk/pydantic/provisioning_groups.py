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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from okta_python_sdk.pydantic.provisioning_groups_assignments import ProvisioningGroupsAssignments
from okta_python_sdk.pydantic.provisioning_groups_filter import ProvisioningGroupsFilter

class ProvisioningGroups(BaseModel):
    action: typing.Optional[Literal["NONE", "APPEND", "SYNC", "ASSIGN"]] = Field(None, alias='action')

    assignments: typing.Optional[ProvisioningGroupsAssignments] = Field(None, alias='assignments')

    filter: typing.Optional[ProvisioningGroupsFilter] = Field(None, alias='filter')

    source_attribute_name: typing.Optional[str] = Field(None, alias='sourceAttributeName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

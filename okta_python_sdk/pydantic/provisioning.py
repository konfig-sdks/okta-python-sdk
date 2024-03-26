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

from okta_python_sdk.pydantic.provisioning_conditions import ProvisioningConditions
from okta_python_sdk.pydantic.provisioning_groups import ProvisioningGroups

class Provisioning(BaseModel):
    action: typing.Optional[Literal["AUTO", "CALLOUT", "DISABLED"]] = Field(None, alias='action')

    conditions: typing.Optional[ProvisioningConditions] = Field(None, alias='conditions')

    groups: typing.Optional[ProvisioningGroups] = Field(None, alias='groups')

    profile_master: typing.Optional[bool] = Field(None, alias='profileMaster')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

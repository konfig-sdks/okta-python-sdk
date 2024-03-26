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

from okta_python_sdk.pydantic.provisioning_deprovisioned_condition import ProvisioningDeprovisionedCondition
from okta_python_sdk.pydantic.provisioning_suspended_condition import ProvisioningSuspendedCondition

class ProvisioningConditions(BaseModel):
    deprovisioned: typing.Optional[ProvisioningDeprovisionedCondition] = Field(None, alias='deprovisioned')

    suspended: typing.Optional[ProvisioningSuspendedCondition] = Field(None, alias='suspended')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

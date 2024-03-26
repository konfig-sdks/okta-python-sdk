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

from okta_python_sdk.pydantic.access_policy_constraints import AccessPolicyConstraints

class VerificationMethod(BaseModel):
    constraints: typing.Optional[typing.List[AccessPolicyConstraints]] = Field(None, alias='constraints')

    factor_mode: typing.Optional[str] = Field(None, alias='factorMode')

    inactivity_period: typing.Optional[str] = Field(None, alias='inactivityPeriod')

    reauthenticate_in: typing.Optional[str] = Field(None, alias='reauthenticateIn')

    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.access_policy_constraint_methods import AccessPolicyConstraintMethods
from okta_python_sdk.pydantic.access_policy_constraint_types import AccessPolicyConstraintTypes

class AccessPolicyConstraint(BaseModel):
    methods: typing.Optional[AccessPolicyConstraintMethods] = Field(None, alias='methods')

    reauthenticate_in: typing.Optional[str] = Field(None, alias='reauthenticateIn')

    types: typing.Optional[AccessPolicyConstraintTypes] = Field(None, alias='types')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

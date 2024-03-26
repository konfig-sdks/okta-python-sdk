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


class ProfileEnrollmentPolicyRuleProfileAttribute(BaseModel):
    label: typing.Optional[str] = Field(None, alias='label')

    name: typing.Optional[str] = Field(None, alias='name')

    required: typing.Optional[bool] = Field(None, alias='required')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

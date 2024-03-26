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

from okta_python_sdk.pydantic.factor_result_type import FactorResultType
from okta_python_sdk.pydantic.push_user_factor_profile import PushUserFactorProfile

class PushUserFactor(BaseModel):
    expires_at: typing.Optional[datetime] = Field(None, alias='expiresAt')

    factor_result: typing.Optional[FactorResultType] = Field(None, alias='factorResult')

    profile: typing.Optional[PushUserFactorProfile] = Field(None, alias='profile')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

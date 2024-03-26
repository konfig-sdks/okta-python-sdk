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

from okta_python_sdk.pydantic.change_enum import ChangeEnum
from okta_python_sdk.pydantic.enabled_status import EnabledStatus
from okta_python_sdk.pydantic.seed_enum import SeedEnum

class PasswordSettingObject(BaseModel):
    change: typing.Optional[ChangeEnum] = Field(None, alias='change')

    seed: typing.Optional[SeedEnum] = Field(None, alias='seed')

    status: typing.Optional[EnabledStatus] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

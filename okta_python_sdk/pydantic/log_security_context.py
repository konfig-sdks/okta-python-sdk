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


class LogSecurityContext(BaseModel):
    as_number: typing.Optional[int] = Field(None, alias='asNumber')

    as_org: typing.Optional[str] = Field(None, alias='asOrg')

    domain: typing.Optional[str] = Field(None, alias='domain')

    is_proxy: typing.Optional[bool] = Field(None, alias='isProxy')

    isp: typing.Optional[str] = Field(None, alias='isp')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

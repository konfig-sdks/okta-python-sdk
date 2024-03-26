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


class SamlAttributeStatement(BaseModel):
    filter_type: typing.Optional[str] = Field(None, alias='filterType')

    filter_value: typing.Optional[str] = Field(None, alias='filterValue')

    name: typing.Optional[str] = Field(None, alias='name')

    namespace: typing.Optional[str] = Field(None, alias='namespace')

    type: typing.Optional[str] = Field(None, alias='type')

    values: typing.Optional[typing.List[str]] = Field(None, alias='values')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

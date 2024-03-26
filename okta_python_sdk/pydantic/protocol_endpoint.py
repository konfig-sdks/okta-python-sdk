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


class ProtocolEndpoint(BaseModel):
    binding: typing.Optional[Literal["HTTP-POST", "HTTP-REDIRECT"]] = Field(None, alias='binding')

    destination: typing.Optional[str] = Field(None, alias='destination')

    type: typing.Optional[Literal["INSTANCE", "ORG"]] = Field(None, alias='type')

    url: typing.Optional[str] = Field(None, alias='url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

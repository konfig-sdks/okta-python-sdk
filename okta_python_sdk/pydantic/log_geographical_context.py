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

from okta_python_sdk.pydantic.log_geolocation import LogGeolocation

class LogGeographicalContext(BaseModel):
    city: typing.Optional[str] = Field(None, alias='city')

    country: typing.Optional[str] = Field(None, alias='country')

    geolocation: typing.Optional[LogGeolocation] = Field(None, alias='geolocation')

    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    state: typing.Optional[str] = Field(None, alias='state')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

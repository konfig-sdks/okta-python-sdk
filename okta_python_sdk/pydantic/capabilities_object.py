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

from okta_python_sdk.pydantic.capabilities_create_object import CapabilitiesCreateObject
from okta_python_sdk.pydantic.capabilities_update_object import CapabilitiesUpdateObject

class CapabilitiesObject(BaseModel):
    create: typing.Optional[CapabilitiesCreateObject] = Field(None, alias='create')

    update: typing.Optional[CapabilitiesUpdateObject] = Field(None, alias='update')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

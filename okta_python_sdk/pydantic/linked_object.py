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

from okta_python_sdk.pydantic.linked_object_details import LinkedObjectDetails
from okta_python_sdk.pydantic.linked_object_links import LinkedObjectLinks

class LinkedObject(BaseModel):
    _links: typing.Optional[LinkedObjectLinks] = Field(None, alias='_links')

    associated: typing.Optional[LinkedObjectDetails] = Field(None, alias='associated')

    primary: typing.Optional[LinkedObjectDetails] = Field(None, alias='primary')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

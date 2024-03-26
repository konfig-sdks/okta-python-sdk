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


class EmailTemplateCustomizationRequest(BaseModel):
    body: typing.Optional[str] = Field(None, alias='body')

    is_default: typing.Optional[bool] = Field(None, alias='isDefault')

    # unique under each email template
    language: typing.Optional[str] = Field(None, alias='language')

    subject: typing.Optional[str] = Field(None, alias='subject')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.ion_field_value import IonFieldValue
if TYPE_CHECKING:
    from okta_python_sdk.pydantic.ion_form import IonForm

class IonField(BaseModel):
    form: typing.Optional['IonForm'] = Field(None, alias='form')

    label: typing.Optional[str] = Field(None, alias='label')

    mutable: typing.Optional[bool] = Field(None, alias='mutable')

    name: typing.Optional[str] = Field(None, alias='name')

    required: typing.Optional[bool] = Field(None, alias='required')

    secret: typing.Optional[bool] = Field(None, alias='secret')

    type: typing.Optional[str] = Field(None, alias='type')

    value: typing.Optional[IonFieldValue] = Field(None, alias='value')

    visible: typing.Optional[bool] = Field(None, alias='visible')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

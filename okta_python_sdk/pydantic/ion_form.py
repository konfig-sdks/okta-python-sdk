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

from okta_python_sdk.pydantic.ion_field import IonField
from okta_python_sdk.pydantic.ion_form_rel import IonFormRel
from okta_python_sdk.pydantic.ion_form_relates_to import IonFormRelatesTo

class IonForm(BaseModel):
    accepts: typing.Optional[str] = Field(None, alias='accepts')

    href: typing.Optional[str] = Field(None, alias='href')

    method: typing.Optional[str] = Field(None, alias='method')

    name: typing.Optional[str] = Field(None, alias='name')

    produces: typing.Optional[str] = Field(None, alias='produces')

    refresh: typing.Optional[int] = Field(None, alias='refresh')

    rel: typing.Optional[IonFormRel] = Field(None, alias='rel')

    relates_to: typing.Optional[IonFormRelatesTo] = Field(None, alias='relatesTo')

    value: typing.Optional['typing.List[IonField]'] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

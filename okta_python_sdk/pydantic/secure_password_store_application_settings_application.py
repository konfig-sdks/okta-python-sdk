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


class SecurePasswordStoreApplicationSettingsApplication(BaseModel):
    optional_field1: typing.Optional[str] = Field(None, alias='optionalField1')

    optional_field1_value: typing.Optional[str] = Field(None, alias='optionalField1Value')

    optional_field2: typing.Optional[str] = Field(None, alias='optionalField2')

    optional_field2_value: typing.Optional[str] = Field(None, alias='optionalField2Value')

    optional_field3: typing.Optional[str] = Field(None, alias='optionalField3')

    optional_field3_value: typing.Optional[str] = Field(None, alias='optionalField3Value')

    password_field: typing.Optional[str] = Field(None, alias='passwordField')

    url: typing.Optional[str] = Field(None, alias='url')

    username_field: typing.Optional[str] = Field(None, alias='usernameField')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

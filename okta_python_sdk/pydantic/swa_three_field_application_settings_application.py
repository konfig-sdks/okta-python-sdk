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


class SwaThreeFieldApplicationSettingsApplication(BaseModel):
    button_selector: typing.Optional[str] = Field(None, alias='buttonSelector')

    extra_field_selector: typing.Optional[str] = Field(None, alias='extraFieldSelector')

    extra_field_value: typing.Optional[str] = Field(None, alias='extraFieldValue')

    login_url_regex: typing.Optional[str] = Field(None, alias='loginUrlRegex')

    password_selector: typing.Optional[str] = Field(None, alias='passwordSelector')

    target_u_r_l: typing.Optional[str] = Field(None, alias='targetURL')

    user_name_selector: typing.Optional[str] = Field(None, alias='userNameSelector')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

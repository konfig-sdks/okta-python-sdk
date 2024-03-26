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


class ApplicationSettingsApplication(BaseModel):
    acs_url: typing.Optional[str] = Field(None, alias='acsUrl')

    button_field: typing.Optional[str] = Field(None, alias='buttonField')

    login_url_regex: typing.Optional[str] = Field(None, alias='loginUrlRegex')

    org_name: typing.Optional[str] = Field(None, alias='orgName')

    password_field: typing.Optional[str] = Field(None, alias='passwordField')

    url: typing.Optional[str] = Field(None, alias='url')

    username_field: typing.Optional[str] = Field(None, alias='usernameField')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

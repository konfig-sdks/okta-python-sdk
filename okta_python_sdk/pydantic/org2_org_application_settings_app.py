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


class Org2OrgApplicationSettingsApp(BaseModel):
    acs_url: typing.Optional[str] = Field(None, alias='acsUrl')

    aud_restriction: typing.Optional[str] = Field(None, alias='audRestriction')

    base_url: typing.Optional[str] = Field(None, alias='baseUrl')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

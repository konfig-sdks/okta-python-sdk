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


class OrgPreferences(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='_links')

    show_end_user_footer: typing.Optional[bool] = Field(None, alias='showEndUserFooter')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

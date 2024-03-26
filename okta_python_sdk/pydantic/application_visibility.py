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

from okta_python_sdk.pydantic.application_visibility_app_links import ApplicationVisibilityAppLinks
from okta_python_sdk.pydantic.application_visibility_hide import ApplicationVisibilityHide

class ApplicationVisibility(BaseModel):
    app_links: typing.Optional[ApplicationVisibilityAppLinks] = Field(None, alias='appLinks')

    auto_launch: typing.Optional[bool] = Field(None, alias='autoLaunch')

    auto_submit_toolbar: typing.Optional[bool] = Field(None, alias='autoSubmitToolbar')

    hide: typing.Optional[ApplicationVisibilityHide] = Field(None, alias='hide')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

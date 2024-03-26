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

from okta_python_sdk.pydantic.email_template_touch_point_variant import EmailTemplateTouchPointVariant
from okta_python_sdk.pydantic.end_user_dashboard_touch_point_variant import EndUserDashboardTouchPointVariant
from okta_python_sdk.pydantic.error_page_touch_point_variant import ErrorPageTouchPointVariant
from okta_python_sdk.pydantic.sign_in_page_touch_point_variant import SignInPageTouchPointVariant

class ThemeResponse(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='_links')

    background_image: typing.Optional[str] = Field(None, alias='backgroundImage')

    email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = Field(None, alias='emailTemplateTouchPointVariant')

    end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = Field(None, alias='endUserDashboardTouchPointVariant')

    error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = Field(None, alias='errorPageTouchPointVariant')

    favicon: typing.Optional[str] = Field(None, alias='favicon')

    id: typing.Optional[str] = Field(None, alias='id')

    logo: typing.Optional[str] = Field(None, alias='logo')

    primary_color_contrast_hex: typing.Optional[str] = Field(None, alias='primaryColorContrastHex')

    primary_color_hex: typing.Optional[str] = Field(None, alias='primaryColorHex')

    secondary_color_contrast_hex: typing.Optional[str] = Field(None, alias='secondaryColorContrastHex')

    secondary_color_hex: typing.Optional[str] = Field(None, alias='secondaryColorHex')

    sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = Field(None, alias='signInPageTouchPointVariant')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.type.email_template_touch_point_variant import EmailTemplateTouchPointVariant
from okta_python_sdk.type.end_user_dashboard_touch_point_variant import EndUserDashboardTouchPointVariant
from okta_python_sdk.type.error_page_touch_point_variant import ErrorPageTouchPointVariant
from okta_python_sdk.type.sign_in_page_touch_point_variant import SignInPageTouchPointVariant

class RequiredTheme(TypedDict):
    pass

class OptionalTheme(TypedDict, total=False):
    _links: typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    backgroundImage: str

    emailTemplateTouchPointVariant: EmailTemplateTouchPointVariant

    endUserDashboardTouchPointVariant: EndUserDashboardTouchPointVariant

    errorPageTouchPointVariant: ErrorPageTouchPointVariant

    primaryColorContrastHex: str

    primaryColorHex: str

    secondaryColorContrastHex: str

    secondaryColorHex: str

    signInPageTouchPointVariant: SignInPageTouchPointVariant

class Theme(RequiredTheme, OptionalTheme):
    pass

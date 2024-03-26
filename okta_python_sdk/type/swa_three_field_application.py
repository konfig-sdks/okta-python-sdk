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

from okta_python_sdk.type.swa_three_field_application_settings import SwaThreeFieldApplicationSettings

class RequiredSwaThreeFieldApplication(TypedDict):
    pass

class OptionalSwaThreeFieldApplication(TypedDict, total=False):
    name: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    settings: SwaThreeFieldApplicationSettings

class SwaThreeFieldApplication(RequiredSwaThreeFieldApplication, OptionalSwaThreeFieldApplication):
    pass

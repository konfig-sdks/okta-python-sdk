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

from okta_python_sdk.type.swa_three_field_application_settings_application import SwaThreeFieldApplicationSettingsApplication

class RequiredSwaThreeFieldApplicationSettings(TypedDict):
    pass

class OptionalSwaThreeFieldApplicationSettings(TypedDict, total=False):
    app: SwaThreeFieldApplicationSettingsApplication

class SwaThreeFieldApplicationSettings(RequiredSwaThreeFieldApplicationSettings, OptionalSwaThreeFieldApplicationSettings):
    pass

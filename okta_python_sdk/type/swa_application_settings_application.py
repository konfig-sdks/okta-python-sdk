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


class RequiredSwaApplicationSettingsApplication(TypedDict):
    pass

class OptionalSwaApplicationSettingsApplication(TypedDict, total=False):
    buttonField: str

    checkbox: str

    loginUrlRegex: str

    passwordField: str

    redirectUrl: str

    url: str

    usernameField: str

class SwaApplicationSettingsApplication(RequiredSwaApplicationSettingsApplication, OptionalSwaApplicationSettingsApplication):
    pass

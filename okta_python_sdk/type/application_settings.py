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

from okta_python_sdk.type.application_settings_application import ApplicationSettingsApplication
from okta_python_sdk.type.application_settings_notes import ApplicationSettingsNotes
from okta_python_sdk.type.application_settings_notifications import ApplicationSettingsNotifications

class RequiredApplicationSettings(TypedDict):
    pass

class OptionalApplicationSettings(TypedDict, total=False):
    app: ApplicationSettingsApplication

    implicitAssignment: bool

    inlineHookId: str

    notes: ApplicationSettingsNotes

    notifications: ApplicationSettingsNotifications

class ApplicationSettings(RequiredApplicationSettings, OptionalApplicationSettings):
    pass

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

from okta_python_sdk.pydantic.application_settings_application import ApplicationSettingsApplication
from okta_python_sdk.pydantic.application_settings_notes import ApplicationSettingsNotes
from okta_python_sdk.pydantic.application_settings_notifications import ApplicationSettingsNotifications

class ApplicationSettings(BaseModel):
    app: typing.Optional[ApplicationSettingsApplication] = Field(None, alias='app')

    implicit_assignment: typing.Optional[bool] = Field(None, alias='implicitAssignment')

    inline_hook_id: typing.Optional[str] = Field(None, alias='inlineHookId')

    notes: typing.Optional[ApplicationSettingsNotes] = Field(None, alias='notes')

    notifications: typing.Optional[ApplicationSettingsNotifications] = Field(None, alias='notifications')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

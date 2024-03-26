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

from okta_python_sdk.pydantic.password_policy_password_settings_lockout_user_lockout_notification_channels import PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels

class PasswordPolicyPasswordSettingsLockout(BaseModel):
    auto_unlock_minutes: typing.Optional[int] = Field(None, alias='autoUnlockMinutes')

    max_attempts: typing.Optional[int] = Field(None, alias='maxAttempts')

    show_lockout_failures: typing.Optional[bool] = Field(None, alias='showLockoutFailures')

    user_lockout_notification_channels: typing.Optional[PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels] = Field(None, alias='userLockoutNotificationChannels')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

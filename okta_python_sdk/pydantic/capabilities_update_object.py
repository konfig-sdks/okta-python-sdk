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

from okta_python_sdk.pydantic.lifecycle_deactivate_setting_object import LifecycleDeactivateSettingObject
from okta_python_sdk.pydantic.password_setting_object import PasswordSettingObject
from okta_python_sdk.pydantic.profile_setting_object import ProfileSettingObject

class CapabilitiesUpdateObject(BaseModel):
    lifecycle_deactivate: typing.Optional[LifecycleDeactivateSettingObject] = Field(None, alias='lifecycleDeactivate')

    password: typing.Optional[PasswordSettingObject] = Field(None, alias='password')

    profile: typing.Optional[ProfileSettingObject] = Field(None, alias='profile')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

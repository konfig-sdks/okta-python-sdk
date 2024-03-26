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

from okta_python_sdk.type.lifecycle_deactivate_setting_object import LifecycleDeactivateSettingObject
from okta_python_sdk.type.password_setting_object import PasswordSettingObject
from okta_python_sdk.type.profile_setting_object import ProfileSettingObject

class RequiredCapabilitiesUpdateObject(TypedDict):
    pass

class OptionalCapabilitiesUpdateObject(TypedDict, total=False):
    lifecycleDeactivate: LifecycleDeactivateSettingObject

    password: PasswordSettingObject

    profile: ProfileSettingObject

class CapabilitiesUpdateObject(RequiredCapabilitiesUpdateObject, OptionalCapabilitiesUpdateObject):
    pass

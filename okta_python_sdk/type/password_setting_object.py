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

from okta_python_sdk.type.change_enum import ChangeEnum
from okta_python_sdk.type.enabled_status import EnabledStatus
from okta_python_sdk.type.seed_enum import SeedEnum

class RequiredPasswordSettingObject(TypedDict):
    pass

class OptionalPasswordSettingObject(TypedDict, total=False):
    change: ChangeEnum

    seed: SeedEnum

    status: EnabledStatus

class PasswordSettingObject(RequiredPasswordSettingObject, OptionalPasswordSettingObject):
    pass

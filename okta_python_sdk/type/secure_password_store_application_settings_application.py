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


class RequiredSecurePasswordStoreApplicationSettingsApplication(TypedDict):
    pass

class OptionalSecurePasswordStoreApplicationSettingsApplication(TypedDict, total=False):
    optionalField1: str

    optionalField1Value: str

    optionalField2: str

    optionalField2Value: str

    optionalField3: str

    optionalField3Value: str

    passwordField: str

    url: str

    usernameField: str

class SecurePasswordStoreApplicationSettingsApplication(RequiredSecurePasswordStoreApplicationSettingsApplication, OptionalSecurePasswordStoreApplicationSettingsApplication):
    pass

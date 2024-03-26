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

from okta_python_sdk.type.saml_application_settings_sign_on import SamlApplicationSettingsSignOn

class RequiredSamlApplicationSettings(TypedDict):
    pass

class OptionalSamlApplicationSettings(TypedDict, total=False):
    signOn: SamlApplicationSettingsSignOn

class SamlApplicationSettings(RequiredSamlApplicationSettings, OptionalSamlApplicationSettings):
    pass

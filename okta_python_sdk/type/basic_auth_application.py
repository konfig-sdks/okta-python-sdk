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

from okta_python_sdk.type.basic_application_settings import BasicApplicationSettings
from okta_python_sdk.type.scheme_application_credentials import SchemeApplicationCredentials

class RequiredBasicAuthApplication(TypedDict):
    pass

class OptionalBasicAuthApplication(TypedDict, total=False):
    credentials: SchemeApplicationCredentials

    name: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    settings: BasicApplicationSettings

class BasicAuthApplication(RequiredBasicAuthApplication, OptionalBasicAuthApplication):
    pass

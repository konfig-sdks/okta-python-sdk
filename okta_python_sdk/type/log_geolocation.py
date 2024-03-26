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


class RequiredLogGeolocation(TypedDict):
    pass

class OptionalLogGeolocation(TypedDict, total=False):
    lat: typing.Union[int, float]

    lon: typing.Union[int, float]

class LogGeolocation(RequiredLogGeolocation, OptionalLogGeolocation):
    pass

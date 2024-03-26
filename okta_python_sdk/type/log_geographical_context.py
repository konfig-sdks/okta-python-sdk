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

from okta_python_sdk.type.log_geolocation import LogGeolocation

class RequiredLogGeographicalContext(TypedDict):
    pass

class OptionalLogGeographicalContext(TypedDict, total=False):
    city: str

    country: str

    geolocation: LogGeolocation

    postalCode: str

    state: str

class LogGeographicalContext(RequiredLogGeographicalContext, OptionalLogGeographicalContext):
    pass

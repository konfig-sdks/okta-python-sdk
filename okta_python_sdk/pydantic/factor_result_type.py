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


FactorResultType = Literal["SUCCESS", "CHALLENGE", "WAITING", "FAILED", "REJECTED", "TIMEOUT", "TIME_WINDOW_EXCEEDED", "PASSCODE_REPLAYED", "ERROR", "CANCELLED"]

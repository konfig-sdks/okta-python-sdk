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


class PlatformConditionEvaluatorPlatformOperatingSystemVersion(BaseModel):
    match_type: typing.Optional[Literal["EXPRESSION", "SEMVER"]] = Field(None, alias='matchType')

    value: typing.Optional[str] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

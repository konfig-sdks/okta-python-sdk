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

from okta_python_sdk.pydantic.platform_condition_evaluator_platform_operating_system_version import PlatformConditionEvaluatorPlatformOperatingSystemVersion

class PlatformConditionEvaluatorPlatformOperatingSystem(BaseModel):
    version: typing.Optional[PlatformConditionEvaluatorPlatformOperatingSystemVersion] = Field(None, alias='version')

    expression: typing.Optional[str] = Field(None, alias='expression')

    type: typing.Optional[Literal["ANDROID", "IOS", "WINDOWS", "OSX", "OTHER", "ANY"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.duration import Duration
from okta_python_sdk.pydantic.scheduled_user_lifecycle_action import ScheduledUserLifecycleAction

class BeforeScheduledActionPolicyRuleCondition(BaseModel):
    duration: typing.Optional[Duration] = Field(None, alias='duration')

    lifecycle_action: typing.Optional[ScheduledUserLifecycleAction] = Field(None, alias='lifecycleAction')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

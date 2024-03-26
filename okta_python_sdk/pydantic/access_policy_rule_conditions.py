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

from okta_python_sdk.pydantic.access_policy_rule_custom_condition import AccessPolicyRuleCustomCondition
from okta_python_sdk.pydantic.device_access_policy_rule_condition import DeviceAccessPolicyRuleCondition
from okta_python_sdk.pydantic.user_type_condition import UserTypeCondition

class AccessPolicyRuleConditions(BaseModel):
    device: typing.Optional[DeviceAccessPolicyRuleCondition] = Field(None, alias='device')

    el_condition: typing.Optional[AccessPolicyRuleCustomCondition] = Field(None, alias='elCondition')

    user_type: typing.Optional[UserTypeCondition] = Field(None, alias='userType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

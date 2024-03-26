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

from okta_python_sdk.pydantic.app_instance_policy_rule_condition_exclude import AppInstancePolicyRuleConditionExclude
from okta_python_sdk.pydantic.app_instance_policy_rule_condition_include import AppInstancePolicyRuleConditionInclude

class AppInstancePolicyRuleCondition(BaseModel):
    exclude: typing.Optional[AppInstancePolicyRuleConditionExclude] = Field(None, alias='exclude')

    include: typing.Optional[AppInstancePolicyRuleConditionInclude] = Field(None, alias='include')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

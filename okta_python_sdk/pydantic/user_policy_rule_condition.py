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

from okta_python_sdk.pydantic.inactivity_policy_rule_condition import InactivityPolicyRuleCondition
from okta_python_sdk.pydantic.lifecycle_expiration_policy_rule_condition import LifecycleExpirationPolicyRuleCondition
from okta_python_sdk.pydantic.password_expiration_policy_rule_condition import PasswordExpirationPolicyRuleCondition
from okta_python_sdk.pydantic.user_lifecycle_attribute_policy_rule_condition import UserLifecycleAttributePolicyRuleCondition
from okta_python_sdk.pydantic.user_policy_rule_condition_exclude import UserPolicyRuleConditionExclude
from okta_python_sdk.pydantic.user_policy_rule_condition_include import UserPolicyRuleConditionInclude

class UserPolicyRuleCondition(BaseModel):
    exclude: typing.Optional[UserPolicyRuleConditionExclude] = Field(None, alias='exclude')

    inactivity: typing.Optional[InactivityPolicyRuleCondition] = Field(None, alias='inactivity')

    include: typing.Optional[UserPolicyRuleConditionInclude] = Field(None, alias='include')

    lifecycle_expiration: typing.Optional[LifecycleExpirationPolicyRuleCondition] = Field(None, alias='lifecycleExpiration')

    password_expiration: typing.Optional[PasswordExpirationPolicyRuleCondition] = Field(None, alias='passwordExpiration')

    user_lifecycle_attribute: typing.Optional[UserLifecycleAttributePolicyRuleCondition] = Field(None, alias='userLifecycleAttribute')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

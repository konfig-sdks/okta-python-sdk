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

from okta_python_sdk.type.inactivity_policy_rule_condition import InactivityPolicyRuleCondition
from okta_python_sdk.type.lifecycle_expiration_policy_rule_condition import LifecycleExpirationPolicyRuleCondition
from okta_python_sdk.type.password_expiration_policy_rule_condition import PasswordExpirationPolicyRuleCondition
from okta_python_sdk.type.user_lifecycle_attribute_policy_rule_condition import UserLifecycleAttributePolicyRuleCondition
from okta_python_sdk.type.user_policy_rule_condition_exclude import UserPolicyRuleConditionExclude
from okta_python_sdk.type.user_policy_rule_condition_include import UserPolicyRuleConditionInclude

class RequiredUserPolicyRuleCondition(TypedDict):
    pass

class OptionalUserPolicyRuleCondition(TypedDict, total=False):
    exclude: UserPolicyRuleConditionExclude

    inactivity: InactivityPolicyRuleCondition

    include: UserPolicyRuleConditionInclude

    lifecycleExpiration: LifecycleExpirationPolicyRuleCondition

    passwordExpiration: PasswordExpirationPolicyRuleCondition

    userLifecycleAttribute: UserLifecycleAttributePolicyRuleCondition

class UserPolicyRuleCondition(RequiredUserPolicyRuleCondition, OptionalUserPolicyRuleCondition):
    pass

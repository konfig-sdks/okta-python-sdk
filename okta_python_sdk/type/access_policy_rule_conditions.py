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

from okta_python_sdk.type.access_policy_rule_custom_condition import AccessPolicyRuleCustomCondition
from okta_python_sdk.type.device_access_policy_rule_condition import DeviceAccessPolicyRuleCondition
from okta_python_sdk.type.user_type_condition import UserTypeCondition

class RequiredAccessPolicyRuleConditions(TypedDict):
    pass

class OptionalAccessPolicyRuleConditions(TypedDict, total=False):
    device: DeviceAccessPolicyRuleCondition

    elCondition: AccessPolicyRuleCustomCondition

    userType: UserTypeCondition

class AccessPolicyRuleConditions(RequiredAccessPolicyRuleConditions, OptionalAccessPolicyRuleConditions):
    pass

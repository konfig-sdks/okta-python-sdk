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

from okta_python_sdk.type.app_and_instance_condition_evaluator_app_or_instance import AppAndInstanceConditionEvaluatorAppOrInstance

class RequiredAppAndInstancePolicyRuleCondition(TypedDict):
    pass

class OptionalAppAndInstancePolicyRuleCondition(TypedDict, total=False):
    exclude: typing.List[AppAndInstanceConditionEvaluatorAppOrInstance]

    include: typing.List[AppAndInstanceConditionEvaluatorAppOrInstance]

class AppAndInstancePolicyRuleCondition(RequiredAppAndInstancePolicyRuleCondition, OptionalAppAndInstancePolicyRuleCondition):
    pass

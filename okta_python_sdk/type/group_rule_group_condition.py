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

from okta_python_sdk.type.group_rule_group_condition_exclude import GroupRuleGroupConditionExclude
from okta_python_sdk.type.group_rule_group_condition_include import GroupRuleGroupConditionInclude

class RequiredGroupRuleGroupCondition(TypedDict):
    pass

class OptionalGroupRuleGroupCondition(TypedDict, total=False):
    exclude: GroupRuleGroupConditionExclude

    include: GroupRuleGroupConditionInclude

class GroupRuleGroupCondition(RequiredGroupRuleGroupCondition, OptionalGroupRuleGroupCondition):
    pass

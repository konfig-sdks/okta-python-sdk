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

from okta_python_sdk.type.group_rule_action import GroupRuleAction
from okta_python_sdk.type.group_rule_conditions import GroupRuleConditions
from okta_python_sdk.type.group_rule_status import GroupRuleStatus

class RequiredGroupRule(TypedDict):
    pass

class OptionalGroupRule(TypedDict, total=False):
    actions: GroupRuleAction

    conditions: GroupRuleConditions

    created: datetime

    id: str

    lastUpdated: datetime

    name: str

    status: GroupRuleStatus

    type: str

class GroupRule(RequiredGroupRule, OptionalGroupRule):
    pass

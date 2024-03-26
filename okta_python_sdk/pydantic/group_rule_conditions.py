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

from okta_python_sdk.pydantic.group_rule_expression import GroupRuleExpression
from okta_python_sdk.pydantic.group_rule_people_condition import GroupRulePeopleCondition

class GroupRuleConditions(BaseModel):
    expression: typing.Optional[GroupRuleExpression] = Field(None, alias='expression')

    people: typing.Optional[GroupRulePeopleCondition] = Field(None, alias='people')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

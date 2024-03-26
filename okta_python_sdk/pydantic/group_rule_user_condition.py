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

from okta_python_sdk.pydantic.group_rule_user_condition_exclude import GroupRuleUserConditionExclude
from okta_python_sdk.pydantic.group_rule_user_condition_include import GroupRuleUserConditionInclude

class GroupRuleUserCondition(BaseModel):
    exclude: typing.Optional[GroupRuleUserConditionExclude] = Field(None, alias='exclude')

    include: typing.Optional[GroupRuleUserConditionInclude] = Field(None, alias='include')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

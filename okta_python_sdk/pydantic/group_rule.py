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

from okta_python_sdk.pydantic.group_rule_action import GroupRuleAction
from okta_python_sdk.pydantic.group_rule_conditions import GroupRuleConditions
from okta_python_sdk.pydantic.group_rule_status import GroupRuleStatus

class GroupRule(BaseModel):
    actions: typing.Optional[GroupRuleAction] = Field(None, alias='actions')

    conditions: typing.Optional[GroupRuleConditions] = Field(None, alias='conditions')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    status: typing.Optional[GroupRuleStatus] = Field(None, alias='status')

    type: typing.Optional[str] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

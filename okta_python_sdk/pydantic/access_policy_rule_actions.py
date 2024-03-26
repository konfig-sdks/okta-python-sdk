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

from okta_python_sdk.pydantic.access_policy_rule_application_sign_on import AccessPolicyRuleApplicationSignOn

class AccessPolicyRuleActions(BaseModel):
    app_sign_on: typing.Optional[AccessPolicyRuleApplicationSignOn] = Field(None, alias='appSignOn')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

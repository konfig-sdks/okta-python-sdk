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

from okta_python_sdk.pydantic.token_authorization_server_policy_rule_action_inline_hook import TokenAuthorizationServerPolicyRuleActionInlineHook

class TokenAuthorizationServerPolicyRuleAction(BaseModel):
    access_token_lifetime_minutes: typing.Optional[int] = Field(None, alias='accessTokenLifetimeMinutes')

    inline_hook: typing.Optional[TokenAuthorizationServerPolicyRuleActionInlineHook] = Field(None, alias='inlineHook')

    refresh_token_lifetime_minutes: typing.Optional[int] = Field(None, alias='refreshTokenLifetimeMinutes')

    refresh_token_window_minutes: typing.Optional[int] = Field(None, alias='refreshTokenWindowMinutes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

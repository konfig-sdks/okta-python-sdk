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

from okta_python_sdk.pydantic.policy_account_link import PolicyAccountLink
from okta_python_sdk.pydantic.policy_subject import PolicySubject
from okta_python_sdk.pydantic.provisioning import Provisioning

class IdentityProviderPolicy(BaseModel):
    account_link: typing.Optional[PolicyAccountLink] = Field(None, alias='accountLink')

    max_clock_skew: typing.Optional[int] = Field(None, alias='maxClockSkew')

    provisioning: typing.Optional[Provisioning] = Field(None, alias='provisioning')

    subject: typing.Optional[PolicySubject] = Field(None, alias='subject')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

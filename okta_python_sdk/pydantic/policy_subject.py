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

from okta_python_sdk.pydantic.policy_subject_format import PolicySubjectFormat
from okta_python_sdk.pydantic.policy_subject_match_type import PolicySubjectMatchType
from okta_python_sdk.pydantic.policy_user_name_template import PolicyUserNameTemplate

class PolicySubject(BaseModel):
    filter: typing.Optional[str] = Field(None, alias='filter')

    format: typing.Optional[PolicySubjectFormat] = Field(None, alias='format')

    match_attribute: typing.Optional[str] = Field(None, alias='matchAttribute')

    match_type: typing.Optional[PolicySubjectMatchType] = Field(None, alias='matchType')

    user_name_template: typing.Optional[PolicyUserNameTemplate] = Field(None, alias='userNameTemplate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

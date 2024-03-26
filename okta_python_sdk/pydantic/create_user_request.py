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

from okta_python_sdk.pydantic.create_user_request_group_ids import CreateUserRequestGroupIds
from okta_python_sdk.pydantic.user_credentials import UserCredentials
from okta_python_sdk.pydantic.user_profile import UserProfile
from okta_python_sdk.pydantic.user_type import UserType

class CreateUserRequest(BaseModel):
    credentials: typing.Optional[UserCredentials] = Field(None, alias='credentials')

    group_ids: typing.Optional[CreateUserRequestGroupIds] = Field(None, alias='groupIds')

    profile: typing.Optional[UserProfile] = Field(None, alias='profile')

    type: typing.Optional[UserType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

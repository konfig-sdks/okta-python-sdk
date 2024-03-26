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

from okta_python_sdk.type.create_user_request_group_ids import CreateUserRequestGroupIds
from okta_python_sdk.type.user_credentials import UserCredentials
from okta_python_sdk.type.user_profile import UserProfile
from okta_python_sdk.type.user_type import UserType

class RequiredCreateUserRequest(TypedDict):
    pass

class OptionalCreateUserRequest(TypedDict, total=False):
    credentials: UserCredentials

    groupIds: CreateUserRequestGroupIds

    profile: UserProfile

    type: UserType

class CreateUserRequest(RequiredCreateUserRequest, OptionalCreateUserRequest):
    pass

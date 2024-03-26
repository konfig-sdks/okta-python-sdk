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

from okta_python_sdk.type.user_credentials import UserCredentials
from okta_python_sdk.type.user_embedded import UserEmbedded
from okta_python_sdk.type.user_links import UserLinks
from okta_python_sdk.type.user_profile import UserProfile
from okta_python_sdk.type.user_status import UserStatus
from okta_python_sdk.type.user_type import UserType

class RequiredUser(TypedDict):
    pass

class OptionalUser(TypedDict, total=False):
    _embedded: UserEmbedded

    _links: UserLinks

    activated: datetime

    created: datetime

    credentials: UserCredentials

    id: str

    lastLogin: datetime

    lastUpdated: datetime

    passwordChanged: datetime

    profile: UserProfile

    status: UserStatus

    statusChanged: datetime

    transitioningToStatus: UserStatus

    type: UserType

class User(RequiredUser, OptionalUser):
    pass

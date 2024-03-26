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

from okta_python_sdk.type.app_user_credentials import AppUserCredentials
from okta_python_sdk.type.app_user_embedded import AppUserEmbedded
from okta_python_sdk.type.app_user_links import AppUserLinks
from okta_python_sdk.type.app_user_profile import AppUserProfile

class RequiredAppUser(TypedDict):
    pass

class OptionalAppUser(TypedDict, total=False):
    _embedded: AppUserEmbedded

    _links: AppUserLinks

    created: datetime

    credentials: AppUserCredentials

    externalId: str

    id: str

    lastSync: datetime

    lastUpdated: datetime

    passwordChanged: datetime

    profile: AppUserProfile

    scope: str

    status: str

    statusChanged: datetime

    syncState: str

class AppUser(RequiredAppUser, OptionalAppUser):
    pass

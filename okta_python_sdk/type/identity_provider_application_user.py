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

from okta_python_sdk.type.identity_provider_application_user_embedded import IdentityProviderApplicationUserEmbedded
from okta_python_sdk.type.identity_provider_application_user_links import IdentityProviderApplicationUserLinks
from okta_python_sdk.type.identity_provider_application_user_profile import IdentityProviderApplicationUserProfile

class RequiredIdentityProviderApplicationUser(TypedDict):
    pass

class OptionalIdentityProviderApplicationUser(TypedDict, total=False):
    _embedded: IdentityProviderApplicationUserEmbedded

    _links: IdentityProviderApplicationUserLinks

    created: str

    externalId: str

    id: str

    lastUpdated: str

    profile: IdentityProviderApplicationUserProfile

class IdentityProviderApplicationUser(RequiredIdentityProviderApplicationUser, OptionalIdentityProviderApplicationUser):
    pass

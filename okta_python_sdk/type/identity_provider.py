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

from okta_python_sdk.type.identity_provider_links import IdentityProviderLinks
from okta_python_sdk.type.identity_provider_policy import IdentityProviderPolicy
from okta_python_sdk.type.protocol import Protocol

class RequiredIdentityProvider(TypedDict):
    pass

class OptionalIdentityProvider(TypedDict, total=False):
    _links: IdentityProviderLinks

    created: datetime

    id: str

    issuerMode: str

    lastUpdated: datetime

    name: str

    policy: IdentityProviderPolicy

    protocol: Protocol

    status: str

    type: str

class IdentityProvider(RequiredIdentityProvider, OptionalIdentityProvider):
    pass

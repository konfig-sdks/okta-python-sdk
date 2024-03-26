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

from okta_python_sdk.type.authenticator_links import AuthenticatorLinks
from okta_python_sdk.type.authenticator_provider import AuthenticatorProvider
from okta_python_sdk.type.authenticator_settings import AuthenticatorSettings
from okta_python_sdk.type.authenticator_status import AuthenticatorStatus
from okta_python_sdk.type.authenticator_type import AuthenticatorType

class RequiredAuthenticator(TypedDict):
    pass

class OptionalAuthenticator(TypedDict, total=False):
    _links: AuthenticatorLinks

    created: datetime

    id: str

    key: str

    lastUpdated: datetime

    name: str

    provider: AuthenticatorProvider

    settings: AuthenticatorSettings

    status: AuthenticatorStatus

    type: AuthenticatorType

class Authenticator(RequiredAuthenticator, OptionalAuthenticator):
    pass

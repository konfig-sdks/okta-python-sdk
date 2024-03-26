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

from okta_python_sdk.type.authorization_server_audiences import AuthorizationServerAudiences
from okta_python_sdk.type.authorization_server_credentials import AuthorizationServerCredentials
from okta_python_sdk.type.authorization_server_links import AuthorizationServerLinks

class RequiredAuthorizationServer(TypedDict):
    pass

class OptionalAuthorizationServer(TypedDict, total=False):
    description: str

    _links: AuthorizationServerLinks

    audiences: AuthorizationServerAudiences

    created: datetime

    credentials: AuthorizationServerCredentials

    default: bool

    id: str

    issuer: str

    issuerMode: str

    lastUpdated: datetime

    name: str

    status: str

class AuthorizationServer(RequiredAuthorizationServer, OptionalAuthorizationServer):
    pass

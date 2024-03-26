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

from okta_python_sdk.type.session_authentication_method import SessionAuthenticationMethod
from okta_python_sdk.type.session_identity_provider import SessionIdentityProvider
from okta_python_sdk.type.session_links import SessionLinks
from okta_python_sdk.type.session_status import SessionStatus

class RequiredSession(TypedDict):
    pass

class OptionalSession(TypedDict, total=False):
    _links: SessionLinks

    amr: typing.List[SessionAuthenticationMethod]

    createdAt: datetime

    expiresAt: datetime

    id: str

    idp: SessionIdentityProvider

    lastFactorVerification: datetime

    lastPasswordVerification: datetime

    login: str

    status: SessionStatus

    userId: str

class Session(RequiredSession, OptionalSession):
    pass

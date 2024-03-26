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

from okta_python_sdk.pydantic.session_authentication_method import SessionAuthenticationMethod
from okta_python_sdk.pydantic.session_identity_provider import SessionIdentityProvider
from okta_python_sdk.pydantic.session_links import SessionLinks
from okta_python_sdk.pydantic.session_status import SessionStatus

class Session(BaseModel):
    _links: typing.Optional[SessionLinks] = Field(None, alias='_links')

    amr: typing.Optional[typing.List[SessionAuthenticationMethod]] = Field(None, alias='amr')

    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    expires_at: typing.Optional[datetime] = Field(None, alias='expiresAt')

    id: typing.Optional[str] = Field(None, alias='id')

    idp: typing.Optional[SessionIdentityProvider] = Field(None, alias='idp')

    last_factor_verification: typing.Optional[datetime] = Field(None, alias='lastFactorVerification')

    last_password_verification: typing.Optional[datetime] = Field(None, alias='lastPasswordVerification')

    login: typing.Optional[str] = Field(None, alias='login')

    status: typing.Optional[SessionStatus] = Field(None, alias='status')

    user_id: typing.Optional[str] = Field(None, alias='userId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

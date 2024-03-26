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

from okta_python_sdk.pydantic.authenticator_links import AuthenticatorLinks
from okta_python_sdk.pydantic.authenticator_provider import AuthenticatorProvider
from okta_python_sdk.pydantic.authenticator_settings import AuthenticatorSettings
from okta_python_sdk.pydantic.authenticator_status import AuthenticatorStatus
from okta_python_sdk.pydantic.authenticator_type import AuthenticatorType

class Authenticator(BaseModel):
    _links: typing.Optional[AuthenticatorLinks] = Field(None, alias='_links')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    key: typing.Optional[str] = Field(None, alias='key')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    provider: typing.Optional[AuthenticatorProvider] = Field(None, alias='provider')

    settings: typing.Optional[AuthenticatorSettings] = Field(None, alias='settings')

    status: typing.Optional[AuthenticatorStatus] = Field(None, alias='status')

    type: typing.Optional[AuthenticatorType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

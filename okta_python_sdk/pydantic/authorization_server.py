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

from okta_python_sdk.pydantic.authorization_server_audiences import AuthorizationServerAudiences
from okta_python_sdk.pydantic.authorization_server_credentials import AuthorizationServerCredentials
from okta_python_sdk.pydantic.authorization_server_links import AuthorizationServerLinks

class AuthorizationServer(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    _links: typing.Optional[AuthorizationServerLinks] = Field(None, alias='_links')

    audiences: typing.Optional[AuthorizationServerAudiences] = Field(None, alias='audiences')

    created: typing.Optional[datetime] = Field(None, alias='created')

    credentials: typing.Optional[AuthorizationServerCredentials] = Field(None, alias='credentials')

    default: typing.Optional[bool] = Field(None, alias='default')

    id: typing.Optional[str] = Field(None, alias='id')

    issuer: typing.Optional[str] = Field(None, alias='issuer')

    issuer_mode: typing.Optional[Literal["ORG_URL", "CUSTOM_URL", "DYNAMIC"]] = Field(None, alias='issuerMode')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

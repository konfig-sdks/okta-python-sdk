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

from okta_python_sdk.pydantic.o_auth2_actor import OAuth2Actor
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_embedded import OAuth2ScopeConsentGrantEmbedded
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_links import OAuth2ScopeConsentGrantLinks
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_source import OAuth2ScopeConsentGrantSource
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_status import OAuth2ScopeConsentGrantStatus

class OAuth2ScopeConsentGrant(BaseModel):
    _embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[OAuth2ScopeConsentGrantLinks] = Field(None, alias='_links')

    client_id: typing.Optional[str] = Field(None, alias='clientId')

    created: typing.Optional[datetime] = Field(None, alias='created')

    created_by: typing.Optional[OAuth2Actor] = Field(None, alias='createdBy')

    id: typing.Optional[str] = Field(None, alias='id')

    issuer: typing.Optional[str] = Field(None, alias='issuer')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    scope_id: typing.Optional[str] = Field(None, alias='scopeId')

    source: typing.Optional[OAuth2ScopeConsentGrantSource] = Field(None, alias='source')

    status: typing.Optional[OAuth2ScopeConsentGrantStatus] = Field(None, alias='status')

    user_id: typing.Optional[str] = Field(None, alias='userId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

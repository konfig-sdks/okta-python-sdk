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

from okta_python_sdk.type.o_auth2_actor import OAuth2Actor
from okta_python_sdk.type.o_auth2_scope_consent_grant_embedded import OAuth2ScopeConsentGrantEmbedded
from okta_python_sdk.type.o_auth2_scope_consent_grant_links import OAuth2ScopeConsentGrantLinks
from okta_python_sdk.type.o_auth2_scope_consent_grant_source import OAuth2ScopeConsentGrantSource
from okta_python_sdk.type.o_auth2_scope_consent_grant_status import OAuth2ScopeConsentGrantStatus

class RequiredOAuth2ScopeConsentGrant(TypedDict):
    pass

class OptionalOAuth2ScopeConsentGrant(TypedDict, total=False):
    _embedded: OAuth2ScopeConsentGrantEmbedded

    _links: OAuth2ScopeConsentGrantLinks

    clientId: str

    created: datetime

    createdBy: OAuth2Actor

    id: str

    issuer: str

    lastUpdated: datetime

    scopeId: str

    source: OAuth2ScopeConsentGrantSource

    status: OAuth2ScopeConsentGrantStatus

    userId: str

class OAuth2ScopeConsentGrant(RequiredOAuth2ScopeConsentGrant, OptionalOAuth2ScopeConsentGrant):
    pass

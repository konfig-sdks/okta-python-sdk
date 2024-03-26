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

from okta_python_sdk.pydantic.identity_provider_links import IdentityProviderLinks
from okta_python_sdk.pydantic.identity_provider_policy import IdentityProviderPolicy
from okta_python_sdk.pydantic.protocol import Protocol

class IdentityProvider(BaseModel):
    _links: typing.Optional[IdentityProviderLinks] = Field(None, alias='_links')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    issuer_mode: typing.Optional[Literal["ORG_URL", "CUSTOM_URL", "DYNAMIC"]] = Field(None, alias='issuerMode')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    policy: typing.Optional[IdentityProviderPolicy] = Field(None, alias='policy')

    protocol: typing.Optional[Protocol] = Field(None, alias='protocol')

    status: typing.Optional[Literal["ACTIVE", "INACTIVE"]] = Field(None, alias='status')

    type: typing.Optional[Literal["SAML2", "GOOGLE", "FACEBOOK", "LINKEDIN", "MICROSOFT", "OIDC", "OKTA", "IWA", "AgentlessDSSO", "X509"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

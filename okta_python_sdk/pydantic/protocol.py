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

from okta_python_sdk.pydantic.identity_provider_credentials import IdentityProviderCredentials
from okta_python_sdk.pydantic.protocol_algorithms import ProtocolAlgorithms
from okta_python_sdk.pydantic.protocol_endpoint import ProtocolEndpoint
from okta_python_sdk.pydantic.protocol_endpoints import ProtocolEndpoints
from okta_python_sdk.pydantic.protocol_relay_state import ProtocolRelayState
from okta_python_sdk.pydantic.protocol_scopes import ProtocolScopes
from okta_python_sdk.pydantic.protocol_settings import ProtocolSettings

class Protocol(BaseModel):
    algorithms: typing.Optional[ProtocolAlgorithms] = Field(None, alias='algorithms')

    credentials: typing.Optional[IdentityProviderCredentials] = Field(None, alias='credentials')

    endpoints: typing.Optional[ProtocolEndpoints] = Field(None, alias='endpoints')

    issuer: typing.Optional[ProtocolEndpoint] = Field(None, alias='issuer')

    relay_state: typing.Optional[ProtocolRelayState] = Field(None, alias='relayState')

    scopes: typing.Optional[ProtocolScopes] = Field(None, alias='scopes')

    settings: typing.Optional[ProtocolSettings] = Field(None, alias='settings')

    type: typing.Optional[Literal["SAML2", "OIDC", "OAUTH2", "MTLS"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

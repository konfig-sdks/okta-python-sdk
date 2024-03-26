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

from okta_python_sdk.type.identity_provider_credentials import IdentityProviderCredentials
from okta_python_sdk.type.protocol_algorithms import ProtocolAlgorithms
from okta_python_sdk.type.protocol_endpoint import ProtocolEndpoint
from okta_python_sdk.type.protocol_endpoints import ProtocolEndpoints
from okta_python_sdk.type.protocol_relay_state import ProtocolRelayState
from okta_python_sdk.type.protocol_scopes import ProtocolScopes
from okta_python_sdk.type.protocol_settings import ProtocolSettings

class RequiredProtocol(TypedDict):
    pass

class OptionalProtocol(TypedDict, total=False):
    algorithms: ProtocolAlgorithms

    credentials: IdentityProviderCredentials

    endpoints: ProtocolEndpoints

    issuer: ProtocolEndpoint

    relayState: ProtocolRelayState

    scopes: ProtocolScopes

    settings: ProtocolSettings

    type: str

class Protocol(RequiredProtocol, OptionalProtocol):
    pass

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

from okta_python_sdk.type.o_auth_grant_type import OAuthGrantType
from okta_python_sdk.type.o_auth_response_type import OAuthResponseType
from okta_python_sdk.type.open_id_connect_application_consent_method import OpenIdConnectApplicationConsentMethod
from okta_python_sdk.type.open_id_connect_application_idp_initiated_login import OpenIdConnectApplicationIdpInitiatedLogin
from okta_python_sdk.type.open_id_connect_application_issuer_mode import OpenIdConnectApplicationIssuerMode
from okta_python_sdk.type.open_id_connect_application_settings_client_keys import OpenIdConnectApplicationSettingsClientKeys
from okta_python_sdk.type.open_id_connect_application_settings_refresh_token import OpenIdConnectApplicationSettingsRefreshToken
from okta_python_sdk.type.open_id_connect_application_type import OpenIdConnectApplicationType

class RequiredOpenIdConnectApplicationSettingsClient(TypedDict):
    pass

class OptionalOpenIdConnectApplicationSettingsClient(TypedDict, total=False):
    application_type: OpenIdConnectApplicationType

    client_uri: str

    consent_method: OpenIdConnectApplicationConsentMethod

    grant_types: typing.List[OAuthGrantType]

    idp_initiated_login: OpenIdConnectApplicationIdpInitiatedLogin

    initiate_login_uri: str

    issuer_mode: OpenIdConnectApplicationIssuerMode

    jwks: OpenIdConnectApplicationSettingsClientKeys

    logo_uri: str

    policy_uri: str

    post_logout_redirect_uris: typing.List[str]

    redirect_uris: typing.List[str]

    refresh_token: OpenIdConnectApplicationSettingsRefreshToken

    response_types: typing.List[OAuthResponseType]

    tos_uri: str

    wildcard_redirect: str

class OpenIdConnectApplicationSettingsClient(RequiredOpenIdConnectApplicationSettingsClient, OptionalOpenIdConnectApplicationSettingsClient):
    pass

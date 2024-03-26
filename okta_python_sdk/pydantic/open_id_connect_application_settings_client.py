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

from okta_python_sdk.pydantic.o_auth_grant_type import OAuthGrantType
from okta_python_sdk.pydantic.o_auth_response_type import OAuthResponseType
from okta_python_sdk.pydantic.open_id_connect_application_consent_method import OpenIdConnectApplicationConsentMethod
from okta_python_sdk.pydantic.open_id_connect_application_idp_initiated_login import OpenIdConnectApplicationIdpInitiatedLogin
from okta_python_sdk.pydantic.open_id_connect_application_issuer_mode import OpenIdConnectApplicationIssuerMode
from okta_python_sdk.pydantic.open_id_connect_application_settings_client_keys import OpenIdConnectApplicationSettingsClientKeys
from okta_python_sdk.pydantic.open_id_connect_application_settings_refresh_token import OpenIdConnectApplicationSettingsRefreshToken
from okta_python_sdk.pydantic.open_id_connect_application_type import OpenIdConnectApplicationType

class OpenIdConnectApplicationSettingsClient(BaseModel):
    application_type: typing.Optional[OpenIdConnectApplicationType] = Field(None, alias='application_type')

    client_uri: typing.Optional[str] = Field(None, alias='client_uri')

    consent_method: typing.Optional[OpenIdConnectApplicationConsentMethod] = Field(None, alias='consent_method')

    grant_types: typing.Optional[typing.List[OAuthGrantType]] = Field(None, alias='grant_types')

    idp_initiated_login: typing.Optional[OpenIdConnectApplicationIdpInitiatedLogin] = Field(None, alias='idp_initiated_login')

    initiate_login_uri: typing.Optional[str] = Field(None, alias='initiate_login_uri')

    issuer_mode: typing.Optional[OpenIdConnectApplicationIssuerMode] = Field(None, alias='issuer_mode')

    jwks: typing.Optional[OpenIdConnectApplicationSettingsClientKeys] = Field(None, alias='jwks')

    logo_uri: typing.Optional[str] = Field(None, alias='logo_uri')

    policy_uri: typing.Optional[str] = Field(None, alias='policy_uri')

    post_logout_redirect_uris: typing.Optional[typing.List[str]] = Field(None, alias='post_logout_redirect_uris')

    redirect_uris: typing.Optional[typing.List[str]] = Field(None, alias='redirect_uris')

    refresh_token: typing.Optional[OpenIdConnectApplicationSettingsRefreshToken] = Field(None, alias='refresh_token')

    response_types: typing.Optional[typing.List[OAuthResponseType]] = Field(None, alias='response_types')

    tos_uri: typing.Optional[str] = Field(None, alias='tos_uri')

    wildcard_redirect: typing.Optional[str] = Field(None, alias='wildcard_redirect')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

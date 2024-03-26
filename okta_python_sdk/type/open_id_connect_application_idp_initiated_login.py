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

from okta_python_sdk.type.open_id_connect_application_idp_initiated_login_default_scope import OpenIdConnectApplicationIdpInitiatedLoginDefaultScope

class RequiredOpenIdConnectApplicationIdpInitiatedLogin(TypedDict):
    pass

class OptionalOpenIdConnectApplicationIdpInitiatedLogin(TypedDict, total=False):
    default_scope: OpenIdConnectApplicationIdpInitiatedLoginDefaultScope

    mode: str

class OpenIdConnectApplicationIdpInitiatedLogin(RequiredOpenIdConnectApplicationIdpInitiatedLogin, OptionalOpenIdConnectApplicationIdpInitiatedLogin):
    pass

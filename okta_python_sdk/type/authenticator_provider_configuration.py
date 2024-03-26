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

from okta_python_sdk.type.authenticator_provider_configuration_user_name_plate import AuthenticatorProviderConfigurationUserNamePlate

class RequiredAuthenticatorProviderConfiguration(TypedDict):
    pass

class OptionalAuthenticatorProviderConfiguration(TypedDict, total=False):
    authPort: int

    host: str

    hostName: str

    instanceId: str

    integrationKey: str

    secretKey: str

    sharedSecret: str

    userNameTemplate: AuthenticatorProviderConfigurationUserNamePlate

class AuthenticatorProviderConfiguration(RequiredAuthenticatorProviderConfiguration, OptionalAuthenticatorProviderConfiguration):
    pass

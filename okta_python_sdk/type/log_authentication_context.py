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

from okta_python_sdk.type.log_authentication_provider import LogAuthenticationProvider
from okta_python_sdk.type.log_credential_provider import LogCredentialProvider
from okta_python_sdk.type.log_credential_type import LogCredentialType
from okta_python_sdk.type.log_issuer import LogIssuer

class RequiredLogAuthenticationContext(TypedDict):
    pass

class OptionalLogAuthenticationContext(TypedDict, total=False):
    authenticationProvider: LogAuthenticationProvider

    authenticationStep: int

    credentialProvider: LogCredentialProvider

    credentialType: LogCredentialType

    externalSessionId: str

    interface: str

    issuer: LogIssuer

class LogAuthenticationContext(RequiredLogAuthenticationContext, OptionalLogAuthenticationContext):
    pass

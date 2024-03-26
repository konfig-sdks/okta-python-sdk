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

from okta_python_sdk.type.identity_provider_credentials_client import IdentityProviderCredentialsClient
from okta_python_sdk.type.identity_provider_credentials_signing import IdentityProviderCredentialsSigning
from okta_python_sdk.type.identity_provider_credentials_trust import IdentityProviderCredentialsTrust

class RequiredIdentityProviderCredentials(TypedDict):
    pass

class OptionalIdentityProviderCredentials(TypedDict, total=False):
    client: IdentityProviderCredentialsClient

    signing: IdentityProviderCredentialsSigning

    trust: IdentityProviderCredentialsTrust

class IdentityProviderCredentials(RequiredIdentityProviderCredentials, OptionalIdentityProviderCredentials):
    pass

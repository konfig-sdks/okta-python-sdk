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

from okta_python_sdk.pydantic.log_authentication_provider import LogAuthenticationProvider
from okta_python_sdk.pydantic.log_credential_provider import LogCredentialProvider
from okta_python_sdk.pydantic.log_credential_type import LogCredentialType
from okta_python_sdk.pydantic.log_issuer import LogIssuer

class LogAuthenticationContext(BaseModel):
    authentication_provider: typing.Optional[LogAuthenticationProvider] = Field(None, alias='authenticationProvider')

    authentication_step: typing.Optional[int] = Field(None, alias='authenticationStep')

    credential_provider: typing.Optional[LogCredentialProvider] = Field(None, alias='credentialProvider')

    credential_type: typing.Optional[LogCredentialType] = Field(None, alias='credentialType')

    external_session_id: typing.Optional[str] = Field(None, alias='externalSessionId')

    interface: typing.Optional[str] = Field(None, alias='interface')

    issuer: typing.Optional[LogIssuer] = Field(None, alias='issuer')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

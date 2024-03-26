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

from okta_python_sdk.pydantic.authenticator_provider_configuration_user_name_plate import AuthenticatorProviderConfigurationUserNamePlate

class AuthenticatorProviderConfiguration(BaseModel):
    auth_port: typing.Optional[int] = Field(None, alias='authPort')

    host: typing.Optional[str] = Field(None, alias='host')

    host_name: typing.Optional[str] = Field(None, alias='hostName')

    instance_id: typing.Optional[str] = Field(None, alias='instanceId')

    integration_key: typing.Optional[str] = Field(None, alias='integrationKey')

    secret_key: typing.Optional[str] = Field(None, alias='secretKey')

    shared_secret: typing.Optional[str] = Field(None, alias='sharedSecret')

    user_name_template: typing.Optional[AuthenticatorProviderConfigurationUserNamePlate] = Field(None, alias='userNameTemplate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

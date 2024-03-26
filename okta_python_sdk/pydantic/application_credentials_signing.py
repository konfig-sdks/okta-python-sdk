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

from okta_python_sdk.pydantic.application_credentials_signing_use import ApplicationCredentialsSigningUse

class ApplicationCredentialsSigning(BaseModel):
    kid: typing.Optional[str] = Field(None, alias='kid')

    last_rotated: typing.Optional[datetime] = Field(None, alias='lastRotated')

    next_rotation: typing.Optional[datetime] = Field(None, alias='nextRotation')

    rotation_mode: typing.Optional[str] = Field(None, alias='rotationMode')

    use: typing.Optional[ApplicationCredentialsSigningUse] = Field(None, alias='use')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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


class ActivateFactorRequest(BaseModel):
    attestation: typing.Optional[str] = Field(None, alias='attestation')

    client_data: typing.Optional[str] = Field(None, alias='clientData')

    pass_code: typing.Optional[str] = Field(None, alias='passCode')

    registration_data: typing.Optional[str] = Field(None, alias='registrationData')

    state_token: typing.Optional[str] = Field(None, alias='stateToken')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

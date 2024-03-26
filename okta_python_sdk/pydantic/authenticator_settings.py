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

from okta_python_sdk.pydantic.allowed_for_enum import AllowedForEnum
from okta_python_sdk.pydantic.channel_binding import ChannelBinding
from okta_python_sdk.pydantic.compliance import Compliance
from okta_python_sdk.pydantic.user_verification_enum import UserVerificationEnum

class AuthenticatorSettings(BaseModel):
    allowed_for: typing.Optional[AllowedForEnum] = Field(None, alias='allowedFor')

    app_instance_id: typing.Optional[str] = Field(None, alias='appInstanceId')

    channel_binding: typing.Optional[ChannelBinding] = Field(None, alias='channelBinding')

    compliance: typing.Optional[Compliance] = Field(None, alias='compliance')

    token_lifetime_in_minutes: typing.Optional[int] = Field(None, alias='tokenLifetimeInMinutes')

    user_verification: typing.Optional[UserVerificationEnum] = Field(None, alias='userVerification')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

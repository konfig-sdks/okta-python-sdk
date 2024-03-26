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

from okta_python_sdk.type.allowed_for_enum import AllowedForEnum
from okta_python_sdk.type.channel_binding import ChannelBinding
from okta_python_sdk.type.compliance import Compliance
from okta_python_sdk.type.user_verification_enum import UserVerificationEnum

class RequiredAuthenticatorSettings(TypedDict):
    pass

class OptionalAuthenticatorSettings(TypedDict, total=False):
    allowedFor: AllowedForEnum

    appInstanceId: str

    channelBinding: ChannelBinding

    compliance: Compliance

    tokenLifetimeInMinutes: int

    userVerification: UserVerificationEnum

class AuthenticatorSettings(RequiredAuthenticatorSettings, OptionalAuthenticatorSettings):
    pass

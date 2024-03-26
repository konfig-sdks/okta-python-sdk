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

from okta_python_sdk.pydantic.verify_user_factor_response_embedded import VerifyUserFactorResponseEmbedded
from okta_python_sdk.pydantic.verify_user_factor_response_links import VerifyUserFactorResponseLinks

class VerifyUserFactorResponse(BaseModel):
    _embedded: typing.Optional[VerifyUserFactorResponseEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[VerifyUserFactorResponseLinks] = Field(None, alias='_links')

    expires_at: typing.Optional[datetime] = Field(None, alias='expiresAt')

    factor_result: typing.Optional[Literal["SUCCESS", "EXPIRED", "CHALLENGE", "WAITING", "FAILED", "REJECTED", "TIMEOUT", "TIME_WINDOW_EXCEEDED", "PASSCODE_REPLAYED", "ERROR"]] = Field(None, alias='factorResult')

    factor_result_message: typing.Optional[str] = Field(None, alias='factorResultMessage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

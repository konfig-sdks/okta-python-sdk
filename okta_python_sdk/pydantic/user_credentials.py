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

from okta_python_sdk.pydantic.authentication_provider import AuthenticationProvider
from okta_python_sdk.pydantic.password_credential import PasswordCredential
from okta_python_sdk.pydantic.recovery_question_credential import RecoveryQuestionCredential

class UserCredentials(BaseModel):
    password: typing.Optional[PasswordCredential] = Field(None, alias='password')

    provider: typing.Optional[AuthenticationProvider] = Field(None, alias='provider')

    recovery_question: typing.Optional[RecoveryQuestionCredential] = Field(None, alias='recovery_question')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.type.authentication_provider import AuthenticationProvider
from okta_python_sdk.type.password_credential import PasswordCredential
from okta_python_sdk.type.recovery_question_credential import RecoveryQuestionCredential

class RequiredUserCredentials(TypedDict):
    pass

class OptionalUserCredentials(TypedDict, total=False):
    password: PasswordCredential

    provider: AuthenticationProvider

    recovery_question: RecoveryQuestionCredential

class UserCredentials(RequiredUserCredentials, OptionalUserCredentials):
    pass

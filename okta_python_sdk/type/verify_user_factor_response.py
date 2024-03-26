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

from okta_python_sdk.type.verify_user_factor_response_embedded import VerifyUserFactorResponseEmbedded
from okta_python_sdk.type.verify_user_factor_response_links import VerifyUserFactorResponseLinks

class RequiredVerifyUserFactorResponse(TypedDict):
    pass

class OptionalVerifyUserFactorResponse(TypedDict, total=False):
    _embedded: VerifyUserFactorResponseEmbedded

    _links: VerifyUserFactorResponseLinks

    expiresAt: datetime

    factorResult: str

    factorResultMessage: str

class VerifyUserFactorResponse(RequiredVerifyUserFactorResponse, OptionalVerifyUserFactorResponse):
    pass

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

from okta_python_sdk.type.o_auth2_claim_conditions_scopes import OAuth2ClaimConditionsScopes

class RequiredOAuth2ClaimConditions(TypedDict):
    pass

class OptionalOAuth2ClaimConditions(TypedDict, total=False):
    scopes: OAuth2ClaimConditionsScopes

class OAuth2ClaimConditions(RequiredOAuth2ClaimConditions, OptionalOAuth2ClaimConditions):
    pass

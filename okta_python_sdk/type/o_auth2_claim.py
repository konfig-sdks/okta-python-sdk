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

from okta_python_sdk.type.o_auth2_claim_conditions import OAuth2ClaimConditions
from okta_python_sdk.type.o_auth2_claim_links import OAuth2ClaimLinks

class RequiredOAuth2Claim(TypedDict):
    pass

class OptionalOAuth2Claim(TypedDict, total=False):
    _links: OAuth2ClaimLinks

    alwaysIncludeInToken: bool

    claimType: str

    conditions: OAuth2ClaimConditions

    group_filter_type: str

    id: str

    name: str

    status: str

    system: bool

    value: str

    valueType: str

class OAuth2Claim(RequiredOAuth2Claim, OptionalOAuth2Claim):
    pass

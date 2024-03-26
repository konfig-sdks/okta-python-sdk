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


class RequiredOAuth2Scope(TypedDict):
    pass

class OptionalOAuth2Scope(TypedDict, total=False):
    description: str

    consent: str

    default: bool

    displayName: str

    id: str

    metadataPublish: str

    name: str

    system: bool

class OAuth2Scope(RequiredOAuth2Scope, OptionalOAuth2Scope):
    pass

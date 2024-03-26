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

from okta_python_sdk.type.iframe_embed_scope_allowed_apps import IframeEmbedScopeAllowedApps
from okta_python_sdk.type.scope_type import ScopeType

class RequiredScope(TypedDict):
    pass

class OptionalScope(TypedDict, total=False):
    allowedOktaApps: typing.List[IframeEmbedScopeAllowedApps]

    stringValue: str

    type: ScopeType

class Scope(RequiredScope, OptionalScope):
    pass

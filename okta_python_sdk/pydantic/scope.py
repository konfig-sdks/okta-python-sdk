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

from okta_python_sdk.pydantic.iframe_embed_scope_allowed_apps import IframeEmbedScopeAllowedApps
from okta_python_sdk.pydantic.scope_type import ScopeType

class Scope(BaseModel):
    allowed_okta_apps: typing.Optional[typing.List[IframeEmbedScopeAllowedApps]] = Field(None, alias='allowedOktaApps')

    string_value: typing.Optional[str] = Field(None, alias='stringValue')

    type: typing.Optional[ScopeType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

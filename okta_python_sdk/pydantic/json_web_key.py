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

from okta_python_sdk.pydantic.json_web_key_key_ops import JsonWebKeyKeyOps
from okta_python_sdk.pydantic.json_web_key_links import JsonWebKeyLinks
from okta_python_sdk.pydantic.json_web_key_x5_c import JsonWebKeyX5C

class JsonWebKey(BaseModel):
    _links: typing.Optional[JsonWebKeyLinks] = Field(None, alias='_links')

    alg: typing.Optional[str] = Field(None, alias='alg')

    created: typing.Optional[datetime] = Field(None, alias='created')

    e: typing.Optional[str] = Field(None, alias='e')

    expires_at: typing.Optional[datetime] = Field(None, alias='expiresAt')

    key_ops: typing.Optional[JsonWebKeyKeyOps] = Field(None, alias='key_ops')

    kid: typing.Optional[str] = Field(None, alias='kid')

    kty: typing.Optional[str] = Field(None, alias='kty')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    n: typing.Optional[str] = Field(None, alias='n')

    status: typing.Optional[str] = Field(None, alias='status')

    use: typing.Optional[str] = Field(None, alias='use')

    x5c: typing.Optional[JsonWebKeyX5C] = Field(None, alias='x5c')

    x5t: typing.Optional[str] = Field(None, alias='x5t')

    x5t#_s256_: typing.Optional[str] = Field(None, alias='x5t#S256')

    x5u: typing.Optional[str] = Field(None, alias='x5u')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

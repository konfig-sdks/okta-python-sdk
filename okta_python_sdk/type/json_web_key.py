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

from okta_python_sdk.type.json_web_key_key_ops import JsonWebKeyKeyOps
from okta_python_sdk.type.json_web_key_links import JsonWebKeyLinks
from okta_python_sdk.type.json_web_key_x5_c import JsonWebKeyX5C

RequiredJsonWebKey = TypedDict("RequiredJsonWebKey", {
    })

OptionalJsonWebKey = TypedDict("OptionalJsonWebKey", {
    "_links": JsonWebKeyLinks,

    "alg": str,

    "created": datetime,

    "e": str,

    "expiresAt": datetime,

    "key_ops": JsonWebKeyKeyOps,

    "kid": str,

    "kty": str,

    "lastUpdated": datetime,

    "n": str,

    "status": str,

    "use": str,

    "x5c": JsonWebKeyX5C,

    "x5t": str,

    "x5t#S256": str,

    "x5u": str,
    }, total=False)

class JsonWebKey(RequiredJsonWebKey, OptionalJsonWebKey):
    pass

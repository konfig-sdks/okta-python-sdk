# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from okta_python_sdk import schemas  # noqa: F401


class OAuthEndpointAuthenticationMethod(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "none": "NONE",
            "client_secret_post": "CLIENT_SECRET_POST",
            "client_secret_basic": "CLIENT_SECRET_BASIC",
            "client_secret_jwt": "CLIENT_SECRET_JWT",
            "private_key_jwt": "PRIVATE_KEY_JWT",
        }
    
    @schemas.classproperty
    def NONE(cls):
        return cls("none")
    
    @schemas.classproperty
    def CLIENT_SECRET_POST(cls):
        return cls("client_secret_post")
    
    @schemas.classproperty
    def CLIENT_SECRET_BASIC(cls):
        return cls("client_secret_basic")
    
    @schemas.classproperty
    def CLIENT_SECRET_JWT(cls):
        return cls("client_secret_jwt")
    
    @schemas.classproperty
    def PRIVATE_KEY_JWT(cls):
        return cls("private_key_jwt")

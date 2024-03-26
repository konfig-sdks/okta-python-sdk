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


class OAuthGrantType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def AUTHORIZATION_CODE(cls):
        return cls("authorization_code")
    
    @schemas.classproperty
    def IMPLICIT(cls):
        return cls("implicit")
    
    @schemas.classproperty
    def PASSWORD(cls):
        return cls("password")
    
    @schemas.classproperty
    def REFRESH_TOKEN(cls):
        return cls("refresh_token")
    
    @schemas.classproperty
    def CLIENT_CREDENTIALS(cls):
        return cls("client_credentials")
    
    @schemas.classproperty
    def SAML2_BEARER(cls):
        return cls("saml2_bearer")
    
    @schemas.classproperty
    def DEVICE_CODE(cls):
        return cls("device_code")
    
    @schemas.classproperty
    def TOKEN_EXCHANGE(cls):
        return cls("token_exchange")
    
    @schemas.classproperty
    def INTERACTION_CODE(cls):
        return cls("interaction_code")

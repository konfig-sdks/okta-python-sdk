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


class FactorType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def CALL(cls):
        return cls("call")
    
    @schemas.classproperty
    def EMAIL(cls):
        return cls("email")
    
    @schemas.classproperty
    def HOTP(cls):
        return cls("hotp")
    
    @schemas.classproperty
    def PUSH(cls):
        return cls("push")
    
    @schemas.classproperty
    def QUESTION(cls):
        return cls("question")
    
    @schemas.classproperty
    def SIGNED_NONCE(cls):
        return cls("signed_nonce")
    
    @schemas.classproperty
    def SMS(cls):
        return cls("sms")
    
    @schemas.classproperty
    def TOKENHARDWARE(cls):
        return cls("token:hardware")
    
    @schemas.classproperty
    def TOKENHOTP(cls):
        return cls("token:hotp")
    
    @schemas.classproperty
    def TOKENSOFTWARETOTP(cls):
        return cls("token:software:totp")
    
    @schemas.classproperty
    def TOKEN(cls):
        return cls("token")
    
    @schemas.classproperty
    def U2F(cls):
        return cls("u2f")
    
    @schemas.classproperty
    def WEB(cls):
        return cls("web")
    
    @schemas.classproperty
    def WEBAUTHN(cls):
        return cls("webauthn")

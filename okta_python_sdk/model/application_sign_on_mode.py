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


class ApplicationSignOnMode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "BOOKMARK": "BOOKMARK",
            "BASIC_AUTH": "BASIC_AUTH",
            "BROWSER_PLUGIN": "BROWSER_PLUGIN",
            "SECURE_PASSWORD_STORE": "SECURE_PASSWORD_STORE",
            "AUTO_LOGIN": "AUTO_LOGIN",
            "WS_FEDERATION": "WS_FEDERATION",
            "SAML_2_0": "SAML_2_0",
            "OPENID_CONNECT": "OPENID_CONNECT",
            "SAML_1_1": "SAML_1_1",
        }
    
    @schemas.classproperty
    def BOOKMARK(cls):
        return cls("BOOKMARK")
    
    @schemas.classproperty
    def BASIC_AUTH(cls):
        return cls("BASIC_AUTH")
    
    @schemas.classproperty
    def BROWSER_PLUGIN(cls):
        return cls("BROWSER_PLUGIN")
    
    @schemas.classproperty
    def SECURE_PASSWORD_STORE(cls):
        return cls("SECURE_PASSWORD_STORE")
    
    @schemas.classproperty
    def AUTO_LOGIN(cls):
        return cls("AUTO_LOGIN")
    
    @schemas.classproperty
    def WS_FEDERATION(cls):
        return cls("WS_FEDERATION")
    
    @schemas.classproperty
    def SAML_2_0(cls):
        return cls("SAML_2_0")
    
    @schemas.classproperty
    def OPENID_CONNECT(cls):
        return cls("OPENID_CONNECT")
    
    @schemas.classproperty
    def SAML_1_1(cls):
        return cls("SAML_1_1")

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


class LogAuthenticationProvider(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def OKTA_AUTHENTICATION_PROVIDER(cls):
        return cls("OKTA_AUTHENTICATION_PROVIDER")
    
    @schemas.classproperty
    def ACTIVE_DIRECTORY(cls):
        return cls("ACTIVE_DIRECTORY")
    
    @schemas.classproperty
    def LDAP(cls):
        return cls("LDAP")
    
    @schemas.classproperty
    def FEDERATION(cls):
        return cls("FEDERATION")
    
    @schemas.classproperty
    def SOCIAL(cls):
        return cls("SOCIAL")
    
    @schemas.classproperty
    def FACTOR_PROVIDER(cls):
        return cls("FACTOR_PROVIDER")

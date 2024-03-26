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


class FactorStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def PENDING_ACTIVATION(cls):
        return cls("PENDING_ACTIVATION")
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("ACTIVE")
    
    @schemas.classproperty
    def INACTIVE(cls):
        return cls("INACTIVE")
    
    @schemas.classproperty
    def NOT_SETUP(cls):
        return cls("NOT_SETUP")
    
    @schemas.classproperty
    def ENROLLED(cls):
        return cls("ENROLLED")
    
    @schemas.classproperty
    def DISABLED(cls):
        return cls("DISABLED")
    
    @schemas.classproperty
    def EXPIRED(cls):
        return cls("EXPIRED")

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


class UserStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def ACTIVE(cls):
        return cls("ACTIVE")
    
    @schemas.classproperty
    def DEPROVISIONED(cls):
        return cls("DEPROVISIONED")
    
    @schemas.classproperty
    def LOCKED_OUT(cls):
        return cls("LOCKED_OUT")
    
    @schemas.classproperty
    def PASSWORD_EXPIRED(cls):
        return cls("PASSWORD_EXPIRED")
    
    @schemas.classproperty
    def PROVISIONED(cls):
        return cls("PROVISIONED")
    
    @schemas.classproperty
    def RECOVERY(cls):
        return cls("RECOVERY")
    
    @schemas.classproperty
    def STAGED(cls):
        return cls("STAGED")
    
    @schemas.classproperty
    def SUSPENDED(cls):
        return cls("SUSPENDED")

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


class DomainValidationStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def NOT_STARTED(cls):
        return cls("NOT_STARTED")
    
    @schemas.classproperty
    def IN_PROGRESS(cls):
        return cls("IN_PROGRESS")
    
    @schemas.classproperty
    def VERIFIED(cls):
        return cls("VERIFIED")
    
    @schemas.classproperty
    def FAILED_TO_VERIFY(cls):
        return cls("FAILED_TO_VERIFY")
    
    @schemas.classproperty
    def DOMAIN_TAKEN(cls):
        return cls("DOMAIN_TAKEN")
    
    @schemas.classproperty
    def COMPLETED(cls):
        return cls("COMPLETED")

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


class MultifactorEnrollmentPolicyAuthenticatorStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "NOT_ALLOWED": "NOT_ALLOWED",
            "OPTIONAL": "OPTIONAL",
            "REQUIRED": "REQUIRED",
        }
    
    @schemas.classproperty
    def NOT_ALLOWED(cls):
        return cls("NOT_ALLOWED")
    
    @schemas.classproperty
    def OPTIONAL(cls):
        return cls("OPTIONAL")
    
    @schemas.classproperty
    def REQUIRED(cls):
        return cls("REQUIRED")

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


class OpenIdConnectApplicationIssuerMode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "CUSTOM_URL": "CUSTOM_URL",
            "ORG_URL": "ORG_URL",
            "DYNAMIC": "DYNAMIC",
        }
    
    @schemas.classproperty
    def CUSTOM_URL(cls):
        return cls("CUSTOM_URL")
    
    @schemas.classproperty
    def ORG_URL(cls):
        return cls("ORG_URL")
    
    @schemas.classproperty
    def DYNAMIC(cls):
        return cls("DYNAMIC")

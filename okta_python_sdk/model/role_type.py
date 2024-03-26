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


class RoleType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "SUPER_ADMIN": "SUPER_ADMIN",
            "ORG_ADMIN": "ORG_ADMIN",
            "APP_ADMIN": "APP_ADMIN",
            "USER_ADMIN": "USER_ADMIN",
            "HELP_DESK_ADMIN": "HELP_DESK_ADMIN",
            "READ_ONLY_ADMIN": "READ_ONLY_ADMIN",
            "MOBILE_ADMIN": "MOBILE_ADMIN",
            "API_ACCESS_MANAGEMENT_ADMIN": "API_ACCESS_MANAGEMENT_ADMIN",
            "REPORT_ADMIN": "REPORT_ADMIN",
            "GROUP_MEMBERSHIP_ADMIN": "GROUP_MEMBERSHIP_ADMIN",
            "CUSTOM": "CUSTOM",
        }
    
    @schemas.classproperty
    def SUPER_ADMIN(cls):
        return cls("SUPER_ADMIN")
    
    @schemas.classproperty
    def ORG_ADMIN(cls):
        return cls("ORG_ADMIN")
    
    @schemas.classproperty
    def APP_ADMIN(cls):
        return cls("APP_ADMIN")
    
    @schemas.classproperty
    def USER_ADMIN(cls):
        return cls("USER_ADMIN")
    
    @schemas.classproperty
    def HELP_DESK_ADMIN(cls):
        return cls("HELP_DESK_ADMIN")
    
    @schemas.classproperty
    def READ_ONLY_ADMIN(cls):
        return cls("READ_ONLY_ADMIN")
    
    @schemas.classproperty
    def MOBILE_ADMIN(cls):
        return cls("MOBILE_ADMIN")
    
    @schemas.classproperty
    def API_ACCESS_MANAGEMENT_ADMIN(cls):
        return cls("API_ACCESS_MANAGEMENT_ADMIN")
    
    @schemas.classproperty
    def REPORT_ADMIN(cls):
        return cls("REPORT_ADMIN")
    
    @schemas.classproperty
    def GROUP_MEMBERSHIP_ADMIN(cls):
        return cls("GROUP_MEMBERSHIP_ADMIN")
    
    @schemas.classproperty
    def CUSTOM(cls):
        return cls("CUSTOM")

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


class NotificationType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    
    @schemas.classproperty
    def CONNECTOR_AGENT(cls):
        return cls("CONNECTOR_AGENT")
    
    @schemas.classproperty
    def USER_LOCKED_OUT(cls):
        return cls("USER_LOCKED_OUT")
    
    @schemas.classproperty
    def APP_IMPORT(cls):
        return cls("APP_IMPORT")
    
    @schemas.classproperty
    def LDAP_AGENT(cls):
        return cls("LDAP_AGENT")
    
    @schemas.classproperty
    def AD_AGENT(cls):
        return cls("AD_AGENT")
    
    @schemas.classproperty
    def OKTA_ANNOUNCEMENT(cls):
        return cls("OKTA_ANNOUNCEMENT")
    
    @schemas.classproperty
    def OKTA_ISSUE(cls):
        return cls("OKTA_ISSUE")
    
    @schemas.classproperty
    def OKTA_UPDATE(cls):
        return cls("OKTA_UPDATE")
    
    @schemas.classproperty
    def IWA_AGENT(cls):
        return cls("IWA_AGENT")
    
    @schemas.classproperty
    def USER_DEPROVISION(cls):
        return cls("USER_DEPROVISION")
    
    @schemas.classproperty
    def REPORT_SUSPICIOUS_ACTIVITY(cls):
        return cls("REPORT_SUSPICIOUS_ACTIVITY")
    
    @schemas.classproperty
    def RATELIMIT_NOTIFICATION(cls):
        return cls("RATELIMIT_NOTIFICATION")

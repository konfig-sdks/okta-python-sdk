# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from okta_python_sdk.type.log_actor import LogActor
from okta_python_sdk.type.log_authentication_context import LogAuthenticationContext
from okta_python_sdk.type.log_client import LogClient
from okta_python_sdk.type.log_debug_context import LogDebugContext
from okta_python_sdk.type.log_outcome import LogOutcome
from okta_python_sdk.type.log_request import LogRequest
from okta_python_sdk.type.log_security_context import LogSecurityContext
from okta_python_sdk.type.log_severity import LogSeverity
from okta_python_sdk.type.log_target import LogTarget
from okta_python_sdk.type.log_transaction import LogTransaction

class RequiredLogEvent(TypedDict):
    pass

class OptionalLogEvent(TypedDict, total=False):
    version: str

    actor: LogActor

    authenticationContext: LogAuthenticationContext

    client: LogClient

    debugContext: LogDebugContext

    displayMessage: str

    eventType: str

    legacyEventType: str

    outcome: LogOutcome

    published: datetime

    request: LogRequest

    securityContext: LogSecurityContext

    severity: LogSeverity

    target: typing.List[LogTarget]

    transaction: LogTransaction

    uuid: str

class LogEvent(RequiredLogEvent, OptionalLogEvent):
    pass

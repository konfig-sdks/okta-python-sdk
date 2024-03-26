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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from okta_python_sdk.pydantic.log_actor import LogActor
from okta_python_sdk.pydantic.log_authentication_context import LogAuthenticationContext
from okta_python_sdk.pydantic.log_client import LogClient
from okta_python_sdk.pydantic.log_debug_context import LogDebugContext
from okta_python_sdk.pydantic.log_outcome import LogOutcome
from okta_python_sdk.pydantic.log_request import LogRequest
from okta_python_sdk.pydantic.log_security_context import LogSecurityContext
from okta_python_sdk.pydantic.log_severity import LogSeverity
from okta_python_sdk.pydantic.log_target import LogTarget
from okta_python_sdk.pydantic.log_transaction import LogTransaction

class LogEvent(BaseModel):
    version: typing.Optional[str] = Field(None, alias='version')

    actor: typing.Optional[LogActor] = Field(None, alias='actor')

    authentication_context: typing.Optional[LogAuthenticationContext] = Field(None, alias='authenticationContext')

    client: typing.Optional[LogClient] = Field(None, alias='client')

    debug_context: typing.Optional[LogDebugContext] = Field(None, alias='debugContext')

    display_message: typing.Optional[str] = Field(None, alias='displayMessage')

    event_type: typing.Optional[str] = Field(None, alias='eventType')

    legacy_event_type: typing.Optional[str] = Field(None, alias='legacyEventType')

    outcome: typing.Optional[LogOutcome] = Field(None, alias='outcome')

    published: typing.Optional[datetime] = Field(None, alias='published')

    request: typing.Optional[LogRequest] = Field(None, alias='request')

    security_context: typing.Optional[LogSecurityContext] = Field(None, alias='securityContext')

    severity: typing.Optional[LogSeverity] = Field(None, alias='severity')

    target: typing.Optional[typing.List[LogTarget]] = Field(None, alias='target')

    transaction: typing.Optional[LogTransaction] = Field(None, alias='transaction')

    uuid: typing.Optional[str] = Field(None, alias='uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

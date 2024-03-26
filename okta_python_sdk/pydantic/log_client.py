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

from okta_python_sdk.pydantic.log_geographical_context import LogGeographicalContext
from okta_python_sdk.pydantic.log_user_agent import LogUserAgent

class LogClient(BaseModel):
    device: typing.Optional[str] = Field(None, alias='device')

    geographical_context: typing.Optional[LogGeographicalContext] = Field(None, alias='geographicalContext')

    id: typing.Optional[str] = Field(None, alias='id')

    ip_address: typing.Optional[str] = Field(None, alias='ipAddress')

    user_agent: typing.Optional[LogUserAgent] = Field(None, alias='userAgent')

    zone: typing.Optional[str] = Field(None, alias='zone')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

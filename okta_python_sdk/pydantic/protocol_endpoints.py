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

from okta_python_sdk.pydantic.protocol_endpoint import ProtocolEndpoint

class ProtocolEndpoints(BaseModel):
    acs: typing.Optional[ProtocolEndpoint] = Field(None, alias='acs')

    authorization: typing.Optional[ProtocolEndpoint] = Field(None, alias='authorization')

    jwks: typing.Optional[ProtocolEndpoint] = Field(None, alias='jwks')

    metadata: typing.Optional[ProtocolEndpoint] = Field(None, alias='metadata')

    slo: typing.Optional[ProtocolEndpoint] = Field(None, alias='slo')

    sso: typing.Optional[ProtocolEndpoint] = Field(None, alias='sso')

    token: typing.Optional[ProtocolEndpoint] = Field(None, alias='token')

    user_info: typing.Optional[ProtocolEndpoint] = Field(None, alias='userInfo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.application_feature_links import ApplicationFeatureLinks
from okta_python_sdk.pydantic.capabilities_object import CapabilitiesObject
from okta_python_sdk.pydantic.enabled_status import EnabledStatus

class ApplicationFeature(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    _links: typing.Optional[ApplicationFeatureLinks] = Field(None, alias='_links')

    capabilities: typing.Optional[CapabilitiesObject] = Field(None, alias='capabilities')

    name: typing.Optional[str] = Field(None, alias='name')

    status: typing.Optional[EnabledStatus] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

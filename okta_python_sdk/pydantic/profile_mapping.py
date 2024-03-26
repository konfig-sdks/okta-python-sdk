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

from okta_python_sdk.pydantic.profile_mapping_links import ProfileMappingLinks
from okta_python_sdk.pydantic.profile_mapping_properties import ProfileMappingProperties
from okta_python_sdk.pydantic.profile_mapping_source import ProfileMappingSource

class ProfileMapping(BaseModel):
    _links: typing.Optional[ProfileMappingLinks] = Field(None, alias='_links')

    id: typing.Optional[str] = Field(None, alias='id')

    properties: typing.Optional[ProfileMappingProperties] = Field(None, alias='properties')

    source: typing.Optional[ProfileMappingSource] = Field(None, alias='source')

    target: typing.Optional[ProfileMappingSource] = Field(None, alias='target')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

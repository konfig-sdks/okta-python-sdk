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

from okta_python_sdk.pydantic.enabled_status import EnabledStatus
from okta_python_sdk.pydantic.feature_links import FeatureLinks
from okta_python_sdk.pydantic.feature_stage import FeatureStage
from okta_python_sdk.pydantic.feature_type import FeatureType

class Feature(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    _links: typing.Optional[FeatureLinks] = Field(None, alias='_links')

    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    stage: typing.Optional[FeatureStage] = Field(None, alias='stage')

    status: typing.Optional[EnabledStatus] = Field(None, alias='status')

    type: typing.Optional[FeatureType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

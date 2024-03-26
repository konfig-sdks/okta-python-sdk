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


class OAuth2Scope(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    consent: typing.Optional[Literal["REQUIRED", "IMPLICIT", "ADMIN"]] = Field(None, alias='consent')

    default: typing.Optional[bool] = Field(None, alias='default')

    display_name: typing.Optional[str] = Field(None, alias='displayName')

    id: typing.Optional[str] = Field(None, alias='id')

    metadata_publish: typing.Optional[Literal["ALL_CLIENTS", "NO_CLIENTS"]] = Field(None, alias='metadataPublish')

    name: typing.Optional[str] = Field(None, alias='name')

    system: typing.Optional[bool] = Field(None, alias='system')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

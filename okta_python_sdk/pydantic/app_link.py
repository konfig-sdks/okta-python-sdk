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


class AppLink(BaseModel):
    app_assignment_id: typing.Optional[str] = Field(None, alias='appAssignmentId')

    app_instance_id: typing.Optional[str] = Field(None, alias='appInstanceId')

    app_name: typing.Optional[str] = Field(None, alias='appName')

    credentials_setup: typing.Optional[bool] = Field(None, alias='credentialsSetup')

    hidden: typing.Optional[bool] = Field(None, alias='hidden')

    id: typing.Optional[str] = Field(None, alias='id')

    label: typing.Optional[str] = Field(None, alias='label')

    link_url: typing.Optional[str] = Field(None, alias='linkUrl')

    logo_url: typing.Optional[str] = Field(None, alias='logoUrl')

    sort_order: typing.Optional[int] = Field(None, alias='sortOrder')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.role_assignment_type import RoleAssignmentType
from okta_python_sdk.pydantic.role_embedded import RoleEmbedded
from okta_python_sdk.pydantic.role_links import RoleLinks
from okta_python_sdk.pydantic.role_status import RoleStatus
from okta_python_sdk.pydantic.role_type import RoleType

class Role(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    _embedded: typing.Optional[RoleEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[RoleLinks] = Field(None, alias='_links')

    assignment_type: typing.Optional[RoleAssignmentType] = Field(None, alias='assignmentType')

    created: typing.Optional[datetime] = Field(None, alias='created')

    id: typing.Optional[str] = Field(None, alias='id')

    label: typing.Optional[str] = Field(None, alias='label')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    status: typing.Optional[RoleStatus] = Field(None, alias='status')

    type: typing.Optional[RoleType] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

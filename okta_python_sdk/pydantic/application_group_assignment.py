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

from okta_python_sdk.pydantic.application_group_assignment_embedded import ApplicationGroupAssignmentEmbedded
from okta_python_sdk.pydantic.application_group_assignment_links import ApplicationGroupAssignmentLinks
from okta_python_sdk.pydantic.application_group_assignment_profile import ApplicationGroupAssignmentProfile

class ApplicationGroupAssignment(BaseModel):
    _embedded: typing.Optional[ApplicationGroupAssignmentEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[ApplicationGroupAssignmentLinks] = Field(None, alias='_links')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    priority: typing.Optional[int] = Field(None, alias='priority')

    profile: typing.Optional[ApplicationGroupAssignmentProfile] = Field(None, alias='profile')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

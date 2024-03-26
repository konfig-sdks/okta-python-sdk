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

from okta_python_sdk.pydantic.catalog_application_status import CatalogApplicationStatus

class CatalogApplication(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    _links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='_links')

    category: typing.Optional[str] = Field(None, alias='category')

    display_name: typing.Optional[str] = Field(None, alias='displayName')

    features: typing.Optional[typing.List[str]] = Field(None, alias='features')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    name: typing.Optional[str] = Field(None, alias='name')

    sign_on_modes: typing.Optional[typing.List[str]] = Field(None, alias='signOnModes')

    status: typing.Optional[CatalogApplicationStatus] = Field(None, alias='status')

    verification_status: typing.Optional[str] = Field(None, alias='verificationStatus')

    website: typing.Optional[str] = Field(None, alias='website')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.pydantic.application_accessibility import ApplicationAccessibility
from okta_python_sdk.pydantic.application_credentials import ApplicationCredentials
from okta_python_sdk.pydantic.application_embedded import ApplicationEmbedded
from okta_python_sdk.pydantic.application_features import ApplicationFeatures
from okta_python_sdk.pydantic.application_licensing import ApplicationLicensing
from okta_python_sdk.pydantic.application_links import ApplicationLinks
from okta_python_sdk.pydantic.application_profile import ApplicationProfile
from okta_python_sdk.pydantic.application_settings import ApplicationSettings
from okta_python_sdk.pydantic.application_sign_on_mode import ApplicationSignOnMode
from okta_python_sdk.pydantic.application_visibility import ApplicationVisibility

class Application(BaseModel):
    _embedded: typing.Optional[ApplicationEmbedded] = Field(None, alias='_embedded')

    _links: typing.Optional[ApplicationLinks] = Field(None, alias='_links')

    accessibility: typing.Optional[ApplicationAccessibility] = Field(None, alias='accessibility')

    created: typing.Optional[datetime] = Field(None, alias='created')

    credentials: typing.Optional[ApplicationCredentials] = Field(None, alias='credentials')

    features: typing.Optional[ApplicationFeatures] = Field(None, alias='features')

    id: typing.Optional[str] = Field(None, alias='id')

    label: typing.Optional[str] = Field(None, alias='label')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    licensing: typing.Optional[ApplicationLicensing] = Field(None, alias='licensing')

    name: typing.Optional[str] = Field(None, alias='name')

    profile: typing.Optional[ApplicationProfile] = Field(None, alias='profile')

    settings: typing.Optional[ApplicationSettings] = Field(None, alias='settings')

    sign_on_mode: typing.Optional[ApplicationSignOnMode] = Field(None, alias='signOnMode')

    status: typing.Optional[Literal["ACTIVE", "INACTIVE", "DELETED"]] = Field(None, alias='status')

    visibility: typing.Optional[ApplicationVisibility] = Field(None, alias='visibility')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

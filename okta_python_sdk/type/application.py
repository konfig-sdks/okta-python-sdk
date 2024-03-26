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

from okta_python_sdk.type.application_accessibility import ApplicationAccessibility
from okta_python_sdk.type.application_credentials import ApplicationCredentials
from okta_python_sdk.type.application_embedded import ApplicationEmbedded
from okta_python_sdk.type.application_features import ApplicationFeatures
from okta_python_sdk.type.application_licensing import ApplicationLicensing
from okta_python_sdk.type.application_links import ApplicationLinks
from okta_python_sdk.type.application_profile import ApplicationProfile
from okta_python_sdk.type.application_settings import ApplicationSettings
from okta_python_sdk.type.application_sign_on_mode import ApplicationSignOnMode
from okta_python_sdk.type.application_visibility import ApplicationVisibility

class RequiredApplication(TypedDict):
    pass

class OptionalApplication(TypedDict, total=False):
    _embedded: ApplicationEmbedded

    _links: ApplicationLinks

    accessibility: ApplicationAccessibility

    created: datetime

    credentials: ApplicationCredentials

    features: ApplicationFeatures

    id: str

    label: str

    lastUpdated: datetime

    licensing: ApplicationLicensing

    name: str

    profile: ApplicationProfile

    settings: ApplicationSettings

    signOnMode: ApplicationSignOnMode

    status: str

    visibility: ApplicationVisibility

class Application(RequiredApplication, OptionalApplication):
    pass

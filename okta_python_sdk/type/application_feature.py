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

from okta_python_sdk.type.application_feature_links import ApplicationFeatureLinks
from okta_python_sdk.type.capabilities_object import CapabilitiesObject
from okta_python_sdk.type.enabled_status import EnabledStatus

class RequiredApplicationFeature(TypedDict):
    pass

class OptionalApplicationFeature(TypedDict, total=False):
    description: str

    _links: ApplicationFeatureLinks

    capabilities: CapabilitiesObject

    name: str

    status: EnabledStatus

class ApplicationFeature(RequiredApplicationFeature, OptionalApplicationFeature):
    pass

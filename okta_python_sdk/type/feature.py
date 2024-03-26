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

from okta_python_sdk.type.enabled_status import EnabledStatus
from okta_python_sdk.type.feature_links import FeatureLinks
from okta_python_sdk.type.feature_stage import FeatureStage
from okta_python_sdk.type.feature_type import FeatureType

class RequiredFeature(TypedDict):
    pass

class OptionalFeature(TypedDict, total=False):
    description: str

    _links: FeatureLinks

    id: str

    name: str

    stage: FeatureStage

    status: EnabledStatus

    type: FeatureType

class Feature(RequiredFeature, OptionalFeature):
    pass

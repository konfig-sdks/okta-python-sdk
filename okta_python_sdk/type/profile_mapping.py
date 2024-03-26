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

from okta_python_sdk.type.profile_mapping_links import ProfileMappingLinks
from okta_python_sdk.type.profile_mapping_properties import ProfileMappingProperties
from okta_python_sdk.type.profile_mapping_source import ProfileMappingSource

class RequiredProfileMapping(TypedDict):
    pass

class OptionalProfileMapping(TypedDict, total=False):
    _links: ProfileMappingLinks

    id: str

    properties: ProfileMappingProperties

    source: ProfileMappingSource

    target: ProfileMappingSource

class ProfileMapping(RequiredProfileMapping, OptionalProfileMapping):
    pass

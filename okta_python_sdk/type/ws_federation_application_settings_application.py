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


class RequiredWsFederationApplicationSettingsApplication(TypedDict):
    pass

class OptionalWsFederationApplicationSettingsApplication(TypedDict, total=False):
    attributeStatements: str

    audienceRestriction: str

    authnContextClassRef: str

    groupFilter: str

    groupName: str

    groupValueFormat: str

    nameIDFormat: str

    realm: str

    siteURL: str

    usernameAttribute: str

    wReplyOverride: bool

    wReplyURL: str

class WsFederationApplicationSettingsApplication(RequiredWsFederationApplicationSettingsApplication, OptionalWsFederationApplicationSettingsApplication):
    pass

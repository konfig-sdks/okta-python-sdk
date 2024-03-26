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

from okta_python_sdk.type.org2_org_application_settings_app import Org2OrgApplicationSettingsApp

class RequiredOrg2OrgApplicationSettings(TypedDict):
    pass

class OptionalOrg2OrgApplicationSettings(TypedDict, total=False):
    app: Org2OrgApplicationSettingsApp

class Org2OrgApplicationSettings(RequiredOrg2OrgApplicationSettings, OptionalOrg2OrgApplicationSettings):
    pass

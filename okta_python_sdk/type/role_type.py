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


RoleType = Literal["SUPER_ADMIN", "ORG_ADMIN", "APP_ADMIN", "USER_ADMIN", "HELP_DESK_ADMIN", "READ_ONLY_ADMIN", "MOBILE_ADMIN", "API_ACCESS_MANAGEMENT_ADMIN", "REPORT_ADMIN", "GROUP_MEMBERSHIP_ADMIN", "CUSTOM"]

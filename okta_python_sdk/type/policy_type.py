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


PolicyType = Literal["OAUTH_AUTHORIZATION_POLICY", "OKTA_SIGN_ON", "PASSWORD", "IDP_DISCOVERY", "PROFILE_ENROLLMENT", "ACCESS_POLICY", "MFA_ENROLL"]

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


ApplicationSignOnMode = Literal["BOOKMARK", "BASIC_AUTH", "BROWSER_PLUGIN", "SECURE_PASSWORD_STORE", "AUTO_LOGIN", "WS_FEDERATION", "SAML_2_0", "OPENID_CONNECT", "SAML_1_1"]

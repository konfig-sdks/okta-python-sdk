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


ApplicationCredentialsScheme = Literal["SHARED_USERNAME_AND_PASSWORD", "EXTERNAL_PASSWORD_SYNC", "EDIT_USERNAME_AND_PASSWORD", "EDIT_PASSWORD_ONLY", "ADMIN_SETS_CREDENTIALS"]

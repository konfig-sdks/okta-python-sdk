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

from okta_python_sdk.pydantic.password_dictionary import PasswordDictionary
from okta_python_sdk.pydantic.password_policy_password_settings_complexity_exclude_attributes import PasswordPolicyPasswordSettingsComplexityExcludeAttributes

class PasswordPolicyPasswordSettingsComplexity(BaseModel):
    dictionary: typing.Optional[PasswordDictionary] = Field(None, alias='dictionary')

    exclude_attributes: typing.Optional[PasswordPolicyPasswordSettingsComplexityExcludeAttributes] = Field(None, alias='excludeAttributes')

    exclude_username: typing.Optional[bool] = Field(None, alias='excludeUsername')

    min_length: typing.Optional[int] = Field(None, alias='minLength')

    min_lower_case: typing.Optional[int] = Field(None, alias='minLowerCase')

    min_number: typing.Optional[int] = Field(None, alias='minNumber')

    min_symbol: typing.Optional[int] = Field(None, alias='minSymbol')

    min_upper_case: typing.Optional[int] = Field(None, alias='minUpperCase')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

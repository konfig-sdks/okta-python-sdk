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


class UserProfile(BaseModel):
    title: typing.Optional[str] = Field(None, alias='title')

    city: typing.Optional[str] = Field(None, alias='city')

    cost_center: typing.Optional[str] = Field(None, alias='costCenter')

    country_code: typing.Optional[str] = Field(None, alias='countryCode')

    department: typing.Optional[str] = Field(None, alias='department')

    display_name: typing.Optional[str] = Field(None, alias='displayName')

    division: typing.Optional[str] = Field(None, alias='division')

    email: typing.Optional[str] = Field(None, alias='email')

    employee_number: typing.Optional[str] = Field(None, alias='employeeNumber')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    honorific_prefix: typing.Optional[str] = Field(None, alias='honorificPrefix')

    honorific_suffix: typing.Optional[str] = Field(None, alias='honorificSuffix')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    locale: typing.Optional[str] = Field(None, alias='locale')

    login: typing.Optional[str] = Field(None, alias='login')

    manager: typing.Optional[str] = Field(None, alias='manager')

    manager_id: typing.Optional[str] = Field(None, alias='managerId')

    middle_name: typing.Optional[str] = Field(None, alias='middleName')

    mobile_phone: typing.Optional[str] = Field(None, alias='mobilePhone')

    nick_name: typing.Optional[str] = Field(None, alias='nickName')

    organization: typing.Optional[str] = Field(None, alias='organization')

    postal_address: typing.Optional[str] = Field(None, alias='postalAddress')

    preferred_language: typing.Optional[str] = Field(None, alias='preferredLanguage')

    primary_phone: typing.Optional[str] = Field(None, alias='primaryPhone')

    profile_url: typing.Optional[str] = Field(None, alias='profileUrl')

    second_email: typing.Optional[str] = Field(None, alias='secondEmail')

    state: typing.Optional[str] = Field(None, alias='state')

    street_address: typing.Optional[str] = Field(None, alias='streetAddress')

    timezone: typing.Optional[str] = Field(None, alias='timezone')

    user_type: typing.Optional[str] = Field(None, alias='userType')

    zip_code: typing.Optional[str] = Field(None, alias='zipCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

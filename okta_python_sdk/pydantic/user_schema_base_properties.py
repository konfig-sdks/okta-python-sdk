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

from okta_python_sdk.pydantic.user_schema_attribute import UserSchemaAttribute

class UserSchemaBaseProperties(BaseModel):
    title: typing.Optional[UserSchemaAttribute] = Field(None, alias='title')

    city: typing.Optional[UserSchemaAttribute] = Field(None, alias='city')

    cost_center: typing.Optional[UserSchemaAttribute] = Field(None, alias='costCenter')

    country_code: typing.Optional[UserSchemaAttribute] = Field(None, alias='countryCode')

    department: typing.Optional[UserSchemaAttribute] = Field(None, alias='department')

    display_name: typing.Optional[UserSchemaAttribute] = Field(None, alias='displayName')

    division: typing.Optional[UserSchemaAttribute] = Field(None, alias='division')

    email: typing.Optional[UserSchemaAttribute] = Field(None, alias='email')

    employee_number: typing.Optional[UserSchemaAttribute] = Field(None, alias='employeeNumber')

    first_name: typing.Optional[UserSchemaAttribute] = Field(None, alias='firstName')

    honorific_prefix: typing.Optional[UserSchemaAttribute] = Field(None, alias='honorificPrefix')

    honorific_suffix: typing.Optional[UserSchemaAttribute] = Field(None, alias='honorificSuffix')

    last_name: typing.Optional[UserSchemaAttribute] = Field(None, alias='lastName')

    locale: typing.Optional[UserSchemaAttribute] = Field(None, alias='locale')

    login: typing.Optional[UserSchemaAttribute] = Field(None, alias='login')

    manager: typing.Optional[UserSchemaAttribute] = Field(None, alias='manager')

    manager_id: typing.Optional[UserSchemaAttribute] = Field(None, alias='managerId')

    middle_name: typing.Optional[UserSchemaAttribute] = Field(None, alias='middleName')

    mobile_phone: typing.Optional[UserSchemaAttribute] = Field(None, alias='mobilePhone')

    nick_name: typing.Optional[UserSchemaAttribute] = Field(None, alias='nickName')

    organization: typing.Optional[UserSchemaAttribute] = Field(None, alias='organization')

    postal_address: typing.Optional[UserSchemaAttribute] = Field(None, alias='postalAddress')

    preferred_language: typing.Optional[UserSchemaAttribute] = Field(None, alias='preferredLanguage')

    primary_phone: typing.Optional[UserSchemaAttribute] = Field(None, alias='primaryPhone')

    profile_url: typing.Optional[UserSchemaAttribute] = Field(None, alias='profileUrl')

    second_email: typing.Optional[UserSchemaAttribute] = Field(None, alias='secondEmail')

    state: typing.Optional[UserSchemaAttribute] = Field(None, alias='state')

    street_address: typing.Optional[UserSchemaAttribute] = Field(None, alias='streetAddress')

    timezone: typing.Optional[UserSchemaAttribute] = Field(None, alias='timezone')

    user_type: typing.Optional[UserSchemaAttribute] = Field(None, alias='userType')

    zip_code: typing.Optional[UserSchemaAttribute] = Field(None, alias='zipCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

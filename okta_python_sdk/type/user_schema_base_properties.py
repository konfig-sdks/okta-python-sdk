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

from okta_python_sdk.type.user_schema_attribute import UserSchemaAttribute

class RequiredUserSchemaBaseProperties(TypedDict):
    pass

class OptionalUserSchemaBaseProperties(TypedDict, total=False):
    title: UserSchemaAttribute

    city: UserSchemaAttribute

    costCenter: UserSchemaAttribute

    countryCode: UserSchemaAttribute

    department: UserSchemaAttribute

    displayName: UserSchemaAttribute

    division: UserSchemaAttribute

    email: UserSchemaAttribute

    employeeNumber: UserSchemaAttribute

    firstName: UserSchemaAttribute

    honorificPrefix: UserSchemaAttribute

    honorificSuffix: UserSchemaAttribute

    lastName: UserSchemaAttribute

    locale: UserSchemaAttribute

    login: UserSchemaAttribute

    manager: UserSchemaAttribute

    managerId: UserSchemaAttribute

    middleName: UserSchemaAttribute

    mobilePhone: UserSchemaAttribute

    nickName: UserSchemaAttribute

    organization: UserSchemaAttribute

    postalAddress: UserSchemaAttribute

    preferredLanguage: UserSchemaAttribute

    primaryPhone: UserSchemaAttribute

    profileUrl: UserSchemaAttribute

    secondEmail: UserSchemaAttribute

    state: UserSchemaAttribute

    streetAddress: UserSchemaAttribute

    timezone: UserSchemaAttribute

    userType: UserSchemaAttribute

    zipCode: UserSchemaAttribute

class UserSchemaBaseProperties(RequiredUserSchemaBaseProperties, OptionalUserSchemaBaseProperties):
    pass

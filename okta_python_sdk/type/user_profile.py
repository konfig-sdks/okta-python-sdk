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


class RequiredUserProfile(TypedDict):
    pass

class OptionalUserProfile(TypedDict, total=False):
    title: str

    city: str

    costCenter: str

    countryCode: str

    department: str

    displayName: str

    division: str

    email: str

    employeeNumber: str

    firstName: str

    honorificPrefix: str

    honorificSuffix: str

    lastName: str

    locale: str

    login: str

    manager: str

    managerId: str

    middleName: str

    mobilePhone: str

    nickName: str

    organization: str

    postalAddress: str

    preferredLanguage: str

    primaryPhone: str

    profileUrl: str

    secondEmail: str

    state: str

    streetAddress: str

    timezone: str

    userType: str

    zipCode: str

class UserProfile(RequiredUserProfile, OptionalUserProfile):
    pass

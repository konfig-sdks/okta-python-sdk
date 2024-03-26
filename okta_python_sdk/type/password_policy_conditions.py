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

from okta_python_sdk.type.password_policy_authentication_provider_condition import PasswordPolicyAuthenticationProviderCondition
from okta_python_sdk.type.policy_people_condition import PolicyPeopleCondition

class RequiredPasswordPolicyConditions(TypedDict):
    pass

class OptionalPasswordPolicyConditions(TypedDict, total=False):
    authProvider: PasswordPolicyAuthenticationProviderCondition

    people: PolicyPeopleCondition

class PasswordPolicyConditions(RequiredPasswordPolicyConditions, OptionalPasswordPolicyConditions):
    pass

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

from okta_python_sdk.type.policy_subject_format import PolicySubjectFormat
from okta_python_sdk.type.policy_subject_match_type import PolicySubjectMatchType
from okta_python_sdk.type.policy_user_name_template import PolicyUserNameTemplate

class RequiredPolicySubject(TypedDict):
    pass

class OptionalPolicySubject(TypedDict, total=False):
    filter: str

    format: PolicySubjectFormat

    matchAttribute: str

    matchType: PolicySubjectMatchType

    userNameTemplate: PolicyUserNameTemplate

class PolicySubject(RequiredPolicySubject, OptionalPolicySubject):
    pass

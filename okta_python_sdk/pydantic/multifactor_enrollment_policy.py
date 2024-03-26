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

from okta_python_sdk.pydantic.multifactor_enrollment_policy_settings import MultifactorEnrollmentPolicySettings
from okta_python_sdk.pydantic.policy import Policy
from okta_python_sdk.pydantic.policy_rule_conditions import PolicyRuleConditions

MultifactorEnrollmentPolicy = typing.Union[Policy,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

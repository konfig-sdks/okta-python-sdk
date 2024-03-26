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

from okta_python_sdk.type.policy_account_link_filter_groups import PolicyAccountLinkFilterGroups

class RequiredPolicyAccountLinkFilter(TypedDict):
    pass

class OptionalPolicyAccountLinkFilter(TypedDict, total=False):
    groups: PolicyAccountLinkFilterGroups

class PolicyAccountLinkFilter(RequiredPolicyAccountLinkFilter, OptionalPolicyAccountLinkFilter):
    pass

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

from okta_python_sdk.type.notification_type import NotificationType
from okta_python_sdk.type.subscription_channels import SubscriptionChannels
from okta_python_sdk.type.subscription_links import SubscriptionLinks
from okta_python_sdk.type.subscription_status import SubscriptionStatus

class RequiredSubscription(TypedDict):
    pass

class OptionalSubscription(TypedDict, total=False):
    _links: SubscriptionLinks

    channels: SubscriptionChannels

    notificationType: NotificationType

    status: SubscriptionStatus

class Subscription(RequiredSubscription, OptionalSubscription):
    pass

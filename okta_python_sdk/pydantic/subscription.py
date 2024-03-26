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

from okta_python_sdk.pydantic.notification_type import NotificationType
from okta_python_sdk.pydantic.subscription_channels import SubscriptionChannels
from okta_python_sdk.pydantic.subscription_links import SubscriptionLinks
from okta_python_sdk.pydantic.subscription_status import SubscriptionStatus

class Subscription(BaseModel):
    _links: typing.Optional[SubscriptionLinks] = Field(None, alias='_links')

    channels: typing.Optional[SubscriptionChannels] = Field(None, alias='channels')

    notification_type: typing.Optional[NotificationType] = Field(None, alias='notificationType')

    status: typing.Optional[SubscriptionStatus] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

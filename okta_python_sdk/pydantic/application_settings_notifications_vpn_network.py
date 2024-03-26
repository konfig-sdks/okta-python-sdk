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

from okta_python_sdk.pydantic.application_settings_notifications_vpn_network_exclude import ApplicationSettingsNotificationsVpnNetworkExclude
from okta_python_sdk.pydantic.application_settings_notifications_vpn_network_include import ApplicationSettingsNotificationsVpnNetworkInclude

class ApplicationSettingsNotificationsVpnNetwork(BaseModel):
    connection: typing.Optional[str] = Field(None, alias='connection')

    exclude: typing.Optional[ApplicationSettingsNotificationsVpnNetworkExclude] = Field(None, alias='exclude')

    include: typing.Optional[ApplicationSettingsNotificationsVpnNetworkInclude] = Field(None, alias='include')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

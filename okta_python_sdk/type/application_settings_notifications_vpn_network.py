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

from okta_python_sdk.type.application_settings_notifications_vpn_network_exclude import ApplicationSettingsNotificationsVpnNetworkExclude
from okta_python_sdk.type.application_settings_notifications_vpn_network_include import ApplicationSettingsNotificationsVpnNetworkInclude

class RequiredApplicationSettingsNotificationsVpnNetwork(TypedDict):
    pass

class OptionalApplicationSettingsNotificationsVpnNetwork(TypedDict, total=False):
    connection: str

    exclude: ApplicationSettingsNotificationsVpnNetworkExclude

    include: ApplicationSettingsNotificationsVpnNetworkInclude

class ApplicationSettingsNotificationsVpnNetwork(RequiredApplicationSettingsNotificationsVpnNetwork, OptionalApplicationSettingsNotificationsVpnNetwork):
    pass

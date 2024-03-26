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

from okta_python_sdk.type.network_zone_address import NetworkZoneAddress
from okta_python_sdk.type.network_zone_asns import NetworkZoneAsns
from okta_python_sdk.type.network_zone_links import NetworkZoneLinks
from okta_python_sdk.type.network_zone_location import NetworkZoneLocation
from okta_python_sdk.type.network_zone_status import NetworkZoneStatus
from okta_python_sdk.type.network_zone_type import NetworkZoneType
from okta_python_sdk.type.network_zone_usage import NetworkZoneUsage

class RequiredNetworkZone(TypedDict):
    pass

class OptionalNetworkZone(TypedDict, total=False):
    _links: NetworkZoneLinks

    asns: NetworkZoneAsns

    created: datetime

    gateways: typing.List[NetworkZoneAddress]

    id: str

    lastUpdated: datetime

    locations: typing.List[NetworkZoneLocation]

    name: str

    proxies: typing.List[NetworkZoneAddress]

    proxyType: str

    status: NetworkZoneStatus

    system: bool

    type: NetworkZoneType

    usage: NetworkZoneUsage

class NetworkZone(RequiredNetworkZone, OptionalNetworkZone):
    pass

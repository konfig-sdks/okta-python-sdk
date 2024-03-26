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

from okta_python_sdk.pydantic.network_zone_address import NetworkZoneAddress
from okta_python_sdk.pydantic.network_zone_asns import NetworkZoneAsns
from okta_python_sdk.pydantic.network_zone_links import NetworkZoneLinks
from okta_python_sdk.pydantic.network_zone_location import NetworkZoneLocation
from okta_python_sdk.pydantic.network_zone_status import NetworkZoneStatus
from okta_python_sdk.pydantic.network_zone_type import NetworkZoneType
from okta_python_sdk.pydantic.network_zone_usage import NetworkZoneUsage

class NetworkZone(BaseModel):
    _links: typing.Optional[NetworkZoneLinks] = Field(None, alias='_links')

    asns: typing.Optional[NetworkZoneAsns] = Field(None, alias='asns')

    created: typing.Optional[datetime] = Field(None, alias='created')

    gateways: typing.Optional[typing.List[NetworkZoneAddress]] = Field(None, alias='gateways')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    locations: typing.Optional[typing.List[NetworkZoneLocation]] = Field(None, alias='locations')

    name: typing.Optional[str] = Field(None, alias='name')

    proxies: typing.Optional[typing.List[NetworkZoneAddress]] = Field(None, alias='proxies')

    proxy_type: typing.Optional[str] = Field(None, alias='proxyType')

    status: typing.Optional[NetworkZoneStatus] = Field(None, alias='status')

    system: typing.Optional[bool] = Field(None, alias='system')

    type: typing.Optional[NetworkZoneType] = Field(None, alias='type')

    usage: typing.Optional[NetworkZoneUsage] = Field(None, alias='usage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

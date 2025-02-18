# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_zones_zone_id_lifecycle_activate.post import ActivateLifecycleRaw
from okta_python_sdk.paths.api_v1_zones.post import CreateNewRaw
from okta_python_sdk.paths.api_v1_zones_zone_id_lifecycle_deactivate.post import DeactivateZoneLifecycleRaw
from okta_python_sdk.paths.api_v1_zones_zone_id.get import GetByIdRaw
from okta_python_sdk.paths.api_v1_zones.get import ListZonesRaw
from okta_python_sdk.paths.api_v1_zones_zone_id.delete import RemoveZoneRaw
from okta_python_sdk.paths.api_v1_zones_zone_id.put import UpdateZoneRaw


class NetworkZoneApiRaw(
    ActivateLifecycleRaw,
    CreateNewRaw,
    DeactivateZoneLifecycleRaw,
    GetByIdRaw,
    ListZonesRaw,
    RemoveZoneRaw,
    UpdateZoneRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

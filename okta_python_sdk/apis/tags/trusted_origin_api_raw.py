# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_trusted_origins_trusted_origin_id_lifecycle_activate.post import ActivateLifecycleSuccessRaw
from okta_python_sdk.paths.api_v1_trusted_origins.post import CreateSuccessRaw
from okta_python_sdk.paths.api_v1_trusted_origins_trusted_origin_id_lifecycle_deactivate.post import DeactivateLifecycleSuccessRaw
from okta_python_sdk.paths.api_v1_trusted_origins_trusted_origin_id.delete import DeleteSuccessRaw
from okta_python_sdk.paths.api_v1_trusted_origins.get import GetListRaw
from okta_python_sdk.paths.api_v1_trusted_origins_trusted_origin_id.get import GetSuccessByIdRaw
from okta_python_sdk.paths.api_v1_trusted_origins_trusted_origin_id.put import UpdateSuccessRaw


class TrustedOriginApiRaw(
    ActivateLifecycleSuccessRaw,
    CreateSuccessRaw,
    DeactivateLifecycleSuccessRaw,
    DeleteSuccessRaw,
    GetListRaw,
    GetSuccessByIdRaw,
    UpdateSuccessRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

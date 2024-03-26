# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_threats_configuration.get import GetCurrentConfigurationRaw
from okta_python_sdk.paths.api_v1_threats_configuration.post import UpdateConfigurationRaw


class ThreatInsightApiRaw(
    GetCurrentConfigurationRaw,
    UpdateConfigurationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

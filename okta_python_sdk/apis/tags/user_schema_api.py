# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_meta_schemas_user_schema_id.get import GetSchemaById
from okta_python_sdk.paths.api_v1_meta_schemas_apps_app_instance_id_default.get import GetUserSchema
from okta_python_sdk.paths.api_v1_meta_schemas_apps_app_instance_id_default.post import PartialUpdateUserProfile
from okta_python_sdk.paths.api_v1_meta_schemas_user_schema_id.post import PartialUpdateUserProfile0
from okta_python_sdk.apis.tags.user_schema_api_raw import UserSchemaApiRaw


class UserSchemaApi(
    GetSchemaById,
    GetUserSchema,
    PartialUpdateUserProfile,
    PartialUpdateUserProfile0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UserSchemaApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UserSchemaApiRaw(api_client)

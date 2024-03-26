# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

import unittest
from unittest.mock import patch

import urllib3

import okta_python_sdk
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name_application_id import delete
from okta_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1UsersUserIdRolesRoleIdTargetsCatalogAppsAppNameApplicationId(ApiTestMixin, unittest.TestCase):
    """
    ApiV1UsersUserIdRolesRoleIdTargetsCatalogAppsAppNameApplicationId unit test stubs
        Remove App Instance Target to App Administrator Role given to a User
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()

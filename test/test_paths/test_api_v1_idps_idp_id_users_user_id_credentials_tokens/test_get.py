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
from okta_python_sdk.paths.api_v1_idps_idp_id_users_user_id_credentials_tokens import get
from okta_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1IdpsIdpIdUsersUserIdCredentialsTokens(ApiTestMixin, unittest.TestCase):
    """
    ApiV1IdpsIdpIdUsersUserIdCredentialsTokens unit test stubs
        Social Authentication Token Operation
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

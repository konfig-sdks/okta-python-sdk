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
from okta_python_sdk.paths.api_v1_apps_app_id_logo import post
from okta_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1AppsAppIdLogo(ApiTestMixin, unittest.TestCase):
    """
    ApiV1AppsAppIdLogo unit test stubs
        The file must be in PNG, JPG, or GIF format, and less than 1 MB in size. For best results use landscape orientation, a transparent background, and a minimum size of 420px by 120px to prevent upscaling.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201
    response_body = ''




if __name__ == '__main__':
    unittest.main()

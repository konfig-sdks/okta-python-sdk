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
from okta_python_sdk.paths.api_v1_groups_rules_rule_id import get
from okta_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1GroupsRulesRuleId(ApiTestMixin, unittest.TestCase):
    """
    ApiV1GroupsRulesRuleId unit test stubs
        Get Group Rule
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()

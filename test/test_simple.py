# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

import unittest

import os
from pprint import pprint
from okta_python_sdk import Okta

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        okta = Okta(
        
                        api_token = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(okta)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

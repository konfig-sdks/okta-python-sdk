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
from okta_python_sdk.paths.api_v1_users_user_id_subscriptions_notification_type_subscribe import post
from okta_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV1UsersUserIdSubscriptionsNotificationTypeSubscribe(ApiTestMixin, unittest.TestCase):
    """
    ApiV1UsersUserIdSubscriptionsNotificationTypeSubscribe unit test stubs
        Subscribe to a specific notification type
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_roles_role_type_or_role_id_subscriptions_notification_type_unsubscribe.post import CustomRoleNotificationUnsubscribe
from okta_python_sdk.paths.api_v1_roles_role_type_or_role_id_subscriptions_notification_type.get import GetRoleSubscriptionsByNotificationType
from okta_python_sdk.paths.api_v1_roles_role_type_or_role_id_subscriptions.get import ListRoleSubscriptions
from okta_python_sdk.paths.api_v1_roles_role_type_or_role_id_subscriptions_notification_type_subscribe.post import RoleNotificationSubscribe
from okta_python_sdk.paths.api_v1_users_user_id_subscriptions_notification_type_unsubscribe.post import UnsubscribeUserSubscriptionByNotificationType
from okta_python_sdk.paths.api_v1_users_user_id_subscriptions_notification_type_subscribe.post import UserNotificationSubscribe
from okta_python_sdk.apis.tags.subscription_api_raw import SubscriptionApiRaw


class SubscriptionApi(
    CustomRoleNotificationUnsubscribe,
    GetRoleSubscriptionsByNotificationType,
    ListRoleSubscriptions,
    RoleNotificationSubscribe,
    UnsubscribeUserSubscriptionByNotificationType,
    UserNotificationSubscribe,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: SubscriptionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = SubscriptionApiRaw(api_client)

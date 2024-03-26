# coding: utf-8
"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

import typing
import inspect
from datetime import date, datetime
from okta_python_sdk.client_custom import ClientCustom
from okta_python_sdk.configuration import Configuration
from okta_python_sdk.api_client import ApiClient
from okta_python_sdk.type_util import copy_signature
from okta_python_sdk.apis.tags.application_api import ApplicationApi
from okta_python_sdk.apis.tags.authenticator_api import AuthenticatorApi
from okta_python_sdk.apis.tags.authorization_server_api import AuthorizationServerApi
from okta_python_sdk.apis.tags.brand_api import BrandApi
from okta_python_sdk.apis.tags.domain_api import DomainApi
from okta_python_sdk.apis.tags.event_hook_api import EventHookApi
from okta_python_sdk.apis.tags.feature_api import FeatureApi
from okta_python_sdk.apis.tags.group_api import GroupApi
from okta_python_sdk.apis.tags.group_schema_api import GroupSchemaApi
from okta_python_sdk.apis.tags.identity_provider_api import IdentityProviderApi
from okta_python_sdk.apis.tags.inline_hook_api import InlineHookApi
from okta_python_sdk.apis.tags.linked_object_api import LinkedObjectApi
from okta_python_sdk.apis.tags.log_api import LogApi
from okta_python_sdk.apis.tags.network_zone_api import NetworkZoneApi
from okta_python_sdk.apis.tags.org_api import OrgApi
from okta_python_sdk.apis.tags.policy_api import PolicyApi
from okta_python_sdk.apis.tags.profile_mapping_api import ProfileMappingApi
from okta_python_sdk.apis.tags.session_api import SessionApi
from okta_python_sdk.apis.tags.subscription_api import SubscriptionApi
from okta_python_sdk.apis.tags.template_api import TemplateApi
from okta_python_sdk.apis.tags.threat_insight_api import ThreatInsightApi
from okta_python_sdk.apis.tags.trusted_origin_api import TrustedOriginApi
from okta_python_sdk.apis.tags.user_api import UserApi
from okta_python_sdk.apis.tags.user_factor_api import UserFactorApi
from okta_python_sdk.apis.tags.user_schema_api import UserSchemaApi
from okta_python_sdk.apis.tags.user_type_api import UserTypeApi



class Okta(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.application: ApplicationApi = ApplicationApi(api_client)
        self.authenticator: AuthenticatorApi = AuthenticatorApi(api_client)
        self.authorization_server: AuthorizationServerApi = AuthorizationServerApi(api_client)
        self.brand: BrandApi = BrandApi(api_client)
        self.domain: DomainApi = DomainApi(api_client)
        self.event_hook: EventHookApi = EventHookApi(api_client)
        self.feature: FeatureApi = FeatureApi(api_client)
        self.group: GroupApi = GroupApi(api_client)
        self.group_schema: GroupSchemaApi = GroupSchemaApi(api_client)
        self.identity_provider: IdentityProviderApi = IdentityProviderApi(api_client)
        self.inline_hook: InlineHookApi = InlineHookApi(api_client)
        self.linked_object: LinkedObjectApi = LinkedObjectApi(api_client)
        self.log: LogApi = LogApi(api_client)
        self.network_zone: NetworkZoneApi = NetworkZoneApi(api_client)
        self.org: OrgApi = OrgApi(api_client)
        self.policy: PolicyApi = PolicyApi(api_client)
        self.profile_mapping: ProfileMappingApi = ProfileMappingApi(api_client)
        self.session: SessionApi = SessionApi(api_client)
        self.subscription: SubscriptionApi = SubscriptionApi(api_client)
        self.template: TemplateApi = TemplateApi(api_client)
        self.threat_insight: ThreatInsightApi = ThreatInsightApi(api_client)
        self.trusted_origin: TrustedOriginApi = TrustedOriginApi(api_client)
        self.user: UserApi = UserApi(api_client)
        self.user_factor: UserFactorApi = UserFactorApi(api_client)
        self.user_schema: UserSchemaApi = UserSchemaApi(api_client)
        self.user_type: UserTypeApi = UserTypeApi(api_client)

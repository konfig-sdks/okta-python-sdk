import typing_extensions

from okta_python_sdk.apis.tags import TagValues
from okta_python_sdk.apis.tags.user_api import UserApi
from okta_python_sdk.apis.tags.application_api import ApplicationApi
from okta_python_sdk.apis.tags.authorization_server_api import AuthorizationServerApi
from okta_python_sdk.apis.tags.group_api import GroupApi
from okta_python_sdk.apis.tags.identity_provider_api import IdentityProviderApi
from okta_python_sdk.apis.tags.brand_api import BrandApi
from okta_python_sdk.apis.tags.org_api import OrgApi
from okta_python_sdk.apis.tags.policy_api import PolicyApi
from okta_python_sdk.apis.tags.user_factor_api import UserFactorApi
from okta_python_sdk.apis.tags.event_hook_api import EventHookApi
from okta_python_sdk.apis.tags.inline_hook_api import InlineHookApi
from okta_python_sdk.apis.tags.trusted_origin_api import TrustedOriginApi
from okta_python_sdk.apis.tags.network_zone_api import NetworkZoneApi
from okta_python_sdk.apis.tags.authenticator_api import AuthenticatorApi
from okta_python_sdk.apis.tags.domain_api import DomainApi
from okta_python_sdk.apis.tags.user_type_api import UserTypeApi
from okta_python_sdk.apis.tags.subscription_api import SubscriptionApi
from okta_python_sdk.apis.tags.template_api import TemplateApi
from okta_python_sdk.apis.tags.feature_api import FeatureApi
from okta_python_sdk.apis.tags.user_schema_api import UserSchemaApi
from okta_python_sdk.apis.tags.linked_object_api import LinkedObjectApi
from okta_python_sdk.apis.tags.session_api import SessionApi
from okta_python_sdk.apis.tags.profile_mapping_api import ProfileMappingApi
from okta_python_sdk.apis.tags.group_schema_api import GroupSchemaApi
from okta_python_sdk.apis.tags.threat_insight_api import ThreatInsightApi
from okta_python_sdk.apis.tags.log_api import LogApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USER: UserApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.AUTHORIZATION_SERVER: AuthorizationServerApi,
        TagValues.GROUP: GroupApi,
        TagValues.IDENTITY_PROVIDER: IdentityProviderApi,
        TagValues.BRAND: BrandApi,
        TagValues.ORG: OrgApi,
        TagValues.POLICY: PolicyApi,
        TagValues.USER_FACTOR: UserFactorApi,
        TagValues.EVENT_HOOK: EventHookApi,
        TagValues.INLINE_HOOK: InlineHookApi,
        TagValues.TRUSTED_ORIGIN: TrustedOriginApi,
        TagValues.NETWORK_ZONE: NetworkZoneApi,
        TagValues.AUTHENTICATOR: AuthenticatorApi,
        TagValues.DOMAIN: DomainApi,
        TagValues.USER_TYPE: UserTypeApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.FEATURE: FeatureApi,
        TagValues.USER_SCHEMA: UserSchemaApi,
        TagValues.LINKED_OBJECT: LinkedObjectApi,
        TagValues.SESSION: SessionApi,
        TagValues.PROFILE_MAPPING: ProfileMappingApi,
        TagValues.GROUP_SCHEMA: GroupSchemaApi,
        TagValues.THREAT_INSIGHT: ThreatInsightApi,
        TagValues.LOG: LogApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USER: UserApi,
        TagValues.APPLICATION: ApplicationApi,
        TagValues.AUTHORIZATION_SERVER: AuthorizationServerApi,
        TagValues.GROUP: GroupApi,
        TagValues.IDENTITY_PROVIDER: IdentityProviderApi,
        TagValues.BRAND: BrandApi,
        TagValues.ORG: OrgApi,
        TagValues.POLICY: PolicyApi,
        TagValues.USER_FACTOR: UserFactorApi,
        TagValues.EVENT_HOOK: EventHookApi,
        TagValues.INLINE_HOOK: InlineHookApi,
        TagValues.TRUSTED_ORIGIN: TrustedOriginApi,
        TagValues.NETWORK_ZONE: NetworkZoneApi,
        TagValues.AUTHENTICATOR: AuthenticatorApi,
        TagValues.DOMAIN: DomainApi,
        TagValues.USER_TYPE: UserTypeApi,
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.FEATURE: FeatureApi,
        TagValues.USER_SCHEMA: UserSchemaApi,
        TagValues.LINKED_OBJECT: LinkedObjectApi,
        TagValues.SESSION: SessionApi,
        TagValues.PROFILE_MAPPING: ProfileMappingApi,
        TagValues.GROUP_SCHEMA: GroupSchemaApi,
        TagValues.THREAT_INSIGHT: ThreatInsightApi,
        TagValues.LOG: LogApi,
    }
)

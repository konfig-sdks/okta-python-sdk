# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from okta_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    USER = "User"
    APPLICATION = "Application"
    AUTHORIZATION_SERVER = "AuthorizationServer"
    GROUP = "Group"
    IDENTITY_PROVIDER = "IdentityProvider"
    BRAND = "Brand"
    ORG = "Org"
    POLICY = "Policy"
    USER_FACTOR = "UserFactor"
    EVENT_HOOK = "EventHook"
    INLINE_HOOK = "InlineHook"
    TRUSTED_ORIGIN = "TrustedOrigin"
    NETWORK_ZONE = "NetworkZone"
    AUTHENTICATOR = "Authenticator"
    DOMAIN = "Domain"
    USER_TYPE = "UserType"
    SUBSCRIPTION = "Subscription"
    TEMPLATE = "Template"
    FEATURE = "Feature"
    USER_SCHEMA = "UserSchema"
    LINKED_OBJECT = "LinkedObject"
    SESSION = "Session"
    PROFILE_MAPPING = "ProfileMapping"
    GROUP_SCHEMA = "GroupSchema"
    THREAT_INSIGHT = "ThreatInsight"
    LOG = "Log"

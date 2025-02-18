# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from okta_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_V1_APPS = "/api/v1/apps"
    API_V1_APPS_APP_ID = "/api/v1/apps/{appId}"
    API_V1_APPS_APP_ID_CONNECTIONS_DEFAULT = "/api/v1/apps/{appId}/connections/default"
    API_V1_APPS_APP_ID_CONNECTIONS_DEFAULT_LIFECYCLE_ACTIVATE = "/api/v1/apps/{appId}/connections/default/lifecycle/activate"
    API_V1_APPS_APP_ID_CONNECTIONS_DEFAULT_LIFECYCLE_DEACTIVATE = "/api/v1/apps/{appId}/connections/default/lifecycle/deactivate"
    API_V1_APPS_APP_ID_CREDENTIALS_CSRS = "/api/v1/apps/{appId}/credentials/csrs"
    API_V1_APPS_APP_ID_CREDENTIALS_CSRS_CSR_ID = "/api/v1/apps/{appId}/credentials/csrs/{csrId}"
    API_V1_APPS_APP_ID_CREDENTIALS_CSRS_CSR_ID_LIFECYCLE_PUBLISH = "/api/v1/apps/{appId}/credentials/csrs/{csrId}/lifecycle/publish"
    API_V1_APPS_APP_ID_CREDENTIALS_KEYS = "/api/v1/apps/{appId}/credentials/keys"
    API_V1_APPS_APP_ID_CREDENTIALS_KEYS_GENERATE = "/api/v1/apps/{appId}/credentials/keys/generate"
    API_V1_APPS_APP_ID_CREDENTIALS_KEYS_KEY_ID = "/api/v1/apps/{appId}/credentials/keys/{keyId}"
    API_V1_APPS_APP_ID_CREDENTIALS_KEYS_KEY_ID_CLONE = "/api/v1/apps/{appId}/credentials/keys/{keyId}/clone"
    API_V1_APPS_APP_ID_CREDENTIALS_SECRETS = "/api/v1/apps/{appId}/credentials/secrets"
    API_V1_APPS_APP_ID_CREDENTIALS_SECRETS_SECRET_ID = "/api/v1/apps/{appId}/credentials/secrets/{secretId}"
    API_V1_APPS_APP_ID_CREDENTIALS_SECRETS_SECRET_ID_LIFECYCLE_ACTIVATE = "/api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/activate"
    API_V1_APPS_APP_ID_CREDENTIALS_SECRETS_SECRET_ID_LIFECYCLE_DEACTIVATE = "/api/v1/apps/{appId}/credentials/secrets/{secretId}/lifecycle/deactivate"
    API_V1_APPS_APP_ID_FEATURES = "/api/v1/apps/{appId}/features"
    API_V1_APPS_APP_ID_FEATURES_NAME = "/api/v1/apps/{appId}/features/{name}"
    API_V1_APPS_APP_ID_GRANTS = "/api/v1/apps/{appId}/grants"
    API_V1_APPS_APP_ID_GRANTS_GRANT_ID = "/api/v1/apps/{appId}/grants/{grantId}"
    API_V1_APPS_APP_ID_GROUPS = "/api/v1/apps/{appId}/groups"
    API_V1_APPS_APP_ID_GROUPS_GROUP_ID = "/api/v1/apps/{appId}/groups/{groupId}"
    API_V1_APPS_APP_ID_LIFECYCLE_ACTIVATE = "/api/v1/apps/{appId}/lifecycle/activate"
    API_V1_APPS_APP_ID_LIFECYCLE_DEACTIVATE = "/api/v1/apps/{appId}/lifecycle/deactivate"
    API_V1_APPS_APP_ID_LOGO = "/api/v1/apps/{appId}/logo"
    API_V1_APPS_APP_ID_POLICIES_POLICY_ID = "/api/v1/apps/{appId}/policies/{policyId}"
    API_V1_APPS_APP_ID_SSO_SAML_METADATA = "/api/v1/apps/{appId}/sso/saml/metadata"
    API_V1_APPS_APP_ID_TOKENS = "/api/v1/apps/{appId}/tokens"
    API_V1_APPS_APP_ID_TOKENS_TOKEN_ID = "/api/v1/apps/{appId}/tokens/{tokenId}"
    API_V1_APPS_APP_ID_USERS = "/api/v1/apps/{appId}/users"
    API_V1_APPS_APP_ID_USERS_USER_ID = "/api/v1/apps/{appId}/users/{userId}"
    API_V1_AUTHENTICATORS = "/api/v1/authenticators"
    API_V1_AUTHENTICATORS_AUTHENTICATOR_ID = "/api/v1/authenticators/{authenticatorId}"
    API_V1_AUTHENTICATORS_AUTHENTICATOR_ID_LIFECYCLE_ACTIVATE = "/api/v1/authenticators/{authenticatorId}/lifecycle/activate"
    API_V1_AUTHENTICATORS_AUTHENTICATOR_ID_LIFECYCLE_DEACTIVATE = "/api/v1/authenticators/{authenticatorId}/lifecycle/deactivate"
    API_V1_AUTHORIZATION_SERVERS = "/api/v1/authorizationServers"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID = "/api/v1/authorizationServers/{authServerId}"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_CLAIMS = "/api/v1/authorizationServers/{authServerId}/claims"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_CLAIMS_CLAIM_ID = "/api/v1/authorizationServers/{authServerId}/claims/{claimId}"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_CLIENTS = "/api/v1/authorizationServers/{authServerId}/clients"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_CLIENTS_CLIENT_ID_TOKENS = "/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_CLIENTS_CLIENT_ID_TOKENS_TOKEN_ID = "/api/v1/authorizationServers/{authServerId}/clients/{clientId}/tokens/{tokenId}"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_CREDENTIALS_KEYS = "/api/v1/authorizationServers/{authServerId}/credentials/keys"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_CREDENTIALS_LIFECYCLE_KEY_ROTATE = "/api/v1/authorizationServers/{authServerId}/credentials/lifecycle/keyRotate"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_LIFECYCLE_ACTIVATE = "/api/v1/authorizationServers/{authServerId}/lifecycle/activate"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_LIFECYCLE_DEACTIVATE = "/api/v1/authorizationServers/{authServerId}/lifecycle/deactivate"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES = "/api/v1/authorizationServers/{authServerId}/policies"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES_POLICY_ID = "/api/v1/authorizationServers/{authServerId}/policies/{policyId}"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES_POLICY_ID_LIFECYCLE_ACTIVATE = "/api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/activate"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES_POLICY_ID_LIFECYCLE_DEACTIVATE = "/api/v1/authorizationServers/{authServerId}/policies/{policyId}/lifecycle/deactivate"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES_POLICY_ID_RULES = "/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES_POLICY_ID_RULES_RULE_ID = "/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES_POLICY_ID_RULES_RULE_ID_LIFECYCLE_ACTIVATE = "/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/activate"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_POLICIES_POLICY_ID_RULES_RULE_ID_LIFECYCLE_DEACTIVATE = "/api/v1/authorizationServers/{authServerId}/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_SCOPES = "/api/v1/authorizationServers/{authServerId}/scopes"
    API_V1_AUTHORIZATION_SERVERS_AUTH_SERVER_ID_SCOPES_SCOPE_ID = "/api/v1/authorizationServers/{authServerId}/scopes/{scopeId}"
    API_V1_BRANDS = "/api/v1/brands"
    API_V1_BRANDS_BRAND_ID = "/api/v1/brands/{brandId}"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL = "/api/v1/brands/{brandId}/templates/email"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL_TEMPLATE_NAME = "/api/v1/brands/{brandId}/templates/email/{templateName}"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL_TEMPLATE_NAME_CUSTOMIZATIONS = "/api/v1/brands/{brandId}/templates/email/{templateName}/customizations"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL_TEMPLATE_NAME_CUSTOMIZATIONS_CUSTOMIZATION_ID = "/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL_TEMPLATE_NAME_CUSTOMIZATIONS_CUSTOMIZATION_ID_PREVIEW = "/api/v1/brands/{brandId}/templates/email/{templateName}/customizations/{customizationId}/preview"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL_TEMPLATE_NAME_DEFAULTCONTENT = "/api/v1/brands/{brandId}/templates/email/{templateName}/default-content"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL_TEMPLATE_NAME_DEFAULTCONTENT_PREVIEW = "/api/v1/brands/{brandId}/templates/email/{templateName}/default-content/preview"
    API_V1_BRANDS_BRAND_ID_TEMPLATES_EMAIL_TEMPLATE_NAME_TEST = "/api/v1/brands/{brandId}/templates/email/{templateName}/test"
    API_V1_BRANDS_BRAND_ID_THEMES = "/api/v1/brands/{brandId}/themes"
    API_V1_BRANDS_BRAND_ID_THEMES_THEME_ID = "/api/v1/brands/{brandId}/themes/{themeId}"
    API_V1_BRANDS_BRAND_ID_THEMES_THEME_ID_BACKGROUNDIMAGE = "/api/v1/brands/{brandId}/themes/{themeId}/background-image"
    API_V1_BRANDS_BRAND_ID_THEMES_THEME_ID_FAVICON = "/api/v1/brands/{brandId}/themes/{themeId}/favicon"
    API_V1_BRANDS_BRAND_ID_THEMES_THEME_ID_LOGO = "/api/v1/brands/{brandId}/themes/{themeId}/logo"
    API_V1_DOMAINS = "/api/v1/domains"
    API_V1_DOMAINS_DOMAIN_ID = "/api/v1/domains/{domainId}"
    API_V1_DOMAINS_DOMAIN_ID_CERTIFICATE = "/api/v1/domains/{domainId}/certificate"
    API_V1_DOMAINS_DOMAIN_ID_VERIFY = "/api/v1/domains/{domainId}/verify"
    API_V1_EVENT_HOOKS = "/api/v1/eventHooks"
    API_V1_EVENT_HOOKS_EVENT_HOOK_ID = "/api/v1/eventHooks/{eventHookId}"
    API_V1_EVENT_HOOKS_EVENT_HOOK_ID_LIFECYCLE_ACTIVATE = "/api/v1/eventHooks/{eventHookId}/lifecycle/activate"
    API_V1_EVENT_HOOKS_EVENT_HOOK_ID_LIFECYCLE_DEACTIVATE = "/api/v1/eventHooks/{eventHookId}/lifecycle/deactivate"
    API_V1_EVENT_HOOKS_EVENT_HOOK_ID_LIFECYCLE_VERIFY = "/api/v1/eventHooks/{eventHookId}/lifecycle/verify"
    API_V1_FEATURES = "/api/v1/features"
    API_V1_FEATURES_FEATURE_ID = "/api/v1/features/{featureId}"
    API_V1_FEATURES_FEATURE_ID_DEPENDENCIES = "/api/v1/features/{featureId}/dependencies"
    API_V1_FEATURES_FEATURE_ID_DEPENDENTS = "/api/v1/features/{featureId}/dependents"
    API_V1_FEATURES_FEATURE_ID_LIFECYCLE = "/api/v1/features/{featureId}/{lifecycle}"
    API_V1_GROUPS = "/api/v1/groups"
    API_V1_GROUPS_RULES = "/api/v1/groups/rules"
    API_V1_GROUPS_RULES_RULE_ID = "/api/v1/groups/rules/{ruleId}"
    API_V1_GROUPS_RULES_RULE_ID_LIFECYCLE_ACTIVATE = "/api/v1/groups/rules/{ruleId}/lifecycle/activate"
    API_V1_GROUPS_RULES_RULE_ID_LIFECYCLE_DEACTIVATE = "/api/v1/groups/rules/{ruleId}/lifecycle/deactivate"
    API_V1_GROUPS_GROUP_ID = "/api/v1/groups/{groupId}"
    API_V1_GROUPS_GROUP_ID_APPS = "/api/v1/groups/{groupId}/apps"
    API_V1_GROUPS_GROUP_ID_ROLES = "/api/v1/groups/{groupId}/roles"
    API_V1_GROUPS_GROUP_ID_ROLES_ROLE_ID = "/api/v1/groups/{groupId}/roles/{roleId}"
    API_V1_GROUPS_GROUP_ID_ROLES_ROLE_ID_TARGETS_CATALOG_APPS = "/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps"
    API_V1_GROUPS_GROUP_ID_ROLES_ROLE_ID_TARGETS_CATALOG_APPS_APP_NAME = "/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}"
    API_V1_GROUPS_GROUP_ID_ROLES_ROLE_ID_TARGETS_CATALOG_APPS_APP_NAME_APPLICATION_ID = "/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}"
    API_V1_GROUPS_GROUP_ID_ROLES_ROLE_ID_TARGETS_GROUPS = "/api/v1/groups/{groupId}/roles/{roleId}/targets/groups"
    API_V1_GROUPS_GROUP_ID_ROLES_ROLE_ID_TARGETS_GROUPS_TARGET_GROUP_ID = "/api/v1/groups/{groupId}/roles/{roleId}/targets/groups/{targetGroupId}"
    API_V1_GROUPS_GROUP_ID_USERS = "/api/v1/groups/{groupId}/users"
    API_V1_GROUPS_GROUP_ID_USERS_USER_ID = "/api/v1/groups/{groupId}/users/{userId}"
    API_V1_IDPS = "/api/v1/idps"
    API_V1_IDPS_CREDENTIALS_KEYS = "/api/v1/idps/credentials/keys"
    API_V1_IDPS_CREDENTIALS_KEYS_KEY_ID = "/api/v1/idps/credentials/keys/{keyId}"
    API_V1_IDPS_IDP_ID = "/api/v1/idps/{idpId}"
    API_V1_IDPS_IDP_ID_CREDENTIALS_CSRS = "/api/v1/idps/{idpId}/credentials/csrs"
    API_V1_IDPS_IDP_ID_CREDENTIALS_CSRS_CSR_ID = "/api/v1/idps/{idpId}/credentials/csrs/{csrId}"
    API_V1_IDPS_IDP_ID_CREDENTIALS_CSRS_CSR_ID_LIFECYCLE_PUBLISH = "/api/v1/idps/{idpId}/credentials/csrs/{csrId}/lifecycle/publish"
    API_V1_IDPS_IDP_ID_CREDENTIALS_KEYS = "/api/v1/idps/{idpId}/credentials/keys"
    API_V1_IDPS_IDP_ID_CREDENTIALS_KEYS_GENERATE = "/api/v1/idps/{idpId}/credentials/keys/generate"
    API_V1_IDPS_IDP_ID_CREDENTIALS_KEYS_KEY_ID = "/api/v1/idps/{idpId}/credentials/keys/{keyId}"
    API_V1_IDPS_IDP_ID_CREDENTIALS_KEYS_KEY_ID_CLONE = "/api/v1/idps/{idpId}/credentials/keys/{keyId}/clone"
    API_V1_IDPS_IDP_ID_LIFECYCLE_ACTIVATE = "/api/v1/idps/{idpId}/lifecycle/activate"
    API_V1_IDPS_IDP_ID_LIFECYCLE_DEACTIVATE = "/api/v1/idps/{idpId}/lifecycle/deactivate"
    API_V1_IDPS_IDP_ID_USERS = "/api/v1/idps/{idpId}/users"
    API_V1_IDPS_IDP_ID_USERS_USER_ID = "/api/v1/idps/{idpId}/users/{userId}"
    API_V1_IDPS_IDP_ID_USERS_USER_ID_CREDENTIALS_TOKENS = "/api/v1/idps/{idpId}/users/{userId}/credentials/tokens"
    API_V1_INLINE_HOOKS = "/api/v1/inlineHooks"
    API_V1_INLINE_HOOKS_INLINE_HOOK_ID = "/api/v1/inlineHooks/{inlineHookId}"
    API_V1_INLINE_HOOKS_INLINE_HOOK_ID_EXECUTE = "/api/v1/inlineHooks/{inlineHookId}/execute"
    API_V1_INLINE_HOOKS_INLINE_HOOK_ID_LIFECYCLE_ACTIVATE = "/api/v1/inlineHooks/{inlineHookId}/lifecycle/activate"
    API_V1_INLINE_HOOKS_INLINE_HOOK_ID_LIFECYCLE_DEACTIVATE = "/api/v1/inlineHooks/{inlineHookId}/lifecycle/deactivate"
    API_V1_LOGS = "/api/v1/logs"
    API_V1_MAPPINGS = "/api/v1/mappings"
    API_V1_MAPPINGS_MAPPING_ID = "/api/v1/mappings/{mappingId}"
    API_V1_META_SCHEMAS_APPS_APP_INSTANCE_ID_DEFAULT = "/api/v1/meta/schemas/apps/{appInstanceId}/default"
    API_V1_META_SCHEMAS_GROUP_DEFAULT = "/api/v1/meta/schemas/group/default"
    API_V1_META_SCHEMAS_USER_LINKED_OBJECTS = "/api/v1/meta/schemas/user/linkedObjects"
    API_V1_META_SCHEMAS_USER_LINKED_OBJECTS_LINKED_OBJECT_NAME = "/api/v1/meta/schemas/user/linkedObjects/{linkedObjectName}"
    API_V1_META_SCHEMAS_USER_SCHEMA_ID = "/api/v1/meta/schemas/user/{schemaId}"
    API_V1_META_TYPES_USER = "/api/v1/meta/types/user"
    API_V1_META_TYPES_USER_TYPE_ID = "/api/v1/meta/types/user/{typeId}"
    API_V1_ORG = "/api/v1/org"
    API_V1_ORG_CONTACTS = "/api/v1/org/contacts"
    API_V1_ORG_CONTACTS_CONTACT_TYPE = "/api/v1/org/contacts/{contactType}"
    API_V1_ORG_LOGO = "/api/v1/org/logo"
    API_V1_ORG_PREFERENCES = "/api/v1/org/preferences"
    API_V1_ORG_PREFERENCES_HIDE_END_USER_FOOTER = "/api/v1/org/preferences/hideEndUserFooter"
    API_V1_ORG_PREFERENCES_SHOW_END_USER_FOOTER = "/api/v1/org/preferences/showEndUserFooter"
    API_V1_ORG_PRIVACY_OKTA_COMMUNICATION = "/api/v1/org/privacy/oktaCommunication"
    API_V1_ORG_PRIVACY_OKTA_COMMUNICATION_OPT_IN = "/api/v1/org/privacy/oktaCommunication/optIn"
    API_V1_ORG_PRIVACY_OKTA_COMMUNICATION_OPT_OUT = "/api/v1/org/privacy/oktaCommunication/optOut"
    API_V1_ORG_PRIVACY_OKTA_SUPPORT = "/api/v1/org/privacy/oktaSupport"
    API_V1_ORG_PRIVACY_OKTA_SUPPORT_EXTEND = "/api/v1/org/privacy/oktaSupport/extend"
    API_V1_ORG_PRIVACY_OKTA_SUPPORT_GRANT = "/api/v1/org/privacy/oktaSupport/grant"
    API_V1_ORG_PRIVACY_OKTA_SUPPORT_REVOKE = "/api/v1/org/privacy/oktaSupport/revoke"
    API_V1_POLICIES = "/api/v1/policies"
    API_V1_POLICIES_POLICY_ID = "/api/v1/policies/{policyId}"
    API_V1_POLICIES_POLICY_ID_LIFECYCLE_ACTIVATE = "/api/v1/policies/{policyId}/lifecycle/activate"
    API_V1_POLICIES_POLICY_ID_LIFECYCLE_DEACTIVATE = "/api/v1/policies/{policyId}/lifecycle/deactivate"
    API_V1_POLICIES_POLICY_ID_RULES = "/api/v1/policies/{policyId}/rules"
    API_V1_POLICIES_POLICY_ID_RULES_RULE_ID = "/api/v1/policies/{policyId}/rules/{ruleId}"
    API_V1_POLICIES_POLICY_ID_RULES_RULE_ID_LIFECYCLE_ACTIVATE = "/api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/activate"
    API_V1_POLICIES_POLICY_ID_RULES_RULE_ID_LIFECYCLE_DEACTIVATE = "/api/v1/policies/{policyId}/rules/{ruleId}/lifecycle/deactivate"
    API_V1_ROLES_ROLE_TYPE_OR_ROLE_ID_SUBSCRIPTIONS = "/api/v1/roles/{roleTypeOrRoleId}/subscriptions"
    API_V1_ROLES_ROLE_TYPE_OR_ROLE_ID_SUBSCRIPTIONS_NOTIFICATION_TYPE = "/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}"
    API_V1_ROLES_ROLE_TYPE_OR_ROLE_ID_SUBSCRIPTIONS_NOTIFICATION_TYPE_SUBSCRIBE = "/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/subscribe"
    API_V1_ROLES_ROLE_TYPE_OR_ROLE_ID_SUBSCRIPTIONS_NOTIFICATION_TYPE_UNSUBSCRIBE = "/api/v1/roles/{roleTypeOrRoleId}/subscriptions/{notificationType}/unsubscribe"
    API_V1_SESSIONS = "/api/v1/sessions"
    API_V1_SESSIONS_SESSION_ID = "/api/v1/sessions/{sessionId}"
    API_V1_SESSIONS_SESSION_ID_LIFECYCLE_REFRESH = "/api/v1/sessions/{sessionId}/lifecycle/refresh"
    API_V1_TEMPLATES_SMS = "/api/v1/templates/sms"
    API_V1_TEMPLATES_SMS_TEMPLATE_ID = "/api/v1/templates/sms/{templateId}"
    API_V1_THREATS_CONFIGURATION = "/api/v1/threats/configuration"
    API_V1_TRUSTED_ORIGINS = "/api/v1/trustedOrigins"
    API_V1_TRUSTED_ORIGINS_TRUSTED_ORIGIN_ID = "/api/v1/trustedOrigins/{trustedOriginId}"
    API_V1_TRUSTED_ORIGINS_TRUSTED_ORIGIN_ID_LIFECYCLE_ACTIVATE = "/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/activate"
    API_V1_TRUSTED_ORIGINS_TRUSTED_ORIGIN_ID_LIFECYCLE_DEACTIVATE = "/api/v1/trustedOrigins/{trustedOriginId}/lifecycle/deactivate"
    API_V1_USERS = "/api/v1/users"
    API_V1_USERS_ASSOCIATED_USER_ID_LINKED_OBJECTS_PRIMARY_RELATIONSHIP_NAME_PRIMARY_USER_ID = "/api/v1/users/{associatedUserId}/linkedObjects/{primaryRelationshipName}/{primaryUserId}"
    API_V1_USERS_USER_ID = "/api/v1/users/{userId}"
    API_V1_USERS_USER_ID_APP_LINKS = "/api/v1/users/{userId}/appLinks"
    API_V1_USERS_USER_ID_CLIENTS = "/api/v1/users/{userId}/clients"
    API_V1_USERS_USER_ID_CLIENTS_CLIENT_ID_GRANTS = "/api/v1/users/{userId}/clients/{clientId}/grants"
    API_V1_USERS_USER_ID_CLIENTS_CLIENT_ID_TOKENS = "/api/v1/users/{userId}/clients/{clientId}/tokens"
    API_V1_USERS_USER_ID_CLIENTS_CLIENT_ID_TOKENS_TOKEN_ID = "/api/v1/users/{userId}/clients/{clientId}/tokens/{tokenId}"
    API_V1_USERS_USER_ID_CREDENTIALS_CHANGE_PASSWORD = "/api/v1/users/{userId}/credentials/change_password"
    API_V1_USERS_USER_ID_CREDENTIALS_CHANGE_RECOVERY_QUESTION = "/api/v1/users/{userId}/credentials/change_recovery_question"
    API_V1_USERS_USER_ID_CREDENTIALS_FORGOT_PASSWORD = "/api/v1/users/{userId}/credentials/forgot_password"
    API_V1_USERS_USER_ID_FACTORS = "/api/v1/users/{userId}/factors"
    API_V1_USERS_USER_ID_FACTORS_CATALOG = "/api/v1/users/{userId}/factors/catalog"
    API_V1_USERS_USER_ID_FACTORS_QUESTIONS = "/api/v1/users/{userId}/factors/questions"
    API_V1_USERS_USER_ID_FACTORS_FACTOR_ID = "/api/v1/users/{userId}/factors/{factorId}"
    API_V1_USERS_USER_ID_FACTORS_FACTOR_ID_LIFECYCLE_ACTIVATE = "/api/v1/users/{userId}/factors/{factorId}/lifecycle/activate"
    API_V1_USERS_USER_ID_FACTORS_FACTOR_ID_TRANSACTIONS_TRANSACTION_ID = "/api/v1/users/{userId}/factors/{factorId}/transactions/{transactionId}"
    API_V1_USERS_USER_ID_FACTORS_FACTOR_ID_VERIFY = "/api/v1/users/{userId}/factors/{factorId}/verify"
    API_V1_USERS_USER_ID_GRANTS = "/api/v1/users/{userId}/grants"
    API_V1_USERS_USER_ID_GRANTS_GRANT_ID = "/api/v1/users/{userId}/grants/{grantId}"
    API_V1_USERS_USER_ID_GROUPS = "/api/v1/users/{userId}/groups"
    API_V1_USERS_USER_ID_IDPS = "/api/v1/users/{userId}/idps"
    API_V1_USERS_USER_ID_LIFECYCLE_ACTIVATE = "/api/v1/users/{userId}/lifecycle/activate"
    API_V1_USERS_USER_ID_LIFECYCLE_DEACTIVATE = "/api/v1/users/{userId}/lifecycle/deactivate"
    API_V1_USERS_USER_ID_LIFECYCLE_EXPIRE_PASSWORDTEMP_PASSWORDFALSE = "/api/v1/users/{userId}/lifecycle/expire_password?tempPassword&#x3D;false"
    API_V1_USERS_USER_ID_LIFECYCLE_EXPIRE_PASSWORDTEMP_PASSWORDTRUE = "/api/v1/users/{userId}/lifecycle/expire_password?tempPassword&#x3D;true"
    API_V1_USERS_USER_ID_LIFECYCLE_REACTIVATE = "/api/v1/users/{userId}/lifecycle/reactivate"
    API_V1_USERS_USER_ID_LIFECYCLE_RESET_FACTORS = "/api/v1/users/{userId}/lifecycle/reset_factors"
    API_V1_USERS_USER_ID_LIFECYCLE_RESET_PASSWORD = "/api/v1/users/{userId}/lifecycle/reset_password"
    API_V1_USERS_USER_ID_LIFECYCLE_SUSPEND = "/api/v1/users/{userId}/lifecycle/suspend"
    API_V1_USERS_USER_ID_LIFECYCLE_UNLOCK = "/api/v1/users/{userId}/lifecycle/unlock"
    API_V1_USERS_USER_ID_LIFECYCLE_UNSUSPEND = "/api/v1/users/{userId}/lifecycle/unsuspend"
    API_V1_USERS_USER_ID_LINKED_OBJECTS_RELATIONSHIP_NAME = "/api/v1/users/{userId}/linkedObjects/{relationshipName}"
    API_V1_USERS_USER_ID_ROLES = "/api/v1/users/{userId}/roles"
    API_V1_USERS_USER_ID_ROLES_ROLE_ID = "/api/v1/users/{userId}/roles/{roleId}"
    API_V1_USERS_USER_ID_ROLES_ROLE_ID_TARGETS_CATALOG_APPS = "/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps"
    API_V1_USERS_USER_ID_ROLES_ROLE_ID_TARGETS_CATALOG_APPS_APP_NAME = "/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}"
    API_V1_USERS_USER_ID_ROLES_ROLE_ID_TARGETS_CATALOG_APPS_APP_NAME_APPLICATION_ID = "/api/v1/users/{userId}/roles/{roleId}/targets/catalog/apps/{appName}/{applicationId}"
    API_V1_USERS_USER_ID_ROLES_ROLE_ID_TARGETS_GROUPS = "/api/v1/users/{userId}/roles/{roleId}/targets/groups"
    API_V1_USERS_USER_ID_ROLES_ROLE_ID_TARGETS_GROUPS_GROUP_ID = "/api/v1/users/{userId}/roles/{roleId}/targets/groups/{groupId}"
    API_V1_USERS_USER_ID_SESSIONS = "/api/v1/users/{userId}/sessions"
    API_V1_USERS_USER_ID_SUBSCRIPTIONS = "/api/v1/users/{userId}/subscriptions"
    API_V1_USERS_USER_ID_SUBSCRIPTIONS_NOTIFICATION_TYPE = "/api/v1/users/{userId}/subscriptions/{notificationType}"
    API_V1_USERS_USER_ID_SUBSCRIPTIONS_NOTIFICATION_TYPE_SUBSCRIBE = "/api/v1/users/{userId}/subscriptions/{notificationType}/subscribe"
    API_V1_USERS_USER_ID_SUBSCRIPTIONS_NOTIFICATION_TYPE_UNSUBSCRIBE = "/api/v1/users/{userId}/subscriptions/{notificationType}/unsubscribe"
    API_V1_ZONES = "/api/v1/zones"
    API_V1_ZONES_ZONE_ID = "/api/v1/zones/{zoneId}"
    API_V1_ZONES_ZONE_ID_LIFECYCLE_ACTIVATE = "/api/v1/zones/{zoneId}/lifecycle/activate"
    API_V1_ZONES_ZONE_ID_LIFECYCLE_DEACTIVATE = "/api/v1/zones/{zoneId}/lifecycle/deactivate"

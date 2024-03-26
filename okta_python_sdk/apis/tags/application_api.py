# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id_lifecycle_activate.post import ActivateClientSecret
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default_lifecycle_activate.post import ActivateDefaultProvisioningConnection
from okta_python_sdk.paths.api_v1_apps_app_id_lifecycle_activate.post import ActivateInactive
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets.post import AddClientSecret
from okta_python_sdk.paths.api_v1_apps_app_id_groups_group_id.put import AssignGroupTo
from okta_python_sdk.paths.api_v1_apps_app_id_policies_policy_id.put import AssignPolicyToApplication
from okta_python_sdk.paths.api_v1_apps_app_id_users.post import AssignUserToApplication
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys_key_id_clone.post import CloneApplicationKeyCredential
from okta_python_sdk.paths.api_v1_apps.post import CreateNew
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id_lifecycle_deactivate.post import DeactivateClientSecretById
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default_lifecycle_deactivate.post import DeactivateDefaultProvisioningConnection
from okta_python_sdk.paths.api_v1_apps_app_id_lifecycle_deactivate.post import DeactivateLifecycle
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs_csr_id.delete import DeleteCsrById
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs.post import GenerateCsrForApplication
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys_generate.post import GenerateX509Certificate
from okta_python_sdk.paths.api_v1_apps_app_id.get import GetById
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id.get import GetClientSecret
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs_csr_id.get import GetCredentialsCsrs
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default.get import GetDefaultProvisioningConnection
from okta_python_sdk.paths.api_v1_apps_app_id_features_name.get import GetFeature
from okta_python_sdk.paths.api_v1_apps_app_id_groups_group_id.get import GetGroupAssignment
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys_key_id.get import GetKeyCredential
from okta_python_sdk.paths.api_v1_apps_app_id_grants_grant_id.get import GetSingleScopeConsentGrant
from okta_python_sdk.paths.api_v1_apps_app_id_users_user_id.get import GetSpecificUserAssignment
from okta_python_sdk.paths.api_v1_apps_app_id_tokens_token_id.get import GetToken
from okta_python_sdk.paths.api_v1_apps_app_id_grants.post import GrantConsentToScope
from okta_python_sdk.paths.api_v1_apps.get import ListApps
from okta_python_sdk.paths.api_v1_apps_app_id_users.get import ListAssignedUsers
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets.get import ListClientSecrets
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs.get import ListCsrsForApplication
from okta_python_sdk.paths.api_v1_apps_app_id_features.get import ListFeatures
from okta_python_sdk.paths.api_v1_apps_app_id_groups.get import ListGroupsAssigned
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys.get import ListKeyCredentials
from okta_python_sdk.paths.api_v1_apps_app_id_grants.get import ListScopeConsentGrants
from okta_python_sdk.paths.api_v1_apps_app_id_tokens.get import ListTokens
from okta_python_sdk.paths.api_v1_apps_app_id_sso_saml_metadata.get import PreviewSamlAppMetadata
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs_csr_id_lifecycle_publish.post import PublishCsrLifecycle
from okta_python_sdk.paths.api_v1_apps_app_id_groups_group_id.delete import RemoveGroupAssignment
from okta_python_sdk.paths.api_v1_apps_app_id.delete import RemoveInactive
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id.delete import RemoveSecret
from okta_python_sdk.paths.api_v1_apps_app_id_users_user_id.delete import RemoveUserFrom
from okta_python_sdk.paths.api_v1_apps_app_id_tokens.delete import RevokeAllTokens
from okta_python_sdk.paths.api_v1_apps_app_id_grants_grant_id.delete import RevokePermission
from okta_python_sdk.paths.api_v1_apps_app_id_tokens_token_id.delete import RevokeToken
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default.post import SetDefaultProvisioningConnection
from okta_python_sdk.paths.api_v1_apps_app_id.put import UpdateApplicationInOrg
from okta_python_sdk.paths.api_v1_apps_app_id_features_name.put import UpdateFeature
from okta_python_sdk.paths.api_v1_apps_app_id_logo.post import UpdateLogo
from okta_python_sdk.paths.api_v1_apps_app_id_users_user_id.post import UpdateProfileForUser
from okta_python_sdk.apis.tags.application_api_raw import ApplicationApiRaw


class ApplicationApi(
    ActivateClientSecret,
    ActivateDefaultProvisioningConnection,
    ActivateInactive,
    AddClientSecret,
    AssignGroupTo,
    AssignPolicyToApplication,
    AssignUserToApplication,
    CloneApplicationKeyCredential,
    CreateNew,
    DeactivateClientSecretById,
    DeactivateDefaultProvisioningConnection,
    DeactivateLifecycle,
    DeleteCsrById,
    GenerateCsrForApplication,
    GenerateX509Certificate,
    GetById,
    GetClientSecret,
    GetCredentialsCsrs,
    GetDefaultProvisioningConnection,
    GetFeature,
    GetGroupAssignment,
    GetKeyCredential,
    GetSingleScopeConsentGrant,
    GetSpecificUserAssignment,
    GetToken,
    GrantConsentToScope,
    ListApps,
    ListAssignedUsers,
    ListClientSecrets,
    ListCsrsForApplication,
    ListFeatures,
    ListGroupsAssigned,
    ListKeyCredentials,
    ListScopeConsentGrants,
    ListTokens,
    PreviewSamlAppMetadata,
    PublishCsrLifecycle,
    RemoveGroupAssignment,
    RemoveInactive,
    RemoveSecret,
    RemoveUserFrom,
    RevokeAllTokens,
    RevokePermission,
    RevokeToken,
    SetDefaultProvisioningConnection,
    UpdateApplicationInOrg,
    UpdateFeature,
    UpdateLogo,
    UpdateProfileForUser,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ApplicationApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ApplicationApiRaw(api_client)

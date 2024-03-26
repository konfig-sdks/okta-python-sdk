# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id_lifecycle_activate.post import ActivateClientSecretRaw
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default_lifecycle_activate.post import ActivateDefaultProvisioningConnectionRaw
from okta_python_sdk.paths.api_v1_apps_app_id_lifecycle_activate.post import ActivateInactiveRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets.post import AddClientSecretRaw
from okta_python_sdk.paths.api_v1_apps_app_id_groups_group_id.put import AssignGroupToRaw
from okta_python_sdk.paths.api_v1_apps_app_id_policies_policy_id.put import AssignPolicyToApplicationRaw
from okta_python_sdk.paths.api_v1_apps_app_id_users.post import AssignUserToApplicationRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys_key_id_clone.post import CloneApplicationKeyCredentialRaw
from okta_python_sdk.paths.api_v1_apps.post import CreateNewRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id_lifecycle_deactivate.post import DeactivateClientSecretByIdRaw
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default_lifecycle_deactivate.post import DeactivateDefaultProvisioningConnectionRaw
from okta_python_sdk.paths.api_v1_apps_app_id_lifecycle_deactivate.post import DeactivateLifecycleRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs_csr_id.delete import DeleteCsrByIdRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs.post import GenerateCsrForApplicationRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys_generate.post import GenerateX509CertificateRaw
from okta_python_sdk.paths.api_v1_apps_app_id.get import GetByIdRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id.get import GetClientSecretRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs_csr_id.get import GetCredentialsCsrsRaw
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default.get import GetDefaultProvisioningConnectionRaw
from okta_python_sdk.paths.api_v1_apps_app_id_features_name.get import GetFeatureRaw
from okta_python_sdk.paths.api_v1_apps_app_id_groups_group_id.get import GetGroupAssignmentRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys_key_id.get import GetKeyCredentialRaw
from okta_python_sdk.paths.api_v1_apps_app_id_grants_grant_id.get import GetSingleScopeConsentGrantRaw
from okta_python_sdk.paths.api_v1_apps_app_id_users_user_id.get import GetSpecificUserAssignmentRaw
from okta_python_sdk.paths.api_v1_apps_app_id_tokens_token_id.get import GetTokenRaw
from okta_python_sdk.paths.api_v1_apps_app_id_grants.post import GrantConsentToScopeRaw
from okta_python_sdk.paths.api_v1_apps.get import ListAppsRaw
from okta_python_sdk.paths.api_v1_apps_app_id_users.get import ListAssignedUsersRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets.get import ListClientSecretsRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs.get import ListCsrsForApplicationRaw
from okta_python_sdk.paths.api_v1_apps_app_id_features.get import ListFeaturesRaw
from okta_python_sdk.paths.api_v1_apps_app_id_groups.get import ListGroupsAssignedRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_keys.get import ListKeyCredentialsRaw
from okta_python_sdk.paths.api_v1_apps_app_id_grants.get import ListScopeConsentGrantsRaw
from okta_python_sdk.paths.api_v1_apps_app_id_tokens.get import ListTokensRaw
from okta_python_sdk.paths.api_v1_apps_app_id_sso_saml_metadata.get import PreviewSamlAppMetadataRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_csrs_csr_id_lifecycle_publish.post import PublishCsrLifecycleRaw
from okta_python_sdk.paths.api_v1_apps_app_id_groups_group_id.delete import RemoveGroupAssignmentRaw
from okta_python_sdk.paths.api_v1_apps_app_id.delete import RemoveInactiveRaw
from okta_python_sdk.paths.api_v1_apps_app_id_credentials_secrets_secret_id.delete import RemoveSecretRaw
from okta_python_sdk.paths.api_v1_apps_app_id_users_user_id.delete import RemoveUserFromRaw
from okta_python_sdk.paths.api_v1_apps_app_id_tokens.delete import RevokeAllTokensRaw
from okta_python_sdk.paths.api_v1_apps_app_id_grants_grant_id.delete import RevokePermissionRaw
from okta_python_sdk.paths.api_v1_apps_app_id_tokens_token_id.delete import RevokeTokenRaw
from okta_python_sdk.paths.api_v1_apps_app_id_connections_default.post import SetDefaultProvisioningConnectionRaw
from okta_python_sdk.paths.api_v1_apps_app_id.put import UpdateApplicationInOrgRaw
from okta_python_sdk.paths.api_v1_apps_app_id_features_name.put import UpdateFeatureRaw
from okta_python_sdk.paths.api_v1_apps_app_id_logo.post import UpdateLogoRaw
from okta_python_sdk.paths.api_v1_apps_app_id_users_user_id.post import UpdateProfileForUserRaw


class ApplicationApiRaw(
    ActivateClientSecretRaw,
    ActivateDefaultProvisioningConnectionRaw,
    ActivateInactiveRaw,
    AddClientSecretRaw,
    AssignGroupToRaw,
    AssignPolicyToApplicationRaw,
    AssignUserToApplicationRaw,
    CloneApplicationKeyCredentialRaw,
    CreateNewRaw,
    DeactivateClientSecretByIdRaw,
    DeactivateDefaultProvisioningConnectionRaw,
    DeactivateLifecycleRaw,
    DeleteCsrByIdRaw,
    GenerateCsrForApplicationRaw,
    GenerateX509CertificateRaw,
    GetByIdRaw,
    GetClientSecretRaw,
    GetCredentialsCsrsRaw,
    GetDefaultProvisioningConnectionRaw,
    GetFeatureRaw,
    GetGroupAssignmentRaw,
    GetKeyCredentialRaw,
    GetSingleScopeConsentGrantRaw,
    GetSpecificUserAssignmentRaw,
    GetTokenRaw,
    GrantConsentToScopeRaw,
    ListAppsRaw,
    ListAssignedUsersRaw,
    ListClientSecretsRaw,
    ListCsrsForApplicationRaw,
    ListFeaturesRaw,
    ListGroupsAssignedRaw,
    ListKeyCredentialsRaw,
    ListScopeConsentGrantsRaw,
    ListTokensRaw,
    PreviewSamlAppMetadataRaw,
    PublishCsrLifecycleRaw,
    RemoveGroupAssignmentRaw,
    RemoveInactiveRaw,
    RemoveSecretRaw,
    RemoveUserFromRaw,
    RevokeAllTokensRaw,
    RevokePermissionRaw,
    RevokeTokenRaw,
    SetDefaultProvisioningConnectionRaw,
    UpdateApplicationInOrgRaw,
    UpdateFeatureRaw,
    UpdateLogoRaw,
    UpdateProfileForUserRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_activate.post import ActivateLifecycleRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name_application_id.put import AddAppInstanceTargetToAppAdministratorRoleGivenToUserRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles.post import AssignRoleRaw
from okta_python_sdk.paths.api_v1_users_user_id_credentials_change_password.post import ChangePasswordValidationRaw
from okta_python_sdk.paths.api_v1_users.post import CreateNewUserRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_deactivate.post import DeactivateLifecycleRaw
from okta_python_sdk.paths.api_v1_users_user_id_linked_objects_relationship_name.delete import DeleteLinkedObjectsRaw
from okta_python_sdk.paths.api_v1_users_user_id.delete import DeletePermanentlyRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name.delete import DeleteTargetAppRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_expire_passwordtemp_passwordfalse.post import ExpirePasswordAndGetTemporaryPasswordRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_expire_passwordtemp_passwordtrue.post import ExpirePasswordAndTemporaryPasswordRaw
from okta_python_sdk.paths.api_v1_users_user_id_credentials_forgot_password.post import ForgotPasswordRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_reset_password.post import GeneratePasswordResetTokenRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id.get import GetAssignedRoleRaw
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens_token_id.get import GetClientRefreshTokenRaw
from okta_python_sdk.paths.api_v1_users_user_id_grants_grant_id.get import GetGrantByIdRaw
from okta_python_sdk.paths.api_v1_users_user_id_linked_objects_relationship_name.get import GetLinkedObjectsRaw
from okta_python_sdk.paths.api_v1_users_user_id_groups.get import GetMemberGroupsRaw
from okta_python_sdk.paths.api_v1_users_user_id.get import GetOktaUserRaw
from okta_python_sdk.paths.api_v1_users_user_id_subscriptions_notification_type.get import GetSubscriptionByNotificationRaw
from okta_python_sdk.paths.api_v1_users.get import ListActiveUsersRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps.get import ListAppTargetsForRoleRaw
from okta_python_sdk.paths.api_v1_users_user_id_app_links.get import ListAssignedAppLinksRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles.get import ListAssignedRolesRaw
from okta_python_sdk.paths.api_v1_users_user_id_clients.get import ListClientsRaw
from okta_python_sdk.paths.api_v1_users_user_id_grants.get import ListGrantsRaw
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_grants.get import ListGrantsForClientRaw
from okta_python_sdk.paths.api_v1_users_user_id_idps.get import ListIdpsForUserRaw
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens.get import ListRefreshTokensForUserAndClientRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_groups.get import ListRoleTargetsGroupsRaw
from okta_python_sdk.paths.api_v1_users_user_id_subscriptions.get import ListSubscriptionsRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_reactivate.post import ReactivateUserRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name_application_id.delete import RemoveAppInstanceTargetToAppAdministratorRoleGivenToRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_groups_group_id.delete import RemoveTargetGroupRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_reset_factors.post import ResetFactorsOperationRaw
from okta_python_sdk.paths.api_v1_users_user_id_sessions.delete import RevokeAllSessionsRaw
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens.delete import RevokeAllTokensRaw
from okta_python_sdk.paths.api_v1_users_user_id_grants_grant_id.delete import RevokeGrantRaw
from okta_python_sdk.paths.api_v1_users_user_id_grants.delete import RevokeGrantsRaw
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_grants.delete import RevokeGrantsForUserAndClientRaw
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens_token_id.delete import RevokeTokenForClientRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_suspend.post import SuspendLifecycleRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id.delete import UnassignRoleRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_unlock.post import UnlockUserStatusRaw
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_unsuspend.post import UnsuspendLifecycleRaw
from okta_python_sdk.paths.api_v1_users_associated_user_id_linked_objects_primary_relationship_name_primary_user_id.put import UpdateLinkedObjectRaw
from okta_python_sdk.paths.api_v1_users_user_id.put import UpdateProfileRaw
from okta_python_sdk.paths.api_v1_users_user_id.post import UpdateProfile0Raw
from okta_python_sdk.paths.api_v1_users_user_id_credentials_change_recovery_question.post import UpdateRecoveryQuestionRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps.put import UpdateRolesCatalogAppsRaw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name.put import UpdateRolesCatalogApps0Raw
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_groups_group_id.put import UpdateRolesCatalogApps1Raw


class UserApiRaw(
    ActivateLifecycleRaw,
    AddAppInstanceTargetToAppAdministratorRoleGivenToUserRaw,
    AssignRoleRaw,
    ChangePasswordValidationRaw,
    CreateNewUserRaw,
    DeactivateLifecycleRaw,
    DeleteLinkedObjectsRaw,
    DeletePermanentlyRaw,
    DeleteTargetAppRaw,
    ExpirePasswordAndGetTemporaryPasswordRaw,
    ExpirePasswordAndTemporaryPasswordRaw,
    ForgotPasswordRaw,
    GeneratePasswordResetTokenRaw,
    GetAssignedRoleRaw,
    GetClientRefreshTokenRaw,
    GetGrantByIdRaw,
    GetLinkedObjectsRaw,
    GetMemberGroupsRaw,
    GetOktaUserRaw,
    GetSubscriptionByNotificationRaw,
    ListActiveUsersRaw,
    ListAppTargetsForRoleRaw,
    ListAssignedAppLinksRaw,
    ListAssignedRolesRaw,
    ListClientsRaw,
    ListGrantsRaw,
    ListGrantsForClientRaw,
    ListIdpsForUserRaw,
    ListRefreshTokensForUserAndClientRaw,
    ListRoleTargetsGroupsRaw,
    ListSubscriptionsRaw,
    ReactivateUserRaw,
    RemoveAppInstanceTargetToAppAdministratorRoleGivenToRaw,
    RemoveTargetGroupRaw,
    ResetFactorsOperationRaw,
    RevokeAllSessionsRaw,
    RevokeAllTokensRaw,
    RevokeGrantRaw,
    RevokeGrantsRaw,
    RevokeGrantsForUserAndClientRaw,
    RevokeTokenForClientRaw,
    SuspendLifecycleRaw,
    UnassignRoleRaw,
    UnlockUserStatusRaw,
    UnsuspendLifecycleRaw,
    UpdateLinkedObjectRaw,
    UpdateProfileRaw,
    UpdateProfile0Raw,
    UpdateRecoveryQuestionRaw,
    UpdateRolesCatalogAppsRaw,
    UpdateRolesCatalogApps0Raw,
    UpdateRolesCatalogApps1Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

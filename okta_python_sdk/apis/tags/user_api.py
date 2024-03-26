# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_activate.post import ActivateLifecycle
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name_application_id.put import AddAppInstanceTargetToAppAdministratorRoleGivenToUser
from okta_python_sdk.paths.api_v1_users_user_id_roles.post import AssignRole
from okta_python_sdk.paths.api_v1_users_user_id_credentials_change_password.post import ChangePasswordValidation
from okta_python_sdk.paths.api_v1_users.post import CreateNewUser
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_deactivate.post import DeactivateLifecycle
from okta_python_sdk.paths.api_v1_users_user_id_linked_objects_relationship_name.delete import DeleteLinkedObjects
from okta_python_sdk.paths.api_v1_users_user_id.delete import DeletePermanently
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name.delete import DeleteTargetApp
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_expire_passwordtemp_passwordfalse.post import ExpirePasswordAndGetTemporaryPassword
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_expire_passwordtemp_passwordtrue.post import ExpirePasswordAndTemporaryPassword
from okta_python_sdk.paths.api_v1_users_user_id_credentials_forgot_password.post import ForgotPassword
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_reset_password.post import GeneratePasswordResetToken
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id.get import GetAssignedRole
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens_token_id.get import GetClientRefreshToken
from okta_python_sdk.paths.api_v1_users_user_id_grants_grant_id.get import GetGrantById
from okta_python_sdk.paths.api_v1_users_user_id_linked_objects_relationship_name.get import GetLinkedObjects
from okta_python_sdk.paths.api_v1_users_user_id_groups.get import GetMemberGroups
from okta_python_sdk.paths.api_v1_users_user_id.get import GetOktaUser
from okta_python_sdk.paths.api_v1_users_user_id_subscriptions_notification_type.get import GetSubscriptionByNotification
from okta_python_sdk.paths.api_v1_users.get import ListActiveUsers
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps.get import ListAppTargetsForRole
from okta_python_sdk.paths.api_v1_users_user_id_app_links.get import ListAssignedAppLinks
from okta_python_sdk.paths.api_v1_users_user_id_roles.get import ListAssignedRoles
from okta_python_sdk.paths.api_v1_users_user_id_clients.get import ListClients
from okta_python_sdk.paths.api_v1_users_user_id_grants.get import ListGrants
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_grants.get import ListGrantsForClient
from okta_python_sdk.paths.api_v1_users_user_id_idps.get import ListIdpsForUser
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens.get import ListRefreshTokensForUserAndClient
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_groups.get import ListRoleTargetsGroups
from okta_python_sdk.paths.api_v1_users_user_id_subscriptions.get import ListSubscriptions
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_reactivate.post import ReactivateUser
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name_application_id.delete import RemoveAppInstanceTargetToAppAdministratorRoleGivenTo
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_groups_group_id.delete import RemoveTargetGroup
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_reset_factors.post import ResetFactorsOperation
from okta_python_sdk.paths.api_v1_users_user_id_sessions.delete import RevokeAllSessions
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens.delete import RevokeAllTokens
from okta_python_sdk.paths.api_v1_users_user_id_grants_grant_id.delete import RevokeGrant
from okta_python_sdk.paths.api_v1_users_user_id_grants.delete import RevokeGrants
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_grants.delete import RevokeGrantsForUserAndClient
from okta_python_sdk.paths.api_v1_users_user_id_clients_client_id_tokens_token_id.delete import RevokeTokenForClient
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_suspend.post import SuspendLifecycle
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id.delete import UnassignRole
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_unlock.post import UnlockUserStatus
from okta_python_sdk.paths.api_v1_users_user_id_lifecycle_unsuspend.post import UnsuspendLifecycle
from okta_python_sdk.paths.api_v1_users_associated_user_id_linked_objects_primary_relationship_name_primary_user_id.put import UpdateLinkedObject
from okta_python_sdk.paths.api_v1_users_user_id.put import UpdateProfile
from okta_python_sdk.paths.api_v1_users_user_id.post import UpdateProfile0
from okta_python_sdk.paths.api_v1_users_user_id_credentials_change_recovery_question.post import UpdateRecoveryQuestion
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps.put import UpdateRolesCatalogApps
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_catalog_apps_app_name.put import UpdateRolesCatalogApps0
from okta_python_sdk.paths.api_v1_users_user_id_roles_role_id_targets_groups_group_id.put import UpdateRolesCatalogApps1
from okta_python_sdk.apis.tags.user_api_raw import UserApiRaw


class UserApi(
    ActivateLifecycle,
    AddAppInstanceTargetToAppAdministratorRoleGivenToUser,
    AssignRole,
    ChangePasswordValidation,
    CreateNewUser,
    DeactivateLifecycle,
    DeleteLinkedObjects,
    DeletePermanently,
    DeleteTargetApp,
    ExpirePasswordAndGetTemporaryPassword,
    ExpirePasswordAndTemporaryPassword,
    ForgotPassword,
    GeneratePasswordResetToken,
    GetAssignedRole,
    GetClientRefreshToken,
    GetGrantById,
    GetLinkedObjects,
    GetMemberGroups,
    GetOktaUser,
    GetSubscriptionByNotification,
    ListActiveUsers,
    ListAppTargetsForRole,
    ListAssignedAppLinks,
    ListAssignedRoles,
    ListClients,
    ListGrants,
    ListGrantsForClient,
    ListIdpsForUser,
    ListRefreshTokensForUserAndClient,
    ListRoleTargetsGroups,
    ListSubscriptions,
    ReactivateUser,
    RemoveAppInstanceTargetToAppAdministratorRoleGivenTo,
    RemoveTargetGroup,
    ResetFactorsOperation,
    RevokeAllSessions,
    RevokeAllTokens,
    RevokeGrant,
    RevokeGrants,
    RevokeGrantsForUserAndClient,
    RevokeTokenForClient,
    SuspendLifecycle,
    UnassignRole,
    UnlockUserStatus,
    UnsuspendLifecycle,
    UpdateLinkedObject,
    UpdateProfile,
    UpdateProfile0,
    UpdateRecoveryQuestion,
    UpdateRolesCatalogApps,
    UpdateRolesCatalogApps0,
    UpdateRolesCatalogApps1,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UserApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UserApiRaw(api_client)

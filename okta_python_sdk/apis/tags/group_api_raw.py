# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_groups_rules_rule_id_lifecycle_activate.post import ActivateRuleLifecycleRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_catalog_apps_app_name_application_id.put import AddAppInstanceTargetToAppAdminRoleGivenToGroupRaw
from okta_python_sdk.paths.api_v1_groups_rules.post import AddRuleRaw
from okta_python_sdk.paths.api_v1_groups_group_id_users_user_id.put import AddUserToGroupRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles.post import AssignRoleToGroupRaw
from okta_python_sdk.paths.api_v1_groups.post import CreateNewGroupRaw
from okta_python_sdk.paths.api_v1_groups_rules_rule_id_lifecycle_deactivate.post import DeactivateRuleLifecycleRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_catalog_apps_app_name.delete import DeleteTargetGroupRolesCatalogAppsRaw
from okta_python_sdk.paths.api_v1_groups_group_id_users.get import EnumerateGroupMembersRaw
from okta_python_sdk.paths.api_v1_groups_rules.get import GetAllRulesRaw
from okta_python_sdk.paths.api_v1_groups_rules_rule_id.get import GetGroupRuleByIdRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles.get import GetRoleListRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id.get import GetRoleSuccessRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_catalog_apps.get import GetRoleTargetsCatalogAppsRaw
from okta_python_sdk.paths.api_v1_groups_group_id.get import GetRulesRaw
from okta_python_sdk.paths.api_v1_groups.get import ListRaw
from okta_python_sdk.paths.api_v1_groups_group_id_apps.get import ListAssignedAppsRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_groups.get import ListRoleTargetsGroupsRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_catalog_apps_app_name_application_id.delete import RemoveAppInstanceTargetToAppAdminRoleGivenToGroupRaw
from okta_python_sdk.paths.api_v1_groups_group_id.delete import RemoveOperationRaw
from okta_python_sdk.paths.api_v1_groups_rules_rule_id.delete import RemoveRuleByIdRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_groups_target_group_id.delete import RemoveTargetGroupRaw
from okta_python_sdk.paths.api_v1_groups_group_id_users_user_id.delete import RemoveUserFromRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id.delete import UnassignRoleRaw
from okta_python_sdk.paths.api_v1_groups_group_id.put import UpdateProfileRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_catalog_apps_app_name.put import UpdateRolesCatalogAppsRaw
from okta_python_sdk.paths.api_v1_groups_rules_rule_id.put import UpdateRuleRaw
from okta_python_sdk.paths.api_v1_groups_group_id_roles_role_id_targets_groups_target_group_id.put import UpdateTargetGroupsRoleRaw


class GroupApiRaw(
    ActivateRuleLifecycleRaw,
    AddAppInstanceTargetToAppAdminRoleGivenToGroupRaw,
    AddRuleRaw,
    AddUserToGroupRaw,
    AssignRoleToGroupRaw,
    CreateNewGroupRaw,
    DeactivateRuleLifecycleRaw,
    DeleteTargetGroupRolesCatalogAppsRaw,
    EnumerateGroupMembersRaw,
    GetAllRulesRaw,
    GetGroupRuleByIdRaw,
    GetRoleListRaw,
    GetRoleSuccessRaw,
    GetRoleTargetsCatalogAppsRaw,
    GetRulesRaw,
    ListRaw,
    ListAssignedAppsRaw,
    ListRoleTargetsGroupsRaw,
    RemoveAppInstanceTargetToAppAdminRoleGivenToGroupRaw,
    RemoveOperationRaw,
    RemoveRuleByIdRaw,
    RemoveTargetGroupRaw,
    RemoveUserFromRaw,
    UnassignRoleRaw,
    UpdateProfileRaw,
    UpdateRolesCatalogAppsRaw,
    UpdateRuleRaw,
    UpdateTargetGroupsRoleRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

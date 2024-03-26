# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_lifecycle_activate.post import ActivateLifecycleSuccessRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_lifecycle_activate.post import ActivatePolicyLifecycleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id_lifecycle_activate.post import ActivatePolicyRuleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims.post import CreateClaimsRaw
from okta_python_sdk.paths.api_v1_authorization_servers.post import CreateNewServerRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies.post import CreatePolicyRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules.post import CreatePolicyRuleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes.post import CreateScopeRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_lifecycle_deactivate.post import DeactivateLifecycleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_lifecycle_deactivate.post import DeactivatePolicyLifecycleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id_lifecycle_deactivate.post import DeactivatePolicyRuleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens_token_id.delete import DeleteAuthTokenRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims_claim_id.delete import DeleteClaimRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens.delete import DeleteClientTokenRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id.delete import DeletePolicyByIdRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id.delete import DeletePolicyRuleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes_scope_id.delete import DeleteScopeRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id.delete import DeleteSuccessRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules.get import EnumeratePolicyRulesRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id.get import GetByIdRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims.get import GetClaimsRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims_claim_id.get import GetClaims0Raw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens_token_id.get import GetClientAuthTokenRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens.get import GetClientTokensRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id.get import GetPoliciesRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies.get import GetPoliciesSuccessRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id.get import GetPolicyRuleByIdRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes.get import GetScopesRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes_scope_id.get import GetScopes0Raw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients.get import ListClientsRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_credentials_keys.get import ListCredentialsKeysRaw
from okta_python_sdk.paths.api_v1_authorization_servers.get import ListServersRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_credentials_lifecycle_key_rotate.post import RotateKeyLifecycleRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id.put import UpdateByIdRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims_claim_id.put import UpdateClaimSuccessRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id.put import UpdatePolicyRuleConfigurationRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id.put import UpdatePolicySuccessRaw
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes_scope_id.put import UpdateScopeSuccessRaw


class AuthorizationServerApiRaw(
    ActivateLifecycleSuccessRaw,
    ActivatePolicyLifecycleRaw,
    ActivatePolicyRuleRaw,
    CreateClaimsRaw,
    CreateNewServerRaw,
    CreatePolicyRaw,
    CreatePolicyRuleRaw,
    CreateScopeRaw,
    DeactivateLifecycleRaw,
    DeactivatePolicyLifecycleRaw,
    DeactivatePolicyRuleRaw,
    DeleteAuthTokenRaw,
    DeleteClaimRaw,
    DeleteClientTokenRaw,
    DeletePolicyByIdRaw,
    DeletePolicyRuleRaw,
    DeleteScopeRaw,
    DeleteSuccessRaw,
    EnumeratePolicyRulesRaw,
    GetByIdRaw,
    GetClaimsRaw,
    GetClaims0Raw,
    GetClientAuthTokenRaw,
    GetClientTokensRaw,
    GetPoliciesRaw,
    GetPoliciesSuccessRaw,
    GetPolicyRuleByIdRaw,
    GetScopesRaw,
    GetScopes0Raw,
    ListClientsRaw,
    ListCredentialsKeysRaw,
    ListServersRaw,
    RotateKeyLifecycleRaw,
    UpdateByIdRaw,
    UpdateClaimSuccessRaw,
    UpdatePolicyRuleConfigurationRaw,
    UpdatePolicySuccessRaw,
    UpdateScopeSuccessRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass

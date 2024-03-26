# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_lifecycle_activate.post import ActivateLifecycleSuccess
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_lifecycle_activate.post import ActivatePolicyLifecycle
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id_lifecycle_activate.post import ActivatePolicyRule
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims.post import CreateClaims
from okta_python_sdk.paths.api_v1_authorization_servers.post import CreateNewServer
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies.post import CreatePolicy
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules.post import CreatePolicyRule
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes.post import CreateScope
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_lifecycle_deactivate.post import DeactivateLifecycle
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_lifecycle_deactivate.post import DeactivatePolicyLifecycle
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id_lifecycle_deactivate.post import DeactivatePolicyRule
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens_token_id.delete import DeleteAuthToken
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims_claim_id.delete import DeleteClaim
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens.delete import DeleteClientToken
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id.delete import DeletePolicyById
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id.delete import DeletePolicyRule
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes_scope_id.delete import DeleteScope
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id.delete import DeleteSuccess
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules.get import EnumeratePolicyRules
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id.get import GetById
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims.get import GetClaims
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims_claim_id.get import GetClaims0
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens_token_id.get import GetClientAuthToken
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients_client_id_tokens.get import GetClientTokens
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id.get import GetPolicies
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies.get import GetPoliciesSuccess
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id.get import GetPolicyRuleById
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes.get import GetScopes
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes_scope_id.get import GetScopes0
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_clients.get import ListClients
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_credentials_keys.get import ListCredentialsKeys
from okta_python_sdk.paths.api_v1_authorization_servers.get import ListServers
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_credentials_lifecycle_key_rotate.post import RotateKeyLifecycle
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id.put import UpdateById
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_claims_claim_id.put import UpdateClaimSuccess
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id_rules_rule_id.put import UpdatePolicyRuleConfiguration
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_policies_policy_id.put import UpdatePolicySuccess
from okta_python_sdk.paths.api_v1_authorization_servers_auth_server_id_scopes_scope_id.put import UpdateScopeSuccess
from okta_python_sdk.apis.tags.authorization_server_api_raw import AuthorizationServerApiRaw


class AuthorizationServerApi(
    ActivateLifecycleSuccess,
    ActivatePolicyLifecycle,
    ActivatePolicyRule,
    CreateClaims,
    CreateNewServer,
    CreatePolicy,
    CreatePolicyRule,
    CreateScope,
    DeactivateLifecycle,
    DeactivatePolicyLifecycle,
    DeactivatePolicyRule,
    DeleteAuthToken,
    DeleteClaim,
    DeleteClientToken,
    DeletePolicyById,
    DeletePolicyRule,
    DeleteScope,
    DeleteSuccess,
    EnumeratePolicyRules,
    GetById,
    GetClaims,
    GetClaims0,
    GetClientAuthToken,
    GetClientTokens,
    GetPolicies,
    GetPoliciesSuccess,
    GetPolicyRuleById,
    GetScopes,
    GetScopes0,
    ListClients,
    ListCredentialsKeys,
    ListServers,
    RotateKeyLifecycle,
    UpdateById,
    UpdateClaimSuccess,
    UpdatePolicyRuleConfiguration,
    UpdatePolicySuccess,
    UpdateScopeSuccess,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AuthorizationServerApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AuthorizationServerApiRaw(api_client)

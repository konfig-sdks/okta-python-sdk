# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from okta_python_sdk.type.app_and_instance_policy_rule_condition import AppAndInstancePolicyRuleCondition
from okta_python_sdk.type.app_instance_policy_rule_condition import AppInstancePolicyRuleCondition
from okta_python_sdk.type.before_scheduled_action_policy_rule_condition import BeforeScheduledActionPolicyRuleCondition
from okta_python_sdk.type.client_policy_condition import ClientPolicyCondition
from okta_python_sdk.type.context_policy_rule_condition import ContextPolicyRuleCondition
from okta_python_sdk.type.device_policy_rule_condition import DevicePolicyRuleCondition
from okta_python_sdk.type.grant_type_policy_rule_condition import GrantTypePolicyRuleCondition
from okta_python_sdk.type.group_policy_rule_condition import GroupPolicyRuleCondition
from okta_python_sdk.type.identity_provider_policy_rule_condition import IdentityProviderPolicyRuleCondition
from okta_python_sdk.type.mdm_enrollment_policy_rule_condition import MDMEnrollmentPolicyRuleCondition
from okta_python_sdk.type.o_auth2_scopes_mediation_policy_rule_condition import OAuth2ScopesMediationPolicyRuleCondition
from okta_python_sdk.type.password_policy_authentication_provider_condition import PasswordPolicyAuthenticationProviderCondition
from okta_python_sdk.type.platform_policy_rule_condition import PlatformPolicyRuleCondition
from okta_python_sdk.type.policy_network_condition import PolicyNetworkCondition
from okta_python_sdk.type.policy_people_condition import PolicyPeopleCondition
from okta_python_sdk.type.policy_rule_auth_context_condition import PolicyRuleAuthContextCondition
from okta_python_sdk.type.risk_policy_rule_condition import RiskPolicyRuleCondition
from okta_python_sdk.type.risk_score_policy_rule_condition import RiskScorePolicyRuleCondition
from okta_python_sdk.type.user_identifier_policy_rule_condition import UserIdentifierPolicyRuleCondition
from okta_python_sdk.type.user_policy_rule_condition import UserPolicyRuleCondition
from okta_python_sdk.type.user_status_policy_rule_condition import UserStatusPolicyRuleCondition

class RequiredPolicyRuleConditions(TypedDict):
    pass

class OptionalPolicyRuleConditions(TypedDict, total=False):
    app: AppAndInstancePolicyRuleCondition

    apps: AppInstancePolicyRuleCondition

    authContext: PolicyRuleAuthContextCondition

    authProvider: PasswordPolicyAuthenticationProviderCondition

    beforeScheduledAction: BeforeScheduledActionPolicyRuleCondition

    clients: ClientPolicyCondition

    context: ContextPolicyRuleCondition

    device: DevicePolicyRuleCondition

    grantTypes: GrantTypePolicyRuleCondition

    groups: GroupPolicyRuleCondition

    identityProvider: IdentityProviderPolicyRuleCondition

    mdmEnrollment: MDMEnrollmentPolicyRuleCondition

    network: PolicyNetworkCondition

    people: PolicyPeopleCondition

    platform: PlatformPolicyRuleCondition

    risk: RiskPolicyRuleCondition

    riskScore: RiskScorePolicyRuleCondition

    scopes: OAuth2ScopesMediationPolicyRuleCondition

    userIdentifier: UserIdentifierPolicyRuleCondition

    userStatus: UserStatusPolicyRuleCondition

    users: UserPolicyRuleCondition

class PolicyRuleConditions(RequiredPolicyRuleConditions, OptionalPolicyRuleConditions):
    pass

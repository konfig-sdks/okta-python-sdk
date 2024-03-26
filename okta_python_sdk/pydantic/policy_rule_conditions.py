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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from okta_python_sdk.pydantic.app_and_instance_policy_rule_condition import AppAndInstancePolicyRuleCondition
from okta_python_sdk.pydantic.app_instance_policy_rule_condition import AppInstancePolicyRuleCondition
from okta_python_sdk.pydantic.before_scheduled_action_policy_rule_condition import BeforeScheduledActionPolicyRuleCondition
from okta_python_sdk.pydantic.client_policy_condition import ClientPolicyCondition
from okta_python_sdk.pydantic.context_policy_rule_condition import ContextPolicyRuleCondition
from okta_python_sdk.pydantic.device_policy_rule_condition import DevicePolicyRuleCondition
from okta_python_sdk.pydantic.grant_type_policy_rule_condition import GrantTypePolicyRuleCondition
from okta_python_sdk.pydantic.group_policy_rule_condition import GroupPolicyRuleCondition
from okta_python_sdk.pydantic.identity_provider_policy_rule_condition import IdentityProviderPolicyRuleCondition
from okta_python_sdk.pydantic.mdm_enrollment_policy_rule_condition import MDMEnrollmentPolicyRuleCondition
from okta_python_sdk.pydantic.o_auth2_scopes_mediation_policy_rule_condition import OAuth2ScopesMediationPolicyRuleCondition
from okta_python_sdk.pydantic.password_policy_authentication_provider_condition import PasswordPolicyAuthenticationProviderCondition
from okta_python_sdk.pydantic.platform_policy_rule_condition import PlatformPolicyRuleCondition
from okta_python_sdk.pydantic.policy_network_condition import PolicyNetworkCondition
from okta_python_sdk.pydantic.policy_people_condition import PolicyPeopleCondition
from okta_python_sdk.pydantic.policy_rule_auth_context_condition import PolicyRuleAuthContextCondition
from okta_python_sdk.pydantic.risk_policy_rule_condition import RiskPolicyRuleCondition
from okta_python_sdk.pydantic.risk_score_policy_rule_condition import RiskScorePolicyRuleCondition
from okta_python_sdk.pydantic.user_identifier_policy_rule_condition import UserIdentifierPolicyRuleCondition
from okta_python_sdk.pydantic.user_policy_rule_condition import UserPolicyRuleCondition
from okta_python_sdk.pydantic.user_status_policy_rule_condition import UserStatusPolicyRuleCondition

class PolicyRuleConditions(BaseModel):
    app: typing.Optional[AppAndInstancePolicyRuleCondition] = Field(None, alias='app')

    apps: typing.Optional[AppInstancePolicyRuleCondition] = Field(None, alias='apps')

    auth_context: typing.Optional[PolicyRuleAuthContextCondition] = Field(None, alias='authContext')

    auth_provider: typing.Optional[PasswordPolicyAuthenticationProviderCondition] = Field(None, alias='authProvider')

    before_scheduled_action: typing.Optional[BeforeScheduledActionPolicyRuleCondition] = Field(None, alias='beforeScheduledAction')

    clients: typing.Optional[ClientPolicyCondition] = Field(None, alias='clients')

    context: typing.Optional[ContextPolicyRuleCondition] = Field(None, alias='context')

    device: typing.Optional[DevicePolicyRuleCondition] = Field(None, alias='device')

    grant_types: typing.Optional[GrantTypePolicyRuleCondition] = Field(None, alias='grantTypes')

    groups: typing.Optional[GroupPolicyRuleCondition] = Field(None, alias='groups')

    identity_provider: typing.Optional[IdentityProviderPolicyRuleCondition] = Field(None, alias='identityProvider')

    mdm_enrollment: typing.Optional[MDMEnrollmentPolicyRuleCondition] = Field(None, alias='mdmEnrollment')

    network: typing.Optional[PolicyNetworkCondition] = Field(None, alias='network')

    people: typing.Optional[PolicyPeopleCondition] = Field(None, alias='people')

    platform: typing.Optional[PlatformPolicyRuleCondition] = Field(None, alias='platform')

    risk: typing.Optional[RiskPolicyRuleCondition] = Field(None, alias='risk')

    risk_score: typing.Optional[RiskScorePolicyRuleCondition] = Field(None, alias='riskScore')

    scopes: typing.Optional[OAuth2ScopesMediationPolicyRuleCondition] = Field(None, alias='scopes')

    user_identifier: typing.Optional[UserIdentifierPolicyRuleCondition] = Field(None, alias='userIdentifier')

    user_status: typing.Optional[UserStatusPolicyRuleCondition] = Field(None, alias='userStatus')

    users: typing.Optional[UserPolicyRuleCondition] = Field(None, alias='users')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

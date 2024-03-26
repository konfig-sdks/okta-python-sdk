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

from okta_python_sdk.pydantic.pre_registration_inline_hook import PreRegistrationInlineHook
from okta_python_sdk.pydantic.profile_enrollment_policy_rule_action_target_group_ids import ProfileEnrollmentPolicyRuleActionTargetGroupIds
from okta_python_sdk.pydantic.profile_enrollment_policy_rule_activation_requirement import ProfileEnrollmentPolicyRuleActivationRequirement
from okta_python_sdk.pydantic.profile_enrollment_policy_rule_profile_attribute import ProfileEnrollmentPolicyRuleProfileAttribute

class ProfileEnrollmentPolicyRuleAction(BaseModel):
    access: typing.Optional[str] = Field(None, alias='access')

    activation_requirements: typing.Optional[ProfileEnrollmentPolicyRuleActivationRequirement] = Field(None, alias='activationRequirements')

    pre_registration_inline_hooks: typing.Optional[typing.List[PreRegistrationInlineHook]] = Field(None, alias='preRegistrationInlineHooks')

    profile_attributes: typing.Optional[typing.List[ProfileEnrollmentPolicyRuleProfileAttribute]] = Field(None, alias='profileAttributes')

    target_group_ids: typing.Optional[ProfileEnrollmentPolicyRuleActionTargetGroupIds] = Field(None, alias='targetGroupIds')

    ui_schema_id: typing.Optional[str] = Field(None, alias='uiSchemaId')

    unknown_user_action: typing.Optional[str] = Field(None, alias='unknownUserAction')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

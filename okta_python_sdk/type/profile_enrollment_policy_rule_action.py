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

from okta_python_sdk.type.pre_registration_inline_hook import PreRegistrationInlineHook
from okta_python_sdk.type.profile_enrollment_policy_rule_action_target_group_ids import ProfileEnrollmentPolicyRuleActionTargetGroupIds
from okta_python_sdk.type.profile_enrollment_policy_rule_activation_requirement import ProfileEnrollmentPolicyRuleActivationRequirement
from okta_python_sdk.type.profile_enrollment_policy_rule_profile_attribute import ProfileEnrollmentPolicyRuleProfileAttribute

class RequiredProfileEnrollmentPolicyRuleAction(TypedDict):
    pass

class OptionalProfileEnrollmentPolicyRuleAction(TypedDict, total=False):
    access: str

    activationRequirements: ProfileEnrollmentPolicyRuleActivationRequirement

    preRegistrationInlineHooks: typing.List[PreRegistrationInlineHook]

    profileAttributes: typing.List[ProfileEnrollmentPolicyRuleProfileAttribute]

    targetGroupIds: ProfileEnrollmentPolicyRuleActionTargetGroupIds

    uiSchemaId: str

    unknownUserAction: str

class ProfileEnrollmentPolicyRuleAction(RequiredProfileEnrollmentPolicyRuleAction, OptionalProfileEnrollmentPolicyRuleAction):
    pass

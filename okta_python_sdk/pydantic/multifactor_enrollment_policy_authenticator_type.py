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


MultifactorEnrollmentPolicyAuthenticatorType = Literal["custom_app", "custom_otp", "duo", "external_idp", "google_otp", "okta_email", "okta_password", "okta_verify", "onprem_mfa", "phone_number", "rsa_token", "security_question", "symantec_vip", "webauthn", "yubikey_token"]

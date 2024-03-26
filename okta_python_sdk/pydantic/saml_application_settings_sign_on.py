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

from okta_python_sdk.pydantic.acs_endpoint import AcsEndpoint
from okta_python_sdk.pydantic.saml_attribute_statement import SamlAttributeStatement
from okta_python_sdk.pydantic.sign_on_inline_hook import SignOnInlineHook
from okta_python_sdk.pydantic.single_logout import SingleLogout
from okta_python_sdk.pydantic.sp_certificate import SpCertificate

class SamlApplicationSettingsSignOn(BaseModel):
    acs_endpoints: typing.Optional[typing.List[AcsEndpoint]] = Field(None, alias='acsEndpoints')

    allow_multiple_acs_endpoints: typing.Optional[bool] = Field(None, alias='allowMultipleAcsEndpoints')

    assertion_signed: typing.Optional[bool] = Field(None, alias='assertionSigned')

    attribute_statements: typing.Optional[typing.List[SamlAttributeStatement]] = Field(None, alias='attributeStatements')

    audience: typing.Optional[str] = Field(None, alias='audience')

    audience_override: typing.Optional[str] = Field(None, alias='audienceOverride')

    authn_context_class_ref: typing.Optional[str] = Field(None, alias='authnContextClassRef')

    default_relay_state: typing.Optional[str] = Field(None, alias='defaultRelayState')

    destination: typing.Optional[str] = Field(None, alias='destination')

    destination_override: typing.Optional[str] = Field(None, alias='destinationOverride')

    digest_algorithm: typing.Optional[str] = Field(None, alias='digestAlgorithm')

    honor_force_authn: typing.Optional[bool] = Field(None, alias='honorForceAuthn')

    idp_issuer: typing.Optional[str] = Field(None, alias='idpIssuer')

    inline_hooks: typing.Optional[typing.List[SignOnInlineHook]] = Field(None, alias='inlineHooks')

    recipient: typing.Optional[str] = Field(None, alias='recipient')

    recipient_override: typing.Optional[str] = Field(None, alias='recipientOverride')

    request_compressed: typing.Optional[bool] = Field(None, alias='requestCompressed')

    response_signed: typing.Optional[bool] = Field(None, alias='responseSigned')

    saml_signed_request_enabled: typing.Optional[bool] = Field(None, alias='samlSignedRequestEnabled')

    signature_algorithm: typing.Optional[str] = Field(None, alias='signatureAlgorithm')

    slo: typing.Optional[SingleLogout] = Field(None, alias='slo')

    sp_certificate: typing.Optional[SpCertificate] = Field(None, alias='spCertificate')

    sp_issuer: typing.Optional[str] = Field(None, alias='spIssuer')

    sso_acs_url: typing.Optional[str] = Field(None, alias='ssoAcsUrl')

    sso_acs_url_override: typing.Optional[str] = Field(None, alias='ssoAcsUrlOverride')

    subject_name_id_format: typing.Optional[str] = Field(None, alias='subjectNameIdFormat')

    subject_name_id_template: typing.Optional[str] = Field(None, alias='subjectNameIdTemplate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

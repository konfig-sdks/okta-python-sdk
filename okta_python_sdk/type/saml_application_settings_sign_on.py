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

from okta_python_sdk.type.acs_endpoint import AcsEndpoint
from okta_python_sdk.type.saml_attribute_statement import SamlAttributeStatement
from okta_python_sdk.type.sign_on_inline_hook import SignOnInlineHook
from okta_python_sdk.type.single_logout import SingleLogout
from okta_python_sdk.type.sp_certificate import SpCertificate

class RequiredSamlApplicationSettingsSignOn(TypedDict):
    pass

class OptionalSamlApplicationSettingsSignOn(TypedDict, total=False):
    acsEndpoints: typing.List[AcsEndpoint]

    allowMultipleAcsEndpoints: bool

    assertionSigned: bool

    attributeStatements: typing.List[SamlAttributeStatement]

    audience: str

    audienceOverride: str

    authnContextClassRef: str

    defaultRelayState: str

    destination: str

    destinationOverride: str

    digestAlgorithm: str

    honorForceAuthn: bool

    idpIssuer: str

    inlineHooks: typing.List[SignOnInlineHook]

    recipient: str

    recipientOverride: str

    requestCompressed: bool

    responseSigned: bool

    samlSignedRequestEnabled: bool

    signatureAlgorithm: str

    slo: SingleLogout

    spCertificate: SpCertificate

    spIssuer: str

    ssoAcsUrl: str

    ssoAcsUrlOverride: str

    subjectNameIdFormat: str

    subjectNameIdTemplate: str

class SamlApplicationSettingsSignOn(RequiredSamlApplicationSettingsSignOn, OptionalSamlApplicationSettingsSignOn):
    pass

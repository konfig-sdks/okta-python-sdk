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

from okta_python_sdk.pydantic.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_key_descriptor import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor
from okta_python_sdk.pydantic.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_name_id_format import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat
from okta_python_sdk.pydantic.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_single_logout_service import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService
from okta_python_sdk.pydantic.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_single_sign_on_service import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService

class ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptor(BaseModel):
    key_descriptor: typing.Optional[ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor] = Field(None, alias='KeyDescriptor')

    name_i_d_format: typing.Optional[ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat] = Field(None, alias='NameIDFormat')

    single_logout_service: typing.Optional[ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService] = Field(None, alias='SingleLogoutService')

    single_sign_on_service: typing.Optional[ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService] = Field(None, alias='SingleSignOnService')

    want_authn_requests_signed: typing.Optional[bool] = Field(None, alias='WantAuthnRequestsSigned')

    protocol_support_enumeration: typing.Optional[str] = Field(None, alias='protocolSupportEnumeration')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

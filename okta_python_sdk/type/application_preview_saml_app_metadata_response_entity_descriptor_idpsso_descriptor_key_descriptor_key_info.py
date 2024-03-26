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

from okta_python_sdk.type.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_key_descriptor_key_info_x509_data import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptorKeyInfoX509Data

class RequiredApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptorKeyInfo(TypedDict):
    pass

class OptionalApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptorKeyInfo(TypedDict, total=False):
    X509Data: ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptorKeyInfoX509Data

class ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptorKeyInfo(RequiredApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptorKeyInfo, OptionalApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptorKeyInfo):
    pass

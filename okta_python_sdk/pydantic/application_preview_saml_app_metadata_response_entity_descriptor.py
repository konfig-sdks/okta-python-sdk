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

from okta_python_sdk.pydantic.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptor

class ApplicationPreviewSamlAppMetadataResponseEntityDescriptor(BaseModel):
    i_d_p_s_s_o_descriptor: typing.Optional[ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptor] = Field(None, alias='IDPSSODescriptor')

    entity_i_d: typing.Optional[str] = Field(None, alias='entityID')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

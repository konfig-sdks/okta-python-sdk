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

from okta_python_sdk.pydantic.csr_metadata_subject import CsrMetadataSubject
from okta_python_sdk.pydantic.csr_metadata_subject_alt_names import CsrMetadataSubjectAltNames

class CsrMetadata(BaseModel):
    subject: typing.Optional[CsrMetadataSubject] = Field(None, alias='subject')

    subject_alt_names: typing.Optional[CsrMetadataSubjectAltNames] = Field(None, alias='subjectAltNames')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from okta_python_sdk import schemas  # noqa: F401


class ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def KeyDescriptor() -> typing.Type['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor']:
                return ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor
        
            @staticmethod
            def NameIDFormat() -> typing.Type['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat']:
                return ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat
        
            @staticmethod
            def SingleLogoutService() -> typing.Type['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService']:
                return ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService
        
            @staticmethod
            def SingleSignOnService() -> typing.Type['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService']:
                return ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService
            WantAuthnRequestsSigned = schemas.BoolSchema
            protocolSupportEnumeration = schemas.StrSchema
            __annotations__ = {
                "KeyDescriptor": KeyDescriptor,
                "NameIDFormat": NameIDFormat,
                "SingleLogoutService": SingleLogoutService,
                "SingleSignOnService": SingleSignOnService,
                "WantAuthnRequestsSigned": WantAuthnRequestsSigned,
                "protocolSupportEnumeration": protocolSupportEnumeration,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["KeyDescriptor"]) -> 'ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NameIDFormat"]) -> 'ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SingleLogoutService"]) -> 'ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SingleSignOnService"]) -> 'ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WantAuthnRequestsSigned"]) -> MetaOapg.properties.WantAuthnRequestsSigned: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocolSupportEnumeration"]) -> MetaOapg.properties.protocolSupportEnumeration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["KeyDescriptor", "NameIDFormat", "SingleLogoutService", "SingleSignOnService", "WantAuthnRequestsSigned", "protocolSupportEnumeration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["KeyDescriptor"]) -> typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NameIDFormat"]) -> typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SingleLogoutService"]) -> typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SingleSignOnService"]) -> typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WantAuthnRequestsSigned"]) -> typing.Union[MetaOapg.properties.WantAuthnRequestsSigned, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocolSupportEnumeration"]) -> typing.Union[MetaOapg.properties.protocolSupportEnumeration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["KeyDescriptor", "NameIDFormat", "SingleLogoutService", "SingleSignOnService", "WantAuthnRequestsSigned", "protocolSupportEnumeration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        KeyDescriptor: typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor', schemas.Unset] = schemas.unset,
        NameIDFormat: typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat', schemas.Unset] = schemas.unset,
        SingleLogoutService: typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService', schemas.Unset] = schemas.unset,
        SingleSignOnService: typing.Union['ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService', schemas.Unset] = schemas.unset,
        WantAuthnRequestsSigned: typing.Union[MetaOapg.properties.WantAuthnRequestsSigned, bool, schemas.Unset] = schemas.unset,
        protocolSupportEnumeration: typing.Union[MetaOapg.properties.protocolSupportEnumeration, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptor':
        return super().__new__(
            cls,
            *args,
            KeyDescriptor=KeyDescriptor,
            NameIDFormat=NameIDFormat,
            SingleLogoutService=SingleLogoutService,
            SingleSignOnService=SingleSignOnService,
            WantAuthnRequestsSigned=WantAuthnRequestsSigned,
            protocolSupportEnumeration=protocolSupportEnumeration,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_key_descriptor import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorKeyDescriptor
from okta_python_sdk.model.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_name_id_format import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorNameIdFormat
from okta_python_sdk.model.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_single_logout_service import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleLogoutService
from okta_python_sdk.model.application_preview_saml_app_metadata_response_entity_descriptor_idpsso_descriptor_single_sign_on_service import ApplicationPreviewSamlAppMetadataResponseEntityDescriptorIdpssoDescriptorSingleSignOnService

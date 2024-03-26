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


class CsrMetadataSubject(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            commonName = schemas.StrSchema
            countryName = schemas.StrSchema
            localityName = schemas.StrSchema
            organizationName = schemas.StrSchema
            organizationalUnitName = schemas.StrSchema
            stateOrProvinceName = schemas.StrSchema
            __annotations__ = {
                "commonName": commonName,
                "countryName": countryName,
                "localityName": localityName,
                "organizationName": organizationName,
                "organizationalUnitName": organizationalUnitName,
                "stateOrProvinceName": stateOrProvinceName,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commonName"]) -> MetaOapg.properties.commonName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryName"]) -> MetaOapg.properties.countryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["localityName"]) -> MetaOapg.properties.localityName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationName"]) -> MetaOapg.properties.organizationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organizationalUnitName"]) -> MetaOapg.properties.organizationalUnitName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateOrProvinceName"]) -> MetaOapg.properties.stateOrProvinceName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["commonName", "countryName", "localityName", "organizationName", "organizationalUnitName", "stateOrProvinceName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commonName"]) -> typing.Union[MetaOapg.properties.commonName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryName"]) -> typing.Union[MetaOapg.properties.countryName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["localityName"]) -> typing.Union[MetaOapg.properties.localityName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationName"]) -> typing.Union[MetaOapg.properties.organizationName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organizationalUnitName"]) -> typing.Union[MetaOapg.properties.organizationalUnitName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateOrProvinceName"]) -> typing.Union[MetaOapg.properties.stateOrProvinceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["commonName", "countryName", "localityName", "organizationName", "organizationalUnitName", "stateOrProvinceName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        commonName: typing.Union[MetaOapg.properties.commonName, str, schemas.Unset] = schemas.unset,
        countryName: typing.Union[MetaOapg.properties.countryName, str, schemas.Unset] = schemas.unset,
        localityName: typing.Union[MetaOapg.properties.localityName, str, schemas.Unset] = schemas.unset,
        organizationName: typing.Union[MetaOapg.properties.organizationName, str, schemas.Unset] = schemas.unset,
        organizationalUnitName: typing.Union[MetaOapg.properties.organizationalUnitName, str, schemas.Unset] = schemas.unset,
        stateOrProvinceName: typing.Union[MetaOapg.properties.stateOrProvinceName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CsrMetadataSubject':
        return super().__new__(
            cls,
            *args,
            commonName=commonName,
            countryName=countryName,
            localityName=localityName,
            organizationName=organizationName,
            organizationalUnitName=organizationalUnitName,
            stateOrProvinceName=stateOrProvinceName,
            _configuration=_configuration,
            **kwargs,
        )

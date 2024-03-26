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


class SecurePasswordStoreApplicationSettingsApplication(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            optionalField1 = schemas.StrSchema
            optionalField1Value = schemas.StrSchema
            optionalField2 = schemas.StrSchema
            optionalField2Value = schemas.StrSchema
            optionalField3 = schemas.StrSchema
            optionalField3Value = schemas.StrSchema
            passwordField = schemas.StrSchema
            url = schemas.StrSchema
            usernameField = schemas.StrSchema
            __annotations__ = {
                "optionalField1": optionalField1,
                "optionalField1Value": optionalField1Value,
                "optionalField2": optionalField2,
                "optionalField2Value": optionalField2Value,
                "optionalField3": optionalField3,
                "optionalField3Value": optionalField3Value,
                "passwordField": passwordField,
                "url": url,
                "usernameField": usernameField,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalField1"]) -> MetaOapg.properties.optionalField1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalField1Value"]) -> MetaOapg.properties.optionalField1Value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalField2"]) -> MetaOapg.properties.optionalField2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalField2Value"]) -> MetaOapg.properties.optionalField2Value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalField3"]) -> MetaOapg.properties.optionalField3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["optionalField3Value"]) -> MetaOapg.properties.optionalField3Value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["passwordField"]) -> MetaOapg.properties.passwordField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usernameField"]) -> MetaOapg.properties.usernameField: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["optionalField1", "optionalField1Value", "optionalField2", "optionalField2Value", "optionalField3", "optionalField3Value", "passwordField", "url", "usernameField", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalField1"]) -> typing.Union[MetaOapg.properties.optionalField1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalField1Value"]) -> typing.Union[MetaOapg.properties.optionalField1Value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalField2"]) -> typing.Union[MetaOapg.properties.optionalField2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalField2Value"]) -> typing.Union[MetaOapg.properties.optionalField2Value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalField3"]) -> typing.Union[MetaOapg.properties.optionalField3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["optionalField3Value"]) -> typing.Union[MetaOapg.properties.optionalField3Value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["passwordField"]) -> typing.Union[MetaOapg.properties.passwordField, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usernameField"]) -> typing.Union[MetaOapg.properties.usernameField, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["optionalField1", "optionalField1Value", "optionalField2", "optionalField2Value", "optionalField3", "optionalField3Value", "passwordField", "url", "usernameField", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        optionalField1: typing.Union[MetaOapg.properties.optionalField1, str, schemas.Unset] = schemas.unset,
        optionalField1Value: typing.Union[MetaOapg.properties.optionalField1Value, str, schemas.Unset] = schemas.unset,
        optionalField2: typing.Union[MetaOapg.properties.optionalField2, str, schemas.Unset] = schemas.unset,
        optionalField2Value: typing.Union[MetaOapg.properties.optionalField2Value, str, schemas.Unset] = schemas.unset,
        optionalField3: typing.Union[MetaOapg.properties.optionalField3, str, schemas.Unset] = schemas.unset,
        optionalField3Value: typing.Union[MetaOapg.properties.optionalField3Value, str, schemas.Unset] = schemas.unset,
        passwordField: typing.Union[MetaOapg.properties.passwordField, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, str, schemas.Unset] = schemas.unset,
        usernameField: typing.Union[MetaOapg.properties.usernameField, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SecurePasswordStoreApplicationSettingsApplication':
        return super().__new__(
            cls,
            *args,
            optionalField1=optionalField1,
            optionalField1Value=optionalField1Value,
            optionalField2=optionalField2,
            optionalField2Value=optionalField2Value,
            optionalField3=optionalField3,
            optionalField3Value=optionalField3Value,
            passwordField=passwordField,
            url=url,
            usernameField=usernameField,
            _configuration=_configuration,
            **kwargs,
        )

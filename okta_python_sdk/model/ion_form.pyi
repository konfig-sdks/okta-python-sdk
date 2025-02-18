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


class IonForm(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            accepts = schemas.StrSchema
            href = schemas.StrSchema
            method = schemas.StrSchema
            name = schemas.StrSchema
            produces = schemas.StrSchema
            refresh = schemas.IntSchema
        
            @staticmethod
            def rel() -> typing.Type['IonFormRel']:
                return IonFormRel
        
            @staticmethod
            def relatesTo() -> typing.Type['IonFormRelatesTo']:
                return IonFormRelatesTo
            
            
            class value(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IonField']:
                        return IonField
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['IonField'], typing.List['IonField']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'value':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IonField':
                    return super().__getitem__(i)
            __annotations__ = {
                "accepts": accepts,
                "href": href,
                "method": method,
                "name": name,
                "produces": produces,
                "refresh": refresh,
                "rel": rel,
                "relatesTo": relatesTo,
                "value": value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accepts"]) -> MetaOapg.properties.accepts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["href"]) -> MetaOapg.properties.href: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["produces"]) -> MetaOapg.properties.produces: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refresh"]) -> MetaOapg.properties.refresh: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rel"]) -> 'IonFormRel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relatesTo"]) -> 'IonFormRelatesTo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accepts", "href", "method", "name", "produces", "refresh", "rel", "relatesTo", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accepts"]) -> typing.Union[MetaOapg.properties.accepts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["href"]) -> typing.Union[MetaOapg.properties.href, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> typing.Union[MetaOapg.properties.method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["produces"]) -> typing.Union[MetaOapg.properties.produces, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refresh"]) -> typing.Union[MetaOapg.properties.refresh, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rel"]) -> typing.Union['IonFormRel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relatesTo"]) -> typing.Union['IonFormRelatesTo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accepts", "href", "method", "name", "produces", "refresh", "rel", "relatesTo", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accepts: typing.Union[MetaOapg.properties.accepts, str, schemas.Unset] = schemas.unset,
        href: typing.Union[MetaOapg.properties.href, str, schemas.Unset] = schemas.unset,
        method: typing.Union[MetaOapg.properties.method, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        produces: typing.Union[MetaOapg.properties.produces, str, schemas.Unset] = schemas.unset,
        refresh: typing.Union[MetaOapg.properties.refresh, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rel: typing.Union['IonFormRel', schemas.Unset] = schemas.unset,
        relatesTo: typing.Union['IonFormRelatesTo', schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IonForm':
        return super().__new__(
            cls,
            *args,
            accepts=accepts,
            href=href,
            method=method,
            name=name,
            produces=produces,
            refresh=refresh,
            rel=rel,
            relatesTo=relatesTo,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.ion_field import IonField
from okta_python_sdk.model.ion_form_rel import IonFormRel
from okta_python_sdk.model.ion_form_relates_to import IonFormRelatesTo

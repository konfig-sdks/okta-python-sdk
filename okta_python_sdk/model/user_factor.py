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


class UserFactor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def _embedded() -> typing.Type['UserFactorEmbedded']:
                return UserFactorEmbedded
        
            @staticmethod
            def _links() -> typing.Type['UserFactorLinks']:
                return UserFactorLinks
            created = schemas.DateTimeSchema
        
            @staticmethod
            def factorType() -> typing.Type['FactorType']:
                return FactorType
            id = schemas.StrSchema
            lastUpdated = schemas.DateTimeSchema
        
            @staticmethod
            def provider() -> typing.Type['FactorProvider']:
                return FactorProvider
        
            @staticmethod
            def status() -> typing.Type['FactorStatus']:
                return FactorStatus
        
            @staticmethod
            def verify() -> typing.Type['VerifyFactorRequest']:
                return VerifyFactorRequest
            __annotations__ = {
                "_embedded": _embedded,
                "_links": _links,
                "created": created,
                "factorType": factorType,
                "id": id,
                "lastUpdated": lastUpdated,
                "provider": provider,
                "status": status,
                "verify": verify,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_embedded"]) -> 'UserFactorEmbedded': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'UserFactorLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["factorType"]) -> 'FactorType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdated"]) -> MetaOapg.properties.lastUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> 'FactorProvider': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'FactorStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verify"]) -> 'VerifyFactorRequest': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_embedded", "_links", "created", "factorType", "id", "lastUpdated", "provider", "status", "verify", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_embedded"]) -> typing.Union['UserFactorEmbedded', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['UserFactorLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["factorType"]) -> typing.Union['FactorType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdated"]) -> typing.Union[MetaOapg.properties.lastUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union['FactorProvider', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['FactorStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verify"]) -> typing.Union['VerifyFactorRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_embedded", "_links", "created", "factorType", "id", "lastUpdated", "provider", "status", "verify", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _embedded: typing.Union['UserFactorEmbedded', schemas.Unset] = schemas.unset,
        _links: typing.Union['UserFactorLinks', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        factorType: typing.Union['FactorType', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        lastUpdated: typing.Union[MetaOapg.properties.lastUpdated, str, datetime, schemas.Unset] = schemas.unset,
        provider: typing.Union['FactorProvider', schemas.Unset] = schemas.unset,
        status: typing.Union['FactorStatus', schemas.Unset] = schemas.unset,
        verify: typing.Union['VerifyFactorRequest', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserFactor':
        return super().__new__(
            cls,
            *args,
            _embedded=_embedded,
            _links=_links,
            created=created,
            factorType=factorType,
            id=id,
            lastUpdated=lastUpdated,
            provider=provider,
            status=status,
            verify=verify,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.factor_provider import FactorProvider
from okta_python_sdk.model.factor_status import FactorStatus
from okta_python_sdk.model.factor_type import FactorType
from okta_python_sdk.model.user_factor_embedded import UserFactorEmbedded
from okta_python_sdk.model.user_factor_links import UserFactorLinks
from okta_python_sdk.model.verify_factor_request import VerifyFactorRequest

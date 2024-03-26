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


class Authenticator(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def _links() -> typing.Type['AuthenticatorLinks']:
                return AuthenticatorLinks
            created = schemas.DateTimeSchema
            id = schemas.StrSchema
            key = schemas.StrSchema
            lastUpdated = schemas.DateTimeSchema
            name = schemas.StrSchema
        
            @staticmethod
            def provider() -> typing.Type['AuthenticatorProvider']:
                return AuthenticatorProvider
        
            @staticmethod
            def settings() -> typing.Type['AuthenticatorSettings']:
                return AuthenticatorSettings
        
            @staticmethod
            def status() -> typing.Type['AuthenticatorStatus']:
                return AuthenticatorStatus
        
            @staticmethod
            def type() -> typing.Type['AuthenticatorType']:
                return AuthenticatorType
            __annotations__ = {
                "_links": _links,
                "created": created,
                "id": id,
                "key": key,
                "lastUpdated": lastUpdated,
                "name": name,
                "provider": provider,
                "settings": settings,
                "status": status,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'AuthenticatorLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdated"]) -> MetaOapg.properties.lastUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> 'AuthenticatorProvider': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'AuthenticatorSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'AuthenticatorStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'AuthenticatorType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "created", "id", "key", "lastUpdated", "name", "provider", "settings", "status", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['AuthenticatorLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdated"]) -> typing.Union[MetaOapg.properties.lastUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union['AuthenticatorProvider', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['AuthenticatorSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['AuthenticatorStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['AuthenticatorType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "created", "id", "key", "lastUpdated", "name", "provider", "settings", "status", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _links: typing.Union['AuthenticatorLinks', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        key: typing.Union[MetaOapg.properties.key, str, schemas.Unset] = schemas.unset,
        lastUpdated: typing.Union[MetaOapg.properties.lastUpdated, str, datetime, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        provider: typing.Union['AuthenticatorProvider', schemas.Unset] = schemas.unset,
        settings: typing.Union['AuthenticatorSettings', schemas.Unset] = schemas.unset,
        status: typing.Union['AuthenticatorStatus', schemas.Unset] = schemas.unset,
        type: typing.Union['AuthenticatorType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Authenticator':
        return super().__new__(
            cls,
            *args,
            _links=_links,
            created=created,
            id=id,
            key=key,
            lastUpdated=lastUpdated,
            name=name,
            provider=provider,
            settings=settings,
            status=status,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.authenticator_links import AuthenticatorLinks
from okta_python_sdk.model.authenticator_provider import AuthenticatorProvider
from okta_python_sdk.model.authenticator_settings import AuthenticatorSettings
from okta_python_sdk.model.authenticator_status import AuthenticatorStatus
from okta_python_sdk.model.authenticator_type import AuthenticatorType

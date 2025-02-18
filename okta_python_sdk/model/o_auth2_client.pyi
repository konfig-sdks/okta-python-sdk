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


class OAuth2Client(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def _links() -> typing.Type['OAuth2ClientLinks']:
                return OAuth2ClientLinks
            client_id = schemas.StrSchema
            client_name = schemas.StrSchema
            client_uri = schemas.StrSchema
            logo_uri = schemas.StrSchema
            __annotations__ = {
                "_links": _links,
                "client_id": client_id,
                "client_name": client_name,
                "client_uri": client_uri,
                "logo_uri": logo_uri,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'OAuth2ClientLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_name"]) -> MetaOapg.properties.client_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_uri"]) -> MetaOapg.properties.client_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo_uri"]) -> MetaOapg.properties.logo_uri: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "client_id", "client_name", "client_uri", "logo_uri", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['OAuth2ClientLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_name"]) -> typing.Union[MetaOapg.properties.client_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_uri"]) -> typing.Union[MetaOapg.properties.client_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo_uri"]) -> typing.Union[MetaOapg.properties.logo_uri, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "client_id", "client_name", "client_uri", "logo_uri", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _links: typing.Union['OAuth2ClientLinks', schemas.Unset] = schemas.unset,
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        client_name: typing.Union[MetaOapg.properties.client_name, str, schemas.Unset] = schemas.unset,
        client_uri: typing.Union[MetaOapg.properties.client_uri, str, schemas.Unset] = schemas.unset,
        logo_uri: typing.Union[MetaOapg.properties.logo_uri, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OAuth2Client':
        return super().__new__(
            cls,
            *args,
            _links=_links,
            client_id=client_id,
            client_name=client_name,
            client_uri=client_uri,
            logo_uri=logo_uri,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.o_auth2_client_links import OAuth2ClientLinks

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


class OpenIdConnectApplicationSettingsRefreshToken(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            leeway = schemas.IntSchema
        
            @staticmethod
            def rotation_type() -> typing.Type['OpenIdConnectRefreshTokenRotationType']:
                return OpenIdConnectRefreshTokenRotationType
            __annotations__ = {
                "leeway": leeway,
                "rotation_type": rotation_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["leeway"]) -> MetaOapg.properties.leeway: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rotation_type"]) -> 'OpenIdConnectRefreshTokenRotationType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["leeway", "rotation_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["leeway"]) -> typing.Union[MetaOapg.properties.leeway, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rotation_type"]) -> typing.Union['OpenIdConnectRefreshTokenRotationType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["leeway", "rotation_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        leeway: typing.Union[MetaOapg.properties.leeway, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rotation_type: typing.Union['OpenIdConnectRefreshTokenRotationType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OpenIdConnectApplicationSettingsRefreshToken':
        return super().__new__(
            cls,
            *args,
            leeway=leeway,
            rotation_type=rotation_type,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.open_id_connect_refresh_token_rotation_type import OpenIdConnectRefreshTokenRotationType

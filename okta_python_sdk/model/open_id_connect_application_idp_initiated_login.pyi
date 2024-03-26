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


class OpenIdConnectApplicationIdpInitiatedLogin(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def default_scope() -> typing.Type['OpenIdConnectApplicationIdpInitiatedLoginDefaultScope']:
                return OpenIdConnectApplicationIdpInitiatedLoginDefaultScope
            mode = schemas.StrSchema
            __annotations__ = {
                "default_scope": default_scope,
                "mode": mode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_scope"]) -> 'OpenIdConnectApplicationIdpInitiatedLoginDefaultScope': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> MetaOapg.properties.mode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["default_scope", "mode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_scope"]) -> typing.Union['OpenIdConnectApplicationIdpInitiatedLoginDefaultScope', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> typing.Union[MetaOapg.properties.mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["default_scope", "mode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        default_scope: typing.Union['OpenIdConnectApplicationIdpInitiatedLoginDefaultScope', schemas.Unset] = schemas.unset,
        mode: typing.Union[MetaOapg.properties.mode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OpenIdConnectApplicationIdpInitiatedLogin':
        return super().__new__(
            cls,
            *args,
            default_scope=default_scope,
            mode=mode,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.open_id_connect_application_idp_initiated_login_default_scope import OpenIdConnectApplicationIdpInitiatedLoginDefaultScope

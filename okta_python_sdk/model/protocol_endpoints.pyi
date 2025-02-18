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


class ProtocolEndpoints(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def acs() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def authorization() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def jwks() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def metadata() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def slo() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def sso() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def token() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def userInfo() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
            __annotations__ = {
                "acs": acs,
                "authorization": authorization,
                "jwks": jwks,
                "metadata": metadata,
                "slo": slo,
                "sso": sso,
                "token": token,
                "userInfo": userInfo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acs"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorization"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jwks"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slo"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sso"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userInfo"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["acs", "authorization", "jwks", "metadata", "slo", "sso", "token", "userInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acs"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorization"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jwks"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slo"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sso"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userInfo"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["acs", "authorization", "jwks", "metadata", "slo", "sso", "token", "userInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        acs: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        authorization: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        jwks: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        metadata: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        slo: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        sso: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        token: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        userInfo: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProtocolEndpoints':
        return super().__new__(
            cls,
            *args,
            acs=acs,
            authorization=authorization,
            jwks=jwks,
            metadata=metadata,
            slo=slo,
            sso=sso,
            token=token,
            userInfo=userInfo,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.protocol_endpoint import ProtocolEndpoint

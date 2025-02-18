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


class Protocol(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def algorithms() -> typing.Type['ProtocolAlgorithms']:
                return ProtocolAlgorithms
        
            @staticmethod
            def credentials() -> typing.Type['IdentityProviderCredentials']:
                return IdentityProviderCredentials
        
            @staticmethod
            def endpoints() -> typing.Type['ProtocolEndpoints']:
                return ProtocolEndpoints
        
            @staticmethod
            def issuer() -> typing.Type['ProtocolEndpoint']:
                return ProtocolEndpoint
        
            @staticmethod
            def relayState() -> typing.Type['ProtocolRelayState']:
                return ProtocolRelayState
        
            @staticmethod
            def scopes() -> typing.Type['ProtocolScopes']:
                return ProtocolScopes
        
            @staticmethod
            def settings() -> typing.Type['ProtocolSettings']:
                return ProtocolSettings
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SAML2": "SAML2",
                        "OIDC": "OIDC",
                        "OAUTH2": "OAUTH2",
                        "MTLS": "MTLS",
                    }
                
                @schemas.classproperty
                def SAML2(cls):
                    return cls("SAML2")
                
                @schemas.classproperty
                def OIDC(cls):
                    return cls("OIDC")
                
                @schemas.classproperty
                def OAUTH2(cls):
                    return cls("OAUTH2")
                
                @schemas.classproperty
                def MTLS(cls):
                    return cls("MTLS")
            __annotations__ = {
                "algorithms": algorithms,
                "credentials": credentials,
                "endpoints": endpoints,
                "issuer": issuer,
                "relayState": relayState,
                "scopes": scopes,
                "settings": settings,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithms"]) -> 'ProtocolAlgorithms': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credentials"]) -> 'IdentityProviderCredentials': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpoints"]) -> 'ProtocolEndpoints': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuer"]) -> 'ProtocolEndpoint': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relayState"]) -> 'ProtocolRelayState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scopes"]) -> 'ProtocolScopes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'ProtocolSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["algorithms", "credentials", "endpoints", "issuer", "relayState", "scopes", "settings", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithms"]) -> typing.Union['ProtocolAlgorithms', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credentials"]) -> typing.Union['IdentityProviderCredentials', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpoints"]) -> typing.Union['ProtocolEndpoints', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuer"]) -> typing.Union['ProtocolEndpoint', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relayState"]) -> typing.Union['ProtocolRelayState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scopes"]) -> typing.Union['ProtocolScopes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['ProtocolSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["algorithms", "credentials", "endpoints", "issuer", "relayState", "scopes", "settings", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        algorithms: typing.Union['ProtocolAlgorithms', schemas.Unset] = schemas.unset,
        credentials: typing.Union['IdentityProviderCredentials', schemas.Unset] = schemas.unset,
        endpoints: typing.Union['ProtocolEndpoints', schemas.Unset] = schemas.unset,
        issuer: typing.Union['ProtocolEndpoint', schemas.Unset] = schemas.unset,
        relayState: typing.Union['ProtocolRelayState', schemas.Unset] = schemas.unset,
        scopes: typing.Union['ProtocolScopes', schemas.Unset] = schemas.unset,
        settings: typing.Union['ProtocolSettings', schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Protocol':
        return super().__new__(
            cls,
            *args,
            algorithms=algorithms,
            credentials=credentials,
            endpoints=endpoints,
            issuer=issuer,
            relayState=relayState,
            scopes=scopes,
            settings=settings,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.identity_provider_credentials import IdentityProviderCredentials
from okta_python_sdk.model.protocol_algorithms import ProtocolAlgorithms
from okta_python_sdk.model.protocol_endpoint import ProtocolEndpoint
from okta_python_sdk.model.protocol_endpoints import ProtocolEndpoints
from okta_python_sdk.model.protocol_relay_state import ProtocolRelayState
from okta_python_sdk.model.protocol_scopes import ProtocolScopes
from okta_python_sdk.model.protocol_settings import ProtocolSettings

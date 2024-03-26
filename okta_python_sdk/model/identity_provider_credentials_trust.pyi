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


class IdentityProviderCredentialsTrust(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            audience = schemas.StrSchema
            issuer = schemas.StrSchema
            kid = schemas.StrSchema
            
            
            class revocation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CRL(cls):
                    return cls("CRL")
                
                @schemas.classproperty
                def DELTA_CRL(cls):
                    return cls("DELTA_CRL")
                
                @schemas.classproperty
                def OCSP(cls):
                    return cls("OCSP")
            revocationCacheLifetime = schemas.IntSchema
            __annotations__ = {
                "audience": audience,
                "issuer": issuer,
                "kid": kid,
                "revocation": revocation,
                "revocationCacheLifetime": revocationCacheLifetime,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["audience"]) -> MetaOapg.properties.audience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuer"]) -> MetaOapg.properties.issuer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kid"]) -> MetaOapg.properties.kid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revocation"]) -> MetaOapg.properties.revocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revocationCacheLifetime"]) -> MetaOapg.properties.revocationCacheLifetime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["audience", "issuer", "kid", "revocation", "revocationCacheLifetime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["audience"]) -> typing.Union[MetaOapg.properties.audience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuer"]) -> typing.Union[MetaOapg.properties.issuer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kid"]) -> typing.Union[MetaOapg.properties.kid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revocation"]) -> typing.Union[MetaOapg.properties.revocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revocationCacheLifetime"]) -> typing.Union[MetaOapg.properties.revocationCacheLifetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["audience", "issuer", "kid", "revocation", "revocationCacheLifetime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        audience: typing.Union[MetaOapg.properties.audience, str, schemas.Unset] = schemas.unset,
        issuer: typing.Union[MetaOapg.properties.issuer, str, schemas.Unset] = schemas.unset,
        kid: typing.Union[MetaOapg.properties.kid, str, schemas.Unset] = schemas.unset,
        revocation: typing.Union[MetaOapg.properties.revocation, str, schemas.Unset] = schemas.unset,
        revocationCacheLifetime: typing.Union[MetaOapg.properties.revocationCacheLifetime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IdentityProviderCredentialsTrust':
        return super().__new__(
            cls,
            *args,
            audience=audience,
            issuer=issuer,
            kid=kid,
            revocation=revocation,
            revocationCacheLifetime=revocationCacheLifetime,
            _configuration=_configuration,
            **kwargs,
        )

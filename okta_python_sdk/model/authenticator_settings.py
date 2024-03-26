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


class AuthenticatorSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def allowedFor() -> typing.Type['AllowedForEnum']:
                return AllowedForEnum
            appInstanceId = schemas.StrSchema
        
            @staticmethod
            def channelBinding() -> typing.Type['ChannelBinding']:
                return ChannelBinding
        
            @staticmethod
            def compliance() -> typing.Type['Compliance']:
                return Compliance
            tokenLifetimeInMinutes = schemas.IntSchema
        
            @staticmethod
            def userVerification() -> typing.Type['UserVerificationEnum']:
                return UserVerificationEnum
            __annotations__ = {
                "allowedFor": allowedFor,
                "appInstanceId": appInstanceId,
                "channelBinding": channelBinding,
                "compliance": compliance,
                "tokenLifetimeInMinutes": tokenLifetimeInMinutes,
                "userVerification": userVerification,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowedFor"]) -> 'AllowedForEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appInstanceId"]) -> MetaOapg.properties.appInstanceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["channelBinding"]) -> 'ChannelBinding': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compliance"]) -> 'Compliance': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokenLifetimeInMinutes"]) -> MetaOapg.properties.tokenLifetimeInMinutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userVerification"]) -> 'UserVerificationEnum': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allowedFor", "appInstanceId", "channelBinding", "compliance", "tokenLifetimeInMinutes", "userVerification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowedFor"]) -> typing.Union['AllowedForEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appInstanceId"]) -> typing.Union[MetaOapg.properties.appInstanceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["channelBinding"]) -> typing.Union['ChannelBinding', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compliance"]) -> typing.Union['Compliance', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokenLifetimeInMinutes"]) -> typing.Union[MetaOapg.properties.tokenLifetimeInMinutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userVerification"]) -> typing.Union['UserVerificationEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allowedFor", "appInstanceId", "channelBinding", "compliance", "tokenLifetimeInMinutes", "userVerification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        allowedFor: typing.Union['AllowedForEnum', schemas.Unset] = schemas.unset,
        appInstanceId: typing.Union[MetaOapg.properties.appInstanceId, str, schemas.Unset] = schemas.unset,
        channelBinding: typing.Union['ChannelBinding', schemas.Unset] = schemas.unset,
        compliance: typing.Union['Compliance', schemas.Unset] = schemas.unset,
        tokenLifetimeInMinutes: typing.Union[MetaOapg.properties.tokenLifetimeInMinutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        userVerification: typing.Union['UserVerificationEnum', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthenticatorSettings':
        return super().__new__(
            cls,
            *args,
            allowedFor=allowedFor,
            appInstanceId=appInstanceId,
            channelBinding=channelBinding,
            compliance=compliance,
            tokenLifetimeInMinutes=tokenLifetimeInMinutes,
            userVerification=userVerification,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.allowed_for_enum import AllowedForEnum
from okta_python_sdk.model.channel_binding import ChannelBinding
from okta_python_sdk.model.compliance import Compliance
from okta_python_sdk.model.user_verification_enum import UserVerificationEnum

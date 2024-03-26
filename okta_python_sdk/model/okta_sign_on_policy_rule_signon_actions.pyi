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


class OktaSignOnPolicyRuleSignonActions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class access(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALLOW(cls):
                    return cls("ALLOW")
                
                @schemas.classproperty
                def DENY(cls):
                    return cls("DENY")
            factorLifetime = schemas.IntSchema
            
            
            class factorPromptMode(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALWAYS(cls):
                    return cls("ALWAYS")
                
                @schemas.classproperty
                def DEVICE(cls):
                    return cls("DEVICE")
                
                @schemas.classproperty
                def SESSION(cls):
                    return cls("SESSION")
            rememberDeviceByDefault = schemas.BoolSchema
            requireFactor = schemas.BoolSchema
        
            @staticmethod
            def session() -> typing.Type['OktaSignOnPolicyRuleSignonSessionActions']:
                return OktaSignOnPolicyRuleSignonSessionActions
            __annotations__ = {
                "access": access,
                "factorLifetime": factorLifetime,
                "factorPromptMode": factorPromptMode,
                "rememberDeviceByDefault": rememberDeviceByDefault,
                "requireFactor": requireFactor,
                "session": session,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> MetaOapg.properties.access: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["factorLifetime"]) -> MetaOapg.properties.factorLifetime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["factorPromptMode"]) -> MetaOapg.properties.factorPromptMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rememberDeviceByDefault"]) -> MetaOapg.properties.rememberDeviceByDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requireFactor"]) -> MetaOapg.properties.requireFactor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session"]) -> 'OktaSignOnPolicyRuleSignonSessionActions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["access", "factorLifetime", "factorPromptMode", "rememberDeviceByDefault", "requireFactor", "session", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union[MetaOapg.properties.access, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["factorLifetime"]) -> typing.Union[MetaOapg.properties.factorLifetime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["factorPromptMode"]) -> typing.Union[MetaOapg.properties.factorPromptMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rememberDeviceByDefault"]) -> typing.Union[MetaOapg.properties.rememberDeviceByDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requireFactor"]) -> typing.Union[MetaOapg.properties.requireFactor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session"]) -> typing.Union['OktaSignOnPolicyRuleSignonSessionActions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["access", "factorLifetime", "factorPromptMode", "rememberDeviceByDefault", "requireFactor", "session", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        access: typing.Union[MetaOapg.properties.access, str, schemas.Unset] = schemas.unset,
        factorLifetime: typing.Union[MetaOapg.properties.factorLifetime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        factorPromptMode: typing.Union[MetaOapg.properties.factorPromptMode, str, schemas.Unset] = schemas.unset,
        rememberDeviceByDefault: typing.Union[MetaOapg.properties.rememberDeviceByDefault, bool, schemas.Unset] = schemas.unset,
        requireFactor: typing.Union[MetaOapg.properties.requireFactor, bool, schemas.Unset] = schemas.unset,
        session: typing.Union['OktaSignOnPolicyRuleSignonSessionActions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OktaSignOnPolicyRuleSignonActions':
        return super().__new__(
            cls,
            *args,
            access=access,
            factorLifetime=factorLifetime,
            factorPromptMode=factorPromptMode,
            rememberDeviceByDefault=rememberDeviceByDefault,
            requireFactor=requireFactor,
            session=session,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.okta_sign_on_policy_rule_signon_session_actions import OktaSignOnPolicyRuleSignonSessionActions

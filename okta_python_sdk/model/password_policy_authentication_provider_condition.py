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


class PasswordPolicyAuthenticationProviderCondition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def include() -> typing.Type['PasswordPolicyAuthenticationProviderConditionInclude']:
                return PasswordPolicyAuthenticationProviderConditionInclude
            
            
            class provider(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACTIVE_DIRECTORY": "ACTIVE_DIRECTORY",
                        "ANY": "ANY",
                        "LDAP": "LDAP",
                        "OKTA": "OKTA",
                    }
                
                @schemas.classproperty
                def ACTIVE_DIRECTORY(cls):
                    return cls("ACTIVE_DIRECTORY")
                
                @schemas.classproperty
                def ANY(cls):
                    return cls("ANY")
                
                @schemas.classproperty
                def LDAP(cls):
                    return cls("LDAP")
                
                @schemas.classproperty
                def OKTA(cls):
                    return cls("OKTA")
            __annotations__ = {
                "include": include,
                "provider": provider,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include"]) -> 'PasswordPolicyAuthenticationProviderConditionInclude': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["include", "provider", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include"]) -> typing.Union['PasswordPolicyAuthenticationProviderConditionInclude', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> typing.Union[MetaOapg.properties.provider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["include", "provider", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        include: typing.Union['PasswordPolicyAuthenticationProviderConditionInclude', schemas.Unset] = schemas.unset,
        provider: typing.Union[MetaOapg.properties.provider, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PasswordPolicyAuthenticationProviderCondition':
        return super().__new__(
            cls,
            *args,
            include=include,
            provider=provider,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.password_policy_authentication_provider_condition_include import PasswordPolicyAuthenticationProviderConditionInclude

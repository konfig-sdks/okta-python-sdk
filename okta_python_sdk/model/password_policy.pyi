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


class PasswordPolicy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def conditions() -> typing.Type['PasswordPolicyConditions']:
                return PasswordPolicyConditions
        
            @staticmethod
            def settings() -> typing.Type['PasswordPolicySettings']:
                return PasswordPolicySettings
            __annotations__ = {
                "conditions": conditions,
                "settings": settings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> 'PasswordPolicyConditions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'PasswordPolicySettings': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["conditions", "settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union['PasswordPolicyConditions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['PasswordPolicySettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["conditions", "settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        conditions: typing.Union['PasswordPolicyConditions', schemas.Unset] = schemas.unset,
        settings: typing.Union['PasswordPolicySettings', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PasswordPolicy':
        return super().__new__(
            cls,
            *args,
            conditions=conditions,
            settings=settings,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.password_policy_conditions import PasswordPolicyConditions
from okta_python_sdk.model.password_policy_settings import PasswordPolicySettings

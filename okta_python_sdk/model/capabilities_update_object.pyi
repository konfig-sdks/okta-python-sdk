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


class CapabilitiesUpdateObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def lifecycleDeactivate() -> typing.Type['LifecycleDeactivateSettingObject']:
                return LifecycleDeactivateSettingObject
        
            @staticmethod
            def password() -> typing.Type['PasswordSettingObject']:
                return PasswordSettingObject
        
            @staticmethod
            def profile() -> typing.Type['ProfileSettingObject']:
                return ProfileSettingObject
            __annotations__ = {
                "lifecycleDeactivate": lifecycleDeactivate,
                "password": password,
                "profile": profile,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lifecycleDeactivate"]) -> 'LifecycleDeactivateSettingObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> 'PasswordSettingObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile"]) -> 'ProfileSettingObject': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lifecycleDeactivate", "password", "profile", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lifecycleDeactivate"]) -> typing.Union['LifecycleDeactivateSettingObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union['PasswordSettingObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile"]) -> typing.Union['ProfileSettingObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lifecycleDeactivate", "password", "profile", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lifecycleDeactivate: typing.Union['LifecycleDeactivateSettingObject', schemas.Unset] = schemas.unset,
        password: typing.Union['PasswordSettingObject', schemas.Unset] = schemas.unset,
        profile: typing.Union['ProfileSettingObject', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CapabilitiesUpdateObject':
        return super().__new__(
            cls,
            *args,
            lifecycleDeactivate=lifecycleDeactivate,
            password=password,
            profile=profile,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.lifecycle_deactivate_setting_object import LifecycleDeactivateSettingObject
from okta_python_sdk.model.password_setting_object import PasswordSettingObject
from okta_python_sdk.model.profile_setting_object import ProfileSettingObject

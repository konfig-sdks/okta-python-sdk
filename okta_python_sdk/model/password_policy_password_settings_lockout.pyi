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


class PasswordPolicyPasswordSettingsLockout(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            autoUnlockMinutes = schemas.IntSchema
            maxAttempts = schemas.IntSchema
            showLockoutFailures = schemas.BoolSchema
        
            @staticmethod
            def userLockoutNotificationChannels() -> typing.Type['PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels']:
                return PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels
            __annotations__ = {
                "autoUnlockMinutes": autoUnlockMinutes,
                "maxAttempts": maxAttempts,
                "showLockoutFailures": showLockoutFailures,
                "userLockoutNotificationChannels": userLockoutNotificationChannels,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoUnlockMinutes"]) -> MetaOapg.properties.autoUnlockMinutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxAttempts"]) -> MetaOapg.properties.maxAttempts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["showLockoutFailures"]) -> MetaOapg.properties.showLockoutFailures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userLockoutNotificationChannels"]) -> 'PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["autoUnlockMinutes", "maxAttempts", "showLockoutFailures", "userLockoutNotificationChannels", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoUnlockMinutes"]) -> typing.Union[MetaOapg.properties.autoUnlockMinutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxAttempts"]) -> typing.Union[MetaOapg.properties.maxAttempts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["showLockoutFailures"]) -> typing.Union[MetaOapg.properties.showLockoutFailures, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userLockoutNotificationChannels"]) -> typing.Union['PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["autoUnlockMinutes", "maxAttempts", "showLockoutFailures", "userLockoutNotificationChannels", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        autoUnlockMinutes: typing.Union[MetaOapg.properties.autoUnlockMinutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxAttempts: typing.Union[MetaOapg.properties.maxAttempts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        showLockoutFailures: typing.Union[MetaOapg.properties.showLockoutFailures, bool, schemas.Unset] = schemas.unset,
        userLockoutNotificationChannels: typing.Union['PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PasswordPolicyPasswordSettingsLockout':
        return super().__new__(
            cls,
            *args,
            autoUnlockMinutes=autoUnlockMinutes,
            maxAttempts=maxAttempts,
            showLockoutFailures=showLockoutFailures,
            userLockoutNotificationChannels=userLockoutNotificationChannels,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.password_policy_password_settings_lockout_user_lockout_notification_channels import PasswordPolicyPasswordSettingsLockoutUserLockoutNotificationChannels

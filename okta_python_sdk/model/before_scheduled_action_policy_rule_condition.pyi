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


class BeforeScheduledActionPolicyRuleCondition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def duration() -> typing.Type['Duration']:
                return Duration
        
            @staticmethod
            def lifecycleAction() -> typing.Type['ScheduledUserLifecycleAction']:
                return ScheduledUserLifecycleAction
            __annotations__ = {
                "duration": duration,
                "lifecycleAction": lifecycleAction,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> 'Duration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lifecycleAction"]) -> 'ScheduledUserLifecycleAction': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["duration", "lifecycleAction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union['Duration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lifecycleAction"]) -> typing.Union['ScheduledUserLifecycleAction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["duration", "lifecycleAction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        duration: typing.Union['Duration', schemas.Unset] = schemas.unset,
        lifecycleAction: typing.Union['ScheduledUserLifecycleAction', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BeforeScheduledActionPolicyRuleCondition':
        return super().__new__(
            cls,
            *args,
            duration=duration,
            lifecycleAction=lifecycleAction,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.duration import Duration
from okta_python_sdk.model.scheduled_user_lifecycle_action import ScheduledUserLifecycleAction

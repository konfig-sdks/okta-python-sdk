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


class PasswordPolicyPasswordSettingsAge(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            expireWarnDays = schemas.IntSchema
            historyCount = schemas.IntSchema
            maxAgeDays = schemas.IntSchema
            minAgeMinutes = schemas.IntSchema
            __annotations__ = {
                "expireWarnDays": expireWarnDays,
                "historyCount": historyCount,
                "maxAgeDays": maxAgeDays,
                "minAgeMinutes": minAgeMinutes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expireWarnDays"]) -> MetaOapg.properties.expireWarnDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["historyCount"]) -> MetaOapg.properties.historyCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxAgeDays"]) -> MetaOapg.properties.maxAgeDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minAgeMinutes"]) -> MetaOapg.properties.minAgeMinutes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expireWarnDays", "historyCount", "maxAgeDays", "minAgeMinutes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expireWarnDays"]) -> typing.Union[MetaOapg.properties.expireWarnDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["historyCount"]) -> typing.Union[MetaOapg.properties.historyCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxAgeDays"]) -> typing.Union[MetaOapg.properties.maxAgeDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minAgeMinutes"]) -> typing.Union[MetaOapg.properties.minAgeMinutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expireWarnDays", "historyCount", "maxAgeDays", "minAgeMinutes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        expireWarnDays: typing.Union[MetaOapg.properties.expireWarnDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        historyCount: typing.Union[MetaOapg.properties.historyCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        maxAgeDays: typing.Union[MetaOapg.properties.maxAgeDays, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minAgeMinutes: typing.Union[MetaOapg.properties.minAgeMinutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PasswordPolicyPasswordSettingsAge':
        return super().__new__(
            cls,
            *args,
            expireWarnDays=expireWarnDays,
            historyCount=historyCount,
            maxAgeDays=maxAgeDays,
            minAgeMinutes=minAgeMinutes,
            _configuration=_configuration,
            **kwargs,
        )

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


class DeviceAccessPolicyRuleCondition(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            managed = schemas.BoolSchema
            registered = schemas.BoolSchema
            __annotations__ = {
                "managed": managed,
                "registered": registered,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["managed"]) -> MetaOapg.properties.managed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registered"]) -> MetaOapg.properties.registered: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["managed", "registered", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["managed"]) -> typing.Union[MetaOapg.properties.managed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registered"]) -> typing.Union[MetaOapg.properties.registered, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["managed", "registered", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        managed: typing.Union[MetaOapg.properties.managed, bool, schemas.Unset] = schemas.unset,
        registered: typing.Union[MetaOapg.properties.registered, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceAccessPolicyRuleCondition':
        return super().__new__(
            cls,
            *args,
            managed=managed,
            registered=registered,
            _configuration=_configuration,
            **kwargs,
        )

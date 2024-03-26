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


class CapabilitiesObject(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def create() -> typing.Type['CapabilitiesCreateObject']:
                return CapabilitiesCreateObject
        
            @staticmethod
            def update() -> typing.Type['CapabilitiesUpdateObject']:
                return CapabilitiesUpdateObject
            __annotations__ = {
                "create": create,
                "update": update,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create"]) -> 'CapabilitiesCreateObject': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update"]) -> 'CapabilitiesUpdateObject': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["create", "update", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create"]) -> typing.Union['CapabilitiesCreateObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update"]) -> typing.Union['CapabilitiesUpdateObject', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["create", "update", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        create: typing.Union['CapabilitiesCreateObject', schemas.Unset] = schemas.unset,
        update: typing.Union['CapabilitiesUpdateObject', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CapabilitiesObject':
        return super().__new__(
            cls,
            *args,
            create=create,
            update=update,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.capabilities_create_object import CapabilitiesCreateObject
from okta_python_sdk.model.capabilities_update_object import CapabilitiesUpdateObject

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


class PlatformConditionEvaluatorPlatformOperatingSystem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def version() -> typing.Type['PlatformConditionEvaluatorPlatformOperatingSystemVersion']:
                return PlatformConditionEvaluatorPlatformOperatingSystemVersion
            expression = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ANDROID": "ANDROID",
                        "IOS": "IOS",
                        "WINDOWS": "WINDOWS",
                        "OSX": "OSX",
                        "OTHER": "OTHER",
                        "ANY": "ANY",
                    }
                
                @schemas.classproperty
                def ANDROID(cls):
                    return cls("ANDROID")
                
                @schemas.classproperty
                def IOS(cls):
                    return cls("IOS")
                
                @schemas.classproperty
                def WINDOWS(cls):
                    return cls("WINDOWS")
                
                @schemas.classproperty
                def OSX(cls):
                    return cls("OSX")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("OTHER")
                
                @schemas.classproperty
                def ANY(cls):
                    return cls("ANY")
            __annotations__ = {
                "version": version,
                "expression": expression,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> 'PlatformConditionEvaluatorPlatformOperatingSystemVersion': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expression"]) -> MetaOapg.properties.expression: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "expression", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union['PlatformConditionEvaluatorPlatformOperatingSystemVersion', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expression"]) -> typing.Union[MetaOapg.properties.expression, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "expression", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union['PlatformConditionEvaluatorPlatformOperatingSystemVersion', schemas.Unset] = schemas.unset,
        expression: typing.Union[MetaOapg.properties.expression, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PlatformConditionEvaluatorPlatformOperatingSystem':
        return super().__new__(
            cls,
            *args,
            version=version,
            expression=expression,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.platform_condition_evaluator_platform_operating_system_version import PlatformConditionEvaluatorPlatformOperatingSystemVersion

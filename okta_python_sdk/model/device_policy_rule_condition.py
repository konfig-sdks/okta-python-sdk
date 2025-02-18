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


class DevicePolicyRuleCondition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            migrated = schemas.BoolSchema
        
            @staticmethod
            def platform() -> typing.Type['DevicePolicyRuleConditionPlatform']:
                return DevicePolicyRuleConditionPlatform
            rooted = schemas.BoolSchema
            
            
            class trustLevel(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ANY": "ANY",
                        "TRUSTED": "TRUSTED",
                    }
                
                @schemas.classproperty
                def ANY(cls):
                    return cls("ANY")
                
                @schemas.classproperty
                def TRUSTED(cls):
                    return cls("TRUSTED")
            __annotations__ = {
                "migrated": migrated,
                "platform": platform,
                "rooted": rooted,
                "trustLevel": trustLevel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrated"]) -> MetaOapg.properties.migrated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> 'DevicePolicyRuleConditionPlatform': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rooted"]) -> MetaOapg.properties.rooted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trustLevel"]) -> MetaOapg.properties.trustLevel: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["migrated", "platform", "rooted", "trustLevel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrated"]) -> typing.Union[MetaOapg.properties.migrated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> typing.Union['DevicePolicyRuleConditionPlatform', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rooted"]) -> typing.Union[MetaOapg.properties.rooted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trustLevel"]) -> typing.Union[MetaOapg.properties.trustLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["migrated", "platform", "rooted", "trustLevel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        migrated: typing.Union[MetaOapg.properties.migrated, bool, schemas.Unset] = schemas.unset,
        platform: typing.Union['DevicePolicyRuleConditionPlatform', schemas.Unset] = schemas.unset,
        rooted: typing.Union[MetaOapg.properties.rooted, bool, schemas.Unset] = schemas.unset,
        trustLevel: typing.Union[MetaOapg.properties.trustLevel, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DevicePolicyRuleCondition':
        return super().__new__(
            cls,
            *args,
            migrated=migrated,
            platform=platform,
            rooted=rooted,
            trustLevel=trustLevel,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.device_policy_rule_condition_platform import DevicePolicyRuleConditionPlatform

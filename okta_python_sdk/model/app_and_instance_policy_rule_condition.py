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


class AppAndInstancePolicyRuleCondition(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class exclude(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AppAndInstanceConditionEvaluatorAppOrInstance']:
                        return AppAndInstanceConditionEvaluatorAppOrInstance
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AppAndInstanceConditionEvaluatorAppOrInstance'], typing.List['AppAndInstanceConditionEvaluatorAppOrInstance']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'exclude':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AppAndInstanceConditionEvaluatorAppOrInstance':
                    return super().__getitem__(i)
            
            
            class include(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AppAndInstanceConditionEvaluatorAppOrInstance']:
                        return AppAndInstanceConditionEvaluatorAppOrInstance
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AppAndInstanceConditionEvaluatorAppOrInstance'], typing.List['AppAndInstanceConditionEvaluatorAppOrInstance']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'include':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AppAndInstanceConditionEvaluatorAppOrInstance':
                    return super().__getitem__(i)
            __annotations__ = {
                "exclude": exclude,
                "include": include,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude"]) -> MetaOapg.properties.exclude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include"]) -> MetaOapg.properties.include: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["exclude", "include", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude"]) -> typing.Union[MetaOapg.properties.exclude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include"]) -> typing.Union[MetaOapg.properties.include, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["exclude", "include", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        exclude: typing.Union[MetaOapg.properties.exclude, list, tuple, schemas.Unset] = schemas.unset,
        include: typing.Union[MetaOapg.properties.include, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppAndInstancePolicyRuleCondition':
        return super().__new__(
            cls,
            *args,
            exclude=exclude,
            include=include,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.app_and_instance_condition_evaluator_app_or_instance import AppAndInstanceConditionEvaluatorAppOrInstance

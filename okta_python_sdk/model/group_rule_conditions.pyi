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


class GroupRuleConditions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def expression() -> typing.Type['GroupRuleExpression']:
                return GroupRuleExpression
        
            @staticmethod
            def people() -> typing.Type['GroupRulePeopleCondition']:
                return GroupRulePeopleCondition
            __annotations__ = {
                "expression": expression,
                "people": people,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expression"]) -> 'GroupRuleExpression': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["people"]) -> 'GroupRulePeopleCondition': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["expression", "people", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expression"]) -> typing.Union['GroupRuleExpression', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["people"]) -> typing.Union['GroupRulePeopleCondition', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["expression", "people", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        expression: typing.Union['GroupRuleExpression', schemas.Unset] = schemas.unset,
        people: typing.Union['GroupRulePeopleCondition', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GroupRuleConditions':
        return super().__new__(
            cls,
            *args,
            expression=expression,
            people=people,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.group_rule_expression import GroupRuleExpression
from okta_python_sdk.model.group_rule_people_condition import GroupRulePeopleCondition

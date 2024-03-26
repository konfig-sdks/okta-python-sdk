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


class AccessPolicyRule(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def actions() -> typing.Type['AccessPolicyRuleActions']:
                return AccessPolicyRuleActions
        
            @staticmethod
            def conditions() -> typing.Type['AccessPolicyRuleConditions']:
                return AccessPolicyRuleConditions
            name = schemas.StrSchema
            __annotations__ = {
                "actions": actions,
                "conditions": conditions,
                "name": name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> 'AccessPolicyRuleActions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> 'AccessPolicyRuleConditions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["actions", "conditions", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> typing.Union['AccessPolicyRuleActions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union['AccessPolicyRuleConditions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["actions", "conditions", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        actions: typing.Union['AccessPolicyRuleActions', schemas.Unset] = schemas.unset,
        conditions: typing.Union['AccessPolicyRuleConditions', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessPolicyRule':
        return super().__new__(
            cls,
            *args,
            actions=actions,
            conditions=conditions,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.access_policy_rule_actions import AccessPolicyRuleActions
from okta_python_sdk.model.access_policy_rule_conditions import AccessPolicyRuleConditions

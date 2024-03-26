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


class AuthorizationServerPolicy(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def _embedded() -> typing.Type['AuthorizationServerPolicyEmbedded']:
                return AuthorizationServerPolicyEmbedded
        
            @staticmethod
            def _links() -> typing.Type['AuthorizationServerPolicyLinks']:
                return AuthorizationServerPolicyLinks
        
            @staticmethod
            def conditions() -> typing.Type['PolicyRuleConditions']:
                return PolicyRuleConditions
            created = schemas.DateTimeSchema
            id = schemas.StrSchema
            lastUpdated = schemas.DateTimeSchema
            name = schemas.StrSchema
            priority = schemas.IntSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
            system = schemas.BoolSchema
        
            @staticmethod
            def type() -> typing.Type['PolicyType']:
                return PolicyType
            __annotations__ = {
                "description": description,
                "_embedded": _embedded,
                "_links": _links,
                "conditions": conditions,
                "created": created,
                "id": id,
                "lastUpdated": lastUpdated,
                "name": name,
                "priority": priority,
                "status": status,
                "system": system,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_embedded"]) -> 'AuthorizationServerPolicyEmbedded': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'AuthorizationServerPolicyLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> 'PolicyRuleConditions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdated"]) -> MetaOapg.properties.lastUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["system"]) -> MetaOapg.properties.system: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'PolicyType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "_embedded", "_links", "conditions", "created", "id", "lastUpdated", "name", "priority", "status", "system", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_embedded"]) -> typing.Union['AuthorizationServerPolicyEmbedded', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['AuthorizationServerPolicyLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union['PolicyRuleConditions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdated"]) -> typing.Union[MetaOapg.properties.lastUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["system"]) -> typing.Union[MetaOapg.properties.system, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['PolicyType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "_embedded", "_links", "conditions", "created", "id", "lastUpdated", "name", "priority", "status", "system", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _embedded: typing.Union['AuthorizationServerPolicyEmbedded', schemas.Unset] = schemas.unset,
        _links: typing.Union['AuthorizationServerPolicyLinks', schemas.Unset] = schemas.unset,
        conditions: typing.Union['PolicyRuleConditions', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        lastUpdated: typing.Union[MetaOapg.properties.lastUpdated, str, datetime, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        system: typing.Union[MetaOapg.properties.system, bool, schemas.Unset] = schemas.unset,
        type: typing.Union['PolicyType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthorizationServerPolicy':
        return super().__new__(
            cls,
            *args,
            description=description,
            _embedded=_embedded,
            _links=_links,
            conditions=conditions,
            created=created,
            id=id,
            lastUpdated=lastUpdated,
            name=name,
            priority=priority,
            status=status,
            system=system,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.authorization_server_policy_embedded import AuthorizationServerPolicyEmbedded
from okta_python_sdk.model.authorization_server_policy_links import AuthorizationServerPolicyLinks
from okta_python_sdk.model.policy_rule_conditions import PolicyRuleConditions
from okta_python_sdk.model.policy_type import PolicyType

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


class LogEvent(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
        
            @staticmethod
            def actor() -> typing.Type['LogActor']:
                return LogActor
        
            @staticmethod
            def authenticationContext() -> typing.Type['LogAuthenticationContext']:
                return LogAuthenticationContext
        
            @staticmethod
            def client() -> typing.Type['LogClient']:
                return LogClient
        
            @staticmethod
            def debugContext() -> typing.Type['LogDebugContext']:
                return LogDebugContext
            displayMessage = schemas.StrSchema
            eventType = schemas.StrSchema
            legacyEventType = schemas.StrSchema
        
            @staticmethod
            def outcome() -> typing.Type['LogOutcome']:
                return LogOutcome
            published = schemas.DateTimeSchema
        
            @staticmethod
            def request() -> typing.Type['LogRequest']:
                return LogRequest
        
            @staticmethod
            def securityContext() -> typing.Type['LogSecurityContext']:
                return LogSecurityContext
        
            @staticmethod
            def severity() -> typing.Type['LogSeverity']:
                return LogSeverity
            
            
            class target(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LogTarget']:
                        return LogTarget
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LogTarget'], typing.List['LogTarget']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'target':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LogTarget':
                    return super().__getitem__(i)
        
            @staticmethod
            def transaction() -> typing.Type['LogTransaction']:
                return LogTransaction
            uuid = schemas.StrSchema
            __annotations__ = {
                "version": version,
                "actor": actor,
                "authenticationContext": authenticationContext,
                "client": client,
                "debugContext": debugContext,
                "displayMessage": displayMessage,
                "eventType": eventType,
                "legacyEventType": legacyEventType,
                "outcome": outcome,
                "published": published,
                "request": request,
                "securityContext": securityContext,
                "severity": severity,
                "target": target,
                "transaction": transaction,
                "uuid": uuid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor"]) -> 'LogActor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authenticationContext"]) -> 'LogAuthenticationContext': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'LogClient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["debugContext"]) -> 'LogDebugContext': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayMessage"]) -> MetaOapg.properties.displayMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventType"]) -> MetaOapg.properties.eventType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["legacyEventType"]) -> MetaOapg.properties.legacyEventType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outcome"]) -> 'LogOutcome': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published"]) -> MetaOapg.properties.published: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request"]) -> 'LogRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["securityContext"]) -> 'LogSecurityContext': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["severity"]) -> 'LogSeverity': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target"]) -> MetaOapg.properties.target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction"]) -> 'LogTransaction': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "actor", "authenticationContext", "client", "debugContext", "displayMessage", "eventType", "legacyEventType", "outcome", "published", "request", "securityContext", "severity", "target", "transaction", "uuid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor"]) -> typing.Union['LogActor', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authenticationContext"]) -> typing.Union['LogAuthenticationContext', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> typing.Union['LogClient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["debugContext"]) -> typing.Union['LogDebugContext', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayMessage"]) -> typing.Union[MetaOapg.properties.displayMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventType"]) -> typing.Union[MetaOapg.properties.eventType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["legacyEventType"]) -> typing.Union[MetaOapg.properties.legacyEventType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outcome"]) -> typing.Union['LogOutcome', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published"]) -> typing.Union[MetaOapg.properties.published, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request"]) -> typing.Union['LogRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["securityContext"]) -> typing.Union['LogSecurityContext', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["severity"]) -> typing.Union['LogSeverity', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target"]) -> typing.Union[MetaOapg.properties.target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction"]) -> typing.Union['LogTransaction', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "actor", "authenticationContext", "client", "debugContext", "displayMessage", "eventType", "legacyEventType", "outcome", "published", "request", "securityContext", "severity", "target", "transaction", "uuid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        actor: typing.Union['LogActor', schemas.Unset] = schemas.unset,
        authenticationContext: typing.Union['LogAuthenticationContext', schemas.Unset] = schemas.unset,
        client: typing.Union['LogClient', schemas.Unset] = schemas.unset,
        debugContext: typing.Union['LogDebugContext', schemas.Unset] = schemas.unset,
        displayMessage: typing.Union[MetaOapg.properties.displayMessage, str, schemas.Unset] = schemas.unset,
        eventType: typing.Union[MetaOapg.properties.eventType, str, schemas.Unset] = schemas.unset,
        legacyEventType: typing.Union[MetaOapg.properties.legacyEventType, str, schemas.Unset] = schemas.unset,
        outcome: typing.Union['LogOutcome', schemas.Unset] = schemas.unset,
        published: typing.Union[MetaOapg.properties.published, str, datetime, schemas.Unset] = schemas.unset,
        request: typing.Union['LogRequest', schemas.Unset] = schemas.unset,
        securityContext: typing.Union['LogSecurityContext', schemas.Unset] = schemas.unset,
        severity: typing.Union['LogSeverity', schemas.Unset] = schemas.unset,
        target: typing.Union[MetaOapg.properties.target, list, tuple, schemas.Unset] = schemas.unset,
        transaction: typing.Union['LogTransaction', schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogEvent':
        return super().__new__(
            cls,
            *args,
            version=version,
            actor=actor,
            authenticationContext=authenticationContext,
            client=client,
            debugContext=debugContext,
            displayMessage=displayMessage,
            eventType=eventType,
            legacyEventType=legacyEventType,
            outcome=outcome,
            published=published,
            request=request,
            securityContext=securityContext,
            severity=severity,
            target=target,
            transaction=transaction,
            uuid=uuid,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.log_actor import LogActor
from okta_python_sdk.model.log_authentication_context import LogAuthenticationContext
from okta_python_sdk.model.log_client import LogClient
from okta_python_sdk.model.log_debug_context import LogDebugContext
from okta_python_sdk.model.log_outcome import LogOutcome
from okta_python_sdk.model.log_request import LogRequest
from okta_python_sdk.model.log_security_context import LogSecurityContext
from okta_python_sdk.model.log_severity import LogSeverity
from okta_python_sdk.model.log_target import LogTarget
from okta_python_sdk.model.log_transaction import LogTransaction

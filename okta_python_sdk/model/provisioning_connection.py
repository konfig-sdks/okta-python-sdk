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


class ProvisioningConnection(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def _links() -> typing.Type['ProvisioningConnectionLinks']:
                return ProvisioningConnectionLinks
        
            @staticmethod
            def authScheme() -> typing.Type['ProvisioningConnectionAuthScheme']:
                return ProvisioningConnectionAuthScheme
        
            @staticmethod
            def status() -> typing.Type['ProvisioningConnectionStatus']:
                return ProvisioningConnectionStatus
            __annotations__ = {
                "_links": _links,
                "authScheme": authScheme,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'ProvisioningConnectionLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authScheme"]) -> 'ProvisioningConnectionAuthScheme': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ProvisioningConnectionStatus': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "authScheme", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['ProvisioningConnectionLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authScheme"]) -> typing.Union['ProvisioningConnectionAuthScheme', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['ProvisioningConnectionStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "authScheme", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _links: typing.Union['ProvisioningConnectionLinks', schemas.Unset] = schemas.unset,
        authScheme: typing.Union['ProvisioningConnectionAuthScheme', schemas.Unset] = schemas.unset,
        status: typing.Union['ProvisioningConnectionStatus', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProvisioningConnection':
        return super().__new__(
            cls,
            *args,
            _links=_links,
            authScheme=authScheme,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.provisioning_connection_auth_scheme import ProvisioningConnectionAuthScheme
from okta_python_sdk.model.provisioning_connection_links import ProvisioningConnectionLinks
from okta_python_sdk.model.provisioning_connection_status import ProvisioningConnectionStatus

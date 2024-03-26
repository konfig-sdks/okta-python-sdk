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


class ApplicationCredentialsUsernameTemplate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            pushStatus = schemas.StrSchema
            suffix = schemas.StrSchema
            template = schemas.StrSchema
            type = schemas.StrSchema
            __annotations__ = {
                "pushStatus": pushStatus,
                "suffix": suffix,
                "template": template,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pushStatus"]) -> MetaOapg.properties.pushStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> MetaOapg.properties.suffix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template"]) -> MetaOapg.properties.template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pushStatus", "suffix", "template", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pushStatus"]) -> typing.Union[MetaOapg.properties.pushStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union[MetaOapg.properties.suffix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template"]) -> typing.Union[MetaOapg.properties.template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pushStatus", "suffix", "template", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pushStatus: typing.Union[MetaOapg.properties.pushStatus, str, schemas.Unset] = schemas.unset,
        suffix: typing.Union[MetaOapg.properties.suffix, str, schemas.Unset] = schemas.unset,
        template: typing.Union[MetaOapg.properties.template, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationCredentialsUsernameTemplate':
        return super().__new__(
            cls,
            *args,
            pushStatus=pushStatus,
            suffix=suffix,
            template=template,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

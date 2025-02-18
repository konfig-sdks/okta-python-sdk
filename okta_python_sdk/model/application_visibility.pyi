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


class ApplicationVisibility(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def appLinks() -> typing.Type['ApplicationVisibilityAppLinks']:
                return ApplicationVisibilityAppLinks
            autoLaunch = schemas.BoolSchema
            autoSubmitToolbar = schemas.BoolSchema
        
            @staticmethod
            def hide() -> typing.Type['ApplicationVisibilityHide']:
                return ApplicationVisibilityHide
            __annotations__ = {
                "appLinks": appLinks,
                "autoLaunch": autoLaunch,
                "autoSubmitToolbar": autoSubmitToolbar,
                "hide": hide,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appLinks"]) -> 'ApplicationVisibilityAppLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoLaunch"]) -> MetaOapg.properties.autoLaunch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoSubmitToolbar"]) -> MetaOapg.properties.autoSubmitToolbar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hide"]) -> 'ApplicationVisibilityHide': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["appLinks", "autoLaunch", "autoSubmitToolbar", "hide", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appLinks"]) -> typing.Union['ApplicationVisibilityAppLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoLaunch"]) -> typing.Union[MetaOapg.properties.autoLaunch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoSubmitToolbar"]) -> typing.Union[MetaOapg.properties.autoSubmitToolbar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hide"]) -> typing.Union['ApplicationVisibilityHide', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["appLinks", "autoLaunch", "autoSubmitToolbar", "hide", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        appLinks: typing.Union['ApplicationVisibilityAppLinks', schemas.Unset] = schemas.unset,
        autoLaunch: typing.Union[MetaOapg.properties.autoLaunch, bool, schemas.Unset] = schemas.unset,
        autoSubmitToolbar: typing.Union[MetaOapg.properties.autoSubmitToolbar, bool, schemas.Unset] = schemas.unset,
        hide: typing.Union['ApplicationVisibilityHide', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicationVisibility':
        return super().__new__(
            cls,
            *args,
            appLinks=appLinks,
            autoLaunch=autoLaunch,
            autoSubmitToolbar=autoSubmitToolbar,
            hide=hide,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.application_visibility_app_links import ApplicationVisibilityAppLinks
from okta_python_sdk.model.application_visibility_hide import ApplicationVisibilityHide

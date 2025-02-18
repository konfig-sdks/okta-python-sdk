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


class Application(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def _embedded() -> typing.Type['ApplicationEmbedded']:
                return ApplicationEmbedded
        
            @staticmethod
            def _links() -> typing.Type['ApplicationLinks']:
                return ApplicationLinks
        
            @staticmethod
            def accessibility() -> typing.Type['ApplicationAccessibility']:
                return ApplicationAccessibility
            created = schemas.DateTimeSchema
        
            @staticmethod
            def credentials() -> typing.Type['ApplicationCredentials']:
                return ApplicationCredentials
        
            @staticmethod
            def features() -> typing.Type['ApplicationFeatures']:
                return ApplicationFeatures
            id = schemas.StrSchema
            label = schemas.StrSchema
            lastUpdated = schemas.DateTimeSchema
        
            @staticmethod
            def licensing() -> typing.Type['ApplicationLicensing']:
                return ApplicationLicensing
            name = schemas.StrSchema
        
            @staticmethod
            def profile() -> typing.Type['ApplicationProfile']:
                return ApplicationProfile
        
            @staticmethod
            def settings() -> typing.Type['ApplicationSettings']:
                return ApplicationSettings
        
            @staticmethod
            def signOnMode() -> typing.Type['ApplicationSignOnMode']:
                return ApplicationSignOnMode
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ACTIVE": "ACTIVE",
                        "INACTIVE": "INACTIVE",
                        "DELETED": "DELETED",
                    }
                
                @schemas.classproperty
                def ACTIVE(cls):
                    return cls("ACTIVE")
                
                @schemas.classproperty
                def INACTIVE(cls):
                    return cls("INACTIVE")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("DELETED")
        
            @staticmethod
            def visibility() -> typing.Type['ApplicationVisibility']:
                return ApplicationVisibility
            __annotations__ = {
                "_embedded": _embedded,
                "_links": _links,
                "accessibility": accessibility,
                "created": created,
                "credentials": credentials,
                "features": features,
                "id": id,
                "label": label,
                "lastUpdated": lastUpdated,
                "licensing": licensing,
                "name": name,
                "profile": profile,
                "settings": settings,
                "signOnMode": signOnMode,
                "status": status,
                "visibility": visibility,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_embedded"]) -> 'ApplicationEmbedded': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> 'ApplicationLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessibility"]) -> 'ApplicationAccessibility': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credentials"]) -> 'ApplicationCredentials': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["features"]) -> 'ApplicationFeatures': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> MetaOapg.properties.label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdated"]) -> MetaOapg.properties.lastUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["licensing"]) -> 'ApplicationLicensing': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile"]) -> 'ApplicationProfile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'ApplicationSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signOnMode"]) -> 'ApplicationSignOnMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["visibility"]) -> 'ApplicationVisibility': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_embedded", "_links", "accessibility", "created", "credentials", "features", "id", "label", "lastUpdated", "licensing", "name", "profile", "settings", "signOnMode", "status", "visibility", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_embedded"]) -> typing.Union['ApplicationEmbedded', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union['ApplicationLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessibility"]) -> typing.Union['ApplicationAccessibility', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credentials"]) -> typing.Union['ApplicationCredentials', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["features"]) -> typing.Union['ApplicationFeatures', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union[MetaOapg.properties.label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdated"]) -> typing.Union[MetaOapg.properties.lastUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["licensing"]) -> typing.Union['ApplicationLicensing', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile"]) -> typing.Union['ApplicationProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['ApplicationSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signOnMode"]) -> typing.Union['ApplicationSignOnMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["visibility"]) -> typing.Union['ApplicationVisibility', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_embedded", "_links", "accessibility", "created", "credentials", "features", "id", "label", "lastUpdated", "licensing", "name", "profile", "settings", "signOnMode", "status", "visibility", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _embedded: typing.Union['ApplicationEmbedded', schemas.Unset] = schemas.unset,
        _links: typing.Union['ApplicationLinks', schemas.Unset] = schemas.unset,
        accessibility: typing.Union['ApplicationAccessibility', schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        credentials: typing.Union['ApplicationCredentials', schemas.Unset] = schemas.unset,
        features: typing.Union['ApplicationFeatures', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        label: typing.Union[MetaOapg.properties.label, str, schemas.Unset] = schemas.unset,
        lastUpdated: typing.Union[MetaOapg.properties.lastUpdated, str, datetime, schemas.Unset] = schemas.unset,
        licensing: typing.Union['ApplicationLicensing', schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        profile: typing.Union['ApplicationProfile', schemas.Unset] = schemas.unset,
        settings: typing.Union['ApplicationSettings', schemas.Unset] = schemas.unset,
        signOnMode: typing.Union['ApplicationSignOnMode', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        visibility: typing.Union['ApplicationVisibility', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Application':
        return super().__new__(
            cls,
            *args,
            _embedded=_embedded,
            _links=_links,
            accessibility=accessibility,
            created=created,
            credentials=credentials,
            features=features,
            id=id,
            label=label,
            lastUpdated=lastUpdated,
            licensing=licensing,
            name=name,
            profile=profile,
            settings=settings,
            signOnMode=signOnMode,
            status=status,
            visibility=visibility,
            _configuration=_configuration,
            **kwargs,
        )

from okta_python_sdk.model.application_accessibility import ApplicationAccessibility
from okta_python_sdk.model.application_credentials import ApplicationCredentials
from okta_python_sdk.model.application_embedded import ApplicationEmbedded
from okta_python_sdk.model.application_features import ApplicationFeatures
from okta_python_sdk.model.application_licensing import ApplicationLicensing
from okta_python_sdk.model.application_links import ApplicationLinks
from okta_python_sdk.model.application_profile import ApplicationProfile
from okta_python_sdk.model.application_settings import ApplicationSettings
from okta_python_sdk.model.application_sign_on_mode import ApplicationSignOnMode
from okta_python_sdk.model.application_visibility import ApplicationVisibility

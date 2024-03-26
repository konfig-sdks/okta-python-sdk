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


class OrgSetting(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class _links(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.DictSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
                ) -> '_links':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            address1 = schemas.StrSchema
            address2 = schemas.StrSchema
            city = schemas.StrSchema
            companyName = schemas.StrSchema
            country = schemas.StrSchema
            created = schemas.DateTimeSchema
            endUserSupportHelpURL = schemas.StrSchema
            expiresAt = schemas.DateTimeSchema
            id = schemas.StrSchema
            lastUpdated = schemas.DateTimeSchema
            phoneNumber = schemas.StrSchema
            postalCode = schemas.StrSchema
            state = schemas.StrSchema
            status = schemas.StrSchema
            subdomain = schemas.StrSchema
            supportPhoneNumber = schemas.StrSchema
            website = schemas.StrSchema
            __annotations__ = {
                "_links": _links,
                "address1": address1,
                "address2": address2,
                "city": city,
                "companyName": companyName,
                "country": country,
                "created": created,
                "endUserSupportHelpURL": endUserSupportHelpURL,
                "expiresAt": expiresAt,
                "id": id,
                "lastUpdated": lastUpdated,
                "phoneNumber": phoneNumber,
                "postalCode": postalCode,
                "state": state,
                "status": status,
                "subdomain": subdomain,
                "supportPhoneNumber": supportPhoneNumber,
                "website": website,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_links"]) -> MetaOapg.properties._links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address1"]) -> MetaOapg.properties.address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address2"]) -> MetaOapg.properties.address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["companyName"]) -> MetaOapg.properties.companyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endUserSupportHelpURL"]) -> MetaOapg.properties.endUserSupportHelpURL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiresAt"]) -> MetaOapg.properties.expiresAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUpdated"]) -> MetaOapg.properties.lastUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumber"]) -> MetaOapg.properties.phoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCode"]) -> MetaOapg.properties.postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subdomain"]) -> MetaOapg.properties.subdomain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportPhoneNumber"]) -> MetaOapg.properties.supportPhoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_links", "address1", "address2", "city", "companyName", "country", "created", "endUserSupportHelpURL", "expiresAt", "id", "lastUpdated", "phoneNumber", "postalCode", "state", "status", "subdomain", "supportPhoneNumber", "website", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_links"]) -> typing.Union[MetaOapg.properties._links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address1"]) -> typing.Union[MetaOapg.properties.address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address2"]) -> typing.Union[MetaOapg.properties.address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["companyName"]) -> typing.Union[MetaOapg.properties.companyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endUserSupportHelpURL"]) -> typing.Union[MetaOapg.properties.endUserSupportHelpURL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiresAt"]) -> typing.Union[MetaOapg.properties.expiresAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUpdated"]) -> typing.Union[MetaOapg.properties.lastUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumber"]) -> typing.Union[MetaOapg.properties.phoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCode"]) -> typing.Union[MetaOapg.properties.postalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subdomain"]) -> typing.Union[MetaOapg.properties.subdomain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportPhoneNumber"]) -> typing.Union[MetaOapg.properties.supportPhoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_links", "address1", "address2", "city", "companyName", "country", "created", "endUserSupportHelpURL", "expiresAt", "id", "lastUpdated", "phoneNumber", "postalCode", "state", "status", "subdomain", "supportPhoneNumber", "website", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _links: typing.Union[MetaOapg.properties._links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        address1: typing.Union[MetaOapg.properties.address1, str, schemas.Unset] = schemas.unset,
        address2: typing.Union[MetaOapg.properties.address2, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        companyName: typing.Union[MetaOapg.properties.companyName, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        endUserSupportHelpURL: typing.Union[MetaOapg.properties.endUserSupportHelpURL, str, schemas.Unset] = schemas.unset,
        expiresAt: typing.Union[MetaOapg.properties.expiresAt, str, datetime, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        lastUpdated: typing.Union[MetaOapg.properties.lastUpdated, str, datetime, schemas.Unset] = schemas.unset,
        phoneNumber: typing.Union[MetaOapg.properties.phoneNumber, str, schemas.Unset] = schemas.unset,
        postalCode: typing.Union[MetaOapg.properties.postalCode, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        subdomain: typing.Union[MetaOapg.properties.subdomain, str, schemas.Unset] = schemas.unset,
        supportPhoneNumber: typing.Union[MetaOapg.properties.supportPhoneNumber, str, schemas.Unset] = schemas.unset,
        website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrgSetting':
        return super().__new__(
            cls,
            *args,
            _links=_links,
            address1=address1,
            address2=address2,
            city=city,
            companyName=companyName,
            country=country,
            created=created,
            endUserSupportHelpURL=endUserSupportHelpURL,
            expiresAt=expiresAt,
            id=id,
            lastUpdated=lastUpdated,
            phoneNumber=phoneNumber,
            postalCode=postalCode,
            state=state,
            status=status,
            subdomain=subdomain,
            supportPhoneNumber=supportPhoneNumber,
            website=website,
            _configuration=_configuration,
            **kwargs,
        )

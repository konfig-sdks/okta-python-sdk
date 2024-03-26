# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class OrgSetting(BaseModel):
    _links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='_links')

    address1: typing.Optional[str] = Field(None, alias='address1')

    address2: typing.Optional[str] = Field(None, alias='address2')

    city: typing.Optional[str] = Field(None, alias='city')

    company_name: typing.Optional[str] = Field(None, alias='companyName')

    country: typing.Optional[str] = Field(None, alias='country')

    created: typing.Optional[datetime] = Field(None, alias='created')

    end_user_support_help_u_r_l: typing.Optional[str] = Field(None, alias='endUserSupportHelpURL')

    expires_at: typing.Optional[datetime] = Field(None, alias='expiresAt')

    id: typing.Optional[str] = Field(None, alias='id')

    last_updated: typing.Optional[datetime] = Field(None, alias='lastUpdated')

    phone_number: typing.Optional[str] = Field(None, alias='phoneNumber')

    postal_code: typing.Optional[str] = Field(None, alias='postalCode')

    state: typing.Optional[str] = Field(None, alias='state')

    status: typing.Optional[str] = Field(None, alias='status')

    subdomain: typing.Optional[str] = Field(None, alias='subdomain')

    support_phone_number: typing.Optional[str] = Field(None, alias='supportPhoneNumber')

    website: typing.Optional[str] = Field(None, alias='website')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

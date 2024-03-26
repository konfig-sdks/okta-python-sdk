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


class WsFederationApplicationSettingsApplication(BaseModel):
    attribute_statements: typing.Optional[str] = Field(None, alias='attributeStatements')

    audience_restriction: typing.Optional[str] = Field(None, alias='audienceRestriction')

    authn_context_class_ref: typing.Optional[str] = Field(None, alias='authnContextClassRef')

    group_filter: typing.Optional[str] = Field(None, alias='groupFilter')

    group_name: typing.Optional[str] = Field(None, alias='groupName')

    group_value_format: typing.Optional[str] = Field(None, alias='groupValueFormat')

    name_i_d_format: typing.Optional[str] = Field(None, alias='nameIDFormat')

    realm: typing.Optional[str] = Field(None, alias='realm')

    site_u_r_l: typing.Optional[str] = Field(None, alias='siteURL')

    username_attribute: typing.Optional[str] = Field(None, alias='usernameAttribute')

    w_reply_override: typing.Optional[bool] = Field(None, alias='wReplyOverride')

    w_reply_u_r_l: typing.Optional[str] = Field(None, alias='wReplyURL')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

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

from okta_python_sdk.type.catalog_application_status import CatalogApplicationStatus

class RequiredCatalogApplication(TypedDict):
    pass

class OptionalCatalogApplication(TypedDict, total=False):
    description: str

    _links: typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    category: str

    displayName: str

    features: typing.List[str]

    id: str

    lastUpdated: datetime

    name: str

    signOnModes: typing.List[str]

    status: CatalogApplicationStatus

    verificationStatus: str

    website: str

class CatalogApplication(RequiredCatalogApplication, OptionalCatalogApplication):
    pass

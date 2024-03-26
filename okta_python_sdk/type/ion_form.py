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

from okta_python_sdk.type.ion_field import IonField
from okta_python_sdk.type.ion_form_rel import IonFormRel
from okta_python_sdk.type.ion_form_relates_to import IonFormRelatesTo

class RequiredIonForm(TypedDict):
    pass

class OptionalIonForm(TypedDict, total=False):
    accepts: str

    href: str

    method: str

    name: str

    produces: str

    refresh: int

    rel: IonFormRel

    relatesTo: IonFormRelatesTo

    value: 'typing.List[IonField]'

class IonForm(RequiredIonForm, OptionalIonForm):
    pass

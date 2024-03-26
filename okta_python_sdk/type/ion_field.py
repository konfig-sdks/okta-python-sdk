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

from okta_python_sdk.type.ion_field_value import IonFieldValue
if TYPE_CHECKING:
    from okta_python_sdk.type.ion_form import IonForm

class RequiredIonField(TypedDict):
    pass

class OptionalIonField(TypedDict, total=False):
    form: 'IonForm'

    label: str

    mutable: bool

    name: str

    required: bool

    secret: bool

    type: str

    value: IonFieldValue

    visible: bool

class IonField(RequiredIonField, OptionalIonField):
    pass

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

from okta_python_sdk.type.sms_template_type import SmsTemplateType

class RequiredSmsTemplate(TypedDict):
    pass

class OptionalSmsTemplate(TypedDict, total=False):
    created: datetime

    id: str

    lastUpdated: datetime

    name: str

    template: str

    translations: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    type: SmsTemplateType

class SmsTemplate(RequiredSmsTemplate, OptionalSmsTemplate):
    pass

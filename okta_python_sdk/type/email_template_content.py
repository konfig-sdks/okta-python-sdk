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


class RequiredEmailTemplateContent(TypedDict):
    pass

class OptionalEmailTemplateContent(TypedDict, total=False):
    _links: typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    body: str

    fromAddress: str

    fromName: str

    subject: str

class EmailTemplateContent(RequiredEmailTemplateContent, OptionalEmailTemplateContent):
    pass

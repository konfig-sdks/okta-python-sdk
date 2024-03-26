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

from okta_python_sdk.type.log_actor_detail import LogActorDetail

class RequiredLogActor(TypedDict):
    pass

class OptionalLogActor(TypedDict, total=False):
    alternateId: str

    detail: LogActorDetail

    displayName: str

    id: str

    type: str

class LogActor(RequiredLogActor, OptionalLogActor):
    pass

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


class InlineHookGetSuccessResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['InlineHook']:
            return InlineHook

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['InlineHook'], typing.List['InlineHook']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InlineHookGetSuccessResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'InlineHook':
        return super().__getitem__(i)

from okta_python_sdk.model.inline_hook import InlineHook

# coding: utf-8

"""
    Okta API

    Allows customers to easily access the Okta API

    The version of the OpenAPI document: 2.16.0
    Contact: devex-public@okta.com
    Created by: https://developer.okta.com/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from okta_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from okta_python_sdk.api_response import AsyncGeneratorResponse
from okta_python_sdk import api_client, exceptions
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



from ...api_client import Dictionary

from . import path

# Query params
RemoveUsersSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'removeUsers': typing.Union[RemoveUsersSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_remove_users = api_client.QueryParameter(
    name="removeUsers",
    style=api_client.ParameterStyle.FORM,
    schema=RemoveUsersSchema,
    explode=True,
)
# Path params
RuleIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'ruleId': typing.Union[RuleIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_rule_id = api_client.PathParameter(
    name="ruleId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RuleIdSchema,
    required=True,
)
_auth = [
    'api_token',
]


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
)
_status_code_to_response = {
    '202': _response_for_202,
}


class BaseApi(api_client.Api):

    def _remove_rule_by_id_mapped_args(
        self,
        rule_id: str,
        remove_users: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if remove_users is not None:
            _query_params["removeUsers"] = remove_users
        if rule_id is not None:
            _path_params["ruleId"] = rule_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aremove_rule_by_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Delete a group Rule
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_rule_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_remove_users,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/groups/rules/{ruleId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _remove_rule_by_id_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Delete a group Rule
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_rule_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_remove_users,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/groups/rules/{ruleId}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class RemoveRuleByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aremove_rule_by_id(
        self,
        rule_id: str,
        remove_users: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_rule_by_id_mapped_args(
            rule_id=rule_id,
            remove_users=remove_users,
        )
        return await self._aremove_rule_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def remove_rule_by_id(
        self,
        rule_id: str,
        remove_users: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_rule_by_id_mapped_args(
            rule_id=rule_id,
            remove_users=remove_users,
        )
        return self._remove_rule_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class RemoveRuleById(BaseApi):

    async def aremove_rule_by_id(
        self,
        rule_id: str,
        remove_users: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aremove_rule_by_id(
            rule_id=rule_id,
            remove_users=remove_users,
            **kwargs,
        )
    
    
    def remove_rule_by_id(
        self,
        rule_id: str,
        remove_users: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.remove_rule_by_id(
            rule_id=rule_id,
            remove_users=remove_users,
        )


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        rule_id: str,
        remove_users: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._remove_rule_by_id_mapped_args(
            rule_id=rule_id,
            remove_users=remove_users,
        )
        return await self._aremove_rule_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        rule_id: str,
        remove_users: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._remove_rule_by_id_mapped_args(
            rule_id=rule_id,
            remove_users=remove_users,
        )
        return self._remove_rule_by_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )


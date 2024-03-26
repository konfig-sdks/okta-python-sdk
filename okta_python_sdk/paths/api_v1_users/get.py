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

from okta_python_sdk.model.user_list_active_users_response import UserListActiveUsersResponse as UserListActiveUsersResponseSchema

from okta_python_sdk.type.user_list_active_users_response import UserListActiveUsersResponse

from ...api_client import Dictionary
from okta_python_sdk.pydantic.user_list_active_users_response import UserListActiveUsersResponse as UserListActiveUsersResponsePydantic

from . import path

# Query params
QSchema = schemas.StrSchema
AfterSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
FilterSchema = schemas.StrSchema
SearchSchema = schemas.StrSchema
SortBySchema = schemas.StrSchema
SortOrderSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'q': typing.Union[QSchema, str, ],
        'after': typing.Union[AfterSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'filter': typing.Union[FilterSchema, str, ],
        'search': typing.Union[SearchSchema, str, ],
        'sortBy': typing.Union[SortBySchema, str, ],
        'sortOrder': typing.Union[SortOrderSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_q = api_client.QueryParameter(
    name="q",
    style=api_client.ParameterStyle.FORM,
    schema=QSchema,
    explode=True,
)
request_query_after = api_client.QueryParameter(
    name="after",
    style=api_client.ParameterStyle.FORM,
    schema=AfterSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sortBy",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_sort_order = api_client.QueryParameter(
    name="sortOrder",
    style=api_client.ParameterStyle.FORM,
    schema=SortOrderSchema,
    explode=True,
)
_auth = [
    'api_token',
]
SchemaFor200ResponseBodyApplicationJson = UserListActiveUsersResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: UserListActiveUsersResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UserListActiveUsersResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_active_users_mapped_args(
        self,
        q: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if q is not None:
            _query_params["q"] = q
        if after is not None:
            _query_params["after"] = after
        if limit is not None:
            _query_params["limit"] = limit
        if filter is not None:
            _query_params["filter"] = filter
        if search is not None:
            _query_params["search"] = search
        if sort_by is not None:
            _query_params["sortBy"] = sort_by
        if sort_order is not None:
            _query_params["sortOrder"] = sort_order
        args.query = _query_params
        return args

    async def _alist_active_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List Users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_q,
            request_query_after,
            request_query_limit,
            request_query_filter,
            request_query_search,
            request_query_sort_by,
            request_query_sort_order,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/users',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _list_active_users_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List Users
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_q,
            request_query_after,
            request_query_limit,
            request_query_filter,
            request_query_search,
            request_query_sort_by,
            request_query_sort_order,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/users',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class ListActiveUsersRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_active_users(
        self,
        q: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_active_users_mapped_args(
            q=q,
            after=after,
            limit=limit,
            filter=filter,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return await self._alist_active_users_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_active_users(
        self,
        q: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_active_users_mapped_args(
            q=q,
            after=after,
            limit=limit,
            filter=filter,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return self._list_active_users_oapg(
            query_params=args.query,
        )

class ListActiveUsers(BaseApi):

    async def alist_active_users(
        self,
        q: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserListActiveUsersResponsePydantic:
        raw_response = await self.raw.alist_active_users(
            q=q,
            after=after,
            limit=limit,
            filter=filter,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
            **kwargs,
        )
        if validate:
            return RootModel[UserListActiveUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserListActiveUsersResponsePydantic, raw_response.body)
    
    
    def list_active_users(
        self,
        q: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UserListActiveUsersResponsePydantic:
        raw_response = self.raw.list_active_users(
            q=q,
            after=after,
            limit=limit,
            filter=filter,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        if validate:
            return RootModel[UserListActiveUsersResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(UserListActiveUsersResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        q: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_active_users_mapped_args(
            q=q,
            after=after,
            limit=limit,
            filter=filter,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return await self._alist_active_users_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        q: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_active_users_mapped_args(
            q=q,
            after=after,
            limit=limit,
            filter=filter,
            search=search,
            sort_by=sort_by,
            sort_order=sort_order,
        )
        return self._list_active_users_oapg(
            query_params=args.query,
        )


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

from okta_python_sdk.model.group_get_role_targets_catalog_apps_response import GroupGetRoleTargetsCatalogAppsResponse as GroupGetRoleTargetsCatalogAppsResponseSchema

from okta_python_sdk.type.group_get_role_targets_catalog_apps_response import GroupGetRoleTargetsCatalogAppsResponse

from ...api_client import Dictionary
from okta_python_sdk.pydantic.group_get_role_targets_catalog_apps_response import GroupGetRoleTargetsCatalogAppsResponse as GroupGetRoleTargetsCatalogAppsResponsePydantic

# Query params
AfterSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'after': typing.Union[AfterSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


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
# Path params
GroupIdSchema = schemas.StrSchema
RoleIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'groupId': typing.Union[GroupIdSchema, str, ],
        'roleId': typing.Union[RoleIdSchema, str, ],
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


request_path_group_id = api_client.PathParameter(
    name="groupId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=GroupIdSchema,
    required=True,
)
request_path_role_id = api_client.PathParameter(
    name="roleId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RoleIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = GroupGetRoleTargetsCatalogAppsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: GroupGetRoleTargetsCatalogAppsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: GroupGetRoleTargetsCatalogAppsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_role_targets_catalog_apps_mapped_args(
        self,
        group_id: str,
        role_id: str,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if after is not None:
            _query_params["after"] = after
        if limit is not None:
            _query_params["limit"] = limit
        if group_id is not None:
            _path_params["groupId"] = group_id
        if role_id is not None:
            _path_params["roleId"] = role_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_role_targets_catalog_apps_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_group_id,
            request_path_role_id,
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
            request_query_after,
            request_query_limit,
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
            path_template='/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps',
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


    def _get_role_targets_catalog_apps_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_group_id,
            request_path_role_id,
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
            request_query_after,
            request_query_limit,
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
            path_template='/api/v1/groups/{groupId}/roles/{roleId}/targets/catalog/apps',
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


class GetRoleTargetsCatalogAppsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_role_targets_catalog_apps(
        self,
        group_id: str,
        role_id: str,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_role_targets_catalog_apps_mapped_args(
            group_id=group_id,
            role_id=role_id,
            after=after,
            limit=limit,
        )
        return await self._aget_role_targets_catalog_apps_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_role_targets_catalog_apps(
        self,
        group_id: str,
        role_id: str,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_role_targets_catalog_apps_mapped_args(
            group_id=group_id,
            role_id=role_id,
            after=after,
            limit=limit,
        )
        return self._get_role_targets_catalog_apps_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetRoleTargetsCatalogApps(BaseApi):

    async def aget_role_targets_catalog_apps(
        self,
        group_id: str,
        role_id: str,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> GroupGetRoleTargetsCatalogAppsResponsePydantic:
        raw_response = await self.raw.aget_role_targets_catalog_apps(
            group_id=group_id,
            role_id=role_id,
            after=after,
            limit=limit,
            **kwargs,
        )
        if validate:
            return RootModel[GroupGetRoleTargetsCatalogAppsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(GroupGetRoleTargetsCatalogAppsResponsePydantic, raw_response.body)
    
    
    def get_role_targets_catalog_apps(
        self,
        group_id: str,
        role_id: str,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> GroupGetRoleTargetsCatalogAppsResponsePydantic:
        raw_response = self.raw.get_role_targets_catalog_apps(
            group_id=group_id,
            role_id=role_id,
            after=after,
            limit=limit,
        )
        if validate:
            return RootModel[GroupGetRoleTargetsCatalogAppsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(GroupGetRoleTargetsCatalogAppsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        group_id: str,
        role_id: str,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_role_targets_catalog_apps_mapped_args(
            group_id=group_id,
            role_id=role_id,
            after=after,
            limit=limit,
        )
        return await self._aget_role_targets_catalog_apps_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        group_id: str,
        role_id: str,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_role_targets_catalog_apps_mapped_args(
            group_id=group_id,
            role_id=role_id,
            after=after,
            limit=limit,
        )
        return self._get_role_targets_catalog_apps_oapg(
            query_params=args.query,
            path_params=args.path,
        )


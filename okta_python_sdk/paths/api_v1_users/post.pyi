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

from okta_python_sdk.model.user_profile import UserProfile as UserProfileSchema
from okta_python_sdk.model.user import User as UserSchema
from okta_python_sdk.model.user_credentials import UserCredentials as UserCredentialsSchema
from okta_python_sdk.model.create_user_request_group_ids import CreateUserRequestGroupIds as CreateUserRequestGroupIdsSchema
from okta_python_sdk.model.create_user_request import CreateUserRequest as CreateUserRequestSchema
from okta_python_sdk.model.user_type import UserType as UserTypeSchema

from okta_python_sdk.type.user_type import UserType
from okta_python_sdk.type.user_profile import UserProfile
from okta_python_sdk.type.user_credentials import UserCredentials
from okta_python_sdk.type.create_user_request_group_ids import CreateUserRequestGroupIds
from okta_python_sdk.type.create_user_request import CreateUserRequest
from okta_python_sdk.type.user import User

from ...api_client import Dictionary
from okta_python_sdk.pydantic.user_type import UserType as UserTypePydantic
from okta_python_sdk.pydantic.create_user_request_group_ids import CreateUserRequestGroupIds as CreateUserRequestGroupIdsPydantic
from okta_python_sdk.pydantic.user import User as UserPydantic
from okta_python_sdk.pydantic.user_credentials import UserCredentials as UserCredentialsPydantic
from okta_python_sdk.pydantic.user_profile import UserProfile as UserProfilePydantic
from okta_python_sdk.pydantic.create_user_request import CreateUserRequest as CreateUserRequestPydantic

# Query params
ActivateSchema = schemas.BoolSchema
ProviderSchema = schemas.BoolSchema
NextLoginSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'activate': typing.Union[ActivateSchema, bool, ],
        'provider': typing.Union[ProviderSchema, bool, ],
        'nextLogin': typing.Union[NextLoginSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_activate = api_client.QueryParameter(
    name="activate",
    style=api_client.ParameterStyle.FORM,
    schema=ActivateSchema,
    explode=True,
)
request_query_provider = api_client.QueryParameter(
    name="provider",
    style=api_client.ParameterStyle.FORM,
    schema=ProviderSchema,
    explode=True,
)
request_query_next_login = api_client.QueryParameter(
    name="nextLogin",
    style=api_client.ParameterStyle.FORM,
    schema=NextLoginSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = CreateUserRequestSchema


request_body_create_user_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = UserSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: User


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: User


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

    def _create_new_user_mapped_args(
        self,
        credentials: typing.Optional[UserCredentials] = None,
        group_ids: typing.Optional[CreateUserRequestGroupIds] = None,
        profile: typing.Optional[UserProfile] = None,
        type: typing.Optional[UserType] = None,
        activate: typing.Optional[bool] = None,
        provider: typing.Optional[bool] = None,
        next_login: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if credentials is not None:
            _body["credentials"] = credentials
        if group_ids is not None:
            _body["groupIds"] = group_ids
        if profile is not None:
            _body["profile"] = profile
        if type is not None:
            _body["type"] = type
        args.body = _body
        if activate is not None:
            _query_params["activate"] = activate
        if provider is not None:
            _query_params["provider"] = provider
        if next_login is not None:
            _query_params["nextLogin"] = next_login
        args.query = _query_params
        return args

    async def _acreate_new_user_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create User
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_activate,
            request_query_provider,
            request_query_next_login,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_user_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _create_new_user_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create User
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_activate,
            request_query_provider,
            request_query_next_login,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/users',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_user_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class CreateNewUserRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_user(
        self,
        credentials: typing.Optional[UserCredentials] = None,
        group_ids: typing.Optional[CreateUserRequestGroupIds] = None,
        profile: typing.Optional[UserProfile] = None,
        type: typing.Optional[UserType] = None,
        activate: typing.Optional[bool] = None,
        provider: typing.Optional[bool] = None,
        next_login: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_user_mapped_args(
            credentials=credentials,
            group_ids=group_ids,
            profile=profile,
            type=type,
            activate=activate,
            provider=provider,
            next_login=next_login,
        )
        return await self._acreate_new_user_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def create_new_user(
        self,
        credentials: typing.Optional[UserCredentials] = None,
        group_ids: typing.Optional[CreateUserRequestGroupIds] = None,
        profile: typing.Optional[UserProfile] = None,
        type: typing.Optional[UserType] = None,
        activate: typing.Optional[bool] = None,
        provider: typing.Optional[bool] = None,
        next_login: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_user_mapped_args(
            credentials=credentials,
            group_ids=group_ids,
            profile=profile,
            type=type,
            activate=activate,
            provider=provider,
            next_login=next_login,
        )
        return self._create_new_user_oapg(
            body=args.body,
            query_params=args.query,
        )

class CreateNewUser(BaseApi):

    async def acreate_new_user(
        self,
        credentials: typing.Optional[UserCredentials] = None,
        group_ids: typing.Optional[CreateUserRequestGroupIds] = None,
        profile: typing.Optional[UserProfile] = None,
        type: typing.Optional[UserType] = None,
        activate: typing.Optional[bool] = None,
        provider: typing.Optional[bool] = None,
        next_login: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserPydantic:
        raw_response = await self.raw.acreate_new_user(
            credentials=credentials,
            group_ids=group_ids,
            profile=profile,
            type=type,
            activate=activate,
            provider=provider,
            next_login=next_login,
            **kwargs,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)
    
    
    def create_new_user(
        self,
        credentials: typing.Optional[UserCredentials] = None,
        group_ids: typing.Optional[CreateUserRequestGroupIds] = None,
        profile: typing.Optional[UserProfile] = None,
        type: typing.Optional[UserType] = None,
        activate: typing.Optional[bool] = None,
        provider: typing.Optional[bool] = None,
        next_login: typing.Optional[str] = None,
        validate: bool = False,
    ) -> UserPydantic:
        raw_response = self.raw.create_new_user(
            credentials=credentials,
            group_ids=group_ids,
            profile=profile,
            type=type,
            activate=activate,
            provider=provider,
            next_login=next_login,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        credentials: typing.Optional[UserCredentials] = None,
        group_ids: typing.Optional[CreateUserRequestGroupIds] = None,
        profile: typing.Optional[UserProfile] = None,
        type: typing.Optional[UserType] = None,
        activate: typing.Optional[bool] = None,
        provider: typing.Optional[bool] = None,
        next_login: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_user_mapped_args(
            credentials=credentials,
            group_ids=group_ids,
            profile=profile,
            type=type,
            activate=activate,
            provider=provider,
            next_login=next_login,
        )
        return await self._acreate_new_user_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        credentials: typing.Optional[UserCredentials] = None,
        group_ids: typing.Optional[CreateUserRequestGroupIds] = None,
        profile: typing.Optional[UserProfile] = None,
        type: typing.Optional[UserType] = None,
        activate: typing.Optional[bool] = None,
        provider: typing.Optional[bool] = None,
        next_login: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_user_mapped_args(
            credentials=credentials,
            group_ids=group_ids,
            profile=profile,
            type=type,
            activate=activate,
            provider=provider,
            next_login=next_login,
        )
        return self._create_new_user_oapg(
            body=args.body,
            query_params=args.query,
        )


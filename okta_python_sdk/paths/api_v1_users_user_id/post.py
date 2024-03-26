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
from okta_python_sdk.model.user_links import UserLinks as UserLinksSchema
from okta_python_sdk.model.user import User as UserSchema
from okta_python_sdk.model.user_credentials import UserCredentials as UserCredentialsSchema
from okta_python_sdk.model.user_embedded import UserEmbedded as UserEmbeddedSchema
from okta_python_sdk.model.user_status import UserStatus as UserStatusSchema
from okta_python_sdk.model.user_type import UserType as UserTypeSchema

from okta_python_sdk.type.user_status import UserStatus
from okta_python_sdk.type.user_type import UserType
from okta_python_sdk.type.user_embedded import UserEmbedded
from okta_python_sdk.type.user_profile import UserProfile
from okta_python_sdk.type.user_credentials import UserCredentials
from okta_python_sdk.type.user_links import UserLinks
from okta_python_sdk.type.user import User

from ...api_client import Dictionary
from okta_python_sdk.pydantic.user_type import UserType as UserTypePydantic
from okta_python_sdk.pydantic.user import User as UserPydantic
from okta_python_sdk.pydantic.user_credentials import UserCredentials as UserCredentialsPydantic
from okta_python_sdk.pydantic.user_embedded import UserEmbedded as UserEmbeddedPydantic
from okta_python_sdk.pydantic.user_status import UserStatus as UserStatusPydantic
from okta_python_sdk.pydantic.user_links import UserLinks as UserLinksPydantic
from okta_python_sdk.pydantic.user_profile import UserProfile as UserProfilePydantic

from . import path

# Query params
StrictSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'strict': typing.Union[StrictSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_strict = api_client.QueryParameter(
    name="strict",
    style=api_client.ParameterStyle.FORM,
    schema=StrictSchema,
    explode=True,
)
# Path params
UserIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'userId': typing.Union[UserIdSchema, str, ],
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


request_path_user_id = api_client.PathParameter(
    name="userId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UserSchema


request_body_user = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_token',
]
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
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_profile_0_mapped_args(
        self,
        user_id: str,
        embedded: typing.Optional[UserEmbedded] = None,
        links: typing.Optional[UserLinks] = None,
        activated: typing.Optional[datetime] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[UserCredentials] = None,
        id: typing.Optional[str] = None,
        last_login: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        password_changed: typing.Optional[datetime] = None,
        profile: typing.Optional[UserProfile] = None,
        status: typing.Optional[UserStatus] = None,
        status_changed: typing.Optional[datetime] = None,
        transitioning_to_status: typing.Optional[UserStatus] = None,
        type: typing.Optional[UserType] = None,
        strict: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if embedded is not None:
            _body["_embedded"] = embedded
        if links is not None:
            _body["_links"] = links
        if activated is not None:
            _body["activated"] = activated
        if created is not None:
            _body["created"] = created
        if credentials is not None:
            _body["credentials"] = credentials
        if id is not None:
            _body["id"] = id
        if last_login is not None:
            _body["lastLogin"] = last_login
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if password_changed is not None:
            _body["passwordChanged"] = password_changed
        if profile is not None:
            _body["profile"] = profile
        if status is not None:
            _body["status"] = status
        if status_changed is not None:
            _body["statusChanged"] = status_changed
        if transitioning_to_status is not None:
            _body["transitioningToStatus"] = transitioning_to_status
        if type is not None:
            _body["type"] = type
        args.body = _body
        if strict is not None:
            _query_params["strict"] = strict
        if user_id is not None:
            _path_params["userId"] = user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_profile_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
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
            request_query_strict,
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
            path_template='/api/v1/users/{userId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_user.serialize(body, content_type)
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


    def _update_profile_0_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
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
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
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
            request_query_strict,
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
            path_template='/api/v1/users/{userId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_user.serialize(body, content_type)
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


class UpdateProfile0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_profile_0(
        self,
        user_id: str,
        embedded: typing.Optional[UserEmbedded] = None,
        links: typing.Optional[UserLinks] = None,
        activated: typing.Optional[datetime] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[UserCredentials] = None,
        id: typing.Optional[str] = None,
        last_login: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        password_changed: typing.Optional[datetime] = None,
        profile: typing.Optional[UserProfile] = None,
        status: typing.Optional[UserStatus] = None,
        status_changed: typing.Optional[datetime] = None,
        transitioning_to_status: typing.Optional[UserStatus] = None,
        type: typing.Optional[UserType] = None,
        strict: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_profile_0_mapped_args(
            user_id=user_id,
            embedded=embedded,
            links=links,
            activated=activated,
            created=created,
            credentials=credentials,
            id=id,
            last_login=last_login,
            last_updated=last_updated,
            password_changed=password_changed,
            profile=profile,
            status=status,
            status_changed=status_changed,
            transitioning_to_status=transitioning_to_status,
            type=type,
            strict=strict,
        )
        return await self._aupdate_profile_0_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_profile_0(
        self,
        user_id: str,
        embedded: typing.Optional[UserEmbedded] = None,
        links: typing.Optional[UserLinks] = None,
        activated: typing.Optional[datetime] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[UserCredentials] = None,
        id: typing.Optional[str] = None,
        last_login: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        password_changed: typing.Optional[datetime] = None,
        profile: typing.Optional[UserProfile] = None,
        status: typing.Optional[UserStatus] = None,
        status_changed: typing.Optional[datetime] = None,
        transitioning_to_status: typing.Optional[UserStatus] = None,
        type: typing.Optional[UserType] = None,
        strict: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_profile_0_mapped_args(
            user_id=user_id,
            embedded=embedded,
            links=links,
            activated=activated,
            created=created,
            credentials=credentials,
            id=id,
            last_login=last_login,
            last_updated=last_updated,
            password_changed=password_changed,
            profile=profile,
            status=status,
            status_changed=status_changed,
            transitioning_to_status=transitioning_to_status,
            type=type,
            strict=strict,
        )
        return self._update_profile_0_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateProfile0(BaseApi):

    async def aupdate_profile_0(
        self,
        user_id: str,
        embedded: typing.Optional[UserEmbedded] = None,
        links: typing.Optional[UserLinks] = None,
        activated: typing.Optional[datetime] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[UserCredentials] = None,
        id: typing.Optional[str] = None,
        last_login: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        password_changed: typing.Optional[datetime] = None,
        profile: typing.Optional[UserProfile] = None,
        status: typing.Optional[UserStatus] = None,
        status_changed: typing.Optional[datetime] = None,
        transitioning_to_status: typing.Optional[UserStatus] = None,
        type: typing.Optional[UserType] = None,
        strict: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> UserPydantic:
        raw_response = await self.raw.aupdate_profile_0(
            user_id=user_id,
            embedded=embedded,
            links=links,
            activated=activated,
            created=created,
            credentials=credentials,
            id=id,
            last_login=last_login,
            last_updated=last_updated,
            password_changed=password_changed,
            profile=profile,
            status=status,
            status_changed=status_changed,
            transitioning_to_status=transitioning_to_status,
            type=type,
            strict=strict,
            **kwargs,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)
    
    
    def update_profile_0(
        self,
        user_id: str,
        embedded: typing.Optional[UserEmbedded] = None,
        links: typing.Optional[UserLinks] = None,
        activated: typing.Optional[datetime] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[UserCredentials] = None,
        id: typing.Optional[str] = None,
        last_login: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        password_changed: typing.Optional[datetime] = None,
        profile: typing.Optional[UserProfile] = None,
        status: typing.Optional[UserStatus] = None,
        status_changed: typing.Optional[datetime] = None,
        transitioning_to_status: typing.Optional[UserStatus] = None,
        type: typing.Optional[UserType] = None,
        strict: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> UserPydantic:
        raw_response = self.raw.update_profile_0(
            user_id=user_id,
            embedded=embedded,
            links=links,
            activated=activated,
            created=created,
            credentials=credentials,
            id=id,
            last_login=last_login,
            last_updated=last_updated,
            password_changed=password_changed,
            profile=profile,
            status=status,
            status_changed=status_changed,
            transitioning_to_status=transitioning_to_status,
            type=type,
            strict=strict,
        )
        if validate:
            return UserPydantic(**raw_response.body)
        return api_client.construct_model_instance(UserPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        user_id: str,
        embedded: typing.Optional[UserEmbedded] = None,
        links: typing.Optional[UserLinks] = None,
        activated: typing.Optional[datetime] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[UserCredentials] = None,
        id: typing.Optional[str] = None,
        last_login: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        password_changed: typing.Optional[datetime] = None,
        profile: typing.Optional[UserProfile] = None,
        status: typing.Optional[UserStatus] = None,
        status_changed: typing.Optional[datetime] = None,
        transitioning_to_status: typing.Optional[UserStatus] = None,
        type: typing.Optional[UserType] = None,
        strict: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_profile_0_mapped_args(
            user_id=user_id,
            embedded=embedded,
            links=links,
            activated=activated,
            created=created,
            credentials=credentials,
            id=id,
            last_login=last_login,
            last_updated=last_updated,
            password_changed=password_changed,
            profile=profile,
            status=status,
            status_changed=status_changed,
            transitioning_to_status=transitioning_to_status,
            type=type,
            strict=strict,
        )
        return await self._aupdate_profile_0_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        user_id: str,
        embedded: typing.Optional[UserEmbedded] = None,
        links: typing.Optional[UserLinks] = None,
        activated: typing.Optional[datetime] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[UserCredentials] = None,
        id: typing.Optional[str] = None,
        last_login: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        password_changed: typing.Optional[datetime] = None,
        profile: typing.Optional[UserProfile] = None,
        status: typing.Optional[UserStatus] = None,
        status_changed: typing.Optional[datetime] = None,
        transitioning_to_status: typing.Optional[UserStatus] = None,
        type: typing.Optional[UserType] = None,
        strict: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_profile_0_mapped_args(
            user_id=user_id,
            embedded=embedded,
            links=links,
            activated=activated,
            created=created,
            credentials=credentials,
            id=id,
            last_login=last_login,
            last_updated=last_updated,
            password_changed=password_changed,
            profile=profile,
            status=status,
            status_changed=status_changed,
            transitioning_to_status=transitioning_to_status,
            type=type,
            strict=strict,
        )
        return self._update_profile_0_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )


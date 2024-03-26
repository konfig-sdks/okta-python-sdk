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

from okta_python_sdk.model.authenticator_provider import AuthenticatorProvider as AuthenticatorProviderSchema
from okta_python_sdk.model.authenticator_links import AuthenticatorLinks as AuthenticatorLinksSchema
from okta_python_sdk.model.authenticator_status import AuthenticatorStatus as AuthenticatorStatusSchema
from okta_python_sdk.model.authenticator import Authenticator as AuthenticatorSchema
from okta_python_sdk.model.authenticator_settings import AuthenticatorSettings as AuthenticatorSettingsSchema
from okta_python_sdk.model.authenticator_type import AuthenticatorType as AuthenticatorTypeSchema

from okta_python_sdk.type.authenticator_type import AuthenticatorType
from okta_python_sdk.type.authenticator import Authenticator
from okta_python_sdk.type.authenticator_provider import AuthenticatorProvider
from okta_python_sdk.type.authenticator_links import AuthenticatorLinks
from okta_python_sdk.type.authenticator_settings import AuthenticatorSettings
from okta_python_sdk.type.authenticator_status import AuthenticatorStatus

from ...api_client import Dictionary
from okta_python_sdk.pydantic.authenticator_type import AuthenticatorType as AuthenticatorTypePydantic
from okta_python_sdk.pydantic.authenticator_provider import AuthenticatorProvider as AuthenticatorProviderPydantic
from okta_python_sdk.pydantic.authenticator_links import AuthenticatorLinks as AuthenticatorLinksPydantic
from okta_python_sdk.pydantic.authenticator import Authenticator as AuthenticatorPydantic
from okta_python_sdk.pydantic.authenticator_settings import AuthenticatorSettings as AuthenticatorSettingsPydantic
from okta_python_sdk.pydantic.authenticator_status import AuthenticatorStatus as AuthenticatorStatusPydantic

from . import path

# Path params
AuthenticatorIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'authenticatorId': typing.Union[AuthenticatorIdSchema, str, ],
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


request_path_authenticator_id = api_client.PathParameter(
    name="authenticatorId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthenticatorIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = AuthenticatorSchema


request_body_authenticator = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_token',
]
SchemaFor200ResponseBodyApplicationJson = AuthenticatorSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Authenticator


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Authenticator


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

    def _update_authenticator_mapped_args(
        self,
        authenticator_id: str,
        links: typing.Optional[AuthenticatorLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[AuthenticatorProvider] = None,
        settings: typing.Optional[AuthenticatorSettings] = None,
        status: typing.Optional[AuthenticatorStatus] = None,
        type: typing.Optional[AuthenticatorType] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if links is not None:
            _body["_links"] = links
        if created is not None:
            _body["created"] = created
        if id is not None:
            _body["id"] = id
        if key is not None:
            _body["key"] = key
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if name is not None:
            _body["name"] = name
        if provider is not None:
            _body["provider"] = provider
        if settings is not None:
            _body["settings"] = settings
        if status is not None:
            _body["status"] = status
        if type is not None:
            _body["type"] = type
        args.body = _body
        if authenticator_id is not None:
            _path_params["authenticatorId"] = authenticator_id
        args.path = _path_params
        return args

    async def _aupdate_authenticator_oapg(
        self,
        body: typing.Any = None,
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
        Update Authenticator
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_authenticator_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/api/v1/authenticators/{authenticatorId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_authenticator.serialize(body, content_type)
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


    def _update_authenticator_oapg(
        self,
        body: typing.Any = None,
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
        Update Authenticator
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_authenticator_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
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
            path_template='/api/v1/authenticators/{authenticatorId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_authenticator.serialize(body, content_type)
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


class UpdateAuthenticatorRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_authenticator(
        self,
        authenticator_id: str,
        links: typing.Optional[AuthenticatorLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[AuthenticatorProvider] = None,
        settings: typing.Optional[AuthenticatorSettings] = None,
        status: typing.Optional[AuthenticatorStatus] = None,
        type: typing.Optional[AuthenticatorType] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_authenticator_mapped_args(
            authenticator_id=authenticator_id,
            links=links,
            created=created,
            id=id,
            key=key,
            last_updated=last_updated,
            name=name,
            provider=provider,
            settings=settings,
            status=status,
            type=type,
        )
        return await self._aupdate_authenticator_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_authenticator(
        self,
        authenticator_id: str,
        links: typing.Optional[AuthenticatorLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[AuthenticatorProvider] = None,
        settings: typing.Optional[AuthenticatorSettings] = None,
        status: typing.Optional[AuthenticatorStatus] = None,
        type: typing.Optional[AuthenticatorType] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_authenticator_mapped_args(
            authenticator_id=authenticator_id,
            links=links,
            created=created,
            id=id,
            key=key,
            last_updated=last_updated,
            name=name,
            provider=provider,
            settings=settings,
            status=status,
            type=type,
        )
        return self._update_authenticator_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateAuthenticator(BaseApi):

    async def aupdate_authenticator(
        self,
        authenticator_id: str,
        links: typing.Optional[AuthenticatorLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[AuthenticatorProvider] = None,
        settings: typing.Optional[AuthenticatorSettings] = None,
        status: typing.Optional[AuthenticatorStatus] = None,
        type: typing.Optional[AuthenticatorType] = None,
        validate: bool = False,
        **kwargs,
    ) -> AuthenticatorPydantic:
        raw_response = await self.raw.aupdate_authenticator(
            authenticator_id=authenticator_id,
            links=links,
            created=created,
            id=id,
            key=key,
            last_updated=last_updated,
            name=name,
            provider=provider,
            settings=settings,
            status=status,
            type=type,
            **kwargs,
        )
        if validate:
            return AuthenticatorPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthenticatorPydantic, raw_response.body)
    
    
    def update_authenticator(
        self,
        authenticator_id: str,
        links: typing.Optional[AuthenticatorLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[AuthenticatorProvider] = None,
        settings: typing.Optional[AuthenticatorSettings] = None,
        status: typing.Optional[AuthenticatorStatus] = None,
        type: typing.Optional[AuthenticatorType] = None,
        validate: bool = False,
    ) -> AuthenticatorPydantic:
        raw_response = self.raw.update_authenticator(
            authenticator_id=authenticator_id,
            links=links,
            created=created,
            id=id,
            key=key,
            last_updated=last_updated,
            name=name,
            provider=provider,
            settings=settings,
            status=status,
            type=type,
        )
        if validate:
            return AuthenticatorPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthenticatorPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        authenticator_id: str,
        links: typing.Optional[AuthenticatorLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[AuthenticatorProvider] = None,
        settings: typing.Optional[AuthenticatorSettings] = None,
        status: typing.Optional[AuthenticatorStatus] = None,
        type: typing.Optional[AuthenticatorType] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_authenticator_mapped_args(
            authenticator_id=authenticator_id,
            links=links,
            created=created,
            id=id,
            key=key,
            last_updated=last_updated,
            name=name,
            provider=provider,
            settings=settings,
            status=status,
            type=type,
        )
        return await self._aupdate_authenticator_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        authenticator_id: str,
        links: typing.Optional[AuthenticatorLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[AuthenticatorProvider] = None,
        settings: typing.Optional[AuthenticatorSettings] = None,
        status: typing.Optional[AuthenticatorStatus] = None,
        type: typing.Optional[AuthenticatorType] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_authenticator_mapped_args(
            authenticator_id=authenticator_id,
            links=links,
            created=created,
            id=id,
            key=key,
            last_updated=last_updated,
            name=name,
            provider=provider,
            settings=settings,
            status=status,
            type=type,
        )
        return self._update_authenticator_oapg(
            body=args.body,
            path_params=args.path,
        )


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

from okta_python_sdk.model.capabilities_update_object import CapabilitiesUpdateObject as CapabilitiesUpdateObjectSchema
from okta_python_sdk.model.capabilities_create_object import CapabilitiesCreateObject as CapabilitiesCreateObjectSchema
from okta_python_sdk.model.capabilities_object import CapabilitiesObject as CapabilitiesObjectSchema
from okta_python_sdk.model.application_feature import ApplicationFeature as ApplicationFeatureSchema

from okta_python_sdk.type.capabilities_object import CapabilitiesObject
from okta_python_sdk.type.capabilities_update_object import CapabilitiesUpdateObject
from okta_python_sdk.type.capabilities_create_object import CapabilitiesCreateObject
from okta_python_sdk.type.application_feature import ApplicationFeature

from ...api_client import Dictionary
from okta_python_sdk.pydantic.application_feature import ApplicationFeature as ApplicationFeaturePydantic
from okta_python_sdk.pydantic.capabilities_create_object import CapabilitiesCreateObject as CapabilitiesCreateObjectPydantic
from okta_python_sdk.pydantic.capabilities_update_object import CapabilitiesUpdateObject as CapabilitiesUpdateObjectPydantic
from okta_python_sdk.pydantic.capabilities_object import CapabilitiesObject as CapabilitiesObjectPydantic

# Path params
AppIdSchema = schemas.StrSchema
NameSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'appId': typing.Union[AppIdSchema, str, ],
        'name': typing.Union[NameSchema, str, ],
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


request_path_app_id = api_client.PathParameter(
    name="appId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AppIdSchema,
    required=True,
)
request_path_name = api_client.PathParameter(
    name="name",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NameSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CapabilitiesObjectSchema


request_body_capabilities_object = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ApplicationFeatureSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ApplicationFeature


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ApplicationFeature


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_feature_mapped_args(
        self,
        app_id: str,
        name: str,
        create: typing.Optional[CapabilitiesCreateObject] = None,
        update: typing.Optional[CapabilitiesUpdateObject] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if create is not None:
            _body["create"] = create
        if update is not None:
            _body["update"] = update
        args.body = _body
        if app_id is not None:
            _path_params["appId"] = app_id
        if name is not None:
            _path_params["name"] = name
        args.path = _path_params
        return args

    async def _aupdate_feature_oapg(
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
        Updates a Feature object for an application.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
            request_path_name,
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
            path_template='/api/v1/apps/{appId}/features/{name}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_capabilities_object.serialize(body, content_type)
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


    def _update_feature_oapg(
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
        Updates a Feature object for an application.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_app_id,
            request_path_name,
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
            path_template='/api/v1/apps/{appId}/features/{name}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_capabilities_object.serialize(body, content_type)
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


class UpdateFeatureRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_feature(
        self,
        app_id: str,
        name: str,
        create: typing.Optional[CapabilitiesCreateObject] = None,
        update: typing.Optional[CapabilitiesUpdateObject] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_feature_mapped_args(
            app_id=app_id,
            name=name,
            create=create,
            update=update,
        )
        return await self._aupdate_feature_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_feature(
        self,
        app_id: str,
        name: str,
        create: typing.Optional[CapabilitiesCreateObject] = None,
        update: typing.Optional[CapabilitiesUpdateObject] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_feature_mapped_args(
            app_id=app_id,
            name=name,
            create=create,
            update=update,
        )
        return self._update_feature_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateFeature(BaseApi):

    async def aupdate_feature(
        self,
        app_id: str,
        name: str,
        create: typing.Optional[CapabilitiesCreateObject] = None,
        update: typing.Optional[CapabilitiesUpdateObject] = None,
        validate: bool = False,
        **kwargs,
    ) -> ApplicationFeaturePydantic:
        raw_response = await self.raw.aupdate_feature(
            app_id=app_id,
            name=name,
            create=create,
            update=update,
            **kwargs,
        )
        if validate:
            return ApplicationFeaturePydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationFeaturePydantic, raw_response.body)
    
    
    def update_feature(
        self,
        app_id: str,
        name: str,
        create: typing.Optional[CapabilitiesCreateObject] = None,
        update: typing.Optional[CapabilitiesUpdateObject] = None,
        validate: bool = False,
    ) -> ApplicationFeaturePydantic:
        raw_response = self.raw.update_feature(
            app_id=app_id,
            name=name,
            create=create,
            update=update,
        )
        if validate:
            return ApplicationFeaturePydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationFeaturePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        app_id: str,
        name: str,
        create: typing.Optional[CapabilitiesCreateObject] = None,
        update: typing.Optional[CapabilitiesUpdateObject] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_feature_mapped_args(
            app_id=app_id,
            name=name,
            create=create,
            update=update,
        )
        return await self._aupdate_feature_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        app_id: str,
        name: str,
        create: typing.Optional[CapabilitiesCreateObject] = None,
        update: typing.Optional[CapabilitiesUpdateObject] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_feature_mapped_args(
            app_id=app_id,
            name=name,
            create=create,
            update=update,
        )
        return self._update_feature_oapg(
            body=args.body,
            path_params=args.path,
        )


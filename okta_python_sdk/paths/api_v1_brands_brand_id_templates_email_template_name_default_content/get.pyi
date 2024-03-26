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

from okta_python_sdk.model.email_template_content import EmailTemplateContent as EmailTemplateContentSchema

from okta_python_sdk.type.email_template_content import EmailTemplateContent

from ...api_client import Dictionary
from okta_python_sdk.pydantic.email_template_content import EmailTemplateContent as EmailTemplateContentPydantic

# Path params
BrandIdSchema = schemas.StrSchema
TemplateNameSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'brandId': typing.Union[BrandIdSchema, str, ],
        'templateName': typing.Union[TemplateNameSchema, str, ],
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


request_path_brand_id = api_client.PathParameter(
    name="brandId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=BrandIdSchema,
    required=True,
)
request_path_template_name = api_client.PathParameter(
    name="templateName",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TemplateNameSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = EmailTemplateContentSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: EmailTemplateContent


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: EmailTemplateContent


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

    def _get_email_template_default_content_mapped_args(
        self,
        brand_id: str,
        template_name: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if brand_id is not None:
            _path_params["brandId"] = brand_id
        if template_name is not None:
            _path_params["templateName"] = template_name
        args.path = _path_params
        return args

    async def _aget_email_template_default_content_oapg(
        self,
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
        Get Default Content of Email Template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_brand_id,
            request_path_template_name,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/brands/{brandId}/templates/email/{templateName}/default-content',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_email_template_default_content_oapg(
        self,
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
        Get Default Content of Email Template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_brand_id,
            request_path_template_name,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/brands/{brandId}/templates/email/{templateName}/default-content',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetEmailTemplateDefaultContentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_email_template_default_content(
        self,
        brand_id: str,
        template_name: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_email_template_default_content_mapped_args(
            brand_id=brand_id,
            template_name=template_name,
        )
        return await self._aget_email_template_default_content_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_email_template_default_content(
        self,
        brand_id: str,
        template_name: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_email_template_default_content_mapped_args(
            brand_id=brand_id,
            template_name=template_name,
        )
        return self._get_email_template_default_content_oapg(
            path_params=args.path,
        )

class GetEmailTemplateDefaultContent(BaseApi):

    async def aget_email_template_default_content(
        self,
        brand_id: str,
        template_name: str,
        validate: bool = False,
        **kwargs,
    ) -> EmailTemplateContentPydantic:
        raw_response = await self.raw.aget_email_template_default_content(
            brand_id=brand_id,
            template_name=template_name,
            **kwargs,
        )
        if validate:
            return EmailTemplateContentPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmailTemplateContentPydantic, raw_response.body)
    
    
    def get_email_template_default_content(
        self,
        brand_id: str,
        template_name: str,
        validate: bool = False,
    ) -> EmailTemplateContentPydantic:
        raw_response = self.raw.get_email_template_default_content(
            brand_id=brand_id,
            template_name=template_name,
        )
        if validate:
            return EmailTemplateContentPydantic(**raw_response.body)
        return api_client.construct_model_instance(EmailTemplateContentPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        brand_id: str,
        template_name: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_email_template_default_content_mapped_args(
            brand_id=brand_id,
            template_name=template_name,
        )
        return await self._aget_email_template_default_content_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        brand_id: str,
        template_name: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_email_template_default_content_mapped_args(
            brand_id=brand_id,
            template_name=template_name,
        )
        return self._get_email_template_default_content_oapg(
            path_params=args.path,
        )


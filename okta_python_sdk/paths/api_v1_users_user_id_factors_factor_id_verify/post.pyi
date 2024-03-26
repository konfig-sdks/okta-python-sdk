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

from okta_python_sdk.model.verify_user_factor_response import VerifyUserFactorResponse as VerifyUserFactorResponseSchema
from okta_python_sdk.model.verify_factor_request import VerifyFactorRequest as VerifyFactorRequestSchema

from okta_python_sdk.type.verify_user_factor_response import VerifyUserFactorResponse
from okta_python_sdk.type.verify_factor_request import VerifyFactorRequest

from ...api_client import Dictionary
from okta_python_sdk.pydantic.verify_factor_request import VerifyFactorRequest as VerifyFactorRequestPydantic
from okta_python_sdk.pydantic.verify_user_factor_response import VerifyUserFactorResponse as VerifyUserFactorResponsePydantic

# Query params
TemplateIdSchema = schemas.StrSchema
TokenLifetimeSecondsSchema = schemas.Int32Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'templateId': typing.Union[TemplateIdSchema, str, ],
        'tokenLifetimeSeconds': typing.Union[TokenLifetimeSecondsSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_template_id = api_client.QueryParameter(
    name="templateId",
    style=api_client.ParameterStyle.FORM,
    schema=TemplateIdSchema,
    explode=True,
)
request_query_token_lifetime_seconds = api_client.QueryParameter(
    name="tokenLifetimeSeconds",
    style=api_client.ParameterStyle.FORM,
    schema=TokenLifetimeSecondsSchema,
    explode=True,
)
# Header params
XForwardedForSchema = schemas.StrSchema
UserAgentSchema = schemas.StrSchema
AcceptLanguageSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Forwarded-For': typing.Union[XForwardedForSchema, str, ],
        'User-Agent': typing.Union[UserAgentSchema, str, ],
        'Accept-Language': typing.Union[AcceptLanguageSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_forwarded_for = api_client.HeaderParameter(
    name="X-Forwarded-For",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XForwardedForSchema,
)
request_header_user_agent = api_client.HeaderParameter(
    name="User-Agent",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserAgentSchema,
)
request_header_accept_language = api_client.HeaderParameter(
    name="Accept-Language",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AcceptLanguageSchema,
)
# Path params
UserIdSchema = schemas.StrSchema
FactorIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'userId': typing.Union[UserIdSchema, str, ],
        'factorId': typing.Union[FactorIdSchema, str, ],
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
request_path_factor_id = api_client.PathParameter(
    name="factorId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FactorIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = VerifyFactorRequestSchema


request_body_verify_factor_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = VerifyUserFactorResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: VerifyUserFactorResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: VerifyUserFactorResponse


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

    def _verify_otp_mapped_args(
        self,
        user_id: str,
        factor_id: str,
        activation_token: typing.Optional[str] = None,
        answer: typing.Optional[str] = None,
        attestation: typing.Optional[str] = None,
        client_data: typing.Optional[str] = None,
        next_pass_code: typing.Optional[str] = None,
        pass_code: typing.Optional[str] = None,
        registration_data: typing.Optional[str] = None,
        state_token: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        token_lifetime_seconds: typing.Optional[int] = None,
        x_forwarded_for: typing.Optional[str] = None,
        user_agent: typing.Optional[str] = None,
        accept_language: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        _body = {}
        if activation_token is not None:
            _body["activationToken"] = activation_token
        if answer is not None:
            _body["answer"] = answer
        if attestation is not None:
            _body["attestation"] = attestation
        if client_data is not None:
            _body["clientData"] = client_data
        if next_pass_code is not None:
            _body["nextPassCode"] = next_pass_code
        if pass_code is not None:
            _body["passCode"] = pass_code
        if registration_data is not None:
            _body["registrationData"] = registration_data
        if state_token is not None:
            _body["stateToken"] = state_token
        args.body = _body
        if template_id is not None:
            _query_params["templateId"] = template_id
        if token_lifetime_seconds is not None:
            _query_params["tokenLifetimeSeconds"] = token_lifetime_seconds
        if x_forwarded_for is not None:
            _header_params["X-Forwarded-For"] = x_forwarded_for
        if user_agent is not None:
            _header_params["User-Agent"] = user_agent
        if accept_language is not None:
            _header_params["Accept-Language"] = accept_language
        if user_id is not None:
            _path_params["userId"] = user_id
        if factor_id is not None:
            _path_params["factorId"] = factor_id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _averify_otp_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        Verify MFA Factor
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
            request_path_factor_id,
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
            request_query_template_id,
            request_query_token_lifetime_seconds,
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
        for parameter in (
            request_header_x_forwarded_for,
            request_header_user_agent,
            request_header_accept_language,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/users/{userId}/factors/{factorId}/verify',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_verify_factor_request.serialize(body, content_type)
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


    def _verify_otp_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        Verify MFA Factor
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
            request_path_factor_id,
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
            request_query_template_id,
            request_query_token_lifetime_seconds,
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
        for parameter in (
            request_header_x_forwarded_for,
            request_header_user_agent,
            request_header_accept_language,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/users/{userId}/factors/{factorId}/verify',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_verify_factor_request.serialize(body, content_type)
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


class VerifyOtpRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def averify_otp(
        self,
        user_id: str,
        factor_id: str,
        activation_token: typing.Optional[str] = None,
        answer: typing.Optional[str] = None,
        attestation: typing.Optional[str] = None,
        client_data: typing.Optional[str] = None,
        next_pass_code: typing.Optional[str] = None,
        pass_code: typing.Optional[str] = None,
        registration_data: typing.Optional[str] = None,
        state_token: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        token_lifetime_seconds: typing.Optional[int] = None,
        x_forwarded_for: typing.Optional[str] = None,
        user_agent: typing.Optional[str] = None,
        accept_language: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verify_otp_mapped_args(
            body=body,
            user_id=user_id,
            factor_id=factor_id,
            activation_token=activation_token,
            answer=answer,
            attestation=attestation,
            client_data=client_data,
            next_pass_code=next_pass_code,
            pass_code=pass_code,
            registration_data=registration_data,
            state_token=state_token,
            template_id=template_id,
            token_lifetime_seconds=token_lifetime_seconds,
            x_forwarded_for=x_forwarded_for,
            user_agent=user_agent,
            accept_language=accept_language,
        )
        return await self._averify_otp_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def verify_otp(
        self,
        user_id: str,
        factor_id: str,
        activation_token: typing.Optional[str] = None,
        answer: typing.Optional[str] = None,
        attestation: typing.Optional[str] = None,
        client_data: typing.Optional[str] = None,
        next_pass_code: typing.Optional[str] = None,
        pass_code: typing.Optional[str] = None,
        registration_data: typing.Optional[str] = None,
        state_token: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        token_lifetime_seconds: typing.Optional[int] = None,
        x_forwarded_for: typing.Optional[str] = None,
        user_agent: typing.Optional[str] = None,
        accept_language: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verify_otp_mapped_args(
            body=body,
            user_id=user_id,
            factor_id=factor_id,
            activation_token=activation_token,
            answer=answer,
            attestation=attestation,
            client_data=client_data,
            next_pass_code=next_pass_code,
            pass_code=pass_code,
            registration_data=registration_data,
            state_token=state_token,
            template_id=template_id,
            token_lifetime_seconds=token_lifetime_seconds,
            x_forwarded_for=x_forwarded_for,
            user_agent=user_agent,
            accept_language=accept_language,
        )
        return self._verify_otp_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class VerifyOtp(BaseApi):

    async def averify_otp(
        self,
        user_id: str,
        factor_id: str,
        activation_token: typing.Optional[str] = None,
        answer: typing.Optional[str] = None,
        attestation: typing.Optional[str] = None,
        client_data: typing.Optional[str] = None,
        next_pass_code: typing.Optional[str] = None,
        pass_code: typing.Optional[str] = None,
        registration_data: typing.Optional[str] = None,
        state_token: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        token_lifetime_seconds: typing.Optional[int] = None,
        x_forwarded_for: typing.Optional[str] = None,
        user_agent: typing.Optional[str] = None,
        accept_language: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> VerifyUserFactorResponsePydantic:
        raw_response = await self.raw.averify_otp(
            body=body,
            user_id=user_id,
            factor_id=factor_id,
            activation_token=activation_token,
            answer=answer,
            attestation=attestation,
            client_data=client_data,
            next_pass_code=next_pass_code,
            pass_code=pass_code,
            registration_data=registration_data,
            state_token=state_token,
            template_id=template_id,
            token_lifetime_seconds=token_lifetime_seconds,
            x_forwarded_for=x_forwarded_for,
            user_agent=user_agent,
            accept_language=accept_language,
            **kwargs,
        )
        if validate:
            return VerifyUserFactorResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VerifyUserFactorResponsePydantic, raw_response.body)
    
    
    def verify_otp(
        self,
        user_id: str,
        factor_id: str,
        activation_token: typing.Optional[str] = None,
        answer: typing.Optional[str] = None,
        attestation: typing.Optional[str] = None,
        client_data: typing.Optional[str] = None,
        next_pass_code: typing.Optional[str] = None,
        pass_code: typing.Optional[str] = None,
        registration_data: typing.Optional[str] = None,
        state_token: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        token_lifetime_seconds: typing.Optional[int] = None,
        x_forwarded_for: typing.Optional[str] = None,
        user_agent: typing.Optional[str] = None,
        accept_language: typing.Optional[str] = None,
        validate: bool = False,
    ) -> VerifyUserFactorResponsePydantic:
        raw_response = self.raw.verify_otp(
            body=body,
            user_id=user_id,
            factor_id=factor_id,
            activation_token=activation_token,
            answer=answer,
            attestation=attestation,
            client_data=client_data,
            next_pass_code=next_pass_code,
            pass_code=pass_code,
            registration_data=registration_data,
            state_token=state_token,
            template_id=template_id,
            token_lifetime_seconds=token_lifetime_seconds,
            x_forwarded_for=x_forwarded_for,
            user_agent=user_agent,
            accept_language=accept_language,
        )
        if validate:
            return VerifyUserFactorResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(VerifyUserFactorResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        user_id: str,
        factor_id: str,
        activation_token: typing.Optional[str] = None,
        answer: typing.Optional[str] = None,
        attestation: typing.Optional[str] = None,
        client_data: typing.Optional[str] = None,
        next_pass_code: typing.Optional[str] = None,
        pass_code: typing.Optional[str] = None,
        registration_data: typing.Optional[str] = None,
        state_token: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        token_lifetime_seconds: typing.Optional[int] = None,
        x_forwarded_for: typing.Optional[str] = None,
        user_agent: typing.Optional[str] = None,
        accept_language: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verify_otp_mapped_args(
            body=body,
            user_id=user_id,
            factor_id=factor_id,
            activation_token=activation_token,
            answer=answer,
            attestation=attestation,
            client_data=client_data,
            next_pass_code=next_pass_code,
            pass_code=pass_code,
            registration_data=registration_data,
            state_token=state_token,
            template_id=template_id,
            token_lifetime_seconds=token_lifetime_seconds,
            x_forwarded_for=x_forwarded_for,
            user_agent=user_agent,
            accept_language=accept_language,
        )
        return await self._averify_otp_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        user_id: str,
        factor_id: str,
        activation_token: typing.Optional[str] = None,
        answer: typing.Optional[str] = None,
        attestation: typing.Optional[str] = None,
        client_data: typing.Optional[str] = None,
        next_pass_code: typing.Optional[str] = None,
        pass_code: typing.Optional[str] = None,
        registration_data: typing.Optional[str] = None,
        state_token: typing.Optional[str] = None,
        template_id: typing.Optional[str] = None,
        token_lifetime_seconds: typing.Optional[int] = None,
        x_forwarded_for: typing.Optional[str] = None,
        user_agent: typing.Optional[str] = None,
        accept_language: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verify_otp_mapped_args(
            body=body,
            user_id=user_id,
            factor_id=factor_id,
            activation_token=activation_token,
            answer=answer,
            attestation=attestation,
            client_data=client_data,
            next_pass_code=next_pass_code,
            pass_code=pass_code,
            registration_data=registration_data,
            state_token=state_token,
            template_id=template_id,
            token_lifetime_seconds=token_lifetime_seconds,
            x_forwarded_for=x_forwarded_for,
            user_agent=user_agent,
            accept_language=accept_language,
        )
        return self._verify_otp_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )


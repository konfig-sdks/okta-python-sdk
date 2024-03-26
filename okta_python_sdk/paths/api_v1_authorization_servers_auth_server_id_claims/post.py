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

from okta_python_sdk.model.o_auth2_claim_conditions import OAuth2ClaimConditions as OAuth2ClaimConditionsSchema
from okta_python_sdk.model.o_auth2_claim_links import OAuth2ClaimLinks as OAuth2ClaimLinksSchema
from okta_python_sdk.model.o_auth2_claim import OAuth2Claim as OAuth2ClaimSchema

from okta_python_sdk.type.o_auth2_claim_conditions import OAuth2ClaimConditions
from okta_python_sdk.type.o_auth2_claim_links import OAuth2ClaimLinks
from okta_python_sdk.type.o_auth2_claim import OAuth2Claim

from ...api_client import Dictionary
from okta_python_sdk.pydantic.o_auth2_claim import OAuth2Claim as OAuth2ClaimPydantic
from okta_python_sdk.pydantic.o_auth2_claim_links import OAuth2ClaimLinks as OAuth2ClaimLinksPydantic
from okta_python_sdk.pydantic.o_auth2_claim_conditions import OAuth2ClaimConditions as OAuth2ClaimConditionsPydantic

from . import path

# Path params
AuthServerIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'authServerId': typing.Union[AuthServerIdSchema, str, ],
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


request_path_auth_server_id = api_client.PathParameter(
    name="authServerId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AuthServerIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = OAuth2ClaimSchema


request_body_o_auth2_claim = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_token',
]
SchemaFor200ResponseBodyApplicationJson = OAuth2ClaimSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OAuth2Claim


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OAuth2Claim


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
)
_status_code_to_response = {
    '200': _response_for_200,
    '201': _response_for_201,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_claims_mapped_args(
        self,
        auth_server_id: str,
        links: typing.Optional[OAuth2ClaimLinks] = None,
        always_include_in_token: typing.Optional[bool] = None,
        claim_type: typing.Optional[str] = None,
        conditions: typing.Optional[OAuth2ClaimConditions] = None,
        group_filter_type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        system: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        value_type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if links is not None:
            _body["_links"] = links
        if always_include_in_token is not None:
            _body["alwaysIncludeInToken"] = always_include_in_token
        if claim_type is not None:
            _body["claimType"] = claim_type
        if conditions is not None:
            _body["conditions"] = conditions
        if group_filter_type is not None:
            _body["group_filter_type"] = group_filter_type
        if id is not None:
            _body["id"] = id
        if name is not None:
            _body["name"] = name
        if status is not None:
            _body["status"] = status
        if system is not None:
            _body["system"] = system
        if value is not None:
            _body["value"] = value
        if value_type is not None:
            _body["valueType"] = value_type
        args.body = _body
        if auth_server_id is not None:
            _path_params["authServerId"] = auth_server_id
        args.path = _path_params
        return args

    async def _acreate_claims_oapg(
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
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_auth_server_id,
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
            path_template='/api/v1/authorizationServers/{authServerId}/claims',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_o_auth2_claim.serialize(body, content_type)
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


    def _create_claims_oapg(
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
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_auth_server_id,
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
            path_template='/api/v1/authorizationServers/{authServerId}/claims',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_o_auth2_claim.serialize(body, content_type)
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


class CreateClaimsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_claims(
        self,
        auth_server_id: str,
        links: typing.Optional[OAuth2ClaimLinks] = None,
        always_include_in_token: typing.Optional[bool] = None,
        claim_type: typing.Optional[str] = None,
        conditions: typing.Optional[OAuth2ClaimConditions] = None,
        group_filter_type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        system: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        value_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_claims_mapped_args(
            auth_server_id=auth_server_id,
            links=links,
            always_include_in_token=always_include_in_token,
            claim_type=claim_type,
            conditions=conditions,
            group_filter_type=group_filter_type,
            id=id,
            name=name,
            status=status,
            system=system,
            value=value,
            value_type=value_type,
        )
        return await self._acreate_claims_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_claims(
        self,
        auth_server_id: str,
        links: typing.Optional[OAuth2ClaimLinks] = None,
        always_include_in_token: typing.Optional[bool] = None,
        claim_type: typing.Optional[str] = None,
        conditions: typing.Optional[OAuth2ClaimConditions] = None,
        group_filter_type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        system: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        value_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_claims_mapped_args(
            auth_server_id=auth_server_id,
            links=links,
            always_include_in_token=always_include_in_token,
            claim_type=claim_type,
            conditions=conditions,
            group_filter_type=group_filter_type,
            id=id,
            name=name,
            status=status,
            system=system,
            value=value,
            value_type=value_type,
        )
        return self._create_claims_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateClaims(BaseApi):

    async def acreate_claims(
        self,
        auth_server_id: str,
        links: typing.Optional[OAuth2ClaimLinks] = None,
        always_include_in_token: typing.Optional[bool] = None,
        claim_type: typing.Optional[str] = None,
        conditions: typing.Optional[OAuth2ClaimConditions] = None,
        group_filter_type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        system: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        value_type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OAuth2ClaimPydantic:
        raw_response = await self.raw.acreate_claims(
            auth_server_id=auth_server_id,
            links=links,
            always_include_in_token=always_include_in_token,
            claim_type=claim_type,
            conditions=conditions,
            group_filter_type=group_filter_type,
            id=id,
            name=name,
            status=status,
            system=system,
            value=value,
            value_type=value_type,
            **kwargs,
        )
        if validate:
            return OAuth2ClaimPydantic(**raw_response.body)
        return api_client.construct_model_instance(OAuth2ClaimPydantic, raw_response.body)
    
    
    def create_claims(
        self,
        auth_server_id: str,
        links: typing.Optional[OAuth2ClaimLinks] = None,
        always_include_in_token: typing.Optional[bool] = None,
        claim_type: typing.Optional[str] = None,
        conditions: typing.Optional[OAuth2ClaimConditions] = None,
        group_filter_type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        system: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        value_type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OAuth2ClaimPydantic:
        raw_response = self.raw.create_claims(
            auth_server_id=auth_server_id,
            links=links,
            always_include_in_token=always_include_in_token,
            claim_type=claim_type,
            conditions=conditions,
            group_filter_type=group_filter_type,
            id=id,
            name=name,
            status=status,
            system=system,
            value=value,
            value_type=value_type,
        )
        if validate:
            return OAuth2ClaimPydantic(**raw_response.body)
        return api_client.construct_model_instance(OAuth2ClaimPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        auth_server_id: str,
        links: typing.Optional[OAuth2ClaimLinks] = None,
        always_include_in_token: typing.Optional[bool] = None,
        claim_type: typing.Optional[str] = None,
        conditions: typing.Optional[OAuth2ClaimConditions] = None,
        group_filter_type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        system: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        value_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_claims_mapped_args(
            auth_server_id=auth_server_id,
            links=links,
            always_include_in_token=always_include_in_token,
            claim_type=claim_type,
            conditions=conditions,
            group_filter_type=group_filter_type,
            id=id,
            name=name,
            status=status,
            system=system,
            value=value,
            value_type=value_type,
        )
        return await self._acreate_claims_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        auth_server_id: str,
        links: typing.Optional[OAuth2ClaimLinks] = None,
        always_include_in_token: typing.Optional[bool] = None,
        claim_type: typing.Optional[str] = None,
        conditions: typing.Optional[OAuth2ClaimConditions] = None,
        group_filter_type: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        system: typing.Optional[bool] = None,
        value: typing.Optional[str] = None,
        value_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_claims_mapped_args(
            auth_server_id=auth_server_id,
            links=links,
            always_include_in_token=always_include_in_token,
            claim_type=claim_type,
            conditions=conditions,
            group_filter_type=group_filter_type,
            id=id,
            name=name,
            status=status,
            system=system,
            value=value,
            value_type=value_type,
        )
        return self._create_claims_oapg(
            body=args.body,
            path_params=args.path,
        )


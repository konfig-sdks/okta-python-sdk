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

from okta_python_sdk.model.identity_provider_policy import IdentityProviderPolicy as IdentityProviderPolicySchema
from okta_python_sdk.model.identity_provider import IdentityProvider as IdentityProviderSchema
from okta_python_sdk.model.protocol import Protocol as ProtocolSchema
from okta_python_sdk.model.identity_provider_links import IdentityProviderLinks as IdentityProviderLinksSchema

from okta_python_sdk.type.protocol import Protocol
from okta_python_sdk.type.identity_provider_policy import IdentityProviderPolicy
from okta_python_sdk.type.identity_provider import IdentityProvider
from okta_python_sdk.type.identity_provider_links import IdentityProviderLinks

from ...api_client import Dictionary
from okta_python_sdk.pydantic.identity_provider_policy import IdentityProviderPolicy as IdentityProviderPolicyPydantic
from okta_python_sdk.pydantic.identity_provider import IdentityProvider as IdentityProviderPydantic
from okta_python_sdk.pydantic.identity_provider_links import IdentityProviderLinks as IdentityProviderLinksPydantic
from okta_python_sdk.pydantic.protocol import Protocol as ProtocolPydantic

# body param
SchemaForRequestBodyApplicationJson = IdentityProviderSchema


request_body_identity_provider = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = IdentityProviderSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: IdentityProvider


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: IdentityProvider


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

    def _add_new_idp_mapped_args(
        self,
        links: typing.Optional[IdentityProviderLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        policy: typing.Optional[IdentityProviderPolicy] = None,
        protocol: typing.Optional[Protocol] = None,
        status: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if links is not None:
            _body["_links"] = links
        if created is not None:
            _body["created"] = created
        if id is not None:
            _body["id"] = id
        if issuer_mode is not None:
            _body["issuerMode"] = issuer_mode
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if name is not None:
            _body["name"] = name
        if policy is not None:
            _body["policy"] = policy
        if protocol is not None:
            _body["protocol"] = protocol
        if status is not None:
            _body["status"] = status
        if type is not None:
            _body["type"] = type
        args.body = _body
        return args

    async def _aadd_new_idp_oapg(
        self,
        body: typing.Any = None,
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
        Add Identity Provider
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/api/v1/idps',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_identity_provider.serialize(body, content_type)
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


    def _add_new_idp_oapg(
        self,
        body: typing.Any = None,
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
        Add Identity Provider
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/api/v1/idps',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_identity_provider.serialize(body, content_type)
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


class AddNewIdpRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_new_idp(
        self,
        links: typing.Optional[IdentityProviderLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        policy: typing.Optional[IdentityProviderPolicy] = None,
        protocol: typing.Optional[Protocol] = None,
        status: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_new_idp_mapped_args(
            links=links,
            created=created,
            id=id,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            policy=policy,
            protocol=protocol,
            status=status,
            type=type,
        )
        return await self._aadd_new_idp_oapg(
            body=args.body,
            **kwargs,
        )
    
    def add_new_idp(
        self,
        links: typing.Optional[IdentityProviderLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        policy: typing.Optional[IdentityProviderPolicy] = None,
        protocol: typing.Optional[Protocol] = None,
        status: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_new_idp_mapped_args(
            links=links,
            created=created,
            id=id,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            policy=policy,
            protocol=protocol,
            status=status,
            type=type,
        )
        return self._add_new_idp_oapg(
            body=args.body,
        )

class AddNewIdp(BaseApi):

    async def aadd_new_idp(
        self,
        links: typing.Optional[IdentityProviderLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        policy: typing.Optional[IdentityProviderPolicy] = None,
        protocol: typing.Optional[Protocol] = None,
        status: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> IdentityProviderPydantic:
        raw_response = await self.raw.aadd_new_idp(
            links=links,
            created=created,
            id=id,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            policy=policy,
            protocol=protocol,
            status=status,
            type=type,
            **kwargs,
        )
        if validate:
            return IdentityProviderPydantic(**raw_response.body)
        return api_client.construct_model_instance(IdentityProviderPydantic, raw_response.body)
    
    
    def add_new_idp(
        self,
        links: typing.Optional[IdentityProviderLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        policy: typing.Optional[IdentityProviderPolicy] = None,
        protocol: typing.Optional[Protocol] = None,
        status: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> IdentityProviderPydantic:
        raw_response = self.raw.add_new_idp(
            links=links,
            created=created,
            id=id,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            policy=policy,
            protocol=protocol,
            status=status,
            type=type,
        )
        if validate:
            return IdentityProviderPydantic(**raw_response.body)
        return api_client.construct_model_instance(IdentityProviderPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        links: typing.Optional[IdentityProviderLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        policy: typing.Optional[IdentityProviderPolicy] = None,
        protocol: typing.Optional[Protocol] = None,
        status: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_new_idp_mapped_args(
            links=links,
            created=created,
            id=id,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            policy=policy,
            protocol=protocol,
            status=status,
            type=type,
        )
        return await self._aadd_new_idp_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        links: typing.Optional[IdentityProviderLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        policy: typing.Optional[IdentityProviderPolicy] = None,
        protocol: typing.Optional[Protocol] = None,
        status: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_new_idp_mapped_args(
            links=links,
            created=created,
            id=id,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            policy=policy,
            protocol=protocol,
            status=status,
            type=type,
        )
        return self._add_new_idp_oapg(
            body=args.body,
        )


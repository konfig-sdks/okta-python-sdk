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

from okta_python_sdk.model.authorization_server_audiences import AuthorizationServerAudiences as AuthorizationServerAudiencesSchema
from okta_python_sdk.model.authorization_server import AuthorizationServer as AuthorizationServerSchema
from okta_python_sdk.model.authorization_server_links import AuthorizationServerLinks as AuthorizationServerLinksSchema
from okta_python_sdk.model.authorization_server_credentials import AuthorizationServerCredentials as AuthorizationServerCredentialsSchema

from okta_python_sdk.type.authorization_server import AuthorizationServer
from okta_python_sdk.type.authorization_server_credentials import AuthorizationServerCredentials
from okta_python_sdk.type.authorization_server_links import AuthorizationServerLinks
from okta_python_sdk.type.authorization_server_audiences import AuthorizationServerAudiences

from ...api_client import Dictionary
from okta_python_sdk.pydantic.authorization_server_credentials import AuthorizationServerCredentials as AuthorizationServerCredentialsPydantic
from okta_python_sdk.pydantic.authorization_server import AuthorizationServer as AuthorizationServerPydantic
from okta_python_sdk.pydantic.authorization_server_audiences import AuthorizationServerAudiences as AuthorizationServerAudiencesPydantic
from okta_python_sdk.pydantic.authorization_server_links import AuthorizationServerLinks as AuthorizationServerLinksPydantic

# body param
SchemaForRequestBodyApplicationJson = AuthorizationServerSchema


request_body_authorization_server = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = AuthorizationServerSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AuthorizationServer


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AuthorizationServer


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_server_mapped_args(
        self,
        description: typing.Optional[str] = None,
        links: typing.Optional[AuthorizationServerLinks] = None,
        audiences: typing.Optional[AuthorizationServerAudiences] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[AuthorizationServerCredentials] = None,
        default: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if links is not None:
            _body["_links"] = links
        if audiences is not None:
            _body["audiences"] = audiences
        if created is not None:
            _body["created"] = created
        if credentials is not None:
            _body["credentials"] = credentials
        if default is not None:
            _body["default"] = default
        if id is not None:
            _body["id"] = id
        if issuer is not None:
            _body["issuer"] = issuer
        if issuer_mode is not None:
            _body["issuerMode"] = issuer_mode
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if name is not None:
            _body["name"] = name
        if status is not None:
            _body["status"] = status
        args.body = _body
        return args

    async def _acreate_new_server_oapg(
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
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
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
            path_template='/api/v1/authorizationServers',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_authorization_server.serialize(body, content_type)
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


    def _create_new_server_oapg(
        self,
        body: typing.Any = None,
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
            path_template='/api/v1/authorizationServers',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_authorization_server.serialize(body, content_type)
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


class CreateNewServerRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_server(
        self,
        description: typing.Optional[str] = None,
        links: typing.Optional[AuthorizationServerLinks] = None,
        audiences: typing.Optional[AuthorizationServerAudiences] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[AuthorizationServerCredentials] = None,
        default: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_server_mapped_args(
            description=description,
            links=links,
            audiences=audiences,
            created=created,
            credentials=credentials,
            default=default,
            id=id,
            issuer=issuer,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            status=status,
        )
        return await self._acreate_new_server_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_server(
        self,
        description: typing.Optional[str] = None,
        links: typing.Optional[AuthorizationServerLinks] = None,
        audiences: typing.Optional[AuthorizationServerAudiences] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[AuthorizationServerCredentials] = None,
        default: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_server_mapped_args(
            description=description,
            links=links,
            audiences=audiences,
            created=created,
            credentials=credentials,
            default=default,
            id=id,
            issuer=issuer,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            status=status,
        )
        return self._create_new_server_oapg(
            body=args.body,
        )

class CreateNewServer(BaseApi):

    async def acreate_new_server(
        self,
        description: typing.Optional[str] = None,
        links: typing.Optional[AuthorizationServerLinks] = None,
        audiences: typing.Optional[AuthorizationServerAudiences] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[AuthorizationServerCredentials] = None,
        default: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AuthorizationServerPydantic:
        raw_response = await self.raw.acreate_new_server(
            description=description,
            links=links,
            audiences=audiences,
            created=created,
            credentials=credentials,
            default=default,
            id=id,
            issuer=issuer,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            status=status,
            **kwargs,
        )
        if validate:
            return AuthorizationServerPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthorizationServerPydantic, raw_response.body)
    
    
    def create_new_server(
        self,
        description: typing.Optional[str] = None,
        links: typing.Optional[AuthorizationServerLinks] = None,
        audiences: typing.Optional[AuthorizationServerAudiences] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[AuthorizationServerCredentials] = None,
        default: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AuthorizationServerPydantic:
        raw_response = self.raw.create_new_server(
            description=description,
            links=links,
            audiences=audiences,
            created=created,
            credentials=credentials,
            default=default,
            id=id,
            issuer=issuer,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            status=status,
        )
        if validate:
            return AuthorizationServerPydantic(**raw_response.body)
        return api_client.construct_model_instance(AuthorizationServerPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        description: typing.Optional[str] = None,
        links: typing.Optional[AuthorizationServerLinks] = None,
        audiences: typing.Optional[AuthorizationServerAudiences] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[AuthorizationServerCredentials] = None,
        default: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_server_mapped_args(
            description=description,
            links=links,
            audiences=audiences,
            created=created,
            credentials=credentials,
            default=default,
            id=id,
            issuer=issuer,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            status=status,
        )
        return await self._acreate_new_server_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        description: typing.Optional[str] = None,
        links: typing.Optional[AuthorizationServerLinks] = None,
        audiences: typing.Optional[AuthorizationServerAudiences] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[AuthorizationServerCredentials] = None,
        default: typing.Optional[bool] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        issuer_mode: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        name: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_server_mapped_args(
            description=description,
            links=links,
            audiences=audiences,
            created=created,
            credentials=credentials,
            default=default,
            id=id,
            issuer=issuer,
            issuer_mode=issuer_mode,
            last_updated=last_updated,
            name=name,
            status=status,
        )
        return self._create_new_server_oapg(
            body=args.body,
        )


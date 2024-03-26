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

from okta_python_sdk.model.o_auth2_scope_consent_grant_links import OAuth2ScopeConsentGrantLinks as OAuth2ScopeConsentGrantLinksSchema
from okta_python_sdk.model.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant as OAuth2ScopeConsentGrantSchema
from okta_python_sdk.model.o_auth2_scope_consent_grant_status import OAuth2ScopeConsentGrantStatus as OAuth2ScopeConsentGrantStatusSchema
from okta_python_sdk.model.o_auth2_scope_consent_grant_embedded import OAuth2ScopeConsentGrantEmbedded as OAuth2ScopeConsentGrantEmbeddedSchema
from okta_python_sdk.model.o_auth2_scope_consent_grant_source import OAuth2ScopeConsentGrantSource as OAuth2ScopeConsentGrantSourceSchema
from okta_python_sdk.model.o_auth2_actor import OAuth2Actor as OAuth2ActorSchema

from okta_python_sdk.type.o_auth2_scope_consent_grant_links import OAuth2ScopeConsentGrantLinks
from okta_python_sdk.type.o_auth2_scope_consent_grant_embedded import OAuth2ScopeConsentGrantEmbedded
from okta_python_sdk.type.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant
from okta_python_sdk.type.o_auth2_scope_consent_grant_source import OAuth2ScopeConsentGrantSource
from okta_python_sdk.type.o_auth2_actor import OAuth2Actor
from okta_python_sdk.type.o_auth2_scope_consent_grant_status import OAuth2ScopeConsentGrantStatus

from ...api_client import Dictionary
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_links import OAuth2ScopeConsentGrantLinks as OAuth2ScopeConsentGrantLinksPydantic
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_source import OAuth2ScopeConsentGrantSource as OAuth2ScopeConsentGrantSourcePydantic
from okta_python_sdk.pydantic.o_auth2_actor import OAuth2Actor as OAuth2ActorPydantic
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant import OAuth2ScopeConsentGrant as OAuth2ScopeConsentGrantPydantic
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_embedded import OAuth2ScopeConsentGrantEmbedded as OAuth2ScopeConsentGrantEmbeddedPydantic
from okta_python_sdk.pydantic.o_auth2_scope_consent_grant_status import OAuth2ScopeConsentGrantStatus as OAuth2ScopeConsentGrantStatusPydantic

# Path params
AppIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'appId': typing.Union[AppIdSchema, str, ],
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
# body param
SchemaForRequestBodyApplicationJson = OAuth2ScopeConsentGrantSchema


request_body_o_auth2_scope_consent_grant = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = OAuth2ScopeConsentGrantSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: OAuth2ScopeConsentGrant


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: OAuth2ScopeConsentGrant


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _grant_consent_to_scope_mapped_args(
        self,
        app_id: str,
        embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = None,
        links: typing.Optional[OAuth2ScopeConsentGrantLinks] = None,
        client_id: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        created_by: typing.Optional[OAuth2Actor] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        scope_id: typing.Optional[str] = None,
        source: typing.Optional[OAuth2ScopeConsentGrantSource] = None,
        status: typing.Optional[OAuth2ScopeConsentGrantStatus] = None,
        user_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if embedded is not None:
            _body["_embedded"] = embedded
        if links is not None:
            _body["_links"] = links
        if client_id is not None:
            _body["clientId"] = client_id
        if created is not None:
            _body["created"] = created
        if created_by is not None:
            _body["createdBy"] = created_by
        if id is not None:
            _body["id"] = id
        if issuer is not None:
            _body["issuer"] = issuer
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if scope_id is not None:
            _body["scopeId"] = scope_id
        if source is not None:
            _body["source"] = source
        if status is not None:
            _body["status"] = status
        if user_id is not None:
            _body["userId"] = user_id
        args.body = _body
        if app_id is not None:
            _path_params["appId"] = app_id
        args.path = _path_params
        return args

    async def _agrant_consent_to_scope_oapg(
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
            request_path_app_id,
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
            path_template='/api/v1/apps/{appId}/grants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_o_auth2_scope_consent_grant.serialize(body, content_type)
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


    def _grant_consent_to_scope_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
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
            request_path_app_id,
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
            path_template='/api/v1/apps/{appId}/grants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_o_auth2_scope_consent_grant.serialize(body, content_type)
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


class GrantConsentToScopeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def agrant_consent_to_scope(
        self,
        app_id: str,
        embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = None,
        links: typing.Optional[OAuth2ScopeConsentGrantLinks] = None,
        client_id: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        created_by: typing.Optional[OAuth2Actor] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        scope_id: typing.Optional[str] = None,
        source: typing.Optional[OAuth2ScopeConsentGrantSource] = None,
        status: typing.Optional[OAuth2ScopeConsentGrantStatus] = None,
        user_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._grant_consent_to_scope_mapped_args(
            app_id=app_id,
            embedded=embedded,
            links=links,
            client_id=client_id,
            created=created,
            created_by=created_by,
            id=id,
            issuer=issuer,
            last_updated=last_updated,
            scope_id=scope_id,
            source=source,
            status=status,
            user_id=user_id,
        )
        return await self._agrant_consent_to_scope_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def grant_consent_to_scope(
        self,
        app_id: str,
        embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = None,
        links: typing.Optional[OAuth2ScopeConsentGrantLinks] = None,
        client_id: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        created_by: typing.Optional[OAuth2Actor] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        scope_id: typing.Optional[str] = None,
        source: typing.Optional[OAuth2ScopeConsentGrantSource] = None,
        status: typing.Optional[OAuth2ScopeConsentGrantStatus] = None,
        user_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._grant_consent_to_scope_mapped_args(
            app_id=app_id,
            embedded=embedded,
            links=links,
            client_id=client_id,
            created=created,
            created_by=created_by,
            id=id,
            issuer=issuer,
            last_updated=last_updated,
            scope_id=scope_id,
            source=source,
            status=status,
            user_id=user_id,
        )
        return self._grant_consent_to_scope_oapg(
            body=args.body,
            path_params=args.path,
        )

class GrantConsentToScope(BaseApi):

    async def agrant_consent_to_scope(
        self,
        app_id: str,
        embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = None,
        links: typing.Optional[OAuth2ScopeConsentGrantLinks] = None,
        client_id: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        created_by: typing.Optional[OAuth2Actor] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        scope_id: typing.Optional[str] = None,
        source: typing.Optional[OAuth2ScopeConsentGrantSource] = None,
        status: typing.Optional[OAuth2ScopeConsentGrantStatus] = None,
        user_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OAuth2ScopeConsentGrantPydantic:
        raw_response = await self.raw.agrant_consent_to_scope(
            app_id=app_id,
            embedded=embedded,
            links=links,
            client_id=client_id,
            created=created,
            created_by=created_by,
            id=id,
            issuer=issuer,
            last_updated=last_updated,
            scope_id=scope_id,
            source=source,
            status=status,
            user_id=user_id,
            **kwargs,
        )
        if validate:
            return OAuth2ScopeConsentGrantPydantic(**raw_response.body)
        return api_client.construct_model_instance(OAuth2ScopeConsentGrantPydantic, raw_response.body)
    
    
    def grant_consent_to_scope(
        self,
        app_id: str,
        embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = None,
        links: typing.Optional[OAuth2ScopeConsentGrantLinks] = None,
        client_id: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        created_by: typing.Optional[OAuth2Actor] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        scope_id: typing.Optional[str] = None,
        source: typing.Optional[OAuth2ScopeConsentGrantSource] = None,
        status: typing.Optional[OAuth2ScopeConsentGrantStatus] = None,
        user_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OAuth2ScopeConsentGrantPydantic:
        raw_response = self.raw.grant_consent_to_scope(
            app_id=app_id,
            embedded=embedded,
            links=links,
            client_id=client_id,
            created=created,
            created_by=created_by,
            id=id,
            issuer=issuer,
            last_updated=last_updated,
            scope_id=scope_id,
            source=source,
            status=status,
            user_id=user_id,
        )
        if validate:
            return OAuth2ScopeConsentGrantPydantic(**raw_response.body)
        return api_client.construct_model_instance(OAuth2ScopeConsentGrantPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        app_id: str,
        embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = None,
        links: typing.Optional[OAuth2ScopeConsentGrantLinks] = None,
        client_id: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        created_by: typing.Optional[OAuth2Actor] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        scope_id: typing.Optional[str] = None,
        source: typing.Optional[OAuth2ScopeConsentGrantSource] = None,
        status: typing.Optional[OAuth2ScopeConsentGrantStatus] = None,
        user_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._grant_consent_to_scope_mapped_args(
            app_id=app_id,
            embedded=embedded,
            links=links,
            client_id=client_id,
            created=created,
            created_by=created_by,
            id=id,
            issuer=issuer,
            last_updated=last_updated,
            scope_id=scope_id,
            source=source,
            status=status,
            user_id=user_id,
        )
        return await self._agrant_consent_to_scope_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        app_id: str,
        embedded: typing.Optional[OAuth2ScopeConsentGrantEmbedded] = None,
        links: typing.Optional[OAuth2ScopeConsentGrantLinks] = None,
        client_id: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        created_by: typing.Optional[OAuth2Actor] = None,
        id: typing.Optional[str] = None,
        issuer: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        scope_id: typing.Optional[str] = None,
        source: typing.Optional[OAuth2ScopeConsentGrantSource] = None,
        status: typing.Optional[OAuth2ScopeConsentGrantStatus] = None,
        user_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._grant_consent_to_scope_mapped_args(
            app_id=app_id,
            embedded=embedded,
            links=links,
            client_id=client_id,
            created=created,
            created_by=created_by,
            id=id,
            issuer=issuer,
            last_updated=last_updated,
            scope_id=scope_id,
            source=source,
            status=status,
            user_id=user_id,
        )
        return self._grant_consent_to_scope_oapg(
            body=args.body,
            path_params=args.path,
        )


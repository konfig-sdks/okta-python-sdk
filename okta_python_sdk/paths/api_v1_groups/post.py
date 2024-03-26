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

from okta_python_sdk.model.group_object_class import GroupObjectClass as GroupObjectClassSchema
from okta_python_sdk.model.group_profile import GroupProfile as GroupProfileSchema
from okta_python_sdk.model.group_embedded import GroupEmbedded as GroupEmbeddedSchema
from okta_python_sdk.model.group_links import GroupLinks as GroupLinksSchema
from okta_python_sdk.model.group import Group as GroupSchema
from okta_python_sdk.model.group_type import GroupType as GroupTypeSchema

from okta_python_sdk.type.group_embedded import GroupEmbedded
from okta_python_sdk.type.group import Group
from okta_python_sdk.type.group_links import GroupLinks
from okta_python_sdk.type.group_object_class import GroupObjectClass
from okta_python_sdk.type.group_type import GroupType
from okta_python_sdk.type.group_profile import GroupProfile

from ...api_client import Dictionary
from okta_python_sdk.pydantic.group_links import GroupLinks as GroupLinksPydantic
from okta_python_sdk.pydantic.group_profile import GroupProfile as GroupProfilePydantic
from okta_python_sdk.pydantic.group_object_class import GroupObjectClass as GroupObjectClassPydantic
from okta_python_sdk.pydantic.group_type import GroupType as GroupTypePydantic
from okta_python_sdk.pydantic.group import Group as GroupPydantic
from okta_python_sdk.pydantic.group_embedded import GroupEmbedded as GroupEmbeddedPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = GroupSchema


request_body_group = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_token',
]
SchemaFor200ResponseBodyApplicationJson = GroupSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Group


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Group


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

    def _create_new_group_mapped_args(
        self,
        embedded: typing.Optional[GroupEmbedded] = None,
        links: typing.Optional[GroupLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        last_membership_updated: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        object_class: typing.Optional[GroupObjectClass] = None,
        profile: typing.Optional[GroupProfile] = None,
        type: typing.Optional[GroupType] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if embedded is not None:
            _body["_embedded"] = embedded
        if links is not None:
            _body["_links"] = links
        if created is not None:
            _body["created"] = created
        if id is not None:
            _body["id"] = id
        if last_membership_updated is not None:
            _body["lastMembershipUpdated"] = last_membership_updated
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if object_class is not None:
            _body["objectClass"] = object_class
        if profile is not None:
            _body["profile"] = profile
        if type is not None:
            _body["type"] = type
        args.body = _body
        return args

    async def _acreate_new_group_oapg(
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
        Add Group
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
            path_template='/api/v1/groups',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_group.serialize(body, content_type)
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


    def _create_new_group_oapg(
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
        Add Group
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
            path_template='/api/v1/groups',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_group.serialize(body, content_type)
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


class CreateNewGroupRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_group(
        self,
        embedded: typing.Optional[GroupEmbedded] = None,
        links: typing.Optional[GroupLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        last_membership_updated: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        object_class: typing.Optional[GroupObjectClass] = None,
        profile: typing.Optional[GroupProfile] = None,
        type: typing.Optional[GroupType] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_group_mapped_args(
            embedded=embedded,
            links=links,
            created=created,
            id=id,
            last_membership_updated=last_membership_updated,
            last_updated=last_updated,
            object_class=object_class,
            profile=profile,
            type=type,
        )
        return await self._acreate_new_group_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_group(
        self,
        embedded: typing.Optional[GroupEmbedded] = None,
        links: typing.Optional[GroupLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        last_membership_updated: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        object_class: typing.Optional[GroupObjectClass] = None,
        profile: typing.Optional[GroupProfile] = None,
        type: typing.Optional[GroupType] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_group_mapped_args(
            embedded=embedded,
            links=links,
            created=created,
            id=id,
            last_membership_updated=last_membership_updated,
            last_updated=last_updated,
            object_class=object_class,
            profile=profile,
            type=type,
        )
        return self._create_new_group_oapg(
            body=args.body,
        )

class CreateNewGroup(BaseApi):

    async def acreate_new_group(
        self,
        embedded: typing.Optional[GroupEmbedded] = None,
        links: typing.Optional[GroupLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        last_membership_updated: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        object_class: typing.Optional[GroupObjectClass] = None,
        profile: typing.Optional[GroupProfile] = None,
        type: typing.Optional[GroupType] = None,
        validate: bool = False,
        **kwargs,
    ) -> GroupPydantic:
        raw_response = await self.raw.acreate_new_group(
            embedded=embedded,
            links=links,
            created=created,
            id=id,
            last_membership_updated=last_membership_updated,
            last_updated=last_updated,
            object_class=object_class,
            profile=profile,
            type=type,
            **kwargs,
        )
        if validate:
            return GroupPydantic(**raw_response.body)
        return api_client.construct_model_instance(GroupPydantic, raw_response.body)
    
    
    def create_new_group(
        self,
        embedded: typing.Optional[GroupEmbedded] = None,
        links: typing.Optional[GroupLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        last_membership_updated: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        object_class: typing.Optional[GroupObjectClass] = None,
        profile: typing.Optional[GroupProfile] = None,
        type: typing.Optional[GroupType] = None,
        validate: bool = False,
    ) -> GroupPydantic:
        raw_response = self.raw.create_new_group(
            embedded=embedded,
            links=links,
            created=created,
            id=id,
            last_membership_updated=last_membership_updated,
            last_updated=last_updated,
            object_class=object_class,
            profile=profile,
            type=type,
        )
        if validate:
            return GroupPydantic(**raw_response.body)
        return api_client.construct_model_instance(GroupPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        embedded: typing.Optional[GroupEmbedded] = None,
        links: typing.Optional[GroupLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        last_membership_updated: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        object_class: typing.Optional[GroupObjectClass] = None,
        profile: typing.Optional[GroupProfile] = None,
        type: typing.Optional[GroupType] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_group_mapped_args(
            embedded=embedded,
            links=links,
            created=created,
            id=id,
            last_membership_updated=last_membership_updated,
            last_updated=last_updated,
            object_class=object_class,
            profile=profile,
            type=type,
        )
        return await self._acreate_new_group_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        embedded: typing.Optional[GroupEmbedded] = None,
        links: typing.Optional[GroupLinks] = None,
        created: typing.Optional[datetime] = None,
        id: typing.Optional[str] = None,
        last_membership_updated: typing.Optional[datetime] = None,
        last_updated: typing.Optional[datetime] = None,
        object_class: typing.Optional[GroupObjectClass] = None,
        profile: typing.Optional[GroupProfile] = None,
        type: typing.Optional[GroupType] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_group_mapped_args(
            embedded=embedded,
            links=links,
            created=created,
            id=id,
            last_membership_updated=last_membership_updated,
            last_updated=last_updated,
            object_class=object_class,
            profile=profile,
            type=type,
        )
        return self._create_new_group_oapg(
            body=args.body,
        )


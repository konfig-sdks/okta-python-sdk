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

from okta_python_sdk.model.application_accessibility import ApplicationAccessibility as ApplicationAccessibilitySchema
from okta_python_sdk.model.application_links import ApplicationLinks as ApplicationLinksSchema
from okta_python_sdk.model.application_features import ApplicationFeatures as ApplicationFeaturesSchema
from okta_python_sdk.model.application_settings import ApplicationSettings as ApplicationSettingsSchema
from okta_python_sdk.model.application_visibility import ApplicationVisibility as ApplicationVisibilitySchema
from okta_python_sdk.model.application_credentials import ApplicationCredentials as ApplicationCredentialsSchema
from okta_python_sdk.model.application_licensing import ApplicationLicensing as ApplicationLicensingSchema
from okta_python_sdk.model.application_profile import ApplicationProfile as ApplicationProfileSchema
from okta_python_sdk.model.application_sign_on_mode import ApplicationSignOnMode as ApplicationSignOnModeSchema
from okta_python_sdk.model.application import Application as ApplicationSchema
from okta_python_sdk.model.application_embedded import ApplicationEmbedded as ApplicationEmbeddedSchema

from okta_python_sdk.type.application_settings import ApplicationSettings
from okta_python_sdk.type.application_sign_on_mode import ApplicationSignOnMode
from okta_python_sdk.type.application_embedded import ApplicationEmbedded
from okta_python_sdk.type.application_profile import ApplicationProfile
from okta_python_sdk.type.application_features import ApplicationFeatures
from okta_python_sdk.type.application_links import ApplicationLinks
from okta_python_sdk.type.application_credentials import ApplicationCredentials
from okta_python_sdk.type.application_accessibility import ApplicationAccessibility
from okta_python_sdk.type.application_licensing import ApplicationLicensing
from okta_python_sdk.type.application_visibility import ApplicationVisibility
from okta_python_sdk.type.application import Application

from ...api_client import Dictionary
from okta_python_sdk.pydantic.application_profile import ApplicationProfile as ApplicationProfilePydantic
from okta_python_sdk.pydantic.application import Application as ApplicationPydantic
from okta_python_sdk.pydantic.application_sign_on_mode import ApplicationSignOnMode as ApplicationSignOnModePydantic
from okta_python_sdk.pydantic.application_licensing import ApplicationLicensing as ApplicationLicensingPydantic
from okta_python_sdk.pydantic.application_accessibility import ApplicationAccessibility as ApplicationAccessibilityPydantic
from okta_python_sdk.pydantic.application_settings import ApplicationSettings as ApplicationSettingsPydantic
from okta_python_sdk.pydantic.application_visibility import ApplicationVisibility as ApplicationVisibilityPydantic
from okta_python_sdk.pydantic.application_links import ApplicationLinks as ApplicationLinksPydantic
from okta_python_sdk.pydantic.application_embedded import ApplicationEmbedded as ApplicationEmbeddedPydantic
from okta_python_sdk.pydantic.application_credentials import ApplicationCredentials as ApplicationCredentialsPydantic
from okta_python_sdk.pydantic.application_features import ApplicationFeatures as ApplicationFeaturesPydantic

from . import path

# Query params
ActivateSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'activate': typing.Union[ActivateSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_activate = api_client.QueryParameter(
    name="activate",
    style=api_client.ParameterStyle.FORM,
    schema=ActivateSchema,
    explode=True,
)
# Header params
OktaAccessGatewayAgentSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'OktaAccessGateway-Agent': typing.Union[OktaAccessGatewayAgentSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_okta_access_gateway_agent = api_client.HeaderParameter(
    name="OktaAccessGateway-Agent",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OktaAccessGatewayAgentSchema,
)
# body param
SchemaForRequestBodyApplicationJson = ApplicationSchema


request_body_application = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_token',
]
SchemaFor200ResponseBodyApplicationJson = ApplicationSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Application


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Application


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

    def _create_new_mapped_args(
        self,
        embedded: typing.Optional[ApplicationEmbedded] = None,
        links: typing.Optional[ApplicationLinks] = None,
        accessibility: typing.Optional[ApplicationAccessibility] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[ApplicationCredentials] = None,
        features: typing.Optional[ApplicationFeatures] = None,
        id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        licensing: typing.Optional[ApplicationLicensing] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[ApplicationProfile] = None,
        settings: typing.Optional[ApplicationSettings] = None,
        sign_on_mode: typing.Optional[ApplicationSignOnMode] = None,
        status: typing.Optional[str] = None,
        visibility: typing.Optional[ApplicationVisibility] = None,
        activate: typing.Optional[bool] = None,
        okta_access_gateway_agent: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _body = {}
        if embedded is not None:
            _body["_embedded"] = embedded
        if links is not None:
            _body["_links"] = links
        if accessibility is not None:
            _body["accessibility"] = accessibility
        if created is not None:
            _body["created"] = created
        if credentials is not None:
            _body["credentials"] = credentials
        if features is not None:
            _body["features"] = features
        if id is not None:
            _body["id"] = id
        if label is not None:
            _body["label"] = label
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if licensing is not None:
            _body["licensing"] = licensing
        if name is not None:
            _body["name"] = name
        if profile is not None:
            _body["profile"] = profile
        if settings is not None:
            _body["settings"] = settings
        if sign_on_mode is not None:
            _body["signOnMode"] = sign_on_mode
        if status is not None:
            _body["status"] = status
        if visibility is not None:
            _body["visibility"] = visibility
        args.body = _body
        if activate is not None:
            _query_params["activate"] = activate
        if okta_access_gateway_agent is not None:
            _header_params["OktaAccessGateway-Agent"] = okta_access_gateway_agent
        args.query = _query_params
        args.header = _header_params
        return args

    async def _acreate_new_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        Add Application
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_activate,
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
            request_header_okta_access_gateway_agent,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/apps',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_application.serialize(body, content_type)
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


    def _create_new_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
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
        Add Application
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_activate,
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
            request_header_okta_access_gateway_agent,
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
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v1/apps',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_application.serialize(body, content_type)
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


class CreateNewRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new(
        self,
        embedded: typing.Optional[ApplicationEmbedded] = None,
        links: typing.Optional[ApplicationLinks] = None,
        accessibility: typing.Optional[ApplicationAccessibility] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[ApplicationCredentials] = None,
        features: typing.Optional[ApplicationFeatures] = None,
        id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        licensing: typing.Optional[ApplicationLicensing] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[ApplicationProfile] = None,
        settings: typing.Optional[ApplicationSettings] = None,
        sign_on_mode: typing.Optional[ApplicationSignOnMode] = None,
        status: typing.Optional[str] = None,
        visibility: typing.Optional[ApplicationVisibility] = None,
        activate: typing.Optional[bool] = None,
        okta_access_gateway_agent: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_mapped_args(
            embedded=embedded,
            links=links,
            accessibility=accessibility,
            created=created,
            credentials=credentials,
            features=features,
            id=id,
            label=label,
            last_updated=last_updated,
            licensing=licensing,
            name=name,
            profile=profile,
            settings=settings,
            sign_on_mode=sign_on_mode,
            status=status,
            visibility=visibility,
            activate=activate,
            okta_access_gateway_agent=okta_access_gateway_agent,
        )
        return await self._acreate_new_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def create_new(
        self,
        embedded: typing.Optional[ApplicationEmbedded] = None,
        links: typing.Optional[ApplicationLinks] = None,
        accessibility: typing.Optional[ApplicationAccessibility] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[ApplicationCredentials] = None,
        features: typing.Optional[ApplicationFeatures] = None,
        id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        licensing: typing.Optional[ApplicationLicensing] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[ApplicationProfile] = None,
        settings: typing.Optional[ApplicationSettings] = None,
        sign_on_mode: typing.Optional[ApplicationSignOnMode] = None,
        status: typing.Optional[str] = None,
        visibility: typing.Optional[ApplicationVisibility] = None,
        activate: typing.Optional[bool] = None,
        okta_access_gateway_agent: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_mapped_args(
            embedded=embedded,
            links=links,
            accessibility=accessibility,
            created=created,
            credentials=credentials,
            features=features,
            id=id,
            label=label,
            last_updated=last_updated,
            licensing=licensing,
            name=name,
            profile=profile,
            settings=settings,
            sign_on_mode=sign_on_mode,
            status=status,
            visibility=visibility,
            activate=activate,
            okta_access_gateway_agent=okta_access_gateway_agent,
        )
        return self._create_new_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

class CreateNew(BaseApi):

    async def acreate_new(
        self,
        embedded: typing.Optional[ApplicationEmbedded] = None,
        links: typing.Optional[ApplicationLinks] = None,
        accessibility: typing.Optional[ApplicationAccessibility] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[ApplicationCredentials] = None,
        features: typing.Optional[ApplicationFeatures] = None,
        id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        licensing: typing.Optional[ApplicationLicensing] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[ApplicationProfile] = None,
        settings: typing.Optional[ApplicationSettings] = None,
        sign_on_mode: typing.Optional[ApplicationSignOnMode] = None,
        status: typing.Optional[str] = None,
        visibility: typing.Optional[ApplicationVisibility] = None,
        activate: typing.Optional[bool] = None,
        okta_access_gateway_agent: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ApplicationPydantic:
        raw_response = await self.raw.acreate_new(
            embedded=embedded,
            links=links,
            accessibility=accessibility,
            created=created,
            credentials=credentials,
            features=features,
            id=id,
            label=label,
            last_updated=last_updated,
            licensing=licensing,
            name=name,
            profile=profile,
            settings=settings,
            sign_on_mode=sign_on_mode,
            status=status,
            visibility=visibility,
            activate=activate,
            okta_access_gateway_agent=okta_access_gateway_agent,
            **kwargs,
        )
        if validate:
            return ApplicationPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationPydantic, raw_response.body)
    
    
    def create_new(
        self,
        embedded: typing.Optional[ApplicationEmbedded] = None,
        links: typing.Optional[ApplicationLinks] = None,
        accessibility: typing.Optional[ApplicationAccessibility] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[ApplicationCredentials] = None,
        features: typing.Optional[ApplicationFeatures] = None,
        id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        licensing: typing.Optional[ApplicationLicensing] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[ApplicationProfile] = None,
        settings: typing.Optional[ApplicationSettings] = None,
        sign_on_mode: typing.Optional[ApplicationSignOnMode] = None,
        status: typing.Optional[str] = None,
        visibility: typing.Optional[ApplicationVisibility] = None,
        activate: typing.Optional[bool] = None,
        okta_access_gateway_agent: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ApplicationPydantic:
        raw_response = self.raw.create_new(
            embedded=embedded,
            links=links,
            accessibility=accessibility,
            created=created,
            credentials=credentials,
            features=features,
            id=id,
            label=label,
            last_updated=last_updated,
            licensing=licensing,
            name=name,
            profile=profile,
            settings=settings,
            sign_on_mode=sign_on_mode,
            status=status,
            visibility=visibility,
            activate=activate,
            okta_access_gateway_agent=okta_access_gateway_agent,
        )
        if validate:
            return ApplicationPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        embedded: typing.Optional[ApplicationEmbedded] = None,
        links: typing.Optional[ApplicationLinks] = None,
        accessibility: typing.Optional[ApplicationAccessibility] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[ApplicationCredentials] = None,
        features: typing.Optional[ApplicationFeatures] = None,
        id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        licensing: typing.Optional[ApplicationLicensing] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[ApplicationProfile] = None,
        settings: typing.Optional[ApplicationSettings] = None,
        sign_on_mode: typing.Optional[ApplicationSignOnMode] = None,
        status: typing.Optional[str] = None,
        visibility: typing.Optional[ApplicationVisibility] = None,
        activate: typing.Optional[bool] = None,
        okta_access_gateway_agent: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_mapped_args(
            embedded=embedded,
            links=links,
            accessibility=accessibility,
            created=created,
            credentials=credentials,
            features=features,
            id=id,
            label=label,
            last_updated=last_updated,
            licensing=licensing,
            name=name,
            profile=profile,
            settings=settings,
            sign_on_mode=sign_on_mode,
            status=status,
            visibility=visibility,
            activate=activate,
            okta_access_gateway_agent=okta_access_gateway_agent,
        )
        return await self._acreate_new_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        embedded: typing.Optional[ApplicationEmbedded] = None,
        links: typing.Optional[ApplicationLinks] = None,
        accessibility: typing.Optional[ApplicationAccessibility] = None,
        created: typing.Optional[datetime] = None,
        credentials: typing.Optional[ApplicationCredentials] = None,
        features: typing.Optional[ApplicationFeatures] = None,
        id: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        licensing: typing.Optional[ApplicationLicensing] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[ApplicationProfile] = None,
        settings: typing.Optional[ApplicationSettings] = None,
        sign_on_mode: typing.Optional[ApplicationSignOnMode] = None,
        status: typing.Optional[str] = None,
        visibility: typing.Optional[ApplicationVisibility] = None,
        activate: typing.Optional[bool] = None,
        okta_access_gateway_agent: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_mapped_args(
            embedded=embedded,
            links=links,
            accessibility=accessibility,
            created=created,
            credentials=credentials,
            features=features,
            id=id,
            label=label,
            last_updated=last_updated,
            licensing=licensing,
            name=name,
            profile=profile,
            settings=settings,
            sign_on_mode=sign_on_mode,
            status=status,
            visibility=visibility,
            activate=activate,
            okta_access_gateway_agent=okta_access_gateway_agent,
        )
        return self._create_new_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )


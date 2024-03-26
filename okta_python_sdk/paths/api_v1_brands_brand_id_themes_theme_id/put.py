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

from okta_python_sdk.model.email_template_touch_point_variant import EmailTemplateTouchPointVariant as EmailTemplateTouchPointVariantSchema
from okta_python_sdk.model.error_page_touch_point_variant import ErrorPageTouchPointVariant as ErrorPageTouchPointVariantSchema
from okta_python_sdk.model.sign_in_page_touch_point_variant import SignInPageTouchPointVariant as SignInPageTouchPointVariantSchema
from okta_python_sdk.model.theme_response import ThemeResponse as ThemeResponseSchema
from okta_python_sdk.model.end_user_dashboard_touch_point_variant import EndUserDashboardTouchPointVariant as EndUserDashboardTouchPointVariantSchema
from okta_python_sdk.model.theme import Theme as ThemeSchema

from okta_python_sdk.type.error_page_touch_point_variant import ErrorPageTouchPointVariant
from okta_python_sdk.type.email_template_touch_point_variant import EmailTemplateTouchPointVariant
from okta_python_sdk.type.theme_response import ThemeResponse
from okta_python_sdk.type.theme import Theme
from okta_python_sdk.type.sign_in_page_touch_point_variant import SignInPageTouchPointVariant
from okta_python_sdk.type.end_user_dashboard_touch_point_variant import EndUserDashboardTouchPointVariant

from ...api_client import Dictionary
from okta_python_sdk.pydantic.email_template_touch_point_variant import EmailTemplateTouchPointVariant as EmailTemplateTouchPointVariantPydantic
from okta_python_sdk.pydantic.end_user_dashboard_touch_point_variant import EndUserDashboardTouchPointVariant as EndUserDashboardTouchPointVariantPydantic
from okta_python_sdk.pydantic.theme_response import ThemeResponse as ThemeResponsePydantic
from okta_python_sdk.pydantic.sign_in_page_touch_point_variant import SignInPageTouchPointVariant as SignInPageTouchPointVariantPydantic
from okta_python_sdk.pydantic.error_page_touch_point_variant import ErrorPageTouchPointVariant as ErrorPageTouchPointVariantPydantic
from okta_python_sdk.pydantic.theme import Theme as ThemePydantic

from . import path

# Path params
BrandIdSchema = schemas.StrSchema
ThemeIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'brandId': typing.Union[BrandIdSchema, str, ],
        'themeId': typing.Union[ThemeIdSchema, str, ],
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
request_path_theme_id = api_client.PathParameter(
    name="themeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ThemeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = ThemeSchema


request_body_theme = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'api_token',
]
SchemaFor200ResponseBodyApplicationJson = ThemeResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ThemeResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ThemeResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_theme_mapped_args(
        self,
        brand_id: str,
        theme_id: str,
        links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        background_image: typing.Optional[str] = None,
        email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = None,
        error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = None,
        primary_color_contrast_hex: typing.Optional[str] = None,
        primary_color_hex: typing.Optional[str] = None,
        secondary_color_contrast_hex: typing.Optional[str] = None,
        secondary_color_hex: typing.Optional[str] = None,
        sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if links is not None:
            _body["_links"] = links
        if background_image is not None:
            _body["backgroundImage"] = background_image
        if email_template_touch_point_variant is not None:
            _body["emailTemplateTouchPointVariant"] = email_template_touch_point_variant
        if end_user_dashboard_touch_point_variant is not None:
            _body["endUserDashboardTouchPointVariant"] = end_user_dashboard_touch_point_variant
        if error_page_touch_point_variant is not None:
            _body["errorPageTouchPointVariant"] = error_page_touch_point_variant
        if primary_color_contrast_hex is not None:
            _body["primaryColorContrastHex"] = primary_color_contrast_hex
        if primary_color_hex is not None:
            _body["primaryColorHex"] = primary_color_hex
        if secondary_color_contrast_hex is not None:
            _body["secondaryColorContrastHex"] = secondary_color_contrast_hex
        if secondary_color_hex is not None:
            _body["secondaryColorHex"] = secondary_color_hex
        if sign_in_page_touch_point_variant is not None:
            _body["signInPageTouchPointVariant"] = sign_in_page_touch_point_variant
        args.body = _body
        if brand_id is not None:
            _path_params["brandId"] = brand_id
        if theme_id is not None:
            _path_params["themeId"] = theme_id
        args.path = _path_params
        return args

    async def _aupdate_theme_oapg(
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
        Update a theme for a brand
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_brand_id,
            request_path_theme_id,
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
            path_template='/api/v1/brands/{brandId}/themes/{themeId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_theme.serialize(body, content_type)
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


    def _update_theme_oapg(
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
        Update a theme for a brand
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_brand_id,
            request_path_theme_id,
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
            path_template='/api/v1/brands/{brandId}/themes/{themeId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_theme.serialize(body, content_type)
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


class UpdateThemeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_theme(
        self,
        brand_id: str,
        theme_id: str,
        links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        background_image: typing.Optional[str] = None,
        email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = None,
        error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = None,
        primary_color_contrast_hex: typing.Optional[str] = None,
        primary_color_hex: typing.Optional[str] = None,
        secondary_color_contrast_hex: typing.Optional[str] = None,
        secondary_color_hex: typing.Optional[str] = None,
        sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_theme_mapped_args(
            body=body,
            brand_id=brand_id,
            theme_id=theme_id,
            links=links,
            background_image=background_image,
            email_template_touch_point_variant=email_template_touch_point_variant,
            end_user_dashboard_touch_point_variant=end_user_dashboard_touch_point_variant,
            error_page_touch_point_variant=error_page_touch_point_variant,
            primary_color_contrast_hex=primary_color_contrast_hex,
            primary_color_hex=primary_color_hex,
            secondary_color_contrast_hex=secondary_color_contrast_hex,
            secondary_color_hex=secondary_color_hex,
            sign_in_page_touch_point_variant=sign_in_page_touch_point_variant,
        )
        return await self._aupdate_theme_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_theme(
        self,
        brand_id: str,
        theme_id: str,
        links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        background_image: typing.Optional[str] = None,
        email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = None,
        error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = None,
        primary_color_contrast_hex: typing.Optional[str] = None,
        primary_color_hex: typing.Optional[str] = None,
        secondary_color_contrast_hex: typing.Optional[str] = None,
        secondary_color_hex: typing.Optional[str] = None,
        sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_theme_mapped_args(
            body=body,
            brand_id=brand_id,
            theme_id=theme_id,
            links=links,
            background_image=background_image,
            email_template_touch_point_variant=email_template_touch_point_variant,
            end_user_dashboard_touch_point_variant=end_user_dashboard_touch_point_variant,
            error_page_touch_point_variant=error_page_touch_point_variant,
            primary_color_contrast_hex=primary_color_contrast_hex,
            primary_color_hex=primary_color_hex,
            secondary_color_contrast_hex=secondary_color_contrast_hex,
            secondary_color_hex=secondary_color_hex,
            sign_in_page_touch_point_variant=sign_in_page_touch_point_variant,
        )
        return self._update_theme_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateTheme(BaseApi):

    async def aupdate_theme(
        self,
        brand_id: str,
        theme_id: str,
        links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        background_image: typing.Optional[str] = None,
        email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = None,
        error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = None,
        primary_color_contrast_hex: typing.Optional[str] = None,
        primary_color_hex: typing.Optional[str] = None,
        secondary_color_contrast_hex: typing.Optional[str] = None,
        secondary_color_hex: typing.Optional[str] = None,
        sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = None,
        validate: bool = False,
        **kwargs,
    ) -> ThemeResponsePydantic:
        raw_response = await self.raw.aupdate_theme(
            body=body,
            brand_id=brand_id,
            theme_id=theme_id,
            links=links,
            background_image=background_image,
            email_template_touch_point_variant=email_template_touch_point_variant,
            end_user_dashboard_touch_point_variant=end_user_dashboard_touch_point_variant,
            error_page_touch_point_variant=error_page_touch_point_variant,
            primary_color_contrast_hex=primary_color_contrast_hex,
            primary_color_hex=primary_color_hex,
            secondary_color_contrast_hex=secondary_color_contrast_hex,
            secondary_color_hex=secondary_color_hex,
            sign_in_page_touch_point_variant=sign_in_page_touch_point_variant,
            **kwargs,
        )
        if validate:
            return ThemeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ThemeResponsePydantic, raw_response.body)
    
    
    def update_theme(
        self,
        brand_id: str,
        theme_id: str,
        links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        background_image: typing.Optional[str] = None,
        email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = None,
        error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = None,
        primary_color_contrast_hex: typing.Optional[str] = None,
        primary_color_hex: typing.Optional[str] = None,
        secondary_color_contrast_hex: typing.Optional[str] = None,
        secondary_color_hex: typing.Optional[str] = None,
        sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = None,
        validate: bool = False,
    ) -> ThemeResponsePydantic:
        raw_response = self.raw.update_theme(
            body=body,
            brand_id=brand_id,
            theme_id=theme_id,
            links=links,
            background_image=background_image,
            email_template_touch_point_variant=email_template_touch_point_variant,
            end_user_dashboard_touch_point_variant=end_user_dashboard_touch_point_variant,
            error_page_touch_point_variant=error_page_touch_point_variant,
            primary_color_contrast_hex=primary_color_contrast_hex,
            primary_color_hex=primary_color_hex,
            secondary_color_contrast_hex=secondary_color_contrast_hex,
            secondary_color_hex=secondary_color_hex,
            sign_in_page_touch_point_variant=sign_in_page_touch_point_variant,
        )
        if validate:
            return ThemeResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ThemeResponsePydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        brand_id: str,
        theme_id: str,
        links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        background_image: typing.Optional[str] = None,
        email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = None,
        error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = None,
        primary_color_contrast_hex: typing.Optional[str] = None,
        primary_color_hex: typing.Optional[str] = None,
        secondary_color_contrast_hex: typing.Optional[str] = None,
        secondary_color_hex: typing.Optional[str] = None,
        sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_theme_mapped_args(
            body=body,
            brand_id=brand_id,
            theme_id=theme_id,
            links=links,
            background_image=background_image,
            email_template_touch_point_variant=email_template_touch_point_variant,
            end_user_dashboard_touch_point_variant=end_user_dashboard_touch_point_variant,
            error_page_touch_point_variant=error_page_touch_point_variant,
            primary_color_contrast_hex=primary_color_contrast_hex,
            primary_color_hex=primary_color_hex,
            secondary_color_contrast_hex=secondary_color_contrast_hex,
            secondary_color_hex=secondary_color_hex,
            sign_in_page_touch_point_variant=sign_in_page_touch_point_variant,
        )
        return await self._aupdate_theme_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        brand_id: str,
        theme_id: str,
        links: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        background_image: typing.Optional[str] = None,
        email_template_touch_point_variant: typing.Optional[EmailTemplateTouchPointVariant] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[EndUserDashboardTouchPointVariant] = None,
        error_page_touch_point_variant: typing.Optional[ErrorPageTouchPointVariant] = None,
        primary_color_contrast_hex: typing.Optional[str] = None,
        primary_color_hex: typing.Optional[str] = None,
        secondary_color_contrast_hex: typing.Optional[str] = None,
        secondary_color_hex: typing.Optional[str] = None,
        sign_in_page_touch_point_variant: typing.Optional[SignInPageTouchPointVariant] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_theme_mapped_args(
            body=body,
            brand_id=brand_id,
            theme_id=theme_id,
            links=links,
            background_image=background_image,
            email_template_touch_point_variant=email_template_touch_point_variant,
            end_user_dashboard_touch_point_variant=end_user_dashboard_touch_point_variant,
            error_page_touch_point_variant=error_page_touch_point_variant,
            primary_color_contrast_hex=primary_color_contrast_hex,
            primary_color_hex=primary_color_hex,
            secondary_color_contrast_hex=secondary_color_contrast_hex,
            secondary_color_hex=secondary_color_hex,
            sign_in_page_touch_point_variant=sign_in_page_touch_point_variant,
        )
        return self._update_theme_oapg(
            body=args.body,
            path_params=args.path,
        )


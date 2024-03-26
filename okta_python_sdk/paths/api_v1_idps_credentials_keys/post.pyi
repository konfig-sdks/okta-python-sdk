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

from okta_python_sdk.model.json_web_key_key_ops import JsonWebKeyKeyOps as JsonWebKeyKeyOpsSchema
from okta_python_sdk.model.json_web_key_x5_c import JsonWebKeyX5C as JsonWebKeyX5CSchema
from okta_python_sdk.model.json_web_key_links import JsonWebKeyLinks as JsonWebKeyLinksSchema
from okta_python_sdk.model.json_web_key import JsonWebKey as JsonWebKeySchema

from okta_python_sdk.type.json_web_key_links import JsonWebKeyLinks
from okta_python_sdk.type.json_web_key_x5_c import JsonWebKeyX5C
from okta_python_sdk.type.json_web_key_key_ops import JsonWebKeyKeyOps
from okta_python_sdk.type.json_web_key import JsonWebKey

from ...api_client import Dictionary
from okta_python_sdk.pydantic.json_web_key_key_ops import JsonWebKeyKeyOps as JsonWebKeyKeyOpsPydantic
from okta_python_sdk.pydantic.json_web_key import JsonWebKey as JsonWebKeyPydantic
from okta_python_sdk.pydantic.json_web_key_links import JsonWebKeyLinks as JsonWebKeyLinksPydantic
from okta_python_sdk.pydantic.json_web_key_x5_c import JsonWebKeyX5C as JsonWebKeyX5CPydantic

# body param
SchemaForRequestBodyApplicationJson = JsonWebKeySchema


request_body_json_web_key = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = JsonWebKeySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: JsonWebKey


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: JsonWebKey


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

    def _add_x509_certificate_public_key_mapped_args(
        self,
        links: typing.Optional[JsonWebKeyLinks] = None,
        alg: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        e: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        key_ops: typing.Optional[JsonWebKeyKeyOps] = None,
        kid: typing.Optional[str] = None,
        kty: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        n: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        use: typing.Optional[str] = None,
        x5c: typing.Optional[JsonWebKeyX5C] = None,
        x5t: typing.Optional[str] = None,
        x5t_s256: typing.Optional[str] = None,
        x5u: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if links is not None:
            _body["_links"] = links
        if alg is not None:
            _body["alg"] = alg
        if created is not None:
            _body["created"] = created
        if e is not None:
            _body["e"] = e
        if expires_at is not None:
            _body["expiresAt"] = expires_at
        if key_ops is not None:
            _body["key_ops"] = key_ops
        if kid is not None:
            _body["kid"] = kid
        if kty is not None:
            _body["kty"] = kty
        if last_updated is not None:
            _body["lastUpdated"] = last_updated
        if n is not None:
            _body["n"] = n
        if status is not None:
            _body["status"] = status
        if use is not None:
            _body["use"] = use
        if x5c is not None:
            _body["x5c"] = x5c
        if x5t is not None:
            _body["x5t"] = x5t
        if x5t_s256 is not None:
            _body["x5t#S256"] = x5t_s256
        if x5u is not None:
            _body["x5u"] = x5u
        args.body = _body
        return args

    async def _aadd_x509_certificate_public_key_oapg(
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
        Add X.509 Certificate Public Key
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
            path_template='/api/v1/idps/credentials/keys',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_json_web_key.serialize(body, content_type)
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


    def _add_x509_certificate_public_key_oapg(
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
        Add X.509 Certificate Public Key
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
            path_template='/api/v1/idps/credentials/keys',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_json_web_key.serialize(body, content_type)
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


class AddX509CertificatePublicKeyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_x509_certificate_public_key(
        self,
        links: typing.Optional[JsonWebKeyLinks] = None,
        alg: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        e: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        key_ops: typing.Optional[JsonWebKeyKeyOps] = None,
        kid: typing.Optional[str] = None,
        kty: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        n: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        use: typing.Optional[str] = None,
        x5c: typing.Optional[JsonWebKeyX5C] = None,
        x5t: typing.Optional[str] = None,
        x5t_s256: typing.Optional[str] = None,
        x5u: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_x509_certificate_public_key_mapped_args(
            links=links,
            alg=alg,
            created=created,
            e=e,
            expires_at=expires_at,
            key_ops=key_ops,
            kid=kid,
            kty=kty,
            last_updated=last_updated,
            n=n,
            status=status,
            use=use,
            x5c=x5c,
            x5t=x5t,
            x5t_s256=x5t_s256,
            x5u=x5u,
        )
        return await self._aadd_x509_certificate_public_key_oapg(
            body=args.body,
            **kwargs,
        )
    
    def add_x509_certificate_public_key(
        self,
        links: typing.Optional[JsonWebKeyLinks] = None,
        alg: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        e: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        key_ops: typing.Optional[JsonWebKeyKeyOps] = None,
        kid: typing.Optional[str] = None,
        kty: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        n: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        use: typing.Optional[str] = None,
        x5c: typing.Optional[JsonWebKeyX5C] = None,
        x5t: typing.Optional[str] = None,
        x5t_s256: typing.Optional[str] = None,
        x5u: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_x509_certificate_public_key_mapped_args(
            links=links,
            alg=alg,
            created=created,
            e=e,
            expires_at=expires_at,
            key_ops=key_ops,
            kid=kid,
            kty=kty,
            last_updated=last_updated,
            n=n,
            status=status,
            use=use,
            x5c=x5c,
            x5t=x5t,
            x5t_s256=x5t_s256,
            x5u=x5u,
        )
        return self._add_x509_certificate_public_key_oapg(
            body=args.body,
        )

class AddX509CertificatePublicKey(BaseApi):

    async def aadd_x509_certificate_public_key(
        self,
        links: typing.Optional[JsonWebKeyLinks] = None,
        alg: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        e: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        key_ops: typing.Optional[JsonWebKeyKeyOps] = None,
        kid: typing.Optional[str] = None,
        kty: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        n: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        use: typing.Optional[str] = None,
        x5c: typing.Optional[JsonWebKeyX5C] = None,
        x5t: typing.Optional[str] = None,
        x5t_s256: typing.Optional[str] = None,
        x5u: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> JsonWebKeyPydantic:
        raw_response = await self.raw.aadd_x509_certificate_public_key(
            links=links,
            alg=alg,
            created=created,
            e=e,
            expires_at=expires_at,
            key_ops=key_ops,
            kid=kid,
            kty=kty,
            last_updated=last_updated,
            n=n,
            status=status,
            use=use,
            x5c=x5c,
            x5t=x5t,
            x5t_s256=x5t_s256,
            x5u=x5u,
            **kwargs,
        )
        if validate:
            return JsonWebKeyPydantic(**raw_response.body)
        return api_client.construct_model_instance(JsonWebKeyPydantic, raw_response.body)
    
    
    def add_x509_certificate_public_key(
        self,
        links: typing.Optional[JsonWebKeyLinks] = None,
        alg: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        e: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        key_ops: typing.Optional[JsonWebKeyKeyOps] = None,
        kid: typing.Optional[str] = None,
        kty: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        n: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        use: typing.Optional[str] = None,
        x5c: typing.Optional[JsonWebKeyX5C] = None,
        x5t: typing.Optional[str] = None,
        x5t_s256: typing.Optional[str] = None,
        x5u: typing.Optional[str] = None,
        validate: bool = False,
    ) -> JsonWebKeyPydantic:
        raw_response = self.raw.add_x509_certificate_public_key(
            links=links,
            alg=alg,
            created=created,
            e=e,
            expires_at=expires_at,
            key_ops=key_ops,
            kid=kid,
            kty=kty,
            last_updated=last_updated,
            n=n,
            status=status,
            use=use,
            x5c=x5c,
            x5t=x5t,
            x5t_s256=x5t_s256,
            x5u=x5u,
        )
        if validate:
            return JsonWebKeyPydantic(**raw_response.body)
        return api_client.construct_model_instance(JsonWebKeyPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        links: typing.Optional[JsonWebKeyLinks] = None,
        alg: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        e: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        key_ops: typing.Optional[JsonWebKeyKeyOps] = None,
        kid: typing.Optional[str] = None,
        kty: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        n: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        use: typing.Optional[str] = None,
        x5c: typing.Optional[JsonWebKeyX5C] = None,
        x5t: typing.Optional[str] = None,
        x5t_s256: typing.Optional[str] = None,
        x5u: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_x509_certificate_public_key_mapped_args(
            links=links,
            alg=alg,
            created=created,
            e=e,
            expires_at=expires_at,
            key_ops=key_ops,
            kid=kid,
            kty=kty,
            last_updated=last_updated,
            n=n,
            status=status,
            use=use,
            x5c=x5c,
            x5t=x5t,
            x5t_s256=x5t_s256,
            x5u=x5u,
        )
        return await self._aadd_x509_certificate_public_key_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        links: typing.Optional[JsonWebKeyLinks] = None,
        alg: typing.Optional[str] = None,
        created: typing.Optional[datetime] = None,
        e: typing.Optional[str] = None,
        expires_at: typing.Optional[datetime] = None,
        key_ops: typing.Optional[JsonWebKeyKeyOps] = None,
        kid: typing.Optional[str] = None,
        kty: typing.Optional[str] = None,
        last_updated: typing.Optional[datetime] = None,
        n: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        use: typing.Optional[str] = None,
        x5c: typing.Optional[JsonWebKeyX5C] = None,
        x5t: typing.Optional[str] = None,
        x5t_s256: typing.Optional[str] = None,
        x5u: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_x509_certificate_public_key_mapped_args(
            links=links,
            alg=alg,
            created=created,
            e=e,
            expires_at=expires_at,
            key_ops=key_ops,
            kid=kid,
            kty=kty,
            last_updated=last_updated,
            n=n,
            status=status,
            use=use,
            x5c=x5c,
            x5t=x5t,
            x5t_s256=x5t_s256,
            x5u=x5u,
        )
        return self._add_x509_certificate_public_key_oapg(
            body=args.body,
        )


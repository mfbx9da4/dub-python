"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from dub._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext
from dub.models import errors
import dub.utils as utils
from dub.utils import RetryConfig, SerializedRequestBody
import httpx
from typing import Callable, List, Optional, Tuple

class BaseSDK:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config

    def get_url(self, base_url, url_variables):
        sdk_url, sdk_variables = self.sdk_configuration.get_server_details()

        if base_url is None:
            base_url = sdk_url

        if url_variables is None:
            url_variables = sdk_variables

        return utils.template_url(base_url, url_variables)

    def build_request(
        self,
        method,
        path,
        base_url,
        url_variables,
        request,
        request_body_required,
        request_has_path_params,
        request_has_query_params,
        user_agent_header,
        accept_header_value,
        _globals=None,
        security=None,
        get_serialized_body: Optional[
            Callable[[], Optional[SerializedRequestBody]]
        ] = None,
        url_override: Optional[str] = None,
    ) -> httpx.Request:
        client = self.sdk_configuration.client

        query_params = {}

        url = url_override
        if url is None:
            url = utils.generate_url(
                self.get_url(base_url, url_variables),
                path,
                request if request_has_path_params else None,
                _globals if request_has_path_params else None,
            )

            query_params = utils.get_query_params(
                request if request_has_query_params else None,
                _globals if request_has_query_params else None,
            )

        headers = utils.get_headers(request, _globals)
        headers["Accept"] = accept_header_value
        headers[user_agent_header] = self.sdk_configuration.user_agent

        if security is not None:
            if callable(security):
                security = security()

            security_headers, security_query_params = utils.get_security(security)
            headers = {**headers, **security_headers}
            query_params = {**query_params, **security_query_params}

        serialized_request_body = SerializedRequestBody("application/octet-stream")
        if get_serialized_body is not None:
            rb = get_serialized_body()
            if request_body_required and rb is None:
                raise ValueError("request body is required")

            if rb is not None:
                serialized_request_body = rb

        if (
            serialized_request_body.media_type is not None
            and serialized_request_body.media_type
            not in (
                "multipart/form-data",
                "multipart/mixed",
            )
        ):
            headers["content-type"] = serialized_request_body.media_type

        return client.build_request(
            method,
            url,
            params=query_params,
            content=serialized_request_body.content,
            data=serialized_request_body.data,
            files=serialized_request_body.files,
            headers=headers,
        )

    def do_request(
        self,
        hook_ctx,
        request,
        error_status_codes,
        retry_config: Optional[Tuple[RetryConfig, List[str]]] = None,
    ) -> httpx.Response:
        client = self.sdk_configuration.client

        def do():
            http_res = None
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    BeforeRequestContext(hook_ctx), request
                )
                http_res = client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), None, e
                )
                if e is not None:
                    raise e

            if http_res is None:
                raise errors.SDKError("No response received")

            if utils.match_status_codes(error_status_codes, http_res.status_code):
                result, e = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), http_res, None
                )
                if e is not None:
                    raise e
                if result is not None:
                    http_res = result
                else:
                    raise errors.SDKError("Unexpected error occurred")

            return http_res

        if retry_config is not None:
            http_res = utils.retry(do, utils.Retries(retry_config[0], retry_config[1]))
        else:
            http_res = do()

        if not utils.match_status_codes(error_status_codes, http_res.status_code):
            http_res = self.sdk_configuration.get_hooks().after_success(
                AfterSuccessContext(hook_ctx), http_res
            )

        return http_res

    async def do_request_async(
        self,
        hook_ctx,
        request,
        error_status_codes,
        retry_config: Optional[Tuple[RetryConfig, List[str]]] = None,
    ) -> httpx.Response:
        client = self.sdk_configuration.async_client

        async def do():
            http_res = None
            try:
                req = self.sdk_configuration.get_hooks().before_request(
                    BeforeRequestContext(hook_ctx), request
                )
                http_res = await client.send(req)
            except Exception as e:
                _, e = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), None, e
                )
                if e is not None:
                    raise e

            if http_res is None:
                raise errors.SDKError("No response received")

            if utils.match_status_codes(error_status_codes, http_res.status_code):
                result, e = self.sdk_configuration.get_hooks().after_error(
                    AfterErrorContext(hook_ctx), http_res, None
                )
                if e is not None:
                    raise e
                if result is not None:
                    http_res = result
                else:
                    raise errors.SDKError("Unexpected error occurred")

            return http_res

        if retry_config is not None:
            http_res = await utils.retry_async(
                do, utils.Retries(retry_config[0], retry_config[1])
            )
        else:
            http_res = await do()

        if not utils.match_status_codes(error_status_codes, http_res.status_code):
            http_res = self.sdk_configuration.get_hooks().after_success(
                AfterSuccessContext(hook_ctx), http_res
            )

        return http_res

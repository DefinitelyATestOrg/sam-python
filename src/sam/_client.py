# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import models, complete, sam_plop_plop, models_beta_true, messages_beta_true
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import SamError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.messages import messages

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Sam", "AsyncSam", "Client", "AsyncClient"]


class Sam(SyncAPIClient):
    messages: messages.MessagesResource
    complete: complete.CompleteResource
    models: models.ModelsResource
    messages_beta_true: messages_beta_true.MessagesBetaTrueResource
    models_beta_true: models_beta_true.ModelsBetaTrueResource
    sam_plop_plop: sam_plop_plop.SamPlopPlopResource
    with_raw_response: SamWithRawResponse
    with_streaming_response: SamWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Sam client instance.

        This automatically infers the `api_key` argument from the `API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise SamError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SAM_BASE_URL")
        if base_url is None:
            base_url = f"/api/v3"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.messages = messages.MessagesResource(self)
        self.complete = complete.CompleteResource(self)
        self.models = models.ModelsResource(self)
        self.messages_beta_true = messages_beta_true.MessagesBetaTrueResource(self)
        self.models_beta_true = models_beta_true.ModelsBetaTrueResource(self)
        self.sam_plop_plop = sam_plop_plop.SamPlopPlopResource(self)
        self.with_raw_response = SamWithRawResponse(self)
        self.with_streaming_response = SamWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSam(AsyncAPIClient):
    messages: messages.AsyncMessagesResource
    complete: complete.AsyncCompleteResource
    models: models.AsyncModelsResource
    messages_beta_true: messages_beta_true.AsyncMessagesBetaTrueResource
    models_beta_true: models_beta_true.AsyncModelsBetaTrueResource
    sam_plop_plop: sam_plop_plop.AsyncSamPlopPlopResource
    with_raw_response: AsyncSamWithRawResponse
    with_streaming_response: AsyncSamWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSam client instance.

        This automatically infers the `api_key` argument from the `API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise SamError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SAM_BASE_URL")
        if base_url is None:
            base_url = f"/api/v3"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.messages = messages.AsyncMessagesResource(self)
        self.complete = complete.AsyncCompleteResource(self)
        self.models = models.AsyncModelsResource(self)
        self.messages_beta_true = messages_beta_true.AsyncMessagesBetaTrueResource(self)
        self.models_beta_true = models_beta_true.AsyncModelsBetaTrueResource(self)
        self.sam_plop_plop = sam_plop_plop.AsyncSamPlopPlopResource(self)
        self.with_raw_response = AsyncSamWithRawResponse(self)
        self.with_streaming_response = AsyncSamWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SamWithRawResponse:
    def __init__(self, client: Sam) -> None:
        self.messages = messages.MessagesResourceWithRawResponse(client.messages)
        self.complete = complete.CompleteResourceWithRawResponse(client.complete)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.messages_beta_true = messages_beta_true.MessagesBetaTrueResourceWithRawResponse(client.messages_beta_true)
        self.models_beta_true = models_beta_true.ModelsBetaTrueResourceWithRawResponse(client.models_beta_true)
        self.sam_plop_plop = sam_plop_plop.SamPlopPlopResourceWithRawResponse(client.sam_plop_plop)


class AsyncSamWithRawResponse:
    def __init__(self, client: AsyncSam) -> None:
        self.messages = messages.AsyncMessagesResourceWithRawResponse(client.messages)
        self.complete = complete.AsyncCompleteResourceWithRawResponse(client.complete)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.messages_beta_true = messages_beta_true.AsyncMessagesBetaTrueResourceWithRawResponse(
            client.messages_beta_true
        )
        self.models_beta_true = models_beta_true.AsyncModelsBetaTrueResourceWithRawResponse(client.models_beta_true)
        self.sam_plop_plop = sam_plop_plop.AsyncSamPlopPlopResourceWithRawResponse(client.sam_plop_plop)


class SamWithStreamedResponse:
    def __init__(self, client: Sam) -> None:
        self.messages = messages.MessagesResourceWithStreamingResponse(client.messages)
        self.complete = complete.CompleteResourceWithStreamingResponse(client.complete)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.messages_beta_true = messages_beta_true.MessagesBetaTrueResourceWithStreamingResponse(
            client.messages_beta_true
        )
        self.models_beta_true = models_beta_true.ModelsBetaTrueResourceWithStreamingResponse(client.models_beta_true)
        self.sam_plop_plop = sam_plop_plop.SamPlopPlopResourceWithStreamingResponse(client.sam_plop_plop)


class AsyncSamWithStreamedResponse:
    def __init__(self, client: AsyncSam) -> None:
        self.messages = messages.AsyncMessagesResourceWithStreamingResponse(client.messages)
        self.complete = complete.AsyncCompleteResourceWithStreamingResponse(client.complete)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.messages_beta_true = messages_beta_true.AsyncMessagesBetaTrueResourceWithStreamingResponse(
            client.messages_beta_true
        )
        self.models_beta_true = models_beta_true.AsyncModelsBetaTrueResourceWithStreamingResponse(
            client.models_beta_true
        )
        self.sam_plop_plop = sam_plop_plop.AsyncSamPlopPlopResourceWithStreamingResponse(client.sam_plop_plop)


Client = Sam

AsyncClient = AsyncSam

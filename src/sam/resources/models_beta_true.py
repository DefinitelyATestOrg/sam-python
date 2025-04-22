# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import models_beta_true_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.models_beta_true_list_response import ModelsBetaTrueListResponse

__all__ = ["ModelsBetaTrueResource", "AsyncModelsBetaTrueResource"]


class ModelsBetaTrueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelsBetaTrueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return ModelsBetaTrueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsBetaTrueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return ModelsBetaTrueResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelsBetaTrueListResponse:
        """
        List available models.

        The Models API response can be used to determine which models are available for
        use in the API. More recently released models are listed first.

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/v1/models?beta=true",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "limit": limit,
                    },
                    models_beta_true_list_params.ModelsBetaTrueListParams,
                ),
            ),
            cast_to=ModelsBetaTrueListResponse,
        )


class AsyncModelsBetaTrueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelsBetaTrueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsBetaTrueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsBetaTrueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return AsyncModelsBetaTrueResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelsBetaTrueListResponse:
        """
        List available models.

        The Models API response can be used to determine which models are available for
        use in the API. More recently released models are listed first.

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/v1/models?beta=true",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after_id": after_id,
                        "before_id": before_id,
                        "limit": limit,
                    },
                    models_beta_true_list_params.ModelsBetaTrueListParams,
                ),
            ),
            cast_to=ModelsBetaTrueListResponse,
        )


class ModelsBetaTrueResourceWithRawResponse:
    def __init__(self, models_beta_true: ModelsBetaTrueResource) -> None:
        self._models_beta_true = models_beta_true

        self.list = to_raw_response_wrapper(
            models_beta_true.list,
        )


class AsyncModelsBetaTrueResourceWithRawResponse:
    def __init__(self, models_beta_true: AsyncModelsBetaTrueResource) -> None:
        self._models_beta_true = models_beta_true

        self.list = async_to_raw_response_wrapper(
            models_beta_true.list,
        )


class ModelsBetaTrueResourceWithStreamingResponse:
    def __init__(self, models_beta_true: ModelsBetaTrueResource) -> None:
        self._models_beta_true = models_beta_true

        self.list = to_streamed_response_wrapper(
            models_beta_true.list,
        )


class AsyncModelsBetaTrueResourceWithStreamingResponse:
    def __init__(self, models_beta_true: AsyncModelsBetaTrueResource) -> None:
        self._models_beta_true = models_beta_true

        self.list = async_to_streamed_response_wrapper(
            models_beta_true.list,
        )

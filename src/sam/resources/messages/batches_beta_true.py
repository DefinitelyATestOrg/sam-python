# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.messages import batches_beta_true_list_params, batches_beta_true_create_params
from ...types.messages.batches_beta_true_list_response import BatchesBetaTrueListResponse
from ...types.messages.batches_beta_true_create_response import BatchesBetaTrueCreateResponse

__all__ = ["BatchesBetaTrueResource", "AsyncBatchesBetaTrueResource"]


class BatchesBetaTrueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchesBetaTrueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return BatchesBetaTrueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchesBetaTrueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return BatchesBetaTrueResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        requests: Iterable[batches_beta_true_create_params.Request],
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchesBetaTrueCreateResponse:
        """
        Send a batch of Message creation requests.

        The Message Batches API can be used to process multiple Messages API requests at
        once. Once a Message Batch is created, it begins processing immediately. Batches
        can take up to 24 hours to complete.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          requests: List of requests for prompt completion. Each is an individual request to create
              a Message.

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

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
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/messages/batches?beta=true",
            body=maybe_transform({"requests": requests}, batches_beta_true_create_params.BatchesBetaTrueCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchesBetaTrueCreateResponse,
        )

    def list(
        self,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchesBetaTrueListResponse:
        """List all Message Batches within a Workspace.

        Most recently created batches are
        returned first.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

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
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/v1/messages/batches?beta=true",
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
                    batches_beta_true_list_params.BatchesBetaTrueListParams,
                ),
            ),
            cast_to=BatchesBetaTrueListResponse,
        )


class AsyncBatchesBetaTrueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchesBetaTrueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchesBetaTrueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchesBetaTrueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return AsyncBatchesBetaTrueResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        requests: Iterable[batches_beta_true_create_params.Request],
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchesBetaTrueCreateResponse:
        """
        Send a batch of Message creation requests.

        The Message Batches API can be used to process multiple Messages API requests at
        once. Once a Message Batch is created, it begins processing immediately. Batches
        can take up to 24 hours to complete.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          requests: List of requests for prompt completion. Each is an individual request to create
              a Message.

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

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
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/messages/batches?beta=true",
            body=await async_maybe_transform(
                {"requests": requests}, batches_beta_true_create_params.BatchesBetaTrueCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchesBetaTrueCreateResponse,
        )

    async def list(
        self,
        *,
        after_id: str | NotGiven = NOT_GIVEN,
        before_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchesBetaTrueListResponse:
        """List all Message Batches within a Workspace.

        Most recently created batches are
        returned first.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          after_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately after this object.

          before_id: ID of the object to use as a cursor for pagination. When provided, returns the
              page of results immediately before this object.

          limit: Number of items to return per page.

              Defaults to `20`. Ranges from `1` to `1000`.

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

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
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/v1/messages/batches?beta=true",
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
                    batches_beta_true_list_params.BatchesBetaTrueListParams,
                ),
            ),
            cast_to=BatchesBetaTrueListResponse,
        )


class BatchesBetaTrueResourceWithRawResponse:
    def __init__(self, batches_beta_true: BatchesBetaTrueResource) -> None:
        self._batches_beta_true = batches_beta_true

        self.create = to_raw_response_wrapper(
            batches_beta_true.create,
        )
        self.list = to_raw_response_wrapper(
            batches_beta_true.list,
        )


class AsyncBatchesBetaTrueResourceWithRawResponse:
    def __init__(self, batches_beta_true: AsyncBatchesBetaTrueResource) -> None:
        self._batches_beta_true = batches_beta_true

        self.create = async_to_raw_response_wrapper(
            batches_beta_true.create,
        )
        self.list = async_to_raw_response_wrapper(
            batches_beta_true.list,
        )


class BatchesBetaTrueResourceWithStreamingResponse:
    def __init__(self, batches_beta_true: BatchesBetaTrueResource) -> None:
        self._batches_beta_true = batches_beta_true

        self.create = to_streamed_response_wrapper(
            batches_beta_true.create,
        )
        self.list = to_streamed_response_wrapper(
            batches_beta_true.list,
        )


class AsyncBatchesBetaTrueResourceWithStreamingResponse:
    def __init__(self, batches_beta_true: AsyncBatchesBetaTrueResource) -> None:
        self._batches_beta_true = batches_beta_true

        self.create = async_to_streamed_response_wrapper(
            batches_beta_true.create,
        )
        self.list = async_to_streamed_response_wrapper(
            batches_beta_true.list,
        )

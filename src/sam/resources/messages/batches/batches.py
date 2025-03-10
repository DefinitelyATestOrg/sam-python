# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .beta_true import (
    BetaTrueResource,
    AsyncBetaTrueResource,
    BetaTrueResourceWithRawResponse,
    AsyncBetaTrueResourceWithRawResponse,
    BetaTrueResourceWithStreamingResponse,
    AsyncBetaTrueResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.messages import batch_list_params, batch_create_params
from ...._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ....types.messages.batch_list_response import BatchListResponse
from ....types.messages.batch_cancel_response import BatchCancelResponse
from ....types.messages.batch_create_response import BatchCreateResponse
from ....types.messages.batch_delete_response import BatchDeleteResponse
from ....types.messages.batch_results_response import BatchResultsResponse
from ....types.messages.batch_retrieve_response import BatchRetrieveResponse
from ....types.messages.batch_cancel_beta_response import BatchCancelBetaResponse
from ....types.messages.batch_results_beta_response import BatchResultsBetaResponse

__all__ = ["BatchesResource", "AsyncBatchesResource"]


class BatchesResource(SyncAPIResource):
    @cached_property
    def beta_true(self) -> BetaTrueResource:
        return BetaTrueResource(self._client)

    @cached_property
    def with_raw_response(self) -> BatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return BatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return BatchesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        requests: Iterable[batch_create_params.Request],
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCreateResponse:
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
            "/v1/messages/batches",
            body=maybe_transform({"requests": requests}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCreateResponse,
        )

    def retrieve(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchRetrieveResponse:
        """This endpoint is idempotent and can be used to poll for Message Batch
        completion.

        To access the results of a Message Batch, make a request to the
        `results_url` field in the response.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
            f"/v1/messages/batches/{message_batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchRetrieveResponse,
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
    ) -> BatchListResponse:
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
            "/v1/messages/batches",
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
                    batch_list_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )

    def delete(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchDeleteResponse:
        """
        Delete a Message Batch.

        Message Batches can only be deleted once they've finished processing. If you'd
        like to delete an in-progress batch, you must first cancel it.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
        return self._delete(
            f"/v1/messages/batches/{message_batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
        )

    def cancel(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCancelResponse:
        """Batches may be canceled any time before processing ends.

        Once cancellation is
        initiated, the batch enters a `canceling` state, at which time the system may
        complete any in-progress, non-interruptible requests before finalizing
        cancellation.

        The number of canceled requests is specified in `request_counts`. To determine
        which requests were canceled, check the individual results within the batch.
        Note that cancellation may not result in any canceled requests if they were
        non-interruptible.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
            f"/v1/messages/batches/{message_batch_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCancelResponse,
        )

    def cancel_beta(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCancelBetaResponse:
        """Batches may be canceled any time before processing ends.

        Once cancellation is
        initiated, the batch enters a `canceling` state, at which time the system may
        complete any in-progress, non-interruptible requests before finalizing
        cancellation.

        The number of canceled requests is specified in `request_counts`. To determine
        which requests were canceled, check the individual results within the batch.
        Note that cancellation may not result in any canceled requests if they were
        non-interruptible.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
            f"/v1/messages/batches/{message_batch_id}/cancel?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCancelBetaResponse,
        )

    def results(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JSONLDecoder[BatchResultsResponse]:
        """
        Streams the results of a Message Batch as a `.jsonl` file.

        Each line in the file is a JSON object containing the result of a single request
        in the Message Batch. Results are not guaranteed to be in the same order as
        requests. Use the `custom_id` field to match results to requests.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
        extra_headers = {"Accept": "application/x-jsonl", **(extra_headers or {})}
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
            f"/v1/messages/batches/{message_batch_id}/results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[BatchResultsResponse],
            stream=True,
        )

    def results_beta(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JSONLDecoder[BatchResultsBetaResponse]:
        """
        Streams the results of a Message Batch as a `.jsonl` file.

        Each line in the file is a JSON object containing the result of a single request
        in the Message Batch. Results are not guaranteed to be in the same order as
        requests. Use the `custom_id` field to match results to requests.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
        extra_headers = {"Accept": "application/x-jsonl", **(extra_headers or {})}
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
            f"/v1/messages/batches/{message_batch_id}/results?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[BatchResultsBetaResponse],
            stream=True,
        )


class AsyncBatchesResource(AsyncAPIResource):
    @cached_property
    def beta_true(self) -> AsyncBetaTrueResource:
        return AsyncBetaTrueResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return AsyncBatchesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        requests: Iterable[batch_create_params.Request],
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCreateResponse:
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
            "/v1/messages/batches",
            body=await async_maybe_transform({"requests": requests}, batch_create_params.BatchCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCreateResponse,
        )

    async def retrieve(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchRetrieveResponse:
        """This endpoint is idempotent and can be used to poll for Message Batch
        completion.

        To access the results of a Message Batch, make a request to the
        `results_url` field in the response.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
            f"/v1/messages/batches/{message_batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchRetrieveResponse,
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
    ) -> BatchListResponse:
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
            "/v1/messages/batches",
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
                    batch_list_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )

    async def delete(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchDeleteResponse:
        """
        Delete a Message Batch.

        Message Batches can only be deleted once they've finished processing. If you'd
        like to delete an in-progress batch, you must first cancel it.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
        return await self._delete(
            f"/v1/messages/batches/{message_batch_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
        )

    async def cancel(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCancelResponse:
        """Batches may be canceled any time before processing ends.

        Once cancellation is
        initiated, the batch enters a `canceling` state, at which time the system may
        complete any in-progress, non-interruptible requests before finalizing
        cancellation.

        The number of canceled requests is specified in `request_counts`. To determine
        which requests were canceled, check the individual results within the batch.
        Note that cancellation may not result in any canceled requests if they were
        non-interruptible.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
            f"/v1/messages/batches/{message_batch_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCancelResponse,
        )

    async def cancel_beta(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCancelBetaResponse:
        """Batches may be canceled any time before processing ends.

        Once cancellation is
        initiated, the batch enters a `canceling` state, at which time the system may
        complete any in-progress, non-interruptible requests before finalizing
        cancellation.

        The number of canceled requests is specified in `request_counts`. To determine
        which requests were canceled, check the individual results within the batch.
        Note that cancellation may not result in any canceled requests if they were
        non-interruptible.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
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
            f"/v1/messages/batches/{message_batch_id}/cancel?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCancelBetaResponse,
        )

    async def results(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncJSONLDecoder[BatchResultsResponse]:
        """
        Streams the results of a Message Batch as a `.jsonl` file.

        Each line in the file is a JSON object containing the result of a single request
        in the Message Batch. Results are not guaranteed to be in the same order as
        requests. Use the `custom_id` field to match results to requests.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
        extra_headers = {"Accept": "application/x-jsonl", **(extra_headers or {})}
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
            f"/v1/messages/batches/{message_batch_id}/results",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[BatchResultsResponse],
            stream=True,
        )

    async def results_beta(
        self,
        message_batch_id: str,
        *,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncJSONLDecoder[BatchResultsBetaResponse]:
        """
        Streams the results of a Message Batch as a `.jsonl` file.

        Each line in the file is a JSON object containing the result of a single request
        in the Message Batch. Results are not guaranteed to be in the same order as
        requests. Use the `custom_id` field to match results to requests.

        Learn more about the Message Batches API in our
        [user guide](/en/docs/build-with-claude/batch-processing)

        Args:
          message_batch_id: ID of the Message Batch.

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
        if not message_batch_id:
            raise ValueError(f"Expected a non-empty value for `message_batch_id` but received {message_batch_id!r}")
        extra_headers = {"Accept": "application/x-jsonl", **(extra_headers or {})}
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
            f"/v1/messages/batches/{message_batch_id}/results?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[BatchResultsBetaResponse],
            stream=True,
        )


class BatchesResourceWithRawResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.create = to_raw_response_wrapper(
            batches.create,
        )
        self.retrieve = to_raw_response_wrapper(
            batches.retrieve,
        )
        self.list = to_raw_response_wrapper(
            batches.list,
        )
        self.delete = to_raw_response_wrapper(
            batches.delete,
        )
        self.cancel = to_raw_response_wrapper(
            batches.cancel,
        )
        self.cancel_beta = to_raw_response_wrapper(
            batches.cancel_beta,
        )
        self.results = to_raw_response_wrapper(
            batches.results,
        )
        self.results_beta = to_raw_response_wrapper(
            batches.results_beta,
        )

    @cached_property
    def beta_true(self) -> BetaTrueResourceWithRawResponse:
        return BetaTrueResourceWithRawResponse(self._batches.beta_true)


class AsyncBatchesResourceWithRawResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.create = async_to_raw_response_wrapper(
            batches.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            batches.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            batches.list,
        )
        self.delete = async_to_raw_response_wrapper(
            batches.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            batches.cancel,
        )
        self.cancel_beta = async_to_raw_response_wrapper(
            batches.cancel_beta,
        )
        self.results = async_to_raw_response_wrapper(
            batches.results,
        )
        self.results_beta = async_to_raw_response_wrapper(
            batches.results_beta,
        )

    @cached_property
    def beta_true(self) -> AsyncBetaTrueResourceWithRawResponse:
        return AsyncBetaTrueResourceWithRawResponse(self._batches.beta_true)


class BatchesResourceWithStreamingResponse:
    def __init__(self, batches: BatchesResource) -> None:
        self._batches = batches

        self.create = to_streamed_response_wrapper(
            batches.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            batches.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            batches.list,
        )
        self.delete = to_streamed_response_wrapper(
            batches.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            batches.cancel,
        )
        self.cancel_beta = to_streamed_response_wrapper(
            batches.cancel_beta,
        )
        self.results = to_streamed_response_wrapper(
            batches.results,
        )
        self.results_beta = to_streamed_response_wrapper(
            batches.results_beta,
        )

    @cached_property
    def beta_true(self) -> BetaTrueResourceWithStreamingResponse:
        return BetaTrueResourceWithStreamingResponse(self._batches.beta_true)


class AsyncBatchesResourceWithStreamingResponse:
    def __init__(self, batches: AsyncBatchesResource) -> None:
        self._batches = batches

        self.create = async_to_streamed_response_wrapper(
            batches.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            batches.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            batches.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            batches.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            batches.cancel,
        )
        self.cancel_beta = async_to_streamed_response_wrapper(
            batches.cancel_beta,
        )
        self.results = async_to_streamed_response_wrapper(
            batches.results,
        )
        self.results_beta = async_to_streamed_response_wrapper(
            batches.results_beta,
        )

    @cached_property
    def beta_true(self) -> AsyncBetaTrueResourceWithStreamingResponse:
        return AsyncBetaTrueResourceWithStreamingResponse(self._batches.beta_true)

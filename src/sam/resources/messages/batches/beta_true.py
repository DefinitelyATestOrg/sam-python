# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import is_given, strip_not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.messages.batches.beta_true_delete_response import BetaTrueDeleteResponse
from ....types.messages.batches.beta_true_retrieve_response import BetaTrueRetrieveResponse

__all__ = ["BetaTrueResource", "AsyncBetaTrueResource"]


class BetaTrueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BetaTrueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return BetaTrueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaTrueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return BetaTrueResourceWithStreamingResponse(self)

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
    ) -> BetaTrueRetrieveResponse:
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
            f"/v1/messages/batches/{message_batch_id}?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaTrueRetrieveResponse,
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
    ) -> BetaTrueDeleteResponse:
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
            f"/v1/messages/batches/{message_batch_id}?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaTrueDeleteResponse,
        )


class AsyncBetaTrueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBetaTrueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaTrueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaTrueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return AsyncBetaTrueResourceWithStreamingResponse(self)

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
    ) -> BetaTrueRetrieveResponse:
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
            f"/v1/messages/batches/{message_batch_id}?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaTrueRetrieveResponse,
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
    ) -> BetaTrueDeleteResponse:
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
            f"/v1/messages/batches/{message_batch_id}?beta=true",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BetaTrueDeleteResponse,
        )


class BetaTrueResourceWithRawResponse:
    def __init__(self, beta_true: BetaTrueResource) -> None:
        self._beta_true = beta_true

        self.retrieve = to_raw_response_wrapper(
            beta_true.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            beta_true.delete,
        )


class AsyncBetaTrueResourceWithRawResponse:
    def __init__(self, beta_true: AsyncBetaTrueResource) -> None:
        self._beta_true = beta_true

        self.retrieve = async_to_raw_response_wrapper(
            beta_true.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            beta_true.delete,
        )


class BetaTrueResourceWithStreamingResponse:
    def __init__(self, beta_true: BetaTrueResource) -> None:
        self._beta_true = beta_true

        self.retrieve = to_streamed_response_wrapper(
            beta_true.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            beta_true.delete,
        )


class AsyncBetaTrueResourceWithStreamingResponse:
    def __init__(self, beta_true: AsyncBetaTrueResource) -> None:
        self._beta_true = beta_true

        self.retrieve = async_to_streamed_response_wrapper(
            beta_true.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            beta_true.delete,
        )

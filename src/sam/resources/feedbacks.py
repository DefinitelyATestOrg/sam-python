# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import feedback_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["FeedbacksResource", "AsyncFeedbacksResource"]


class FeedbacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedbacksResourceWithRawResponse:
        return FeedbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbacksResourceWithStreamingResponse:
        return FeedbacksResourceWithStreamingResponse(self)

    def update(
        self,
        feedback_id: str,
        *,
        agent_id: str,
        ticket_message_id: str,
        id: str | NotGiven = NOT_GIVEN,
        created_by: feedback_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["THUMBS_UP", "THUMBS_DOWN", "INSERT"] | NotGiven = NOT_GIVEN,
        updated_by: feedback_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feedback_id:
            raise ValueError(f"Expected a non-empty value for `feedback_id` but received {feedback_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v1/feedbacks/{feedback_id}",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "ticket_message_id": ticket_message_id,
                    "id": id,
                    "created_by": created_by,
                    "text": text,
                    "type": type,
                    "updated_by": updated_by,
                },
                feedback_update_params.FeedbackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncFeedbacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedbacksResourceWithRawResponse:
        return AsyncFeedbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbacksResourceWithStreamingResponse:
        return AsyncFeedbacksResourceWithStreamingResponse(self)

    async def update(
        self,
        feedback_id: str,
        *,
        agent_id: str,
        ticket_message_id: str,
        id: str | NotGiven = NOT_GIVEN,
        created_by: feedback_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        type: Literal["THUMBS_UP", "THUMBS_DOWN", "INSERT"] | NotGiven = NOT_GIVEN,
        updated_by: feedback_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not feedback_id:
            raise ValueError(f"Expected a non-empty value for `feedback_id` but received {feedback_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v1/feedbacks/{feedback_id}",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "ticket_message_id": ticket_message_id,
                    "id": id,
                    "created_by": created_by,
                    "text": text,
                    "type": type,
                    "updated_by": updated_by,
                },
                feedback_update_params.FeedbackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class FeedbacksResourceWithRawResponse:
    def __init__(self, feedbacks: FeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.update = to_custom_raw_response_wrapper(
            feedbacks.update,
            BinaryAPIResponse,
        )


class AsyncFeedbacksResourceWithRawResponse:
    def __init__(self, feedbacks: AsyncFeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.update = async_to_custom_raw_response_wrapper(
            feedbacks.update,
            AsyncBinaryAPIResponse,
        )


class FeedbacksResourceWithStreamingResponse:
    def __init__(self, feedbacks: FeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.update = to_custom_streamed_response_wrapper(
            feedbacks.update,
            StreamedBinaryAPIResponse,
        )


class AsyncFeedbacksResourceWithStreamingResponse:
    def __init__(self, feedbacks: AsyncFeedbacksResource) -> None:
        self._feedbacks = feedbacks

        self.update = async_to_custom_streamed_response_wrapper(
            feedbacks.update,
            AsyncStreamedBinaryAPIResponse,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.agents import hidden_tag_update_params

__all__ = ["HiddenTags", "AsyncHiddenTags"]


class HiddenTags(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HiddenTagsWithRawResponse:
        return HiddenTagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HiddenTagsWithStreamingResponse:
        return HiddenTagsWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        body: List[str],
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v1/agents/{id}/hiddenTags",
            body=maybe_transform(body, hidden_tag_update_params.HiddenTagUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncHiddenTags(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHiddenTagsWithRawResponse:
        return AsyncHiddenTagsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHiddenTagsWithStreamingResponse:
        return AsyncHiddenTagsWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        body: List[str],
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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v1/agents/{id}/hiddenTags",
            body=await async_maybe_transform(body, hidden_tag_update_params.HiddenTagUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class HiddenTagsWithRawResponse:
    def __init__(self, hidden_tags: HiddenTags) -> None:
        self._hidden_tags = hidden_tags

        self.update = to_custom_raw_response_wrapper(
            hidden_tags.update,
            BinaryAPIResponse,
        )


class AsyncHiddenTagsWithRawResponse:
    def __init__(self, hidden_tags: AsyncHiddenTags) -> None:
        self._hidden_tags = hidden_tags

        self.update = async_to_custom_raw_response_wrapper(
            hidden_tags.update,
            AsyncBinaryAPIResponse,
        )


class HiddenTagsWithStreamingResponse:
    def __init__(self, hidden_tags: HiddenTags) -> None:
        self._hidden_tags = hidden_tags

        self.update = to_custom_streamed_response_wrapper(
            hidden_tags.update,
            StreamedBinaryAPIResponse,
        )


class AsyncHiddenTagsWithStreamingResponse:
    def __init__(self, hidden_tags: AsyncHiddenTags) -> None:
        self._hidden_tags = hidden_tags

        self.update = async_to_custom_streamed_response_wrapper(
            hidden_tags.update,
            AsyncStreamedBinaryAPIResponse,
        )

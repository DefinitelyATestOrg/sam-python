# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import action_set_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["ActionSets", "AsyncActionSets"]


class ActionSets(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionSetsWithRawResponse:
        return ActionSetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionSetsWithStreamingResponse:
        return ActionSetsWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
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
        return self._get(
            f"/api/v1/actionsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        *,
        path_id: str,
        name: str,
        body_id: str | NotGiven = NOT_GIVEN,
        agent_id: str | NotGiven = NOT_GIVEN,
        created_by: action_set_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        open_api_url: str | NotGiven = NOT_GIVEN,
        server_url: str | NotGiven = NOT_GIVEN,
        type: Literal["OPEN_API", "MANUAL"] | NotGiven = NOT_GIVEN,
        updated_by: action_set_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
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
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v1/actionsets/{path_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "id": body_id,
                    "agent_id": agent_id,
                    "created_by": created_by,
                    "open_api_url": open_api_url,
                    "server_url": server_url,
                    "type": type,
                    "updated_by": updated_by,
                },
                action_set_update_params.ActionSetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        return self._delete(
            f"/api/v1/actionsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncActionSets(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionSetsWithRawResponse:
        return AsyncActionSetsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionSetsWithStreamingResponse:
        return AsyncActionSetsWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
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
        return await self._get(
            f"/api/v1/actionsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        *,
        path_id: str,
        name: str,
        body_id: str | NotGiven = NOT_GIVEN,
        agent_id: str | NotGiven = NOT_GIVEN,
        created_by: action_set_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        open_api_url: str | NotGiven = NOT_GIVEN,
        server_url: str | NotGiven = NOT_GIVEN,
        type: Literal["OPEN_API", "MANUAL"] | NotGiven = NOT_GIVEN,
        updated_by: action_set_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
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
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v1/actionsets/{path_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "id": body_id,
                    "agent_id": agent_id,
                    "created_by": created_by,
                    "open_api_url": open_api_url,
                    "server_url": server_url,
                    "type": type,
                    "updated_by": updated_by,
                },
                action_set_update_params.ActionSetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
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
        return await self._delete(
            f"/api/v1/actionsets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ActionSetsWithRawResponse:
    def __init__(self, action_sets: ActionSets) -> None:
        self._action_sets = action_sets

        self.retrieve = to_custom_raw_response_wrapper(
            action_sets.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            action_sets.update,
            BinaryAPIResponse,
        )
        self.delete = to_raw_response_wrapper(
            action_sets.delete,
        )


class AsyncActionSetsWithRawResponse:
    def __init__(self, action_sets: AsyncActionSets) -> None:
        self._action_sets = action_sets

        self.retrieve = async_to_custom_raw_response_wrapper(
            action_sets.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            action_sets.update,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_raw_response_wrapper(
            action_sets.delete,
        )


class ActionSetsWithStreamingResponse:
    def __init__(self, action_sets: ActionSets) -> None:
        self._action_sets = action_sets

        self.retrieve = to_custom_streamed_response_wrapper(
            action_sets.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            action_sets.update,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_streamed_response_wrapper(
            action_sets.delete,
        )


class AsyncActionSetsWithStreamingResponse:
    def __init__(self, action_sets: AsyncActionSets) -> None:
        self._action_sets = action_sets

        self.retrieve = async_to_custom_streamed_response_wrapper(
            action_sets.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            action_sets.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_streamed_response_wrapper(
            action_sets.delete,
        )

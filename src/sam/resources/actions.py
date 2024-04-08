# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import action_update_params
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

__all__ = ["Actions", "AsyncActions"]


class Actions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsWithRawResponse:
        return ActionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsWithStreamingResponse:
        return ActionsWithStreamingResponse(self)

    def retrieve(
        self,
        action_id: str,
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
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        action_id: str,
        *,
        action_set_id: str | NotGiven = NOT_GIVEN,
        agent_id: str | NotGiven = NOT_GIVEN,
        created_by: action_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST", "PUT", "DELETE"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[action_update_params.Parameter] | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        request_body_type: Literal["JSON"] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE", "UNSUPPORTED"] | NotGiven = NOT_GIVEN,
        updated_by: action_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
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
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v1/actions/{action_id}",
            body=maybe_transform(
                {
                    "action_set_id": action_set_id,
                    "agent_id": agent_id,
                    "created_by": created_by,
                    "description": description,
                    "error_message": error_message,
                    "method": method,
                    "name": name,
                    "parameters": parameters,
                    "path": path,
                    "request_body_type": request_body_type,
                    "status": status,
                    "updated_by": updated_by,
                },
                action_update_params.ActionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncActions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsWithRawResponse:
        return AsyncActionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsWithStreamingResponse:
        return AsyncActionsWithStreamingResponse(self)

    async def retrieve(
        self,
        action_id: str,
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
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/actions/{action_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        action_id: str,
        *,
        action_set_id: str | NotGiven = NOT_GIVEN,
        agent_id: str | NotGiven = NOT_GIVEN,
        created_by: action_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        error_message: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST", "PUT", "DELETE"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        parameters: Iterable[action_update_params.Parameter] | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        request_body_type: Literal["JSON"] | NotGiven = NOT_GIVEN,
        status: Literal["ACTIVE", "INACTIVE", "UNSUPPORTED"] | NotGiven = NOT_GIVEN,
        updated_by: action_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
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
        if not action_id:
            raise ValueError(f"Expected a non-empty value for `action_id` but received {action_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v1/actions/{action_id}",
            body=await async_maybe_transform(
                {
                    "action_set_id": action_set_id,
                    "agent_id": agent_id,
                    "created_by": created_by,
                    "description": description,
                    "error_message": error_message,
                    "method": method,
                    "name": name,
                    "parameters": parameters,
                    "path": path,
                    "request_body_type": request_body_type,
                    "status": status,
                    "updated_by": updated_by,
                },
                action_update_params.ActionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ActionsWithRawResponse:
    def __init__(self, actions: Actions) -> None:
        self._actions = actions

        self.retrieve = to_custom_raw_response_wrapper(
            actions.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            actions.update,
            BinaryAPIResponse,
        )


class AsyncActionsWithRawResponse:
    def __init__(self, actions: AsyncActions) -> None:
        self._actions = actions

        self.retrieve = async_to_custom_raw_response_wrapper(
            actions.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            actions.update,
            AsyncBinaryAPIResponse,
        )


class ActionsWithStreamingResponse:
    def __init__(self, actions: Actions) -> None:
        self._actions = actions

        self.retrieve = to_custom_streamed_response_wrapper(
            actions.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            actions.update,
            StreamedBinaryAPIResponse,
        )


class AsyncActionsWithStreamingResponse:
    def __init__(self, actions: AsyncActions) -> None:
        self._actions = actions

        self.retrieve = async_to_custom_streamed_response_wrapper(
            actions.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            actions.update,
            AsyncStreamedBinaryAPIResponse,
        )

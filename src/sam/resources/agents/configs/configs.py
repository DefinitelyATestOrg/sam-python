# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .chat import (
    Chat,
    AsyncChat,
    ChatWithRawResponse,
    AsyncChatWithRawResponse,
    ChatWithStreamingResponse,
    AsyncChatWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.agents import config_update_params

__all__ = ["Configs", "AsyncConfigs"]


class Configs(SyncAPIResource):
    @cached_property
    def chat(self) -> Chat:
        return Chat(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self)

    def retrieve(
        self,
        integration: Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"],
        *,
        agent_id: str,
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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not integration:
            raise ValueError(f"Expected a non-empty value for `integration` but received {integration!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/agents/{agent_id}/configs/{integration}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        integration: Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"],
        *,
        agent_id: str,
        class_: str,
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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not integration:
            raise ValueError(f"Expected a non-empty value for `integration` but received {integration!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v1/agents/{agent_id}/configs/{integration}",
            body=maybe_transform({"class_": class_}, config_update_params.ConfigUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncConfigs(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChat:
        return AsyncChat(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self)

    async def retrieve(
        self,
        integration: Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"],
        *,
        agent_id: str,
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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not integration:
            raise ValueError(f"Expected a non-empty value for `integration` but received {integration!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/agents/{agent_id}/configs/{integration}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        integration: Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"],
        *,
        agent_id: str,
        class_: str,
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
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not integration:
            raise ValueError(f"Expected a non-empty value for `integration` but received {integration!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v1/agents/{agent_id}/configs/{integration}",
            body=await async_maybe_transform({"class_": class_}, config_update_params.ConfigUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ConfigsWithRawResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.retrieve = to_custom_raw_response_wrapper(
            configs.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            configs.update,
            BinaryAPIResponse,
        )

    @cached_property
    def chat(self) -> ChatWithRawResponse:
        return ChatWithRawResponse(self._configs.chat)


class AsyncConfigsWithRawResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.retrieve = async_to_custom_raw_response_wrapper(
            configs.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            configs.update,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def chat(self) -> AsyncChatWithRawResponse:
        return AsyncChatWithRawResponse(self._configs.chat)


class ConfigsWithStreamingResponse:
    def __init__(self, configs: Configs) -> None:
        self._configs = configs

        self.retrieve = to_custom_streamed_response_wrapper(
            configs.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            configs.update,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def chat(self) -> ChatWithStreamingResponse:
        return ChatWithStreamingResponse(self._configs.chat)


class AsyncConfigsWithStreamingResponse:
    def __init__(self, configs: AsyncConfigs) -> None:
        self._configs = configs

        self.retrieve = async_to_custom_streamed_response_wrapper(
            configs.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            configs.update,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def chat(self) -> AsyncChatWithStreamingResponse:
        return AsyncChatWithStreamingResponse(self._configs.chat)

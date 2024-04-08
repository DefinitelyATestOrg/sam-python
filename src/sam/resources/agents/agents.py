# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import agent_update_params
from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
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
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from .configs.configs import Configs, AsyncConfigs

__all__ = ["Agents", "AsyncAgents"]


class Agents(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsWithRawResponse:
        return AgentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsWithStreamingResponse:
        return AgentsWithStreamingResponse(self)

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
            f"/api/v1/agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        id: str,
        *,
        agent: agent_update_params.Agent,
        chat_icon: FileTypes | NotGiven = NOT_GIVEN,
        chat_icon_deleted: bool | NotGiven = NOT_GIVEN,
        logo: FileTypes | NotGiven = NOT_GIVEN,
        logo_deleted: bool | NotGiven = NOT_GIVEN,
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
            f"/api/v1/agents/{id}",
            body=maybe_transform(
                {
                    "agent": agent,
                    "chat_icon": chat_icon,
                    "chat_icon_deleted": chat_icon_deleted,
                    "logo": logo,
                    "logo_deleted": logo_deleted,
                },
                agent_update_params.AgentUpdateParams,
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
            f"/api/v1/agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAgents(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsWithRawResponse:
        return AsyncAgentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsWithStreamingResponse:
        return AsyncAgentsWithStreamingResponse(self)

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
            f"/api/v1/agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        id: str,
        *,
        agent: agent_update_params.Agent,
        chat_icon: FileTypes | NotGiven = NOT_GIVEN,
        chat_icon_deleted: bool | NotGiven = NOT_GIVEN,
        logo: FileTypes | NotGiven = NOT_GIVEN,
        logo_deleted: bool | NotGiven = NOT_GIVEN,
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
            f"/api/v1/agents/{id}",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "chat_icon": chat_icon,
                    "chat_icon_deleted": chat_icon_deleted,
                    "logo": logo,
                    "logo_deleted": logo_deleted,
                },
                agent_update_params.AgentUpdateParams,
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
            f"/api/v1/agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AgentsWithRawResponse:
    def __init__(self, agents: Agents) -> None:
        self._agents = agents

        self.retrieve = to_custom_raw_response_wrapper(
            agents.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            agents.update,
            BinaryAPIResponse,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._agents.configs)


class AsyncAgentsWithRawResponse:
    def __init__(self, agents: AsyncAgents) -> None:
        self._agents = agents

        self.retrieve = async_to_custom_raw_response_wrapper(
            agents.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            agents.update,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._agents.configs)


class AgentsWithStreamingResponse:
    def __init__(self, agents: Agents) -> None:
        self._agents = agents

        self.retrieve = to_custom_streamed_response_wrapper(
            agents.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            agents.update,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._agents.configs)


class AsyncAgentsWithStreamingResponse:
    def __init__(self, agents: AsyncAgents) -> None:
        self._agents = agents

        self.retrieve = async_to_custom_streamed_response_wrapper(
            agents.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            agents.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._agents.configs)

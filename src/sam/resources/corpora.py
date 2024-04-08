# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import corpora_update_params
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

__all__ = ["Corpora", "AsyncCorpora"]


class Corpora(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CorporaWithRawResponse:
        return CorporaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CorporaWithStreamingResponse:
        return CorporaWithStreamingResponse(self)

    def retrieve(
        self,
        corpus_id: str,
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
        if not corpus_id:
            raise ValueError(f"Expected a non-empty value for `corpus_id` but received {corpus_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/v1/corpora/{corpus_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def update(
        self,
        corpus_id: str,
        *,
        agent_id: str,
        name: str,
        active: bool | NotGiven = NOT_GIVEN,
        crawl_spec: corpora_update_params.CrawlSpec | NotGiven = NOT_GIVEN,
        created_by: corpora_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        exclude_last_updated_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        html_transformer: Literal["NONE", "EXTRACTUS", "READABLE_TEXT", "READABLE_TEXT_IF_POSSIBLE"]
        | NotGiven = NOT_GIVEN,
        included_kb_article_ids: List[str] | NotGiven = NOT_GIVEN,
        integration: Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"] | NotGiven = NOT_GIVEN,
        integration_category_id: str | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        status: Literal["PROCESSING", "READY", "FAILED"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: Literal[
            "URL", "MANUAL", "FILE_UPLOAD", "EXTERNAL_INTEGRATION", "FRESHDESK_KB", "ZENDESK_KB", "CSV", "UNKNOWN"
        ]
        | NotGiven = NOT_GIVEN,
        updated_by: corpora_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
        url_exclusion_patterns: List[str] | NotGiven = NOT_GIVEN,
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
        if not corpus_id:
            raise ValueError(f"Expected a non-empty value for `corpus_id` but received {corpus_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/api/v1/corpora/{corpus_id}",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "name": name,
                    "active": active,
                    "crawl_spec": crawl_spec,
                    "created_by": created_by,
                    "exclude_last_updated_before": exclude_last_updated_before,
                    "html_transformer": html_transformer,
                    "included_kb_article_ids": included_kb_article_ids,
                    "integration": integration,
                    "integration_category_id": integration_category_id,
                    "source_url": source_url,
                    "status": status,
                    "tags": tags,
                    "type": type,
                    "updated_by": updated_by,
                    "url_exclusion_patterns": url_exclusion_patterns,
                },
                corpora_update_params.CorporaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def delete(
        self,
        corpus_id: str,
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
        if not corpus_id:
            raise ValueError(f"Expected a non-empty value for `corpus_id` but received {corpus_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/api/v1/corpora/{corpus_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCorpora(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCorporaWithRawResponse:
        return AsyncCorporaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCorporaWithStreamingResponse:
        return AsyncCorporaWithStreamingResponse(self)

    async def retrieve(
        self,
        corpus_id: str,
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
        if not corpus_id:
            raise ValueError(f"Expected a non-empty value for `corpus_id` but received {corpus_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/v1/corpora/{corpus_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def update(
        self,
        corpus_id: str,
        *,
        agent_id: str,
        name: str,
        active: bool | NotGiven = NOT_GIVEN,
        crawl_spec: corpora_update_params.CrawlSpec | NotGiven = NOT_GIVEN,
        created_by: corpora_update_params.CreatedBy | NotGiven = NOT_GIVEN,
        exclude_last_updated_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        html_transformer: Literal["NONE", "EXTRACTUS", "READABLE_TEXT", "READABLE_TEXT_IF_POSSIBLE"]
        | NotGiven = NOT_GIVEN,
        included_kb_article_ids: List[str] | NotGiven = NOT_GIVEN,
        integration: Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"] | NotGiven = NOT_GIVEN,
        integration_category_id: str | NotGiven = NOT_GIVEN,
        source_url: str | NotGiven = NOT_GIVEN,
        status: Literal["PROCESSING", "READY", "FAILED"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: Literal[
            "URL", "MANUAL", "FILE_UPLOAD", "EXTERNAL_INTEGRATION", "FRESHDESK_KB", "ZENDESK_KB", "CSV", "UNKNOWN"
        ]
        | NotGiven = NOT_GIVEN,
        updated_by: corpora_update_params.UpdatedBy | NotGiven = NOT_GIVEN,
        url_exclusion_patterns: List[str] | NotGiven = NOT_GIVEN,
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
        if not corpus_id:
            raise ValueError(f"Expected a non-empty value for `corpus_id` but received {corpus_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/api/v1/corpora/{corpus_id}",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "name": name,
                    "active": active,
                    "crawl_spec": crawl_spec,
                    "created_by": created_by,
                    "exclude_last_updated_before": exclude_last_updated_before,
                    "html_transformer": html_transformer,
                    "included_kb_article_ids": included_kb_article_ids,
                    "integration": integration,
                    "integration_category_id": integration_category_id,
                    "source_url": source_url,
                    "status": status,
                    "tags": tags,
                    "type": type,
                    "updated_by": updated_by,
                    "url_exclusion_patterns": url_exclusion_patterns,
                },
                corpora_update_params.CorporaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def delete(
        self,
        corpus_id: str,
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
        if not corpus_id:
            raise ValueError(f"Expected a non-empty value for `corpus_id` but received {corpus_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/api/v1/corpora/{corpus_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CorporaWithRawResponse:
    def __init__(self, corpora: Corpora) -> None:
        self._corpora = corpora

        self.retrieve = to_custom_raw_response_wrapper(
            corpora.retrieve,
            BinaryAPIResponse,
        )
        self.update = to_custom_raw_response_wrapper(
            corpora.update,
            BinaryAPIResponse,
        )
        self.delete = to_raw_response_wrapper(
            corpora.delete,
        )


class AsyncCorporaWithRawResponse:
    def __init__(self, corpora: AsyncCorpora) -> None:
        self._corpora = corpora

        self.retrieve = async_to_custom_raw_response_wrapper(
            corpora.retrieve,
            AsyncBinaryAPIResponse,
        )
        self.update = async_to_custom_raw_response_wrapper(
            corpora.update,
            AsyncBinaryAPIResponse,
        )
        self.delete = async_to_raw_response_wrapper(
            corpora.delete,
        )


class CorporaWithStreamingResponse:
    def __init__(self, corpora: Corpora) -> None:
        self._corpora = corpora

        self.retrieve = to_custom_streamed_response_wrapper(
            corpora.retrieve,
            StreamedBinaryAPIResponse,
        )
        self.update = to_custom_streamed_response_wrapper(
            corpora.update,
            StreamedBinaryAPIResponse,
        )
        self.delete = to_streamed_response_wrapper(
            corpora.delete,
        )


class AsyncCorporaWithStreamingResponse:
    def __init__(self, corpora: AsyncCorpora) -> None:
        self._corpora = corpora

        self.retrieve = async_to_custom_streamed_response_wrapper(
            corpora.retrieve,
            AsyncStreamedBinaryAPIResponse,
        )
        self.update = async_to_custom_streamed_response_wrapper(
            corpora.update,
            AsyncStreamedBinaryAPIResponse,
        )
        self.delete = async_to_streamed_response_wrapper(
            corpora.delete,
        )

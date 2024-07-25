# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["StoreResource", "AsyncStoreResource"]


class StoreResource(SyncAPIResource):
    @cached_property
    def orders(self) -> OrdersResource:
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> StoreResourceWithRawResponse:
        return StoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoreResourceWithStreamingResponse:
        return StoreResourceWithStreamingResponse(self)


class AsyncStoreResource(AsyncAPIResource):
    @cached_property
    def orders(self) -> AsyncOrdersResource:
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStoreResourceWithRawResponse:
        return AsyncStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoreResourceWithStreamingResponse:
        return AsyncStoreResourceWithStreamingResponse(self)


class StoreResourceWithRawResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self._store.orders)


class AsyncStoreResourceWithRawResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self._store.orders)


class StoreResourceWithStreamingResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self._store.orders)


class AsyncStoreResourceWithStreamingResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self._store.orders)

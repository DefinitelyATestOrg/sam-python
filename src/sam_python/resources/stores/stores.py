# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import store_create_order_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.order import Order
from ...types.store_inventory_response import StoreInventoryResponse

__all__ = ["StoresResource", "AsyncStoresResource"]


class StoresResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StoresResourceWithRawResponse:
        return StoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoresResourceWithStreamingResponse:
        return StoresResourceWithStreamingResponse(self)

    def retrieve(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10.

        Other values will
        generate exceptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    def delete(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """For valid response try integer IDs with value < 1000.

        Anything above 1000 or
        nonintegers will generate API errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_order(
        self,
        *,
        id: int | NotGiven = NOT_GIVEN,
        complete: bool | NotGiven = NOT_GIVEN,
        pet_id: int | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        ship_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["placed", "approved", "delivered"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """
        Place a new order in the store

        Args:
          status: Order Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/store/order",
            body=maybe_transform(
                {
                    "id": id,
                    "complete": complete,
                    "pet_id": pet_id,
                    "quantity": quantity,
                    "ship_date": ship_date,
                    "status": status,
                },
                store_create_order_params.StoreCreateOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    def inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StoreInventoryResponse:
        """Returns a map of status codes to quantities"""
        return self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreInventoryResponse,
        )


class AsyncStoresResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStoresResourceWithRawResponse:
        return AsyncStoresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoresResourceWithStreamingResponse:
        return AsyncStoresResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10.

        Other values will
        generate exceptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    async def delete(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """For valid response try integer IDs with value < 1000.

        Anything above 1000 or
        nonintegers will generate API errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_order(
        self,
        *,
        id: int | NotGiven = NOT_GIVEN,
        complete: bool | NotGiven = NOT_GIVEN,
        pet_id: int | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        ship_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["placed", "approved", "delivered"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """
        Place a new order in the store

        Args:
          status: Order Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/store/order",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "complete": complete,
                    "pet_id": pet_id,
                    "quantity": quantity,
                    "ship_date": ship_date,
                    "status": status,
                },
                store_create_order_params.StoreCreateOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    async def inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StoreInventoryResponse:
        """Returns a map of status codes to quantities"""
        return await self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreInventoryResponse,
        )


class StoresResourceWithRawResponse:
    def __init__(self, stores: StoresResource) -> None:
        self._stores = stores

        self.retrieve = to_raw_response_wrapper(
            stores.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            stores.delete,
        )
        self.create_order = to_raw_response_wrapper(
            stores.create_order,
        )
        self.inventory = to_raw_response_wrapper(
            stores.inventory,
        )


class AsyncStoresResourceWithRawResponse:
    def __init__(self, stores: AsyncStoresResource) -> None:
        self._stores = stores

        self.retrieve = async_to_raw_response_wrapper(
            stores.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            stores.delete,
        )
        self.create_order = async_to_raw_response_wrapper(
            stores.create_order,
        )
        self.inventory = async_to_raw_response_wrapper(
            stores.inventory,
        )


class StoresResourceWithStreamingResponse:
    def __init__(self, stores: StoresResource) -> None:
        self._stores = stores

        self.retrieve = to_streamed_response_wrapper(
            stores.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            stores.delete,
        )
        self.create_order = to_streamed_response_wrapper(
            stores.create_order,
        )
        self.inventory = to_streamed_response_wrapper(
            stores.inventory,
        )


class AsyncStoresResourceWithStreamingResponse:
    def __init__(self, stores: AsyncStoresResource) -> None:
        self._stores = stores

        self.retrieve = async_to_streamed_response_wrapper(
            stores.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            stores.delete,
        )
        self.create_order = async_to_streamed_response_wrapper(
            stores.create_order,
        )
        self.inventory = async_to_streamed_response_wrapper(
            stores.inventory,
        )

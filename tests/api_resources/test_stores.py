# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam_python import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam_python.types import StoreInventoryResponse
from sam_python._utils import parse_datetime
from sam_python.types.shared import Order

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStores:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sam) -> None:
        store = client.stores.retrieve(
            0,
        )
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sam) -> None:
        response = client.stores.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = response.parse()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sam) -> None:
        with client.stores.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = response.parse()
            assert_matches_type(Order, store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        store = client.stores.delete(
            0,
        )
        assert store is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.stores.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = response.parse()
        assert store is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.stores.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = response.parse()
            assert store is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_order(self, client: Sam) -> None:
        store = client.stores.create_order()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_method_create_order_with_all_params(self, client: Sam) -> None:
        store = client.stores.create_order(
            id=10,
            complete=True,
            pet_id=198772,
            quantity=7,
            ship_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="approved",
        )
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_raw_response_create_order(self, client: Sam) -> None:
        response = client.stores.with_raw_response.create_order()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = response.parse()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_streaming_response_create_order(self, client: Sam) -> None:
        with client.stores.with_streaming_response.create_order() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = response.parse()
            assert_matches_type(Order, store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_inventory(self, client: Sam) -> None:
        store = client.stores.inventory()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    def test_raw_response_inventory(self, client: Sam) -> None:
        response = client.stores.with_raw_response.inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = response.parse()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    def test_streaming_response_inventory(self, client: Sam) -> None:
        with client.stores.with_streaming_response.inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = response.parse()
            assert_matches_type(StoreInventoryResponse, store, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStores:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSam) -> None:
        store = await async_client.stores.retrieve(
            0,
        )
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSam) -> None:
        response = await async_client.stores.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = await response.parse()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSam) -> None:
        async with async_client.stores.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = await response.parse()
            assert_matches_type(Order, store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        store = await async_client.stores.delete(
            0,
        )
        assert store is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.stores.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = await response.parse()
        assert store is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.stores.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = await response.parse()
            assert store is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_order(self, async_client: AsyncSam) -> None:
        store = await async_client.stores.create_order()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_method_create_order_with_all_params(self, async_client: AsyncSam) -> None:
        store = await async_client.stores.create_order(
            id=10,
            complete=True,
            pet_id=198772,
            quantity=7,
            ship_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="approved",
        )
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_raw_response_create_order(self, async_client: AsyncSam) -> None:
        response = await async_client.stores.with_raw_response.create_order()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = await response.parse()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_streaming_response_create_order(self, async_client: AsyncSam) -> None:
        async with async_client.stores.with_streaming_response.create_order() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = await response.parse()
            assert_matches_type(Order, store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_inventory(self, async_client: AsyncSam) -> None:
        store = await async_client.stores.inventory()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    async def test_raw_response_inventory(self, async_client: AsyncSam) -> None:
        response = await async_client.stores.with_raw_response.inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = await response.parse()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    async def test_streaming_response_inventory(self, async_client: AsyncSam) -> None:
        async with async_client.stores.with_streaming_response.inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = await response.parse()
            assert_matches_type(StoreInventoryResponse, store, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam_python import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from sam_python.types import PhysicalCard

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhysicalCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_shipment_advance(self, client: Increase) -> None:
        physical_card = client.simulations.physical_cards.shipment_advance(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            shipment_status="shipped",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_raw_response_shipment_advance(self, client: Increase) -> None:
        response = client.simulations.physical_cards.with_raw_response.shipment_advance(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            shipment_status="shipped",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    def test_streaming_response_shipment_advance(self, client: Increase) -> None:
        with client.simulations.physical_cards.with_streaming_response.shipment_advance(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            shipment_status="shipped",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_shipment_advance(self, client: Increase) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            client.simulations.physical_cards.with_raw_response.shipment_advance(
                physical_card_id="",
                shipment_status="shipped",
            )


class TestAsyncPhysicalCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_shipment_advance(self, async_client: AsyncIncrease) -> None:
        physical_card = await async_client.simulations.physical_cards.shipment_advance(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            shipment_status="shipped",
        )
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_raw_response_shipment_advance(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.physical_cards.with_raw_response.shipment_advance(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            shipment_status="shipped",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        physical_card = response.parse()
        assert_matches_type(PhysicalCard, physical_card, path=["response"])

    @parametrize
    async def test_streaming_response_shipment_advance(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.physical_cards.with_streaming_response.shipment_advance(
            physical_card_id="physical_card_ode8duyq5v2ynhjoharl",
            shipment_status="shipped",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            physical_card = await response.parse()
            assert_matches_type(PhysicalCard, physical_card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_shipment_advance(self, async_client: AsyncIncrease) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `physical_card_id` but received ''"):
            await async_client.simulations.physical_cards.with_raw_response.shipment_advance(
                physical_card_id="",
                shipment_status="shipped",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam_python import Increase, AsyncIncrease
from tests.utils import assert_matches_type
from sam_python.types import InboundWireTransfer

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWireTransfers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_inbound(self, client: Increase) -> None:
        wire_transfer = client.simulations.wire_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_method_create_inbound_with_all_params(self, client: Increase) -> None:
        wire_transfer = client.simulations.wire_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
            beneficiary_name="x",
            beneficiary_reference="x",
            originator_address_line1="x",
            originator_address_line2="x",
            originator_address_line3="x",
            originator_name="x",
            originator_routing_number="x",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
        )
        assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_raw_response_create_inbound(self, client: Increase) -> None:
        response = client.simulations.wire_transfers.with_raw_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

    @parametrize
    def test_streaming_response_create_inbound(self, client: Increase) -> None:
        with client.simulations.wire_transfers.with_streaming_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_transfer = response.parse()
            assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWireTransfers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_inbound(self, async_client: AsyncIncrease) -> None:
        wire_transfer = await async_client.simulations.wire_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )
        assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_method_create_inbound_with_all_params(self, async_client: AsyncIncrease) -> None:
        wire_transfer = await async_client.simulations.wire_transfers.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
            beneficiary_address_line1="x",
            beneficiary_address_line2="x",
            beneficiary_address_line3="x",
            beneficiary_name="x",
            beneficiary_reference="x",
            originator_address_line1="x",
            originator_address_line2="x",
            originator_address_line3="x",
            originator_name="x",
            originator_routing_number="x",
            originator_to_beneficiary_information_line1="x",
            originator_to_beneficiary_information_line2="x",
            originator_to_beneficiary_information_line3="x",
            originator_to_beneficiary_information_line4="x",
        )
        assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_raw_response_create_inbound(self, async_client: AsyncIncrease) -> None:
        response = await async_client.simulations.wire_transfers.with_raw_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wire_transfer = response.parse()
        assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

    @parametrize
    async def test_streaming_response_create_inbound(self, async_client: AsyncIncrease) -> None:
        async with async_client.simulations.wire_transfers.with_streaming_response.create_inbound(
            account_number_id="account_number_v18nkfqm6afpsrvy82b2",
            amount=1000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wire_transfer = await response.parse()
            assert_matches_type(InboundWireTransfer, wire_transfer, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam.types.messages.batches import BetaTrueDeleteResponse, BetaTrueRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBetaTrue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sam) -> None:
        beta_true = client.messages.batches.beta_true.retrieve(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sam) -> None:
        beta_true = client.messages.batches.beta_true.retrieve(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sam) -> None:
        response = client.messages.batches.beta_true.with_raw_response.retrieve(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta_true = response.parse()
        assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sam) -> None:
        with client.messages.batches.beta_true.with_streaming_response.retrieve(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta_true = response.parse()
            assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.beta_true.with_raw_response.retrieve(
                message_batch_id="",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        beta_true = client.messages.batches.beta_true.delete(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Sam) -> None:
        beta_true = client.messages.batches.beta_true.delete(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.messages.batches.beta_true.with_raw_response.delete(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta_true = response.parse()
        assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.messages.batches.beta_true.with_streaming_response.delete(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta_true = response.parse()
            assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.beta_true.with_raw_response.delete(
                message_batch_id="",
            )


class TestAsyncBetaTrue:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSam) -> None:
        beta_true = await async_client.messages.batches.beta_true.retrieve(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSam) -> None:
        beta_true = await async_client.messages.batches.beta_true.retrieve(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.beta_true.with_raw_response.retrieve(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta_true = await response.parse()
        assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.beta_true.with_streaming_response.retrieve(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta_true = await response.parse()
            assert_matches_type(BetaTrueRetrieveResponse, beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.beta_true.with_raw_response.retrieve(
                message_batch_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        beta_true = await async_client.messages.batches.beta_true.delete(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSam) -> None:
        beta_true = await async_client.messages.batches.beta_true.delete(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.beta_true.with_raw_response.delete(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta_true = await response.parse()
        assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.beta_true.with_streaming_response.delete(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta_true = await response.parse()
            assert_matches_type(BetaTrueDeleteResponse, beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.beta_true.with_raw_response.delete(
                message_batch_id="",
            )

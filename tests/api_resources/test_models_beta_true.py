# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from sam.types import ModelsBetaTrueListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModelsBetaTrue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Sam) -> None:
        models_beta_true = client.models_beta_true.list()
        assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sam) -> None:
        models_beta_true = client.models_beta_true.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sam) -> None:
        response = client.models_beta_true.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_beta_true = response.parse()
        assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sam) -> None:
        with client.models_beta_true.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_beta_true = response.parse()
            assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModelsBetaTrue:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncSam) -> None:
        models_beta_true = await async_client.models_beta_true.list()
        assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSam) -> None:
        models_beta_true = await async_client.models_beta_true.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSam) -> None:
        response = await async_client.models_beta_true.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        models_beta_true = await response.parse()
        assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSam) -> None:
        async with async_client.models_beta_true.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            models_beta_true = await response.parse()
            assert_matches_type(ModelsBetaTrueListResponse, models_beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from sam.types import ModelListResponse, ModelRetrieveResponse, ModelRetrieveBetaResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sam) -> None:
        model = client.models.retrieve(
            model_id="model_id",
        )
        assert_matches_type(ModelRetrieveResponse, model, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sam) -> None:
        model = client.models.retrieve(
            model_id="model_id",
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelRetrieveResponse, model, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sam) -> None:
        response = client.models.with_raw_response.retrieve(
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelRetrieveResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sam) -> None:
        with client.models.with_streaming_response.retrieve(
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelRetrieveResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            client.models.with_raw_response.retrieve(
                model_id="",
            )

    @parametrize
    def test_method_list(self, client: Sam) -> None:
        model = client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sam) -> None:
        model = client.models.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sam) -> None:
        response = client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sam) -> None:
        with client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_beta(self, client: Sam) -> None:
        model = client.models.retrieve_beta(
            model_id="model_id",
        )
        assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

    @parametrize
    def test_method_retrieve_beta_with_all_params(self, client: Sam) -> None:
        model = client.models.retrieve_beta(
            model_id="model_id",
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

    @parametrize
    def test_raw_response_retrieve_beta(self, client: Sam) -> None:
        response = client.models.with_raw_response.retrieve_beta(
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_beta(self, client: Sam) -> None:
        with client.models.with_streaming_response.retrieve_beta(
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_beta(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            client.models.with_raw_response.retrieve_beta(
                model_id="",
            )


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSam) -> None:
        model = await async_client.models.retrieve(
            model_id="model_id",
        )
        assert_matches_type(ModelRetrieveResponse, model, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSam) -> None:
        model = await async_client.models.retrieve(
            model_id="model_id",
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelRetrieveResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSam) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelRetrieveResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSam) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelRetrieveResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                model_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSam) -> None:
        model = await async_client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSam) -> None:
        model = await async_client.models.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSam) -> None:
        response = await async_client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSam) -> None:
        async with async_client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_beta(self, async_client: AsyncSam) -> None:
        model = await async_client.models.retrieve_beta(
            model_id="model_id",
        )
        assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

    @parametrize
    async def test_method_retrieve_beta_with_all_params(self, async_client: AsyncSam) -> None:
        model = await async_client.models.retrieve_beta(
            model_id="model_id",
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_beta(self, async_client: AsyncSam) -> None:
        response = await async_client.models.with_raw_response.retrieve_beta(
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_beta(self, async_client: AsyncSam) -> None:
        async with async_client.models.with_streaming_response.retrieve_beta(
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelRetrieveBetaResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_beta(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            await async_client.models.with_raw_response.retrieve_beta(
                model_id="",
            )

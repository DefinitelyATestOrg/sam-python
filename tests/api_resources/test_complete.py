# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from sam.types import CompleteCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComplete:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Sam) -> None:
        complete = client.complete.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )
        assert_matches_type(CompleteCreateResponse, complete, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Sam) -> None:
        complete = client.complete.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string"],
            stream=True,
            temperature=1,
            top_k=5,
            top_p=0.7,
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(CompleteCreateResponse, complete, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Sam) -> None:
        response = client.complete.with_raw_response.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        complete = response.parse()
        assert_matches_type(CompleteCreateResponse, complete, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Sam) -> None:
        with client.complete.with_streaming_response.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            complete = response.parse()
            assert_matches_type(CompleteCreateResponse, complete, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncComplete:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSam) -> None:
        complete = await async_client.complete.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )
        assert_matches_type(CompleteCreateResponse, complete, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSam) -> None:
        complete = await async_client.complete.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string"],
            stream=True,
            temperature=1,
            top_k=5,
            top_p=0.7,
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(CompleteCreateResponse, complete, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSam) -> None:
        response = await async_client.complete.with_raw_response.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        complete = await response.parse()
        assert_matches_type(CompleteCreateResponse, complete, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSam) -> None:
        async with async_client.complete.with_streaming_response.create(
            max_tokens_to_sample=256,
            model="claude-2.1",
            prompt="\n\nHuman: Hello, world!\n\nAssistant:",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            complete = await response.parse()
            assert_matches_type(CompleteCreateResponse, complete, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam.types.messages import (
    BatchesBetaTrueListResponse,
    BatchesBetaTrueCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatchesBetaTrue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Sam) -> None:
        batches_beta_true = client.messages.batches_beta_true.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                    },
                }
            ],
        )
        assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Sam) -> None:
        batches_beta_true = client.messages.batches_beta_true.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                        "metadata": {"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
                        "stop_sequences": ["string"],
                        "stream": True,
                        "system": [
                            {
                                "text": "Today's date is 2024-06-01.",
                                "type": "text",
                                "cache_control": {"type": "ephemeral"},
                                "citations": [
                                    {
                                        "cited_text": "cited_text",
                                        "document_index": 0,
                                        "document_title": "x",
                                        "end_char_index": 0,
                                        "start_char_index": 0,
                                        "type": "char_location",
                                    }
                                ],
                            }
                        ],
                        "temperature": 1,
                        "thinking": {
                            "budget_tokens": 1024,
                            "type": "enabled",
                        },
                        "tool_choice": {
                            "type": "auto",
                            "disable_parallel_tool_use": True,
                        },
                        "tools": [
                            {
                                "input_schema": {
                                    "type": "object",
                                    "properties": {
                                        "location": {
                                            "description": "The city and state, e.g. San Francisco, CA",
                                            "type": "string",
                                        },
                                        "unit": {
                                            "description": "Unit for the output - one of (celsius, fahrenheit)",
                                            "type": "string",
                                        },
                                    },
                                },
                                "name": "name",
                                "cache_control": {"type": "ephemeral"},
                                "description": "Get the current weather in a given location",
                                "type": "custom",
                            }
                        ],
                        "top_k": 5,
                        "top_p": 0.7,
                    },
                }
            ],
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Sam) -> None:
        response = client.messages.batches_beta_true.with_raw_response.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batches_beta_true = response.parse()
        assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Sam) -> None:
        with client.messages.batches_beta_true.with_streaming_response.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batches_beta_true = response.parse()
            assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Sam) -> None:
        batches_beta_true = client.messages.batches_beta_true.list()
        assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sam) -> None:
        batches_beta_true = client.messages.batches_beta_true.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sam) -> None:
        response = client.messages.batches_beta_true.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batches_beta_true = response.parse()
        assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sam) -> None:
        with client.messages.batches_beta_true.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batches_beta_true = response.parse()
            assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatchesBetaTrue:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSam) -> None:
        batches_beta_true = await async_client.messages.batches_beta_true.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                    },
                }
            ],
        )
        assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSam) -> None:
        batches_beta_true = await async_client.messages.batches_beta_true.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                        "metadata": {"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
                        "stop_sequences": ["string"],
                        "stream": True,
                        "system": [
                            {
                                "text": "Today's date is 2024-06-01.",
                                "type": "text",
                                "cache_control": {"type": "ephemeral"},
                                "citations": [
                                    {
                                        "cited_text": "cited_text",
                                        "document_index": 0,
                                        "document_title": "x",
                                        "end_char_index": 0,
                                        "start_char_index": 0,
                                        "type": "char_location",
                                    }
                                ],
                            }
                        ],
                        "temperature": 1,
                        "thinking": {
                            "budget_tokens": 1024,
                            "type": "enabled",
                        },
                        "tool_choice": {
                            "type": "auto",
                            "disable_parallel_tool_use": True,
                        },
                        "tools": [
                            {
                                "input_schema": {
                                    "type": "object",
                                    "properties": {
                                        "location": {
                                            "description": "The city and state, e.g. San Francisco, CA",
                                            "type": "string",
                                        },
                                        "unit": {
                                            "description": "Unit for the output - one of (celsius, fahrenheit)",
                                            "type": "string",
                                        },
                                    },
                                },
                                "name": "name",
                                "cache_control": {"type": "ephemeral"},
                                "description": "Get the current weather in a given location",
                                "type": "custom",
                            }
                        ],
                        "top_k": 5,
                        "top_p": 0.7,
                    },
                }
            ],
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches_beta_true.with_raw_response.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batches_beta_true = await response.parse()
        assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches_beta_true.with_streaming_response.create(
            requests=[
                {
                    "custom_id": "my-custom-id-1",
                    "params": {
                        "max_tokens": 1024,
                        "messages": [
                            {
                                "content": "Hello, world",
                                "role": "user",
                            }
                        ],
                        "model": "claude-3-7-sonnet-20250219",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batches_beta_true = await response.parse()
            assert_matches_type(BatchesBetaTrueCreateResponse, batches_beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSam) -> None:
        batches_beta_true = await async_client.messages.batches_beta_true.list()
        assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSam) -> None:
        batches_beta_true = await async_client.messages.batches_beta_true.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches_beta_true.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batches_beta_true = await response.parse()
        assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches_beta_true.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batches_beta_true = await response.parse()
            assert_matches_type(BatchesBetaTrueListResponse, batches_beta_true, path=["response"])

        assert cast(Any, response.is_closed) is True

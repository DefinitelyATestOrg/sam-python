# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from sam.types import SamPlopPlopCreateMessageResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSamPlopPlop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_message(self, client: Sam) -> None:
        sam_plop_plop = client.sam_plop_plop.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
        )
        assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

    @parametrize
    def test_method_create_message_with_all_params(self, client: Sam) -> None:
        sam_plop_plop = client.sam_plop_plop.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string"],
            stream=True,
            system=[
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
            temperature=1,
            thinking={
                "budget_tokens": 1024,
                "type": "enabled",
            },
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
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
                }
            ],
            top_k=5,
            top_p=0.7,
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

    @parametrize
    def test_raw_response_create_message(self, client: Sam) -> None:
        response = client.sam_plop_plop.with_raw_response.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sam_plop_plop = response.parse()
        assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

    @parametrize
    def test_streaming_response_create_message(self, client: Sam) -> None:
        with client.sam_plop_plop.with_streaming_response.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sam_plop_plop = response.parse()
            assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSamPlopPlop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_message(self, async_client: AsyncSam) -> None:
        sam_plop_plop = await async_client.sam_plop_plop.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
        )
        assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

    @parametrize
    async def test_method_create_message_with_all_params(self, async_client: AsyncSam) -> None:
        sam_plop_plop = await async_client.sam_plop_plop.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
            metadata={"user_id": "13803d75-b4b5-4c3e-b2a2-6f21399b021b"},
            stop_sequences=["string"],
            stream=True,
            system=[
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
            temperature=1,
            thinking={
                "budget_tokens": 1024,
                "type": "enabled",
            },
            tool_choice={
                "type": "auto",
                "disable_parallel_tool_use": True,
            },
            tools=[
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
                }
            ],
            top_k=5,
            top_p=0.7,
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

    @parametrize
    async def test_raw_response_create_message(self, async_client: AsyncSam) -> None:
        response = await async_client.sam_plop_plop.with_raw_response.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sam_plop_plop = await response.parse()
        assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

    @parametrize
    async def test_streaming_response_create_message(self, async_client: AsyncSam) -> None:
        async with async_client.sam_plop_plop.with_streaming_response.create_message(
            max_tokens=1024,
            messages=[
                {
                    "content": "Hello, world",
                    "role": "user",
                }
            ],
            model="claude-3-7-sonnet-20250219",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sam_plop_plop = await response.parse()
            assert_matches_type(SamPlopPlopCreateMessageResponse, sam_plop_plop, path=["response"])

        assert cast(Any, response.is_closed) is True

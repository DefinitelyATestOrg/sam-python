# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam.types.messages import (
    BatchListResponse,
    BatchCancelResponse,
    BatchCreateResponse,
    BatchDeleteResponse,
    BatchResultsResponse,
    BatchRetrieveResponse,
    BatchCancelBetaResponse,
    BatchResultsBetaResponse,
)
from sam._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Sam) -> None:
        batch = client.messages.batches.create(
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
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Sam) -> None:
        batch = client.messages.batches.create(
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
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.create(
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
        batch = response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.create(
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

            batch = response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Sam) -> None:
        batch = client.messages.batches.retrieve(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sam) -> None:
        batch = client.messages.batches.retrieve(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.retrieve(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.retrieve(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.with_raw_response.retrieve(
                message_batch_id="",
            )

    @parametrize
    def test_method_list(self, client: Sam) -> None:
        batch = client.messages.batches.list()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sam) -> None:
        batch = client.messages.batches.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchListResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        batch = client.messages.batches.delete(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchDeleteResponse, batch, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Sam) -> None:
        batch = client.messages.batches.delete(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchDeleteResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.delete(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchDeleteResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.delete(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchDeleteResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.with_raw_response.delete(
                message_batch_id="",
            )

    @parametrize
    def test_method_cancel(self, client: Sam) -> None:
        batch = client.messages.batches.cancel(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: Sam) -> None:
        batch = client.messages.batches.cancel(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.cancel(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.cancel(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.with_raw_response.cancel(
                message_batch_id="",
            )

    @parametrize
    def test_method_cancel_beta(self, client: Sam) -> None:
        batch = client.messages.batches.cancel_beta(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

    @parametrize
    def test_method_cancel_beta_with_all_params(self, client: Sam) -> None:
        batch = client.messages.batches.cancel_beta(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

    @parametrize
    def test_raw_response_cancel_beta(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.cancel_beta(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

    @parametrize
    def test_streaming_response_cancel_beta(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.cancel_beta(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel_beta(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.with_raw_response.cancel_beta(
                message_batch_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_results(self, client: Sam) -> None:
        batch_stream = client.messages.batches.results(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(JSONLDecoder[BatchResultsResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_results_with_all_params(self, client: Sam) -> None:
        batch_stream = client.messages.batches.results(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(JSONLDecoder[BatchResultsResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_raw_response_results(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.results(
            message_batch_id="message_batch_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_streaming_response_results(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.results(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_path_params_results(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.with_raw_response.results(
                message_batch_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_results_beta(self, client: Sam) -> None:
        batch_stream = client.messages.batches.results_beta(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(JSONLDecoder[BatchResultsBetaResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_method_results_beta_with_all_params(self, client: Sam) -> None:
        batch_stream = client.messages.batches.results_beta(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(JSONLDecoder[BatchResultsBetaResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_raw_response_results_beta(self, client: Sam) -> None:
        response = client.messages.batches.with_raw_response.results_beta(
            message_batch_id="message_batch_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_streaming_response_results_beta(self, client: Sam) -> None:
        with client.messages.batches.with_streaming_response.results_beta(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    def test_path_params_results_beta(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            client.messages.batches.with_raw_response.results_beta(
                message_batch_id="",
            )


class TestAsyncBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.create(
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
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.create(
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
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.create(
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
        batch = await response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.create(
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

            batch = await response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.retrieve(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.retrieve(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.retrieve(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.retrieve(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.with_raw_response.retrieve(
                message_batch_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.list()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.list(
            after_id="after_id",
            before_id="before_id",
            limit=1,
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchListResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.delete(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchDeleteResponse, batch, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.delete(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchDeleteResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.delete(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchDeleteResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.delete(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchDeleteResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.with_raw_response.delete(
                message_batch_id="",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.cancel(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.cancel(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.cancel(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.cancel(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.with_raw_response.cancel(
                message_batch_id="",
            )

    @parametrize
    async def test_method_cancel_beta(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.cancel_beta(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

    @parametrize
    async def test_method_cancel_beta_with_all_params(self, async_client: AsyncSam) -> None:
        batch = await async_client.messages.batches.cancel_beta(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

    @parametrize
    async def test_raw_response_cancel_beta(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.cancel_beta(
            message_batch_id="message_batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

    @parametrize
    async def test_streaming_response_cancel_beta(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.cancel_beta(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCancelBetaResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel_beta(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.with_raw_response.cancel_beta(
                message_batch_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_results(self, async_client: AsyncSam) -> None:
        batch_stream = await async_client.messages.batches.results(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(AsyncJSONLDecoder[BatchResultsResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_results_with_all_params(self, async_client: AsyncSam) -> None:
        batch_stream = await async_client.messages.batches.results(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(AsyncJSONLDecoder[BatchResultsResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_raw_response_results(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.results(
            message_batch_id="message_batch_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_streaming_response_results(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.results(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_path_params_results(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.with_raw_response.results(
                message_batch_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_results_beta(self, async_client: AsyncSam) -> None:
        batch_stream = await async_client.messages.batches.results_beta(
            message_batch_id="message_batch_id",
        )
        assert_matches_type(AsyncJSONLDecoder[BatchResultsBetaResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_method_results_beta_with_all_params(self, async_client: AsyncSam) -> None:
        batch_stream = await async_client.messages.batches.results_beta(
            message_batch_id="message_batch_id",
            anthropic_beta=["string"],
            anthropic_version="anthropic-version",
            x_api_key="x-api-key",
        )
        assert_matches_type(AsyncJSONLDecoder[BatchResultsBetaResponse], batch_stream, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_raw_response_results_beta(self, async_client: AsyncSam) -> None:
        response = await async_client.messages.batches.with_raw_response.results_beta(
            message_batch_id="message_batch_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_streaming_response_results_beta(self, async_client: AsyncSam) -> None:
        async with async_client.messages.batches.with_streaming_response.results_beta(
            message_batch_id="message_batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support JSONL responses yet")
    @parametrize
    async def test_path_params_results_beta(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_batch_id` but received ''"):
            await async_client.messages.batches.with_raw_response.results_beta(
                message_batch_id="",
            )

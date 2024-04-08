# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from sam import Sam, AsyncSam
from sam._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHiddenTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/hiddenTags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        hidden_tag = client.agents.hidden_tags.update(
            "string",
            body=["string"],
        )
        assert hidden_tag.is_closed
        assert hidden_tag.json() == {"foo": "bar"}
        assert cast(Any, hidden_tag.is_closed) is True
        assert isinstance(hidden_tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/hiddenTags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        hidden_tag = client.agents.hidden_tags.with_raw_response.update(
            "string",
            body=["string"],
        )

        assert hidden_tag.is_closed is True
        assert hidden_tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert hidden_tag.json() == {"foo": "bar"}
        assert isinstance(hidden_tag, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/hiddenTags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.agents.hidden_tags.with_streaming_response.update(
            "string",
            body=["string"],
        ) as hidden_tag:
            assert not hidden_tag.is_closed
            assert hidden_tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert hidden_tag.json() == {"foo": "bar"}
            assert cast(Any, hidden_tag.is_closed) is True
            assert isinstance(hidden_tag, StreamedBinaryAPIResponse)

        assert cast(Any, hidden_tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.hidden_tags.with_raw_response.update(
                "",
                body=["string"],
            )


class TestAsyncHiddenTags:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/hiddenTags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        hidden_tag = await async_client.agents.hidden_tags.update(
            "string",
            body=["string"],
        )
        assert hidden_tag.is_closed
        assert await hidden_tag.json() == {"foo": "bar"}
        assert cast(Any, hidden_tag.is_closed) is True
        assert isinstance(hidden_tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/hiddenTags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        hidden_tag = await async_client.agents.hidden_tags.with_raw_response.update(
            "string",
            body=["string"],
        )

        assert hidden_tag.is_closed is True
        assert hidden_tag.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await hidden_tag.json() == {"foo": "bar"}
        assert isinstance(hidden_tag, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/hiddenTags").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.agents.hidden_tags.with_streaming_response.update(
            "string",
            body=["string"],
        ) as hidden_tag:
            assert not hidden_tag.is_closed
            assert hidden_tag.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await hidden_tag.json() == {"foo": "bar"}
            assert cast(Any, hidden_tag.is_closed) is True
            assert isinstance(hidden_tag, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, hidden_tag.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.hidden_tags.with_raw_response.update(
                "",
                body=["string"],
            )

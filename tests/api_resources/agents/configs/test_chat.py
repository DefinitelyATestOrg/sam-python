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


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        chat = client.agents.configs.chat.retrieve(
            "string",
        )
        assert chat.is_closed
        assert chat.json() == {"foo": "bar"}
        assert cast(Any, chat.is_closed) is True
        assert isinstance(chat, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        chat = client.agents.configs.chat.with_raw_response.retrieve(
            "string",
        )

        assert chat.is_closed is True
        assert chat.http_request.headers.get("X-Stainless-Lang") == "python"
        assert chat.json() == {"foo": "bar"}
        assert isinstance(chat, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.agents.configs.chat.with_streaming_response.retrieve(
            "string",
        ) as chat:
            assert not chat.is_closed
            assert chat.http_request.headers.get("X-Stainless-Lang") == "python"

            assert chat.json() == {"foo": "bar"}
            assert cast(Any, chat.is_closed) is True
            assert isinstance(chat, StreamedBinaryAPIResponse)

        assert cast(Any, chat.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.configs.chat.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        chat = client.agents.configs.chat.update(
            "string",
        )
        assert chat.is_closed
        assert chat.json() == {"foo": "bar"}
        assert cast(Any, chat.is_closed) is True
        assert isinstance(chat, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        chat = client.agents.configs.chat.update(
            "string",
            id="string",
            welcome_message="string",
        )
        assert chat.is_closed
        assert chat.json() == {"foo": "bar"}
        assert cast(Any, chat.is_closed) is True
        assert isinstance(chat, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        chat = client.agents.configs.chat.with_raw_response.update(
            "string",
        )

        assert chat.is_closed is True
        assert chat.http_request.headers.get("X-Stainless-Lang") == "python"
        assert chat.json() == {"foo": "bar"}
        assert isinstance(chat, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.agents.configs.chat.with_streaming_response.update(
            "string",
        ) as chat:
            assert not chat.is_closed
            assert chat.http_request.headers.get("X-Stainless-Lang") == "python"

            assert chat.json() == {"foo": "bar"}
            assert cast(Any, chat.is_closed) is True
            assert isinstance(chat, StreamedBinaryAPIResponse)

        assert cast(Any, chat.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.configs.chat.with_raw_response.update(
                "",
            )


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        chat = await async_client.agents.configs.chat.retrieve(
            "string",
        )
        assert chat.is_closed
        assert await chat.json() == {"foo": "bar"}
        assert cast(Any, chat.is_closed) is True
        assert isinstance(chat, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        chat = await async_client.agents.configs.chat.with_raw_response.retrieve(
            "string",
        )

        assert chat.is_closed is True
        assert chat.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await chat.json() == {"foo": "bar"}
        assert isinstance(chat, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.agents.configs.chat.with_streaming_response.retrieve(
            "string",
        ) as chat:
            assert not chat.is_closed
            assert chat.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await chat.json() == {"foo": "bar"}
            assert cast(Any, chat.is_closed) is True
            assert isinstance(chat, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, chat.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.configs.chat.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        chat = await async_client.agents.configs.chat.update(
            "string",
        )
        assert chat.is_closed
        assert await chat.json() == {"foo": "bar"}
        assert cast(Any, chat.is_closed) is True
        assert isinstance(chat, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        chat = await async_client.agents.configs.chat.update(
            "string",
            id="string",
            welcome_message="string",
        )
        assert chat.is_closed
        assert await chat.json() == {"foo": "bar"}
        assert cast(Any, chat.is_closed) is True
        assert isinstance(chat, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        chat = await async_client.agents.configs.chat.with_raw_response.update(
            "string",
        )

        assert chat.is_closed is True
        assert chat.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await chat.json() == {"foo": "bar"}
        assert isinstance(chat, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string/configs/chat").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.agents.configs.chat.with_streaming_response.update(
            "string",
        ) as chat:
            assert not chat.is_closed
            assert chat.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await chat.json() == {"foo": "bar"}
            assert cast(Any, chat.is_closed) is True
            assert isinstance(chat, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, chat.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.configs.chat.with_raw_response.update(
                "",
            )

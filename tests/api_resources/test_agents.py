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


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = client.agents.retrieve(
            "string",
        )
        assert agent.is_closed
        assert agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        agent = client.agents.with_raw_response.retrieve(
            "string",
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert agent.json() == {"foo": "bar"}
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.agents.with_streaming_response.retrieve(
            "string",
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, StreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = client.agents.update(
            "string",
            agent={},
        )
        assert agent.is_closed
        assert agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = client.agents.update(
            "string",
            agent={
                "id": "string",
                "name": "string",
                "brand_color": "string",
                "persona": "ANY",
                "additional_prompt_text": "string",
                "popular_questions": ["string", "string", "string"],
                "bailout_type": "INTEGRATION",
                "bailout_text": "string",
                "bailout_integration": "SALESFORCE",
                "hidden_ticket_tags": ["string"],
                "internal_sales_status": "LIVE",
                "created_by": {
                    "id": "string",
                    "name": "string",
                },
                "updated_by": {
                    "id": "string",
                    "name": "string",
                },
            },
            chat_icon=b"raw file contents",
            chat_icon_deleted=True,
            logo=b"raw file contents",
            logo_deleted=True,
        )
        assert agent.is_closed
        assert agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        agent = client.agents.with_raw_response.update(
            "string",
            agent={},
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert agent.json() == {"foo": "bar"}
        assert isinstance(agent, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.agents.with_streaming_response.update(
            "string",
            agent={},
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, StreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.with_raw_response.update(
                "",
                agent={},
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        agent = client.agents.delete(
            "string",
        )
        assert agent is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.agents.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.agents.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = await async_client.agents.retrieve(
            "string",
        )
        assert agent.is_closed
        assert await agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        agent = await async_client.agents.with_raw_response.retrieve(
            "string",
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await agent.json() == {"foo": "bar"}
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.agents.with_streaming_response.retrieve(
            "string",
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = await async_client.agents.update(
            "string",
            agent={},
        )
        assert agent.is_closed
        assert await agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        agent = await async_client.agents.update(
            "string",
            agent={
                "id": "string",
                "name": "string",
                "brand_color": "string",
                "persona": "ANY",
                "additional_prompt_text": "string",
                "popular_questions": ["string", "string", "string"],
                "bailout_type": "INTEGRATION",
                "bailout_text": "string",
                "bailout_integration": "SALESFORCE",
                "hidden_ticket_tags": ["string"],
                "internal_sales_status": "LIVE",
                "created_by": {
                    "id": "string",
                    "name": "string",
                },
                "updated_by": {
                    "id": "string",
                    "name": "string",
                },
            },
            chat_icon=b"raw file contents",
            chat_icon_deleted=True,
            logo=b"raw file contents",
            logo_deleted=True,
        )
        assert agent.is_closed
        assert await agent.json() == {"foo": "bar"}
        assert cast(Any, agent.is_closed) is True
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        agent = await async_client.agents.with_raw_response.update(
            "string",
            agent={},
        )

        assert agent.is_closed is True
        assert agent.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await agent.json() == {"foo": "bar"}
        assert isinstance(agent, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/agents/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.agents.with_streaming_response.update(
            "string",
            agent={},
        ) as agent:
            assert not agent.is_closed
            assert agent.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await agent.json() == {"foo": "bar"}
            assert cast(Any, agent.is_closed) is True
            assert isinstance(agent, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, agent.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.with_raw_response.update(
                "",
                agent={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        agent = await async_client.agents.delete(
            "string",
        )
        assert agent is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

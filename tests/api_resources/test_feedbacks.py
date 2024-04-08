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


class TestFeedbacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        feedback = client.feedbacks.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
        )
        assert feedback.is_closed
        assert feedback.json() == {"foo": "bar"}
        assert cast(Any, feedback.is_closed) is True
        assert isinstance(feedback, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        feedback = client.feedbacks.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
            id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            text="string",
            type="THUMBS_UP",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert feedback.is_closed
        assert feedback.json() == {"foo": "bar"}
        assert cast(Any, feedback.is_closed) is True
        assert isinstance(feedback, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        feedback = client.feedbacks.with_raw_response.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
        )

        assert feedback.is_closed is True
        assert feedback.http_request.headers.get("X-Stainless-Lang") == "python"
        assert feedback.json() == {"foo": "bar"}
        assert isinstance(feedback, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.feedbacks.with_streaming_response.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
        ) as feedback:
            assert not feedback.is_closed
            assert feedback.http_request.headers.get("X-Stainless-Lang") == "python"

            assert feedback.json() == {"foo": "bar"}
            assert cast(Any, feedback.is_closed) is True
            assert isinstance(feedback, StreamedBinaryAPIResponse)

        assert cast(Any, feedback.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            client.feedbacks.with_raw_response.update(
                "",
                agent_id="string",
                ticket_message_id="string",
            )


class TestAsyncFeedbacks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        feedback = await async_client.feedbacks.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
        )
        assert feedback.is_closed
        assert await feedback.json() == {"foo": "bar"}
        assert cast(Any, feedback.is_closed) is True
        assert isinstance(feedback, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        feedback = await async_client.feedbacks.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
            id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            text="string",
            type="THUMBS_UP",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert feedback.is_closed
        assert await feedback.json() == {"foo": "bar"}
        assert cast(Any, feedback.is_closed) is True
        assert isinstance(feedback, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        feedback = await async_client.feedbacks.with_raw_response.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
        )

        assert feedback.is_closed is True
        assert feedback.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await feedback.json() == {"foo": "bar"}
        assert isinstance(feedback, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/feedbacks/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.feedbacks.with_streaming_response.update(
            "string",
            agent_id="string",
            ticket_message_id="string",
        ) as feedback:
            assert not feedback.is_closed
            assert feedback.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await feedback.json() == {"foo": "bar"}
            assert cast(Any, feedback.is_closed) is True
            assert isinstance(feedback, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, feedback.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            await async_client.feedbacks.with_raw_response.update(
                "",
                agent_id="string",
                ticket_message_id="string",
            )

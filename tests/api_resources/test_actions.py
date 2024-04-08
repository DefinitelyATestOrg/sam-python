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


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action = client.actions.retrieve(
            "string",
        )
        assert action.is_closed
        assert action.json() == {"foo": "bar"}
        assert cast(Any, action.is_closed) is True
        assert isinstance(action, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action = client.actions.with_raw_response.retrieve(
            "string",
        )

        assert action.is_closed is True
        assert action.http_request.headers.get("X-Stainless-Lang") == "python"
        assert action.json() == {"foo": "bar"}
        assert isinstance(action, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.actions.with_streaming_response.retrieve(
            "string",
        ) as action:
            assert not action.is_closed
            assert action.http_request.headers.get("X-Stainless-Lang") == "python"

            assert action.json() == {"foo": "bar"}
            assert cast(Any, action.is_closed) is True
            assert isinstance(action, StreamedBinaryAPIResponse)

        assert cast(Any, action.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.actions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action = client.actions.update(
            "string",
        )
        assert action.is_closed
        assert action.json() == {"foo": "bar"}
        assert cast(Any, action.is_closed) is True
        assert isinstance(action, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action = client.actions.update(
            "string",
            action_set_id="string",
            agent_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            description="string",
            error_message="string",
            method="GET",
            name="string",
            parameters=[
                {
                    "type": "PATH",
                    "name": "string",
                    "description": "string",
                    "validation_type": "STRING",
                    "required": True,
                    "status": "USER_CONTEXT",
                    "error_message": "string",
                },
                {
                    "type": "PATH",
                    "name": "string",
                    "description": "string",
                    "validation_type": "STRING",
                    "required": True,
                    "status": "USER_CONTEXT",
                    "error_message": "string",
                },
                {
                    "type": "PATH",
                    "name": "string",
                    "description": "string",
                    "validation_type": "STRING",
                    "required": True,
                    "status": "USER_CONTEXT",
                    "error_message": "string",
                },
            ],
            path="string",
            request_body_type="JSON",
            status="ACTIVE",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert action.is_closed
        assert action.json() == {"foo": "bar"}
        assert cast(Any, action.is_closed) is True
        assert isinstance(action, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action = client.actions.with_raw_response.update(
            "string",
        )

        assert action.is_closed is True
        assert action.http_request.headers.get("X-Stainless-Lang") == "python"
        assert action.json() == {"foo": "bar"}
        assert isinstance(action, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.actions.with_streaming_response.update(
            "string",
        ) as action:
            assert not action.is_closed
            assert action.http_request.headers.get("X-Stainless-Lang") == "python"

            assert action.json() == {"foo": "bar"}
            assert cast(Any, action.is_closed) is True
            assert isinstance(action, StreamedBinaryAPIResponse)

        assert cast(Any, action.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.actions.with_raw_response.update(
                "",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action = await async_client.actions.retrieve(
            "string",
        )
        assert action.is_closed
        assert await action.json() == {"foo": "bar"}
        assert cast(Any, action.is_closed) is True
        assert isinstance(action, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action = await async_client.actions.with_raw_response.retrieve(
            "string",
        )

        assert action.is_closed is True
        assert action.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await action.json() == {"foo": "bar"}
        assert isinstance(action, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.actions.with_streaming_response.retrieve(
            "string",
        ) as action:
            assert not action.is_closed
            assert action.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await action.json() == {"foo": "bar"}
            assert cast(Any, action.is_closed) is True
            assert isinstance(action, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, action.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.actions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action = await async_client.actions.update(
            "string",
        )
        assert action.is_closed
        assert await action.json() == {"foo": "bar"}
        assert cast(Any, action.is_closed) is True
        assert isinstance(action, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action = await async_client.actions.update(
            "string",
            action_set_id="string",
            agent_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            description="string",
            error_message="string",
            method="GET",
            name="string",
            parameters=[
                {
                    "type": "PATH",
                    "name": "string",
                    "description": "string",
                    "validation_type": "STRING",
                    "required": True,
                    "status": "USER_CONTEXT",
                    "error_message": "string",
                },
                {
                    "type": "PATH",
                    "name": "string",
                    "description": "string",
                    "validation_type": "STRING",
                    "required": True,
                    "status": "USER_CONTEXT",
                    "error_message": "string",
                },
                {
                    "type": "PATH",
                    "name": "string",
                    "description": "string",
                    "validation_type": "STRING",
                    "required": True,
                    "status": "USER_CONTEXT",
                    "error_message": "string",
                },
            ],
            path="string",
            request_body_type="JSON",
            status="ACTIVE",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert action.is_closed
        assert await action.json() == {"foo": "bar"}
        assert cast(Any, action.is_closed) is True
        assert isinstance(action, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action = await async_client.actions.with_raw_response.update(
            "string",
        )

        assert action.is_closed is True
        assert action.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await action.json() == {"foo": "bar"}
        assert isinstance(action, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.actions.with_streaming_response.update(
            "string",
        ) as action:
            assert not action.is_closed
            assert action.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await action.json() == {"foo": "bar"}
            assert cast(Any, action.is_closed) is True
            assert isinstance(action, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, action.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.actions.with_raw_response.update(
                "",
            )

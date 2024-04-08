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


class TestActionSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action_set = client.action_sets.retrieve(
            "string",
        )
        assert action_set.is_closed
        assert action_set.json() == {"foo": "bar"}
        assert cast(Any, action_set.is_closed) is True
        assert isinstance(action_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action_set = client.action_sets.with_raw_response.retrieve(
            "string",
        )

        assert action_set.is_closed is True
        assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert action_set.json() == {"foo": "bar"}
        assert isinstance(action_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.action_sets.with_streaming_response.retrieve(
            "string",
        ) as action_set:
            assert not action_set.is_closed
            assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert action_set.json() == {"foo": "bar"}
            assert cast(Any, action_set.is_closed) is True
            assert isinstance(action_set, StreamedBinaryAPIResponse)

        assert cast(Any, action_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.action_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action_set = client.action_sets.update(
            path_id="string",
            name="string",
        )
        assert action_set.is_closed
        assert action_set.json() == {"foo": "bar"}
        assert cast(Any, action_set.is_closed) is True
        assert isinstance(action_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action_set = client.action_sets.update(
            path_id="string",
            name="string",
            body_id="string",
            agent_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            open_api_url="string",
            server_url="string",
            type="OPEN_API",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert action_set.is_closed
        assert action_set.json() == {"foo": "bar"}
        assert cast(Any, action_set.is_closed) is True
        assert isinstance(action_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action_set = client.action_sets.with_raw_response.update(
            path_id="string",
            name="string",
        )

        assert action_set.is_closed is True
        assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert action_set.json() == {"foo": "bar"}
        assert isinstance(action_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.action_sets.with_streaming_response.update(
            path_id="string",
            name="string",
        ) as action_set:
            assert not action_set.is_closed
            assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert action_set.json() == {"foo": "bar"}
            assert cast(Any, action_set.is_closed) is True
            assert isinstance(action_set, StreamedBinaryAPIResponse)

        assert cast(Any, action_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.action_sets.with_raw_response.update(
                path_id="",
                name="string",
                body_id="",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        action_set = client.action_sets.delete(
            "string",
        )
        assert action_set is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.action_sets.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_set = response.parse()
        assert action_set is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.action_sets.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_set = response.parse()
            assert action_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.action_sets.with_raw_response.delete(
                "",
            )


class TestAsyncActionSets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action_set = await async_client.action_sets.retrieve(
            "string",
        )
        assert action_set.is_closed
        assert await action_set.json() == {"foo": "bar"}
        assert cast(Any, action_set.is_closed) is True
        assert isinstance(action_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action_set = await async_client.action_sets.with_raw_response.retrieve(
            "string",
        )

        assert action_set.is_closed is True
        assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await action_set.json() == {"foo": "bar"}
        assert isinstance(action_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.action_sets.with_streaming_response.retrieve(
            "string",
        ) as action_set:
            assert not action_set.is_closed
            assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await action_set.json() == {"foo": "bar"}
            assert cast(Any, action_set.is_closed) is True
            assert isinstance(action_set, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, action_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.action_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action_set = await async_client.action_sets.update(
            path_id="string",
            name="string",
        )
        assert action_set.is_closed
        assert await action_set.json() == {"foo": "bar"}
        assert cast(Any, action_set.is_closed) is True
        assert isinstance(action_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        action_set = await async_client.action_sets.update(
            path_id="string",
            name="string",
            body_id="string",
            agent_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            open_api_url="string",
            server_url="string",
            type="OPEN_API",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert action_set.is_closed
        assert await action_set.json() == {"foo": "bar"}
        assert cast(Any, action_set.is_closed) is True
        assert isinstance(action_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        action_set = await async_client.action_sets.with_raw_response.update(
            path_id="string",
            name="string",
        )

        assert action_set.is_closed is True
        assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await action_set.json() == {"foo": "bar"}
        assert isinstance(action_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/actionsets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.action_sets.with_streaming_response.update(
            path_id="string",
            name="string",
        ) as action_set:
            assert not action_set.is_closed
            assert action_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await action_set.json() == {"foo": "bar"}
            assert cast(Any, action_set.is_closed) is True
            assert isinstance(action_set, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, action_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.action_sets.with_raw_response.update(
                path_id="",
                name="string",
                body_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        action_set = await async_client.action_sets.delete(
            "string",
        )
        assert action_set is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.action_sets.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action_set = await response.parse()
        assert action_set is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.action_sets.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action_set = await response.parse()
            assert action_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.action_sets.with_raw_response.delete(
                "",
            )

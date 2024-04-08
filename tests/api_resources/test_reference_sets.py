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


class TestReferenceSets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_set = client.reference_sets.retrieve(
            "string",
        )
        assert reference_set.is_closed
        assert reference_set.json() == {"foo": "bar"}
        assert cast(Any, reference_set.is_closed) is True
        assert isinstance(reference_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_set = client.reference_sets.with_raw_response.retrieve(
            "string",
        )

        assert reference_set.is_closed is True
        assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert reference_set.json() == {"foo": "bar"}
        assert isinstance(reference_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.reference_sets.with_streaming_response.retrieve(
            "string",
        ) as reference_set:
            assert not reference_set.is_closed
            assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert reference_set.json() == {"foo": "bar"}
            assert cast(Any, reference_set.is_closed) is True
            assert isinstance(reference_set, StreamedBinaryAPIResponse)

        assert cast(Any, reference_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.reference_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_set = client.reference_sets.update(
            path_id="string",
        )
        assert reference_set.is_closed
        assert reference_set.json() == {"foo": "bar"}
        assert cast(Any, reference_set.is_closed) is True
        assert isinstance(reference_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_set = client.reference_sets.update(
            path_id="string",
            body_id="string",
            agent_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            name="string",
            type="MANUAL",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert reference_set.is_closed
        assert reference_set.json() == {"foo": "bar"}
        assert cast(Any, reference_set.is_closed) is True
        assert isinstance(reference_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_set = client.reference_sets.with_raw_response.update(
            path_id="string",
        )

        assert reference_set.is_closed is True
        assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert reference_set.json() == {"foo": "bar"}
        assert isinstance(reference_set, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.reference_sets.with_streaming_response.update(
            path_id="string",
        ) as reference_set:
            assert not reference_set.is_closed
            assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert reference_set.json() == {"foo": "bar"}
            assert cast(Any, reference_set.is_closed) is True
            assert isinstance(reference_set, StreamedBinaryAPIResponse)

        assert cast(Any, reference_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.reference_sets.with_raw_response.update(
                path_id="",
                body_id="",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        reference_set = client.reference_sets.delete(
            "string",
        )
        assert reference_set is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.reference_sets.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference_set = response.parse()
        assert reference_set is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.reference_sets.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference_set = response.parse()
            assert reference_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.reference_sets.with_raw_response.delete(
                "",
            )


class TestAsyncReferenceSets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_set = await async_client.reference_sets.retrieve(
            "string",
        )
        assert reference_set.is_closed
        assert await reference_set.json() == {"foo": "bar"}
        assert cast(Any, reference_set.is_closed) is True
        assert isinstance(reference_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_set = await async_client.reference_sets.with_raw_response.retrieve(
            "string",
        )

        assert reference_set.is_closed is True
        assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await reference_set.json() == {"foo": "bar"}
        assert isinstance(reference_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.reference_sets.with_streaming_response.retrieve(
            "string",
        ) as reference_set:
            assert not reference_set.is_closed
            assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await reference_set.json() == {"foo": "bar"}
            assert cast(Any, reference_set.is_closed) is True
            assert isinstance(reference_set, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, reference_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.reference_sets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_set = await async_client.reference_sets.update(
            path_id="string",
        )
        assert reference_set.is_closed
        assert await reference_set.json() == {"foo": "bar"}
        assert cast(Any, reference_set.is_closed) is True
        assert isinstance(reference_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_set = await async_client.reference_sets.update(
            path_id="string",
            body_id="string",
            agent_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            name="string",
            type="MANUAL",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert reference_set.is_closed
        assert await reference_set.json() == {"foo": "bar"}
        assert cast(Any, reference_set.is_closed) is True
        assert isinstance(reference_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_set = await async_client.reference_sets.with_raw_response.update(
            path_id="string",
        )

        assert reference_set.is_closed is True
        assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await reference_set.json() == {"foo": "bar"}
        assert isinstance(reference_set, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesets/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.reference_sets.with_streaming_response.update(
            path_id="string",
        ) as reference_set:
            assert not reference_set.is_closed
            assert reference_set.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await reference_set.json() == {"foo": "bar"}
            assert cast(Any, reference_set.is_closed) is True
            assert isinstance(reference_set, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, reference_set.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.reference_sets.with_raw_response.update(
                path_id="",
                body_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        reference_set = await async_client.reference_sets.delete(
            "string",
        )
        assert reference_set is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.reference_sets.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference_set = await response.parse()
        assert reference_set is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.reference_sets.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference_set = await response.parse()
            assert reference_set is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.reference_sets.with_raw_response.delete(
                "",
            )

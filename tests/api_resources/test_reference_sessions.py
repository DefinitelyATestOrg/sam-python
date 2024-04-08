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


class TestReferenceSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_session = client.reference_sessions.retrieve(
            "string",
        )
        assert reference_session.is_closed
        assert reference_session.json() == {"foo": "bar"}
        assert cast(Any, reference_session.is_closed) is True
        assert isinstance(reference_session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_session = client.reference_sessions.with_raw_response.retrieve(
            "string",
        )

        assert reference_session.is_closed is True
        assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert reference_session.json() == {"foo": "bar"}
        assert isinstance(reference_session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.reference_sessions.with_streaming_response.retrieve(
            "string",
        ) as reference_session:
            assert not reference_session.is_closed
            assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert reference_session.json() == {"foo": "bar"}
            assert cast(Any, reference_session.is_closed) is True
            assert isinstance(reference_session, StreamedBinaryAPIResponse)

        assert cast(Any, reference_session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.reference_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_session = client.reference_sessions.update(
            path_id="string",
        )
        assert reference_session.is_closed
        assert reference_session.json() == {"foo": "bar"}
        assert cast(Any, reference_session.is_closed) is True
        assert isinstance(reference_session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_session = client.reference_sessions.update(
            path_id="string",
            body_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            questions=[
                {
                    "question": "string",
                    "expected_answer": "string",
                },
                {
                    "question": "string",
                    "expected_answer": "string",
                },
                {
                    "question": "string",
                    "expected_answer": "string",
                },
            ],
            reference_set_id="string",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert reference_session.is_closed
        assert reference_session.json() == {"foo": "bar"}
        assert cast(Any, reference_session.is_closed) is True
        assert isinstance(reference_session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_session = client.reference_sessions.with_raw_response.update(
            path_id="string",
        )

        assert reference_session.is_closed is True
        assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert reference_session.json() == {"foo": "bar"}
        assert isinstance(reference_session, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.reference_sessions.with_streaming_response.update(
            path_id="string",
        ) as reference_session:
            assert not reference_session.is_closed
            assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert reference_session.json() == {"foo": "bar"}
            assert cast(Any, reference_session.is_closed) is True
            assert isinstance(reference_session, StreamedBinaryAPIResponse)

        assert cast(Any, reference_session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.reference_sessions.with_raw_response.update(
                path_id="",
                body_id="",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        reference_session = client.reference_sessions.delete(
            "string",
        )
        assert reference_session is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.reference_sessions.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference_session = response.parse()
        assert reference_session is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.reference_sessions.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference_session = response.parse()
            assert reference_session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.reference_sessions.with_raw_response.delete(
                "",
            )


class TestAsyncReferenceSessions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_session = await async_client.reference_sessions.retrieve(
            "string",
        )
        assert reference_session.is_closed
        assert await reference_session.json() == {"foo": "bar"}
        assert cast(Any, reference_session.is_closed) is True
        assert isinstance(reference_session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_session = await async_client.reference_sessions.with_raw_response.retrieve(
            "string",
        )

        assert reference_session.is_closed is True
        assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await reference_session.json() == {"foo": "bar"}
        assert isinstance(reference_session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.reference_sessions.with_streaming_response.retrieve(
            "string",
        ) as reference_session:
            assert not reference_session.is_closed
            assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await reference_session.json() == {"foo": "bar"}
            assert cast(Any, reference_session.is_closed) is True
            assert isinstance(reference_session, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, reference_session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.reference_sessions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_session = await async_client.reference_sessions.update(
            path_id="string",
        )
        assert reference_session.is_closed
        assert await reference_session.json() == {"foo": "bar"}
        assert cast(Any, reference_session.is_closed) is True
        assert isinstance(reference_session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        reference_session = await async_client.reference_sessions.update(
            path_id="string",
            body_id="string",
            created_by={
                "id": "string",
                "name": "string",
            },
            questions=[
                {
                    "question": "string",
                    "expected_answer": "string",
                },
                {
                    "question": "string",
                    "expected_answer": "string",
                },
                {
                    "question": "string",
                    "expected_answer": "string",
                },
            ],
            reference_set_id="string",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert reference_session.is_closed
        assert await reference_session.json() == {"foo": "bar"}
        assert cast(Any, reference_session.is_closed) is True
        assert isinstance(reference_session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        reference_session = await async_client.reference_sessions.with_raw_response.update(
            path_id="string",
        )

        assert reference_session.is_closed is True
        assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await reference_session.json() == {"foo": "bar"}
        assert isinstance(reference_session, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/referencesessions/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.reference_sessions.with_streaming_response.update(
            path_id="string",
        ) as reference_session:
            assert not reference_session.is_closed
            assert reference_session.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await reference_session.json() == {"foo": "bar"}
            assert cast(Any, reference_session.is_closed) is True
            assert isinstance(reference_session, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, reference_session.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.reference_sessions.with_raw_response.update(
                path_id="",
                body_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        reference_session = await async_client.reference_sessions.delete(
            "string",
        )
        assert reference_session is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.reference_sessions.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference_session = await response.parse()
        assert reference_session is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.reference_sessions.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference_session = await response.parse()
            assert reference_session is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.reference_sessions.with_raw_response.delete(
                "",
            )

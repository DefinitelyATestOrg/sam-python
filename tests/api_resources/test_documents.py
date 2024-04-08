# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from sam import Sam, AsyncSam
from sam._utils import parse_datetime
from sam._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = client.documents.retrieve(
            "string",
        )
        assert document.is_closed
        assert document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = client.documents.retrieve(
            "string",
            text=True,
        )
        assert document.is_closed
        assert document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = client.documents.with_raw_response.retrieve(
            "string",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert document.json() == {"foo": "bar"}
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.documents.with_streaming_response.retrieve(
            "string",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, StreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = client.documents.update(
            "string",
        )
        assert document.is_closed
        assert document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = client.documents.update(
            "string",
            id="string",
            corpus_policy="INCLUDE",
            created_by={
                "id": "string",
                "name": "string",
            },
            external_lookup_key="string",
            language_code={
                "code": "string",
                "detected": True,
            },
            processing_version=0,
            source_author="string",
            source_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            source_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            source_url="string",
            text="string",
            title="string",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert document.is_closed
        assert document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = client.documents.with_raw_response.update(
            "string",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert document.json() == {"foo": "bar"}
        assert isinstance(document, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.documents.with_streaming_response.update(
            "string",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, StreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.documents.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        document = client.documents.delete(
            "string",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.documents.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.documents.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            client.documents.with_raw_response.delete(
                "",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = await async_client.documents.retrieve(
            "string",
        )
        assert document.is_closed
        assert await document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = await async_client.documents.retrieve(
            "string",
            text=True,
        )
        assert document.is_closed
        assert await document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = await async_client.documents.with_raw_response.retrieve(
            "string",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await document.json() == {"foo": "bar"}
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.documents.with_streaming_response.retrieve(
            "string",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = await async_client.documents.update(
            "string",
        )
        assert document.is_closed
        assert await document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        document = await async_client.documents.update(
            "string",
            id="string",
            corpus_policy="INCLUDE",
            created_by={
                "id": "string",
                "name": "string",
            },
            external_lookup_key="string",
            language_code={
                "code": "string",
                "detected": True,
            },
            processing_version=0,
            source_author="string",
            source_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            source_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            source_url="string",
            text="string",
            title="string",
            updated_by={
                "id": "string",
                "name": "string",
            },
        )
        assert document.is_closed
        assert await document.json() == {"foo": "bar"}
        assert cast(Any, document.is_closed) is True
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        document = await async_client.documents.with_raw_response.update(
            "string",
        )

        assert document.is_closed is True
        assert document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await document.json() == {"foo": "bar"}
        assert isinstance(document, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/document/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.documents.with_streaming_response.update(
            "string",
        ) as document:
            assert not document.is_closed
            assert document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await document.json() == {"foo": "bar"}
            assert cast(Any, document.is_closed) is True
            assert isinstance(document, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, document.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.documents.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        document = await async_client.documents.delete(
            "string",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.documents.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.documents.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `doc_id` but received ''"):
            await async_client.documents.with_raw_response.delete(
                "",
            )

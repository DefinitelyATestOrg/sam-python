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


class TestCorpora:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        corpora = client.corpora.retrieve(
            "string",
        )
        assert corpora.is_closed
        assert corpora.json() == {"foo": "bar"}
        assert cast(Any, corpora.is_closed) is True
        assert isinstance(corpora, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        corpora = client.corpora.with_raw_response.retrieve(
            "string",
        )

        assert corpora.is_closed is True
        assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"
        assert corpora.json() == {"foo": "bar"}
        assert isinstance(corpora, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.corpora.with_streaming_response.retrieve(
            "string",
        ) as corpora:
            assert not corpora.is_closed
            assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"

            assert corpora.json() == {"foo": "bar"}
            assert cast(Any, corpora.is_closed) is True
            assert isinstance(corpora, StreamedBinaryAPIResponse)

        assert cast(Any, corpora.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `corpus_id` but received ''"):
            client.corpora.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        corpora = client.corpora.update(
            "string",
            agent_id="string",
            name="string",
        )
        assert corpora.is_closed
        assert corpora.json() == {"foo": "bar"}
        assert cast(Any, corpora.is_closed) is True
        assert isinstance(corpora, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        corpora = client.corpora.update(
            "string",
            agent_id="string",
            name="string",
            active=True,
            crawl_spec={
                "ingestion_workflow_id": "string",
                "start_urls": ["string", "string", "string"],
                "exclusion_patterns": ["string", "string", "string"],
                "html_transformer": "NONE",
                "remove_elements_css_selector": "string",
                "max_crawl_depth": 0,
                "max_crawl_pages": 0,
                "initial_concurrency": 0,
                "max_concurrency": 0,
                "timeout_seconds": 0,
                "save_html": True,
                "save_markdown": True,
                "use_sitemaps": True,
            },
            created_by={
                "id": "string",
                "name": "string",
            },
            exclude_last_updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            html_transformer="NONE",
            included_kb_article_ids=["string", "string", "string"],
            integration="SALESFORCE",
            integration_category_id="string",
            source_url="string",
            status="PROCESSING",
            tags=["string"],
            type="URL",
            updated_by={
                "id": "string",
                "name": "string",
            },
            url_exclusion_patterns=["string", "string", "string"],
        )
        assert corpora.is_closed
        assert corpora.json() == {"foo": "bar"}
        assert cast(Any, corpora.is_closed) is True
        assert isinstance(corpora, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        corpora = client.corpora.with_raw_response.update(
            "string",
            agent_id="string",
            name="string",
        )

        assert corpora.is_closed is True
        assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"
        assert corpora.json() == {"foo": "bar"}
        assert isinstance(corpora, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.corpora.with_streaming_response.update(
            "string",
            agent_id="string",
            name="string",
        ) as corpora:
            assert not corpora.is_closed
            assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"

            assert corpora.json() == {"foo": "bar"}
            assert cast(Any, corpora.is_closed) is True
            assert isinstance(corpora, StreamedBinaryAPIResponse)

        assert cast(Any, corpora.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `corpus_id` but received ''"):
            client.corpora.with_raw_response.update(
                "",
                agent_id="string",
                name="string",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        corpora = client.corpora.delete(
            "string",
        )
        assert corpora is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.corpora.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        corpora = response.parse()
        assert corpora is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.corpora.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            corpora = response.parse()
            assert corpora is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `corpus_id` but received ''"):
            client.corpora.with_raw_response.delete(
                "",
            )


class TestAsyncCorpora:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        corpora = await async_client.corpora.retrieve(
            "string",
        )
        assert corpora.is_closed
        assert await corpora.json() == {"foo": "bar"}
        assert cast(Any, corpora.is_closed) is True
        assert isinstance(corpora, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        corpora = await async_client.corpora.with_raw_response.retrieve(
            "string",
        )

        assert corpora.is_closed is True
        assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await corpora.json() == {"foo": "bar"}
        assert isinstance(corpora, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.get("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.corpora.with_streaming_response.retrieve(
            "string",
        ) as corpora:
            assert not corpora.is_closed
            assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await corpora.json() == {"foo": "bar"}
            assert cast(Any, corpora.is_closed) is True
            assert isinstance(corpora, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, corpora.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `corpus_id` but received ''"):
            await async_client.corpora.with_raw_response.retrieve(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        corpora = await async_client.corpora.update(
            "string",
            agent_id="string",
            name="string",
        )
        assert corpora.is_closed
        assert await corpora.json() == {"foo": "bar"}
        assert cast(Any, corpora.is_closed) is True
        assert isinstance(corpora, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        corpora = await async_client.corpora.update(
            "string",
            agent_id="string",
            name="string",
            active=True,
            crawl_spec={
                "ingestion_workflow_id": "string",
                "start_urls": ["string", "string", "string"],
                "exclusion_patterns": ["string", "string", "string"],
                "html_transformer": "NONE",
                "remove_elements_css_selector": "string",
                "max_crawl_depth": 0,
                "max_crawl_pages": 0,
                "initial_concurrency": 0,
                "max_concurrency": 0,
                "timeout_seconds": 0,
                "save_html": True,
                "save_markdown": True,
                "use_sitemaps": True,
            },
            created_by={
                "id": "string",
                "name": "string",
            },
            exclude_last_updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            html_transformer="NONE",
            included_kb_article_ids=["string", "string", "string"],
            integration="SALESFORCE",
            integration_category_id="string",
            source_url="string",
            status="PROCESSING",
            tags=["string"],
            type="URL",
            updated_by={
                "id": "string",
                "name": "string",
            },
            url_exclusion_patterns=["string", "string", "string"],
        )
        assert corpora.is_closed
        assert await corpora.json() == {"foo": "bar"}
        assert cast(Any, corpora.is_closed) is True
        assert isinstance(corpora, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        corpora = await async_client.corpora.with_raw_response.update(
            "string",
            agent_id="string",
            name="string",
        )

        assert corpora.is_closed is True
        assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await corpora.json() == {"foo": "bar"}
        assert isinstance(corpora, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/corpora/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.corpora.with_streaming_response.update(
            "string",
            agent_id="string",
            name="string",
        ) as corpora:
            assert not corpora.is_closed
            assert corpora.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await corpora.json() == {"foo": "bar"}
            assert cast(Any, corpora.is_closed) is True
            assert isinstance(corpora, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, corpora.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `corpus_id` but received ''"):
            await async_client.corpora.with_raw_response.update(
                "",
                agent_id="string",
                name="string",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        corpora = await async_client.corpora.delete(
            "string",
        )
        assert corpora is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.corpora.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        corpora = await response.parse()
        assert corpora is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.corpora.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            corpora = await response.parse()
            assert corpora is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `corpus_id` but received ''"):
            await async_client.corpora.with_raw_response.delete(
                "",
            )

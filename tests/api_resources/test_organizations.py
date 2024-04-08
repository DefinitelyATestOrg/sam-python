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


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        organization = client.organizations.update(
            id="string",
            friendly_id="string",
            name="string",
        )
        assert organization.is_closed
        assert organization.json() == {"foo": "bar"}
        assert cast(Any, organization.is_closed) is True
        assert isinstance(organization, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        organization = client.organizations.update(
            id="string",
            friendly_id="string",
            name="string",
            default_language={
                "code": "string",
                "detected": True,
            },
        )
        assert organization.is_closed
        assert organization.json() == {"foo": "bar"}
        assert cast(Any, organization.is_closed) is True
        assert isinstance(organization, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        organization = client.organizations.with_raw_response.update(
            id="string",
            friendly_id="string",
            name="string",
        )

        assert organization.is_closed is True
        assert organization.http_request.headers.get("X-Stainless-Lang") == "python"
        assert organization.json() == {"foo": "bar"}
        assert isinstance(organization, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.organizations.with_streaming_response.update(
            id="string",
            friendly_id="string",
            name="string",
        ) as organization:
            assert not organization.is_closed
            assert organization.http_request.headers.get("X-Stainless-Lang") == "python"

            assert organization.json() == {"foo": "bar"}
            assert cast(Any, organization.is_closed) is True
            assert isinstance(organization, StreamedBinaryAPIResponse)

        assert cast(Any, organization.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        organization = await async_client.organizations.update(
            id="string",
            friendly_id="string",
            name="string",
        )
        assert organization.is_closed
        assert await organization.json() == {"foo": "bar"}
        assert cast(Any, organization.is_closed) is True
        assert isinstance(organization, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        organization = await async_client.organizations.update(
            id="string",
            friendly_id="string",
            name="string",
            default_language={
                "code": "string",
                "detected": True,
            },
        )
        assert organization.is_closed
        assert await organization.json() == {"foo": "bar"}
        assert cast(Any, organization.is_closed) is True
        assert isinstance(organization, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        organization = await async_client.organizations.with_raw_response.update(
            id="string",
            friendly_id="string",
            name="string",
        )

        assert organization.is_closed is True
        assert organization.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await organization.json() == {"foo": "bar"}
        assert isinstance(organization, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/organizations").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.organizations.with_streaming_response.update(
            id="string",
            friendly_id="string",
            name="string",
        ) as organization:
            assert not organization.is_closed
            assert organization.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await organization.json() == {"foo": "bar"}
            assert cast(Any, organization.is_closed) is True
            assert isinstance(organization, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, organization.is_closed) is True

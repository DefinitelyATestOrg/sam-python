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


class TestMembers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        member = client.members.update(
            "string",
        )
        assert member.is_closed
        assert member.json() == {"foo": "bar"}
        assert cast(Any, member.is_closed) is True
        assert isinstance(member, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_update_with_all_params(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        member = client.members.update(
            "string",
            id="string",
            email="string",
            name="string",
            org_id="string",
            picture_url="string",
            role="OWNER",
        )
        assert member.is_closed
        assert member.json() == {"foo": "bar"}
        assert cast(Any, member.is_closed) is True
        assert isinstance(member, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        member = client.members.with_raw_response.update(
            "string",
        )

        assert member.is_closed is True
        assert member.http_request.headers.get("X-Stainless-Lang") == "python"
        assert member.json() == {"foo": "bar"}
        assert isinstance(member, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_update(self, client: Sam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.members.with_streaming_response.update(
            "string",
        ) as member:
            assert not member.is_closed
            assert member.http_request.headers.get("X-Stainless-Lang") == "python"

            assert member.json() == {"foo": "bar"}
            assert cast(Any, member.is_closed) is True
            assert isinstance(member, StreamedBinaryAPIResponse)

        assert cast(Any, member.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        member = client.members.delete(
            "string",
        )
        assert member is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.members.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = response.parse()
        assert member is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.members.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            client.members.with_raw_response.delete(
                "",
            )


class TestAsyncMembers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        member = await async_client.members.update(
            "string",
        )
        assert member.is_closed
        assert await member.json() == {"foo": "bar"}
        assert cast(Any, member.is_closed) is True
        assert isinstance(member, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_update_with_all_params(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        member = await async_client.members.update(
            "string",
            id="string",
            email="string",
            name="string",
            org_id="string",
            picture_url="string",
            role="OWNER",
        )
        assert member.is_closed
        assert await member.json() == {"foo": "bar"}
        assert cast(Any, member.is_closed) is True
        assert isinstance(member, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        member = await async_client.members.with_raw_response.update(
            "string",
        )

        assert member.is_closed is True
        assert member.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await member.json() == {"foo": "bar"}
        assert isinstance(member, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_update(self, async_client: AsyncSam, respx_mock: MockRouter) -> None:
        respx_mock.put("/api/v1/members/string").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.members.with_streaming_response.update(
            "string",
        ) as member:
            assert not member.is_closed
            assert member.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await member.json() == {"foo": "bar"}
            assert cast(Any, member.is_closed) is True
            assert isinstance(member, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, member.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        member = await async_client.members.delete(
            "string",
        )
        assert member is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.members.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member = await response.parse()
        assert member is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.members.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member = await response.parse()
            assert member is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `member_id` but received ''"):
            await async_client.members.with_raw_response.delete(
                "",
            )

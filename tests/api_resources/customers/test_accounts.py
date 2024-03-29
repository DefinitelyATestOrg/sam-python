# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam.types.customers import AccountListResponse, AccountRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sam) -> None:
        account = client.customers.accounts.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sam) -> None:
        response = client.customers.accounts.with_raw_response.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sam) -> None:
        with client.customers.accounts.with_streaming_response.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.accounts.with_raw_response.retrieve(
                "3dc3d5b3-7023-4848-9853-f5400a64e80f",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.customers.accounts.with_raw_response.retrieve(
                "",
                customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
            )

    @parametrize
    def test_method_list(self, client: Sam) -> None:
        account = client.customers.accounts.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sam) -> None:
        account = client.customers.accounts.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
            cash_account_type=["CACC", "CARD", "CASH"],
            status=["enabled", "deleted", "blocked"],
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sam) -> None:
        response = client.customers.accounts.with_raw_response.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sam) -> None:
        with client.customers.accounts.with_streaming_response.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.accounts.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_close(self, client: Sam) -> None:
        account = client.customers.accounts.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert account is None

    @parametrize
    def test_raw_response_close(self, client: Sam) -> None:
        response = client.customers.accounts.with_raw_response.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert account is None

    @parametrize
    def test_streaming_response_close(self, client: Sam) -> None:
        with client.customers.accounts.with_streaming_response.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_close(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.customers.accounts.with_raw_response.close(
                "3dc3d5b3-7023-4848-9853-f5400a64e80f",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.customers.accounts.with_raw_response.close(
                "",
                customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSam) -> None:
        account = await async_client.customers.accounts.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSam) -> None:
        response = await async_client.customers.accounts.with_raw_response.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSam) -> None:
        async with async_client.customers.accounts.with_streaming_response.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.accounts.with_raw_response.retrieve(
                "3dc3d5b3-7023-4848-9853-f5400a64e80f",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.customers.accounts.with_raw_response.retrieve(
                "",
                customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSam) -> None:
        account = await async_client.customers.accounts.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSam) -> None:
        account = await async_client.customers.accounts.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
            cash_account_type=["CACC", "CARD", "CASH"],
            status=["enabled", "deleted", "blocked"],
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSam) -> None:
        response = await async_client.customers.accounts.with_raw_response.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSam) -> None:
        async with async_client.customers.accounts.with_streaming_response.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.accounts.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_close(self, async_client: AsyncSam) -> None:
        account = await async_client.customers.accounts.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert account is None

    @parametrize
    async def test_raw_response_close(self, async_client: AsyncSam) -> None:
        response = await async_client.customers.accounts.with_raw_response.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert account is None

    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncSam) -> None:
        async with async_client.customers.accounts.with_streaming_response.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_close(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.customers.accounts.with_raw_response.close(
                "3dc3d5b3-7023-4848-9853-f5400a64e80f",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.customers.accounts.with_raw_response.close(
                "",
                customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
            )

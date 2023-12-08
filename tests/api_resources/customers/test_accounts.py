# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from sam import Sam, AsyncSam
from sam._client import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam.types.customers import AccountListResponse, AccountRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    strict_client = Sam(base_url=base_url, _strict_response_validation=True)
    loose_client = Sam(base_url=base_url, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert account is None


class TestAsyncAccounts:
    strict_client = AsyncSam(base_url=base_url, _strict_response_validation=True)
    loose_client = AsyncSam(base_url=base_url, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncSam) -> None:
        account = await client.customers.accounts.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncSam) -> None:
        response = await client.customers.accounts.with_raw_response.retrieve(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncSam) -> None:
        account = await client.customers.accounts.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncSam) -> None:
        account = await client.customers.accounts.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
            cash_account_type=["CACC", "CARD", "CASH"],
            status=["enabled", "deleted", "blocked"],
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncSam) -> None:
        response = await client.customers.accounts.with_raw_response.list(
            "6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_method_close(self, client: AsyncSam) -> None:
        account = await client.customers.accounts.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert account is None

    @parametrize
    async def test_raw_response_close(self, client: AsyncSam) -> None:
        response = await client.customers.accounts.with_raw_response.close(
            "3dc3d5b3-7023-4848-9853-f5400a64e80f",
            customer_id="6878951b-256b-4baa-9e81-ad4c577adc4e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert account is None

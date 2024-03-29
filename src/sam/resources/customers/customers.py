# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .accounts import (
    Accounts,
    AsyncAccounts,
    AccountsWithRawResponse,
    AsyncAccountsWithRawResponse,
    AccountsWithStreamingResponse,
    AsyncAccountsWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Customers", "AsyncCustomers"]


class Customers(SyncAPIResource):
    @cached_property
    def accounts(self) -> Accounts:
        return Accounts(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersWithRawResponse:
        return CustomersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersWithStreamingResponse:
        return CustomersWithStreamingResponse(self)


class AsyncCustomers(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersWithRawResponse:
        return AsyncCustomersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersWithStreamingResponse:
        return AsyncCustomersWithStreamingResponse(self)


class CustomersWithRawResponse:
    def __init__(self, customers: Customers) -> None:
        self._customers = customers

    @cached_property
    def accounts(self) -> AccountsWithRawResponse:
        return AccountsWithRawResponse(self._customers.accounts)


class AsyncCustomersWithRawResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self._customers = customers

    @cached_property
    def accounts(self) -> AsyncAccountsWithRawResponse:
        return AsyncAccountsWithRawResponse(self._customers.accounts)


class CustomersWithStreamingResponse:
    def __init__(self, customers: Customers) -> None:
        self._customers = customers

    @cached_property
    def accounts(self) -> AccountsWithStreamingResponse:
        return AccountsWithStreamingResponse(self._customers.accounts)


class AsyncCustomersWithStreamingResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self._customers = customers

    @cached_property
    def accounts(self) -> AsyncAccountsWithStreamingResponse:
        return AsyncAccountsWithStreamingResponse(self._customers.accounts)

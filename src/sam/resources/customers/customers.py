# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .accounts import Accounts, AsyncAccounts, AccountsWithRawResponse, AsyncAccountsWithRawResponse
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


class AsyncCustomers(AsyncAPIResource):
    @cached_property
    def accounts(self) -> AsyncAccounts:
        return AsyncAccounts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersWithRawResponse:
        return AsyncCustomersWithRawResponse(self)


class CustomersWithRawResponse:
    def __init__(self, customers: Customers) -> None:
        self.accounts = AccountsWithRawResponse(customers.accounts)


class AsyncCustomersWithRawResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self.accounts = AsyncAccountsWithRawResponse(customers.accounts)

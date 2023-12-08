# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .accounts import (
    Accounts,
    AsyncAccounts,
    AccountsWithRawResponse,
    AsyncAccountsWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Sam, AsyncSam

__all__ = ["Customers", "AsyncCustomers"]


class Customers(SyncAPIResource):
    accounts: Accounts
    with_raw_response: CustomersWithRawResponse

    def __init__(self, client: Sam) -> None:
        super().__init__(client)
        self.accounts = Accounts(client)
        self.with_raw_response = CustomersWithRawResponse(self)


class AsyncCustomers(AsyncAPIResource):
    accounts: AsyncAccounts
    with_raw_response: AsyncCustomersWithRawResponse

    def __init__(self, client: AsyncSam) -> None:
        super().__init__(client)
        self.accounts = AsyncAccounts(client)
        self.with_raw_response = AsyncCustomersWithRawResponse(self)


class CustomersWithRawResponse:
    def __init__(self, customers: Customers) -> None:
        self.accounts = AccountsWithRawResponse(customers.accounts)


class AsyncCustomersWithRawResponse:
    def __init__(self, customers: AsyncCustomers) -> None:
        self.accounts = AsyncAccountsWithRawResponse(customers.accounts)

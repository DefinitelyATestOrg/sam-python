# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .customers import (
    Customers,
    AsyncCustomers,
    CustomersWithRawResponse,
    AsyncCustomersWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Sam, AsyncSam

__all__ = ["V1", "AsyncV1"]


class V1(SyncAPIResource):
    customers: Customers
    with_raw_response: V1WithRawResponse

    def __init__(self, client: Sam) -> None:
        super().__init__(client)
        self.customers = Customers(client)
        self.with_raw_response = V1WithRawResponse(self)


class AsyncV1(AsyncAPIResource):
    customers: AsyncCustomers
    with_raw_response: AsyncV1WithRawResponse

    def __init__(self, client: AsyncSam) -> None:
        super().__init__(client)
        self.customers = AsyncCustomers(client)
        self.with_raw_response = AsyncV1WithRawResponse(self)


class V1WithRawResponse:
    def __init__(self, v1: V1) -> None:
        self.customers = CustomersWithRawResponse(v1.customers)


class AsyncV1WithRawResponse:
    def __init__(self, v1: AsyncV1) -> None:
        self.customers = AsyncCustomersWithRawResponse(v1.customers)

# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...._base_client import make_request_options
from ....types.v1.customers import (
    AccountsResponse,
    DetailedAccountResponse,
    account_list_params,
)

if TYPE_CHECKING:
    from ...._client import Sam, AsyncSam

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    with_raw_response: AccountsWithRawResponse

    def __init__(self, client: Sam) -> None:
        super().__init__(client)
        self.with_raw_response = AccountsWithRawResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailedAccountResponse:
        """
        Allows retrieval of a single account, fetched by its id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/customers/{customer_id}/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailedAccountResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        cash_account_type: List[
            Literal[
                "CACC",
                "CARD",
                "CASH",
                "CHAR",
                "CISH",
                "COMM",
                "CPAC",
                "LLSV",
                "LOAN",
                "MGLD",
                "MOMA",
                "NREX",
                "ODFT",
                "ONDP",
                "OTHR",
                "SACC",
                "SLRY",
                "SVGS",
                "TAXE",
                "TRAN",
                "TRAS",
                "VACC",
                "NFCA",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        status: List[Literal["enabled", "deleted", "blocked"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountsResponse:
        """Allows retrieval of accounts associated with the current authorised user.

        It's
        possible to filter the accounts list by status or by cashAccountType.

        Args:
          cash_account_type: A filter on the list based on the cashAccountType field. The value must be a 4
              characters string as defined in ISO 20022

          status:
              A filter on the list based on the account status field. Available values:

              - enabled - account is available
              - deleted - account is terminated
              - blocked - account is blocked e.g. for legal reasons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/customers/{customer_id}/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cash_account_type": cash_account_type,
                        "status": status,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountsResponse,
        )

    def close(
        self,
        account_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Allows closure of a single account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/customers/{customer_id}/accounts/{account_id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAccounts(AsyncAPIResource):
    with_raw_response: AsyncAccountsWithRawResponse

    def __init__(self, client: AsyncSam) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAccountsWithRawResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailedAccountResponse:
        """
        Allows retrieval of a single account, fetched by its id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/customers/{customer_id}/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailedAccountResponse,
        )

    async def list(
        self,
        customer_id: str,
        *,
        cash_account_type: List[
            Literal[
                "CACC",
                "CARD",
                "CASH",
                "CHAR",
                "CISH",
                "COMM",
                "CPAC",
                "LLSV",
                "LOAN",
                "MGLD",
                "MOMA",
                "NREX",
                "ODFT",
                "ONDP",
                "OTHR",
                "SACC",
                "SLRY",
                "SVGS",
                "TAXE",
                "TRAN",
                "TRAS",
                "VACC",
                "NFCA",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        status: List[Literal["enabled", "deleted", "blocked"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountsResponse:
        """Allows retrieval of accounts associated with the current authorised user.

        It's
        possible to filter the accounts list by status or by cashAccountType.

        Args:
          cash_account_type: A filter on the list based on the cashAccountType field. The value must be a 4
              characters string as defined in ISO 20022

          status:
              A filter on the list based on the account status field. Available values:

              - enabled - account is available
              - deleted - account is terminated
              - blocked - account is blocked e.g. for legal reasons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/customers/{customer_id}/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cash_account_type": cash_account_type,
                        "status": status,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=AccountsResponse,
        )

    async def close(
        self,
        account_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Allows closure of a single account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/customers/{customer_id}/accounts/{account_id}/close",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AccountsWithRawResponse:
    def __init__(self, accounts: Accounts) -> None:
        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )
        self.close = to_raw_response_wrapper(
            accounts.close,
        )


class AsyncAccountsWithRawResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )
        self.close = async_to_raw_response_wrapper(
            accounts.close,
        )

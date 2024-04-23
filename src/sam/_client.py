# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Sam",
    "AsyncSam",
    "Client",
    "AsyncClient",
]


class Sam(SyncAPIClient):
    reference_sets: resources.ReferenceSetsResource
    reference_sessions: resources.ReferenceSessionsResource
    organizations: resources.OrganizationsResource
    members: resources.MembersResource
    feedbacks: resources.FeedbacksResource
    documents: resources.DocumentsResource
    corpora: resources.CorporaResource
    agents: resources.AgentsResource
    action_sets: resources.ActionSetsResource
    actions: resources.ActionsResource
    with_raw_response: SamWithRawResponse
    with_streaming_response: SamWithStreamedResponse

    # client options
    auth_token: str | None

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous sam client instance.

        This automatically infers the `auth_token` argument from the `MAVENAGI_AUTH_TOKEN` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("MAVENAGI_AUTH_TOKEN")
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("SAM_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8085/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.reference_sets = resources.ReferenceSetsResource(self)
        self.reference_sessions = resources.ReferenceSessionsResource(self)
        self.organizations = resources.OrganizationsResource(self)
        self.members = resources.MembersResource(self)
        self.feedbacks = resources.FeedbacksResource(self)
        self.documents = resources.DocumentsResource(self)
        self.corpora = resources.CorporaResource(self)
        self.agents = resources.AgentsResource(self)
        self.action_sets = resources.ActionSetsResource(self)
        self.actions = resources.ActionsResource(self)
        self.with_raw_response = SamWithRawResponse(self)
        self.with_streaming_response = SamWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        if auth_token is None:
            return {}
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.auth_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the auth_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSam(AsyncAPIClient):
    reference_sets: resources.AsyncReferenceSetsResource
    reference_sessions: resources.AsyncReferenceSessionsResource
    organizations: resources.AsyncOrganizationsResource
    members: resources.AsyncMembersResource
    feedbacks: resources.AsyncFeedbacksResource
    documents: resources.AsyncDocumentsResource
    corpora: resources.AsyncCorporaResource
    agents: resources.AsyncAgentsResource
    action_sets: resources.AsyncActionSetsResource
    actions: resources.AsyncActionsResource
    with_raw_response: AsyncSamWithRawResponse
    with_streaming_response: AsyncSamWithStreamedResponse

    # client options
    auth_token: str | None

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async sam client instance.

        This automatically infers the `auth_token` argument from the `MAVENAGI_AUTH_TOKEN` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("MAVENAGI_AUTH_TOKEN")
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("SAM_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8085/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.reference_sets = resources.AsyncReferenceSetsResource(self)
        self.reference_sessions = resources.AsyncReferenceSessionsResource(self)
        self.organizations = resources.AsyncOrganizationsResource(self)
        self.members = resources.AsyncMembersResource(self)
        self.feedbacks = resources.AsyncFeedbacksResource(self)
        self.documents = resources.AsyncDocumentsResource(self)
        self.corpora = resources.AsyncCorporaResource(self)
        self.agents = resources.AsyncAgentsResource(self)
        self.action_sets = resources.AsyncActionSetsResource(self)
        self.actions = resources.AsyncActionsResource(self)
        self.with_raw_response = AsyncSamWithRawResponse(self)
        self.with_streaming_response = AsyncSamWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        if auth_token is None:
            return {}
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.auth_token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the auth_token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SamWithRawResponse:
    def __init__(self, client: Sam) -> None:
        self.reference_sets = resources.ReferenceSetsResourceWithRawResponse(client.reference_sets)
        self.reference_sessions = resources.ReferenceSessionsResourceWithRawResponse(client.reference_sessions)
        self.organizations = resources.OrganizationsResourceWithRawResponse(client.organizations)
        self.members = resources.MembersResourceWithRawResponse(client.members)
        self.feedbacks = resources.FeedbacksResourceWithRawResponse(client.feedbacks)
        self.documents = resources.DocumentsResourceWithRawResponse(client.documents)
        self.corpora = resources.CorporaResourceWithRawResponse(client.corpora)
        self.agents = resources.AgentsResourceWithRawResponse(client.agents)
        self.action_sets = resources.ActionSetsResourceWithRawResponse(client.action_sets)
        self.actions = resources.ActionsResourceWithRawResponse(client.actions)


class AsyncSamWithRawResponse:
    def __init__(self, client: AsyncSam) -> None:
        self.reference_sets = resources.AsyncReferenceSetsResourceWithRawResponse(client.reference_sets)
        self.reference_sessions = resources.AsyncReferenceSessionsResourceWithRawResponse(client.reference_sessions)
        self.organizations = resources.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.members = resources.AsyncMembersResourceWithRawResponse(client.members)
        self.feedbacks = resources.AsyncFeedbacksResourceWithRawResponse(client.feedbacks)
        self.documents = resources.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.corpora = resources.AsyncCorporaResourceWithRawResponse(client.corpora)
        self.agents = resources.AsyncAgentsResourceWithRawResponse(client.agents)
        self.action_sets = resources.AsyncActionSetsResourceWithRawResponse(client.action_sets)
        self.actions = resources.AsyncActionsResourceWithRawResponse(client.actions)


class SamWithStreamedResponse:
    def __init__(self, client: Sam) -> None:
        self.reference_sets = resources.ReferenceSetsResourceWithStreamingResponse(client.reference_sets)
        self.reference_sessions = resources.ReferenceSessionsResourceWithStreamingResponse(client.reference_sessions)
        self.organizations = resources.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.members = resources.MembersResourceWithStreamingResponse(client.members)
        self.feedbacks = resources.FeedbacksResourceWithStreamingResponse(client.feedbacks)
        self.documents = resources.DocumentsResourceWithStreamingResponse(client.documents)
        self.corpora = resources.CorporaResourceWithStreamingResponse(client.corpora)
        self.agents = resources.AgentsResourceWithStreamingResponse(client.agents)
        self.action_sets = resources.ActionSetsResourceWithStreamingResponse(client.action_sets)
        self.actions = resources.ActionsResourceWithStreamingResponse(client.actions)


class AsyncSamWithStreamedResponse:
    def __init__(self, client: AsyncSam) -> None:
        self.reference_sets = resources.AsyncReferenceSetsResourceWithStreamingResponse(client.reference_sets)
        self.reference_sessions = resources.AsyncReferenceSessionsResourceWithStreamingResponse(
            client.reference_sessions
        )
        self.organizations = resources.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.members = resources.AsyncMembersResourceWithStreamingResponse(client.members)
        self.feedbacks = resources.AsyncFeedbacksResourceWithStreamingResponse(client.feedbacks)
        self.documents = resources.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.corpora = resources.AsyncCorporaResourceWithStreamingResponse(client.corpora)
        self.agents = resources.AsyncAgentsResourceWithStreamingResponse(client.agents)
        self.action_sets = resources.AsyncActionSetsResourceWithStreamingResponse(client.action_sets)
        self.actions = resources.AsyncActionsResourceWithStreamingResponse(client.actions)


Client = Sam

AsyncClient = AsyncSam

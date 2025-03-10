# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BatchesBetaTrueListParams"]


class BatchesBetaTrueListParams(TypedDict, total=False):
    after_id: str
    """ID of the object to use as a cursor for pagination.

    When provided, returns the page of results immediately after this object.
    """

    before_id: str
    """ID of the object to use as a cursor for pagination.

    When provided, returns the page of results immediately before this object.
    """

    limit: int
    """Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.
    """

    anthropic_beta: Annotated[List[str], PropertyInfo(alias="anthropic-beta")]
    """Optional header to specify the beta version(s) you want to use.

    To use multiple betas, use a comma separated list like `beta1,beta2` or specify
    the header multiple times for each beta.
    """

    anthropic_version: Annotated[str, PropertyInfo(alias="anthropic-version")]
    """The version of the Anthropic API you want to use.

    Read more about versioning and our version history
    [here](https://docs.anthropic.com/en/api/versioning).
    """

    x_api_key: Annotated[str, PropertyInfo(alias="x-api-key")]
    """Your unique API key for authentication.

    This key is required in the header of all API requests, to authenticate your
    account and access Anthropic's services. Get your API key through the
    [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
    Workspace.
    """

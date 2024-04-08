# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ChatUpdateParams"]


class ChatUpdateParams(TypedDict, total=False):
    id: str

    welcome_message: Annotated[str, PropertyInfo(alias="welcomeMessage")]

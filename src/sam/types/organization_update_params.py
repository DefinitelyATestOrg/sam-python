# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationUpdateParams", "DefaultLanguage"]


class OrganizationUpdateParams(TypedDict, total=False):
    id: Required[str]

    friendly_id: Required[Annotated[str, PropertyInfo(alias="friendlyId")]]

    name: Required[str]

    default_language: Annotated[DefaultLanguage, PropertyInfo(alias="defaultLanguage")]


class DefaultLanguage(TypedDict, total=False):
    code: str

    detected: bool

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentUpdateParams", "CreatedBy", "LanguageCode", "UpdatedBy"]


class DocumentUpdateParams(TypedDict, total=False):
    id: str

    corpus_policy: Annotated[Literal["INCLUDE", "EXCLUDE_ALWAYS"], PropertyInfo(alias="corpusPolicy")]

    created_by: Annotated[CreatedBy, PropertyInfo(alias="createdBy")]

    external_lookup_key: Annotated[str, PropertyInfo(alias="externalLookupKey")]

    language_code: Annotated[LanguageCode, PropertyInfo(alias="languageCode")]

    processing_version: Annotated[int, PropertyInfo(alias="processingVersion")]

    source_author: Annotated[str, PropertyInfo(alias="sourceAuthor")]

    source_created_at: Annotated[Union[str, datetime], PropertyInfo(alias="sourceCreatedAt", format="iso8601")]

    source_updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="sourceUpdatedAt", format="iso8601")]

    source_url: Annotated[str, PropertyInfo(alias="sourceUrl")]

    text: str

    title: str

    updated_by: Annotated[UpdatedBy, PropertyInfo(alias="updatedBy")]


class CreatedBy(TypedDict, total=False):
    id: str

    name: str


class LanguageCode(TypedDict, total=False):
    code: str

    detected: bool


class UpdatedBy(TypedDict, total=False):
    id: str

    name: str

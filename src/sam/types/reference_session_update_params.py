# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReferenceSessionUpdateParams", "CreatedBy", "Question", "UpdatedBy"]


class ReferenceSessionUpdateParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    body_id: Annotated[str, PropertyInfo(alias="id")]

    created_by: Annotated[CreatedBy, PropertyInfo(alias="createdBy")]

    questions: Iterable[Question]

    reference_set_id: Annotated[str, PropertyInfo(alias="referenceSetId")]

    updated_by: Annotated[UpdatedBy, PropertyInfo(alias="updatedBy")]


class CreatedBy(TypedDict, total=False):
    id: str

    name: str


class Question(TypedDict, total=False):
    expected_answer: Annotated[str, PropertyInfo(alias="expectedAnswer")]

    question: str


class UpdatedBy(TypedDict, total=False):
    id: str

    name: str

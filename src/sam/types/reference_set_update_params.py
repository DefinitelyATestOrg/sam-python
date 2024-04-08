# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReferenceSetUpdateParams", "CreatedBy", "UpdatedBy"]


class ReferenceSetUpdateParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    body_id: Annotated[str, PropertyInfo(alias="id")]

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    created_by: Annotated[CreatedBy, PropertyInfo(alias="createdBy")]

    name: str

    type: Literal["MANUAL", "CSV"]

    updated_by: Annotated[UpdatedBy, PropertyInfo(alias="updatedBy")]


class CreatedBy(TypedDict, total=False):
    id: str

    name: str


class UpdatedBy(TypedDict, total=False):
    id: str

    name: str

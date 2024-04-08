# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ActionSetUpdateParams", "CreatedBy", "UpdatedBy"]


class ActionSetUpdateParams(TypedDict, total=False):
    path_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    name: Required[str]

    body_id: Annotated[str, PropertyInfo(alias="id")]

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    created_by: Annotated[CreatedBy, PropertyInfo(alias="createdBy")]

    open_api_url: Annotated[str, PropertyInfo(alias="openApiUrl")]

    server_url: Annotated[str, PropertyInfo(alias="serverUrl")]

    type: Literal["OPEN_API", "MANUAL"]

    updated_by: Annotated[UpdatedBy, PropertyInfo(alias="updatedBy")]


class CreatedBy(TypedDict, total=False):
    id: str

    name: str


class UpdatedBy(TypedDict, total=False):
    id: str

    name: str

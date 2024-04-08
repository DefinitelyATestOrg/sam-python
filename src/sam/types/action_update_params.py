# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ActionUpdateParams", "CreatedBy", "Parameter", "UpdatedBy"]


class ActionUpdateParams(TypedDict, total=False):
    action_set_id: Annotated[str, PropertyInfo(alias="actionSetId")]

    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    created_by: Annotated[CreatedBy, PropertyInfo(alias="createdBy")]

    description: str

    error_message: Annotated[str, PropertyInfo(alias="errorMessage")]

    method: Literal["GET", "POST", "PUT", "DELETE"]

    name: str

    parameters: Iterable[Parameter]

    path: str

    request_body_type: Annotated[Literal["JSON"], PropertyInfo(alias="requestBodyType")]

    status: Literal["ACTIVE", "INACTIVE", "UNSUPPORTED"]

    updated_by: Annotated[UpdatedBy, PropertyInfo(alias="updatedBy")]


class CreatedBy(TypedDict, total=False):
    id: str

    name: str


class Parameter(TypedDict, total=False):
    description: str

    error_message: Annotated[str, PropertyInfo(alias="errorMessage")]

    name: str

    required: bool

    status: Literal["USER_CONTEXT", "EDITABLE", "UNSUPPORTED"]

    type: Literal["PATH", "QUERY", "BODY"]

    validation_type: Annotated[Literal["STRING", "BOOLEAN", "NUMBER"], PropertyInfo(alias="validationType")]


class UpdatedBy(TypedDict, total=False):
    id: str

    name: str

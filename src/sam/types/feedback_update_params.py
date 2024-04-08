# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FeedbackUpdateParams", "CreatedBy", "UpdatedBy"]


class FeedbackUpdateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    ticket_message_id: Required[Annotated[str, PropertyInfo(alias="ticketMessageId")]]

    id: str

    created_by: Annotated[CreatedBy, PropertyInfo(alias="createdBy")]

    text: str

    type: Literal["THUMBS_UP", "THUMBS_DOWN", "INSERT"]

    updated_by: Annotated[UpdatedBy, PropertyInfo(alias="updatedBy")]


class CreatedBy(TypedDict, total=False):
    id: str

    name: str


class UpdatedBy(TypedDict, total=False):
    id: str

    name: str

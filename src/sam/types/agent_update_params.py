# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["AgentUpdateParams", "Agent", "AgentCreatedBy", "AgentUpdatedBy"]


class AgentUpdateParams(TypedDict, total=False):
    agent: Required[Agent]

    chat_icon: Annotated[FileTypes, PropertyInfo(alias="chatIcon")]

    chat_icon_deleted: Annotated[bool, PropertyInfo(alias="chatIconDeleted")]

    logo: FileTypes

    logo_deleted: Annotated[bool, PropertyInfo(alias="logoDeleted")]


class AgentCreatedBy(TypedDict, total=False):
    id: str

    name: str


class AgentUpdatedBy(TypedDict, total=False):
    id: str

    name: str


class Agent(TypedDict, total=False):
    id: str

    additional_prompt_text: Annotated[str, PropertyInfo(alias="additionalPromptText")]

    bailout_integration: Annotated[
        Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"],
        PropertyInfo(alias="bailoutIntegration"),
    ]

    bailout_text: Annotated[str, PropertyInfo(alias="bailoutText")]

    bailout_type: Annotated[Literal["INTEGRATION", "TEXT"], PropertyInfo(alias="bailoutType")]

    brand_color: Annotated[str, PropertyInfo(alias="brandColor")]

    created_by: Annotated[AgentCreatedBy, PropertyInfo(alias="createdBy")]

    hidden_ticket_tags: Annotated[List[str], PropertyInfo(alias="hiddenTicketTags")]

    internal_sales_status: Annotated[
        Literal["LIVE", "ONBOARDING", "PROSPECT", "TESTING", "Z_INACTIVE"], PropertyInfo(alias="internal__salesStatus")
    ]

    name: str

    persona: Literal[
        "ANY",
        "CASUAL_BUDDY",
        "EMPATHETIC_SUPPORTER",
        "FORMAL_PROFESSIONAL",
        "CONCISE_EXPERT",
        "ENTHUSIASTIC_HELPER",
        "PATIENT_EDUCATOR",
        "PIRATE",
    ]

    popular_questions: Annotated[List[str], PropertyInfo(alias="popularQuestions")]

    updated_by: Annotated[AgentUpdatedBy, PropertyInfo(alias="updatedBy")]

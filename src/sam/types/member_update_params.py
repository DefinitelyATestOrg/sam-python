# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemberUpdateParams"]


class MemberUpdateParams(TypedDict, total=False):
    id: str

    email: str

    name: str

    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    picture_url: Annotated[str, PropertyInfo(alias="pictureUrl")]

    role: Literal["OWNER", "ADMIN", "READER"]

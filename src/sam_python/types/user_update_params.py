# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["UserUpdateParams"]

class UserUpdateParams(TypedDict, total=False):
    path_username: Required[Annotated[str, PropertyInfo(alias="username")]]

    id: int

    email: str

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    password: str

    phone: str

    body_username: Annotated[str, PropertyInfo(alias="username")]

    user_status: Annotated[int, PropertyInfo(alias="userStatus")]
    """User Status"""
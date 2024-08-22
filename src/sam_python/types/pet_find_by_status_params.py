# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["PetFindByStatusParams"]

class PetFindByStatusParams(TypedDict, total=False):
    status: Literal["available", "pending", "sold"]
    """Status values that need to be considered for filter"""
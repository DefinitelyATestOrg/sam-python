# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import List, Iterable

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["PetUpdateParams", "Category", "Tag"]

class PetUpdateParams(TypedDict, total=False):
    name: Required[str]

    photo_urls: Required[Annotated[List[str], PropertyInfo(alias="photoUrls")]]

    id: int

    category: Category

    status: Literal["available", "pending", "sold"]
    """pet status in the store"""

    tags: Iterable[Tag]

class Category(TypedDict, total=False):
    id: int

    name: str

class Tag(TypedDict, total=False):
    id: int

    name: str
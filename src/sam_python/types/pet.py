# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Pet", "Category", "Tag"]

class Category(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

class Tag(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

class Pet(BaseModel):
    name: str

    photo_urls: List[str] = FieldInfo(alias = "photoUrls")

    id: Optional[int] = None

    category: Optional[Category] = None

    status: Optional[Literal["available", "pending", "sold"]] = None
    """pet status in the store"""

    tags: Optional[List[Tag]] = None
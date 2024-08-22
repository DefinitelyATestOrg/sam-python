# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Literal

from .._utils import PropertyInfo

from typing import Union

from datetime import datetime

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["StoreCreateOrderParams"]

class StoreCreateOrderParams(TypedDict, total=False):
    id: int

    complete: bool

    pet_id: Annotated[int, PropertyInfo(alias="petId")]

    quantity: int

    ship_date: Annotated[Union[str, datetime], PropertyInfo(alias="shipDate", format = "iso8601")]

    status: Literal["placed", "approved", "delivered"]
    """Order Status"""
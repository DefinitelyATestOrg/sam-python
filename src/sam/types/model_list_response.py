# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ModelListResponse", "Data"]


class Data(BaseModel):
    id: str
    """Unique model identifier."""

    created_at: datetime
    """RFC 3339 datetime string representing the time at which the model was released.

    May be set to an epoch value if the release date is unknown.
    """

    display_name: str
    """A human-readable name for the model."""

    type: Literal["model"]
    """Object type.

    For Models, this is always `"model"`.
    """


class ModelListResponse(BaseModel):
    data: List[Data]

    first_id: Optional[str] = None
    """First ID in the `data` list.

    Can be used as the `before_id` for the previous page.
    """

    has_more: bool
    """Indicates if there are more results in the requested page direction."""

    last_id: Optional[str] = None
    """Last ID in the `data` list. Can be used as the `after_id` for the next page."""

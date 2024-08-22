# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["APIResponse"]

class APIResponse(BaseModel):
    code: Optional[int] = None

    message: Optional[str] = None

    type: Optional[str] = None
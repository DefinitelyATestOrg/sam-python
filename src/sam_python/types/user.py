# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["User"]

class User(BaseModel):
    id: Optional[int] = None

    email: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias = "firstName", default = None)

    last_name: Optional[str] = FieldInfo(alias = "lastName", default = None)

    password: Optional[str] = None

    phone: Optional[str] = None

    username: Optional[str] = None

    user_status: Optional[int] = FieldInfo(alias = "userStatus", default = None)
    """User Status"""
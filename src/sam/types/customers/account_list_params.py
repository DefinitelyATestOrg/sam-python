# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    cash_account_type: Annotated[
        List[
            Literal[
                "CACC",
                "CARD",
                "CASH",
                "CHAR",
                "CISH",
                "COMM",
                "CPAC",
                "LLSV",
                "LOAN",
                "MGLD",
                "MOMA",
                "NREX",
                "ODFT",
                "ONDP",
                "OTHR",
                "SACC",
                "SLRY",
                "SVGS",
                "TAXE",
                "TRAN",
                "TRAS",
                "VACC",
                "NFCA",
            ]
        ],
        PropertyInfo(alias="cashAccountType"),
    ]
    """A filter on the list based on the cashAccountType field.

    The value must be a 4 characters string as defined in ISO 20022
    """

    status: List[Literal["enabled", "deleted", "blocked"]]
    """A filter on the list based on the account status field. Available values:

    - enabled - account is available
    - deleted - account is terminated
    - blocked - account is blocked e.g. for legal reasons
    """

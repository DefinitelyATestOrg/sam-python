# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccountRetrieveResponse", "Account", "AccountBalance", "AccountBalanceBalanceAmount", "AccountOwnerName"]


class AccountBalanceBalanceAmount(BaseModel):
    amount: str
    """
    The amount given with fractional digits, where fractions must be compliant to
    the currency definition. Up to 14 significant figures. Negative amounts are
    signed by minus. The decimal separator is a dot.

    **Example:** Valid representations for EUR with up to two decimals are:

    - 1056
    - 5768.2
    - -1.50
    - 5877.78
    """

    currency: str
    """ISO 4217 Alpha 3 currency code."""


class AccountBalance(BaseModel):
    balance_amount: AccountBalanceBalanceAmount = FieldInfo(alias="balanceAmount")

    balance_type: Literal["closingBooked", "openingBooked", "interimAvailable", "interimBooked"] = FieldInfo(
        alias="balanceType"
    )
    """The following balance types are defined:

    - "closingBooked": Balance of the account at the end of the pre-agreed account
      reporting period. It is the sum of the opening booked balance at the beginning
      of the period and all entries booked to the account during the pre-agreed
      account reporting period.
    - "openingBooked": Book balance of the account at the beginning of the account
      reporting period. It always equals the closing book balance from the previous
      report.
    - "interimAvailable": Available balance calculated in the course of the account
      ?servicer?s business day, at the time specified, and subject to further
      changes during the business day. The interim balance is calculated on the
      basis of booked credit and debit items during the calculation time/period
      specified.
    - "interimBooked": Balance calculated in the course of the account servicer's
      business day, at the time specified, and subject to further changes during the
      business day. The interim balance is calculated on the basis of booked credit
      and debit items during the calculation time/period specified.
    """

    credit_limit_included: Optional[bool] = FieldInfo(alias="creditLimitIncluded", default=None)
    """
    A flag indicating if the credit limit of the corresponding account is included
    in the calculation of the balance, where applicable.
    """

    last_retrieved_date_time: Optional[datetime] = FieldInfo(alias="lastRetrievedDateTime", default=None)
    """Indicates the date and time of the balance."""


class AccountOwnerName(BaseModel):
    name: str
    """Account owner name"""

    role: Optional[str] = None
    """The following proprietary codes are used:

    - "owner",
    - "legalRepresentative",
    - "authorisedUser"
    """


class Account(BaseModel):
    currency: str
    """ISO 4217 Alpha 3 currency code."""

    resource_id: str = FieldInfo(alias="resourceId")

    status: Literal["enabled", "deleted", "blocked"]
    """Account status. The value is one of the following:

    - "enabled": account is available
    - "deleted": account is terminated
    - "blocked": account is blocked e.g. for legal reasons
    """

    balances: Optional[List[AccountBalance]] = None
    """A list of balances regarding this account, e.g.

    the current balance, the last booked balance. The list might be restricted to
    the current balance.
    """

    bban: Optional[str] = None
    """Basic Bank Account Number (BBAN) Identifier."""

    bic: Optional[str] = None
    """BICFI"""

    cash_account_type: Optional[
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
    ] = FieldInfo(alias="cashAccountType", default=None)
    """ExternalCashAccountType1Code from ISO 20022."""

    details: Optional[str] = None
    """Additional information on the account."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """Name of the account as defined by the user within online channels."""

    iban: Optional[str] = None
    """IBAN of an account."""

    msisdn: Optional[str] = None
    """Mobile phone number."""

    name: Optional[str] = None
    """Name of the account."""

    owner_name: Optional[str] = FieldInfo(alias="ownerName", default=None)
    """Name of the legal account owner.

    If there is more than one owner, then e.g. two names might be noted here. For a
    corporate account, the corporate name is used for this attribute.
    """

    owner_names: Optional[List[AccountOwnerName]] = FieldInfo(alias="ownerNames", default=None)
    """List of owner names."""

    product: Optional[str] = None
    """Product name of the bank for this account, proprietary definition."""

    psu_name: Optional[str] = FieldInfo(alias="psuName", default=None)
    """Name of the user.

    In case of a corporate account, this might be the person acting on behalf of the
    corporate.
    """

    usage: Optional[Literal["PRIV", "ORGA"]] = None
    """Specifies the usage of the account:

    - PRIV: private personal account
    - ORGA: professional account
    """


class AccountRetrieveResponse(BaseModel):
    account: Optional[Account] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """The File's identifier."""

    created_at: datetime
    """The time the File was created."""

    description: Optional[str] = None
    """A description of the File."""

    direction: Literal["to_increase", "from_increase"]
    """Whether the File was generated by Increase or by you and sent to Increase.

    - `to_increase` - This File was sent by you to Increase.
    - `from_increase` - This File was generated by Increase.
    """

    download_url: Optional[str] = None
    """A URL from where the File can be downloaded at this point in time.

    The location of this URL may change over time.
    """

    filename: Optional[str] = None
    """The filename that was provided upon upload or generated by Increase."""

    idempotency_key: Optional[str] = None
    """The idempotency key you chose for this object.

    This value is unique across Increase and is used to ensure that a request is
    only processed once. Learn more about
    [idempotency](https://increase.com/documentation/idempotency-keys).
    """

    mime_type: str
    """The MIME type of the file."""

    purpose: Literal[
        "check_image_front",
        "check_image_back",
        "processed_check_image_front",
        "processed_check_image_back",
        "mailed_check_image",
        "inbound_mail_item",
        "form_1099_int",
        "form_ss_4",
        "identity_document",
        "increase_statement",
        "other",
        "trust_formation_document",
        "digital_wallet_artwork",
        "digital_wallet_app_icon",
        "physical_card_front",
        "physical_card_back",
        "physical_card_carrier",
        "document_request",
        "entity_supplemental_document",
        "export",
        "unusual_activity_report_attachment",
    ]
    """What the File will be used for.

    We may add additional possible values for this enum over time; your application
    should be able to handle such additions gracefully.

    - `check_image_front` - An image of the front of a check, used for check
      deposits.
    - `check_image_back` - An image of the back of a check, used for check deposits.
    - `processed_check_image_front` - An image of the front of a deposited check
      after processing by Increase and submission to the Federal Reserve.
    - `processed_check_image_back` - An image of the back of a deposited check after
      processing by Increase and submission to the Federal Reserve.
    - `mailed_check_image` - An image of a check that was mailed to a recipient.
    - `inbound_mail_item` - A scanned mail item sent to Increase.
    - `form_1099_int` - IRS Form 1099-INT.
    - `form_ss_4` - IRS Form SS-4.
    - `identity_document` - An image of a government-issued ID.
    - `increase_statement` - A statement generated by Increase.
    - `other` - A file purpose not covered by any of the other cases.
    - `trust_formation_document` - A legal document forming a trust.
    - `digital_wallet_artwork` - A card image to be rendered inside digital wallet
      apps. This must be a 1536x969 pixel PNG.
    - `digital_wallet_app_icon` - An icon for you app to be rendered inside digital
      wallet apps. This must be a 100x100 pixel PNG.
    - `physical_card_front` - A card image to be printed on the front of a physical
      card. This must be a 2100x1340 pixel PNG with no other color but black.
    - `physical_card_back` - The image to be printed on the back of a physical card.
    - `physical_card_carrier` - An image representing the entirety of the carrier
      used for a physical card. This must be a 2550x3300 pixel PNG with no other
      color but black.
    - `document_request` - A document requested by Increase.
    - `entity_supplemental_document` - A supplemental document associated an an
      Entity.
    - `export` - The results of an Export you requested via the dashboard or API.
    - `unusual_activity_report_attachment` - An attachment to an Unusual Activity
      Report.
    """

    type: Literal["file"]
    """A constant representing the object's type.

    For this resource it will always be `file`.
    """

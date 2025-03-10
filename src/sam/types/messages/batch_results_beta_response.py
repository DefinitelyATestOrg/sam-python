# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "BatchResultsBetaResponse",
    "Result",
    "ResultBetaSucceededResult",
    "ResultBetaSucceededResultMessage",
    "ResultBetaSucceededResultMessageContent",
    "ResultBetaSucceededResultMessageContentBetaResponseTextBlock",
    "ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitation",
    "ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponseCharLocationCitation",
    "ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponsePageLocationCitation",
    "ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponseContentBlockLocationCitation",
    "ResultBetaSucceededResultMessageContentBetaResponseToolUseBlock",
    "ResultBetaSucceededResultMessageContentBetaResponseThinkingBlock",
    "ResultBetaSucceededResultMessageContentBetaResponseRedactedThinkingBlock",
    "ResultBetaSucceededResultMessageUsage",
    "ResultBetaErroredResult",
    "ResultBetaErroredResultError",
    "ResultBetaErroredResultErrorError",
    "ResultBetaErroredResultErrorErrorBetaInvalidRequestError",
    "ResultBetaErroredResultErrorErrorBetaAuthenticationError",
    "ResultBetaErroredResultErrorErrorBetaBillingError",
    "ResultBetaErroredResultErrorErrorBetaPermissionError",
    "ResultBetaErroredResultErrorErrorBetaNotFoundError",
    "ResultBetaErroredResultErrorErrorBetaRateLimitError",
    "ResultBetaErroredResultErrorErrorBetaGatewayTimeoutError",
    "ResultBetaErroredResultErrorErrorBetaAPIError",
    "ResultBetaErroredResultErrorErrorBetaOverloadedError",
    "ResultBetaCanceledResult",
    "ResultBetaExpiredResult",
]


class ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponseCharLocationCitation(BaseModel):
    cited_text: str

    document_index: int

    document_title: Optional[str] = None

    end_char_index: int

    start_char_index: int

    type: Literal["char_location"]


class ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponsePageLocationCitation(BaseModel):
    cited_text: str

    document_index: int

    document_title: Optional[str] = None

    end_page_number: int

    start_page_number: int

    type: Literal["page_location"]


class ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponseContentBlockLocationCitation(
    BaseModel
):
    cited_text: str

    document_index: int

    document_title: Optional[str] = None

    end_block_index: int

    start_block_index: int

    type: Literal["content_block_location"]


ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitation: TypeAlias = Annotated[
    Union[
        ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponseCharLocationCitation,
        ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponsePageLocationCitation,
        ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitationBetaResponseContentBlockLocationCitation,
    ],
    PropertyInfo(discriminator="type"),
]


class ResultBetaSucceededResultMessageContentBetaResponseTextBlock(BaseModel):
    citations: Optional[List[ResultBetaSucceededResultMessageContentBetaResponseTextBlockCitation]] = None
    """Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited.
    Citing a PDF results in `page_location`, plain text results in `char_location`,
    and content document results in `content_block_location`.
    """

    text: str

    type: Literal["text"]


class ResultBetaSucceededResultMessageContentBetaResponseToolUseBlock(BaseModel):
    id: str

    input: object

    name: str

    type: Literal["tool_use"]


class ResultBetaSucceededResultMessageContentBetaResponseThinkingBlock(BaseModel):
    signature: str

    thinking: str

    type: Literal["thinking"]


class ResultBetaSucceededResultMessageContentBetaResponseRedactedThinkingBlock(BaseModel):
    data: str

    type: Literal["redacted_thinking"]


ResultBetaSucceededResultMessageContent: TypeAlias = Annotated[
    Union[
        ResultBetaSucceededResultMessageContentBetaResponseTextBlock,
        ResultBetaSucceededResultMessageContentBetaResponseToolUseBlock,
        ResultBetaSucceededResultMessageContentBetaResponseThinkingBlock,
        ResultBetaSucceededResultMessageContentBetaResponseRedactedThinkingBlock,
    ],
    PropertyInfo(discriminator="type"),
]


class ResultBetaSucceededResultMessageUsage(BaseModel):
    cache_creation_input_tokens: Optional[int] = None
    """The number of input tokens used to create the cache entry."""

    cache_read_input_tokens: Optional[int] = None
    """The number of input tokens read from the cache."""

    input_tokens: int
    """The number of input tokens which were used."""

    output_tokens: int
    """The number of output tokens which were used."""


class ResultBetaSucceededResultMessage(BaseModel):
    id: str
    """Unique object identifier.

    The format and length of IDs may change over time.
    """

    content: List[ResultBetaSucceededResultMessageContent]
    """Content generated by the model.

    This is an array of content blocks, each of which has a `type` that determines
    its shape.

    Example:

    ```json
    [{ "type": "text", "text": "Hi, I'm Claude." }]
    ```

    If the request input `messages` ended with an `assistant` turn, then the
    response `content` will continue directly from that last turn. You can use this
    to constrain the model's output.

    For example, if the input `messages` were:

    ```json
    [
      {
        "role": "user",
        "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"
      },
      { "role": "assistant", "content": "The best answer is (" }
    ]
    ```

    Then the response `content` might be:

    ```json
    [{ "type": "text", "text": "B)" }]
    ```
    """

    model: str
    """The model that handled the request."""

    role: Literal["assistant"]
    """Conversational role of the generated message.

    This will always be `"assistant"`.
    """

    stop_reason: Optional[Literal["end_turn", "max_tokens", "stop_sequence", "tool_use"]] = None
    """The reason that we stopped.

    This may be one the following values:

    - `"end_turn"`: the model reached a natural stopping point
    - `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    - `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    - `"tool_use"`: the model invoked one or more tools

    In non-streaming mode this value is always non-null. In streaming mode, it is
    null in the `message_start` event and non-null otherwise.
    """

    stop_sequence: Optional[str] = None
    """Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was
    generated.
    """

    type: Literal["message"]
    """Object type.

    For Messages, this is always `"message"`.
    """

    usage: ResultBetaSucceededResultMessageUsage
    """Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the
    underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the
    model. The model's output then goes through a parsing stage before becoming an
    API response. As a result, the token counts in `usage` will not match one-to-one
    with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response
    from Claude.

    Total input tokens in a request is the summation of `input_tokens`,
    `cache_creation_input_tokens`, and `cache_read_input_tokens`.
    """


class ResultBetaSucceededResult(BaseModel):
    message: ResultBetaSucceededResultMessage

    type: Literal["succeeded"]


class ResultBetaErroredResultErrorErrorBetaInvalidRequestError(BaseModel):
    message: str

    type: Literal["invalid_request_error"]


class ResultBetaErroredResultErrorErrorBetaAuthenticationError(BaseModel):
    message: str

    type: Literal["authentication_error"]


class ResultBetaErroredResultErrorErrorBetaBillingError(BaseModel):
    message: str

    type: Literal["billing_error"]


class ResultBetaErroredResultErrorErrorBetaPermissionError(BaseModel):
    message: str

    type: Literal["permission_error"]


class ResultBetaErroredResultErrorErrorBetaNotFoundError(BaseModel):
    message: str

    type: Literal["not_found_error"]


class ResultBetaErroredResultErrorErrorBetaRateLimitError(BaseModel):
    message: str

    type: Literal["rate_limit_error"]


class ResultBetaErroredResultErrorErrorBetaGatewayTimeoutError(BaseModel):
    message: str

    type: Literal["timeout_error"]


class ResultBetaErroredResultErrorErrorBetaAPIError(BaseModel):
    message: str

    type: Literal["api_error"]


class ResultBetaErroredResultErrorErrorBetaOverloadedError(BaseModel):
    message: str

    type: Literal["overloaded_error"]


ResultBetaErroredResultErrorError: TypeAlias = Annotated[
    Union[
        ResultBetaErroredResultErrorErrorBetaInvalidRequestError,
        ResultBetaErroredResultErrorErrorBetaAuthenticationError,
        ResultBetaErroredResultErrorErrorBetaBillingError,
        ResultBetaErroredResultErrorErrorBetaPermissionError,
        ResultBetaErroredResultErrorErrorBetaNotFoundError,
        ResultBetaErroredResultErrorErrorBetaRateLimitError,
        ResultBetaErroredResultErrorErrorBetaGatewayTimeoutError,
        ResultBetaErroredResultErrorErrorBetaAPIError,
        ResultBetaErroredResultErrorErrorBetaOverloadedError,
    ],
    PropertyInfo(discriminator="type"),
]


class ResultBetaErroredResultError(BaseModel):
    error: ResultBetaErroredResultErrorError

    type: Literal["error"]


class ResultBetaErroredResult(BaseModel):
    error: ResultBetaErroredResultError

    type: Literal["errored"]


class ResultBetaCanceledResult(BaseModel):
    type: Literal["canceled"]


class ResultBetaExpiredResult(BaseModel):
    type: Literal["expired"]


Result: TypeAlias = Annotated[
    Union[ResultBetaSucceededResult, ResultBetaErroredResult, ResultBetaCanceledResult, ResultBetaExpiredResult],
    PropertyInfo(discriminator="type"),
]


class BatchResultsBetaResponse(BaseModel):
    custom_id: str
    """Developer-provided ID created for each request in a Message Batch.

    Useful for matching results to requests, as results may be given out of request
    order.

    Must be unique for each request within the Message Batch.
    """

    result: Result
    """Processing result for this request.

    Contains a Message output if processing was successful, an error response if
    processing failed, or the reason why processing was not attempted, such as
    cancellation or expiration.
    """

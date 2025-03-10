# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from ..._models import set_pydantic_config

__all__ = [
    "BatchesBetaTrueCreateParams",
    "Request",
    "RequestParams",
    "RequestParamsMessage",
    "RequestParamsMessageContentUnionMember1",
    "RequestParamsMessageContentUnionMember1BetaRequestTextBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestTextBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestImageBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestImageBlockSource",
    "RequestParamsMessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource",
    "RequestParamsMessageContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource",
    "RequestParamsMessageContentUnionMember1BetaRequestImageBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestToolUseBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestToolUseBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSource",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource",
    "RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaPlainTextSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaUrlpdfSource",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockCacheControl",
    "RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockCitations",
    "RequestParamsMessageContentUnionMember1BetaRequestThinkingBlock",
    "RequestParamsMessageContentUnionMember1BetaRequestRedactedThinkingBlock",
    "RequestParamsMetadata",
    "RequestParamsSystemUnionMember1",
    "RequestParamsSystemUnionMember1CacheControl",
    "RequestParamsSystemUnionMember1Citation",
    "RequestParamsSystemUnionMember1CitationBetaRequestCharLocationCitation",
    "RequestParamsSystemUnionMember1CitationBetaRequestPageLocationCitation",
    "RequestParamsSystemUnionMember1CitationBetaRequestContentBlockLocationCitation",
    "RequestParamsThinking",
    "RequestParamsThinkingBetaThinkingConfigEnabled",
    "RequestParamsThinkingBetaThinkingConfigDisabled",
    "RequestParamsToolChoice",
    "RequestParamsToolChoiceBetaToolChoiceAuto",
    "RequestParamsToolChoiceBetaToolChoiceAny",
    "RequestParamsToolChoiceBetaToolChoiceTool",
    "RequestParamsToolChoiceBetaToolChoiceNone",
    "RequestParamsTool",
    "RequestParamsToolBetaTool",
    "RequestParamsToolBetaToolInputSchema",
    "RequestParamsToolBetaToolCacheControl",
    "RequestParamsToolBetaComputerUseTool20241022",
    "RequestParamsToolBetaComputerUseTool20241022CacheControl",
    "RequestParamsToolBetaBashTool20241022",
    "RequestParamsToolBetaBashTool20241022CacheControl",
    "RequestParamsToolBetaTextEditor20241022",
    "RequestParamsToolBetaTextEditor20241022CacheControl",
    "RequestParamsToolBetaComputerUseTool20250124",
    "RequestParamsToolBetaComputerUseTool20250124CacheControl",
    "RequestParamsToolBetaBashTool20250124",
    "RequestParamsToolBetaBashTool20250124CacheControl",
    "RequestParamsToolBetaTextEditor20250124",
    "RequestParamsToolBetaTextEditor20250124CacheControl",
]


class BatchesBetaTrueCreateParams(TypedDict, total=False):
    requests: Required[Iterable[Request]]
    """List of requests for prompt completion.

    Each is an individual request to create a Message.
    """

    anthropic_beta: Annotated[List[str], PropertyInfo(alias="anthropic-beta")]
    """Optional header to specify the beta version(s) you want to use.

    To use multiple betas, use a comma separated list like `beta1,beta2` or specify
    the header multiple times for each beta.
    """

    anthropic_version: Annotated[str, PropertyInfo(alias="anthropic-version")]
    """The version of the Anthropic API you want to use.

    Read more about versioning and our version history
    [here](https://docs.anthropic.com/en/api/versioning).
    """

    x_api_key: Annotated[str, PropertyInfo(alias="x-api-key")]
    """Your unique API key for authentication.

    This key is required in the header of all API requests, to authenticate your
    account and access Anthropic's services. Get your API key through the
    [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
    Workspace.
    """


class RequestParamsMessageContentUnionMember1BetaRequestTextBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitation: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation,
    RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation,
    RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation,
]


class RequestParamsMessageContentUnionMember1BetaRequestTextBlock(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[RequestParamsMessageContentUnionMember1BetaRequestTextBlockCacheControl]

    citations: Optional[Iterable[RequestParamsMessageContentUnionMember1BetaRequestTextBlockCitation]]


class RequestParamsMessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource(TypedDict, total=False):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    RequestParamsMessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    {"arbitrary_types_allowed": True},
)


class RequestParamsMessageContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource(TypedDict, total=False):
    type: Required[Literal["url"]]

    url: Required[str]


RequestParamsMessageContentUnionMember1BetaRequestImageBlockSource: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    RequestParamsMessageContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource,
]


class RequestParamsMessageContentUnionMember1BetaRequestImageBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestImageBlock(TypedDict, total=False):
    source: Required[RequestParamsMessageContentUnionMember1BetaRequestImageBlockSource]

    type: Required[Literal["image"]]

    cache_control: Optional[RequestParamsMessageContentUnionMember1BetaRequestImageBlockCacheControl]


class RequestParamsMessageContentUnionMember1BetaRequestToolUseBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestToolUseBlock(TypedDict, total=False):
    id: Required[str]

    input: Required[object]

    name: Required[str]

    type: Required[Literal["tool_use"]]

    cache_control: Optional[RequestParamsMessageContentUnionMember1BetaRequestToolUseBlockCacheControl]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitation: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation,
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation,
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation,
]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlock(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[
        RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCacheControl
    ]

    citations: Optional[
        Iterable[
            RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitation
        ]
    ]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource(
    TypedDict, total=False
):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    {"arbitrary_types_allowed": True},
)


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource(
    TypedDict, total=False
):
    type: Required[Literal["url"]]

    url: Required[str]


RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSource: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource,
]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlock(
    TypedDict, total=False
):
    source: Required[
        RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSource
    ]

    type: Required[Literal["image"]]

    cache_control: Optional[
        RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockCacheControl
    ]


RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlock,
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlock,
]


class RequestParamsMessageContentUnionMember1BetaRequestToolResultBlock(TypedDict, total=False):
    tool_use_id: Required[str]

    type: Required[Literal["tool_result"]]

    cache_control: Optional[RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockCacheControl]

    content: Union[str, Iterable[RequestParamsMessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1]]

    is_error: bool


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource(TypedDict, total=False):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["application/pdf"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource,
    {"arbitrary_types_allowed": True},
)


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaPlainTextSource(TypedDict, total=False):
    data: Required[str]

    media_type: Required[Literal["text/plain"]]

    type: Required[Literal["text"]]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitation: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation,
]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlock(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[
        RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCacheControl
    ]

    citations: Optional[
        Iterable[
            RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitation
        ]
    ]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource(
    TypedDict, total=False
):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    {"arbitrary_types_allowed": True},
)


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource(
    TypedDict, total=False
):
    type: Required[Literal["url"]]

    url: Required[str]


RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSource: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource,
]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlock(
    TypedDict, total=False
):
    source: Required[
        RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSource
    ]

    type: Required[Literal["image"]]

    cache_control: Optional[
        RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockCacheControl
    ]


RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlock,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlock,
]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSource(
    TypedDict, total=False
):
    content: Required[
        Union[
            str,
            Iterable[
                RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1
            ],
        ]
    ]

    type: Required[Literal["content"]]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaUrlpdfSource(TypedDict, total=False):
    type: Required[Literal["url"]]

    url: Required[str]


RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSource: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaPlainTextSource,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSource,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSourceBetaUrlpdfSource,
]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockCitations(TypedDict, total=False):
    enabled: bool


class RequestParamsMessageContentUnionMember1BetaRequestDocumentBlock(TypedDict, total=False):
    source: Required[RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockSource]

    type: Required[Literal["document"]]

    cache_control: Optional[RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockCacheControl]

    citations: RequestParamsMessageContentUnionMember1BetaRequestDocumentBlockCitations

    context: Optional[str]

    title: Optional[str]


class RequestParamsMessageContentUnionMember1BetaRequestThinkingBlock(TypedDict, total=False):
    signature: Required[str]

    thinking: Required[str]

    type: Required[Literal["thinking"]]


class RequestParamsMessageContentUnionMember1BetaRequestRedactedThinkingBlock(TypedDict, total=False):
    data: Required[str]

    type: Required[Literal["redacted_thinking"]]


RequestParamsMessageContentUnionMember1: TypeAlias = Union[
    RequestParamsMessageContentUnionMember1BetaRequestTextBlock,
    RequestParamsMessageContentUnionMember1BetaRequestImageBlock,
    RequestParamsMessageContentUnionMember1BetaRequestToolUseBlock,
    RequestParamsMessageContentUnionMember1BetaRequestToolResultBlock,
    RequestParamsMessageContentUnionMember1BetaRequestDocumentBlock,
    RequestParamsMessageContentUnionMember1BetaRequestThinkingBlock,
    RequestParamsMessageContentUnionMember1BetaRequestRedactedThinkingBlock,
]


class RequestParamsMessage(TypedDict, total=False):
    content: Required[Union[str, Iterable[RequestParamsMessageContentUnionMember1]]]

    role: Required[Literal["user", "assistant"]]


class RequestParamsMetadata(TypedDict, total=False):
    user_id: Optional[str]
    """An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use
    this id to help detect abuse. Do not include any identifying information such as
    name, email address, or phone number.
    """


class RequestParamsSystemUnionMember1CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsSystemUnionMember1CitationBetaRequestCharLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class RequestParamsSystemUnionMember1CitationBetaRequestPageLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class RequestParamsSystemUnionMember1CitationBetaRequestContentBlockLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


RequestParamsSystemUnionMember1Citation: TypeAlias = Union[
    RequestParamsSystemUnionMember1CitationBetaRequestCharLocationCitation,
    RequestParamsSystemUnionMember1CitationBetaRequestPageLocationCitation,
    RequestParamsSystemUnionMember1CitationBetaRequestContentBlockLocationCitation,
]


class RequestParamsSystemUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[RequestParamsSystemUnionMember1CacheControl]

    citations: Optional[Iterable[RequestParamsSystemUnionMember1Citation]]


class RequestParamsThinkingBetaThinkingConfigEnabled(TypedDict, total=False):
    budget_tokens: Required[int]
    """Determines how many tokens Claude can use for its internal reasoning process.

    Larger budgets can enable more thorough analysis for complex problems, improving
    response quality.

    Must be ≥1024 and less than `max_tokens`.

    See
    [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
    for details.
    """

    type: Required[Literal["enabled"]]


class RequestParamsThinkingBetaThinkingConfigDisabled(TypedDict, total=False):
    type: Required[Literal["disabled"]]


RequestParamsThinking: TypeAlias = Union[
    RequestParamsThinkingBetaThinkingConfigEnabled, RequestParamsThinkingBetaThinkingConfigDisabled
]


class RequestParamsToolChoiceBetaToolChoiceAuto(TypedDict, total=False):
    type: Required[Literal["auto"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool
    use.
    """


class RequestParamsToolChoiceBetaToolChoiceAny(TypedDict, total=False):
    type: Required[Literal["any"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool
    use.
    """


class RequestParamsToolChoiceBetaToolChoiceTool(TypedDict, total=False):
    name: Required[str]
    """The name of the tool to use."""

    type: Required[Literal["tool"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool
    use.
    """


class RequestParamsToolChoiceBetaToolChoiceNone(TypedDict, total=False):
    type: Required[Literal["none"]]


RequestParamsToolChoice: TypeAlias = Union[
    RequestParamsToolChoiceBetaToolChoiceAuto,
    RequestParamsToolChoiceBetaToolChoiceAny,
    RequestParamsToolChoiceBetaToolChoiceTool,
    RequestParamsToolChoiceBetaToolChoiceNone,
]


class RequestParamsToolBetaToolInputSchemaTyped(TypedDict, total=False):
    type: Required[Literal["object"]]

    properties: Optional[object]


RequestParamsToolBetaToolInputSchema: TypeAlias = Union[RequestParamsToolBetaToolInputSchemaTyped, Dict[str, object]]


class RequestParamsToolBetaToolCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsToolBetaTool(TypedDict, total=False):
    input_schema: Required[RequestParamsToolBetaToolInputSchema]
    """[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model
    will produce.
    """

    name: Required[str]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    cache_control: Optional[RequestParamsToolBetaToolCacheControl]

    description: str
    """Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that
    the model has about what the tool is and how to use it, the better it will
    perform. You can use natural language descriptions to reinforce important
    aspects of the tool input JSON schema.
    """

    type: Optional[Literal["custom"]]


class RequestParamsToolBetaComputerUseTool20241022CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsToolBetaComputerUseTool20241022(TypedDict, total=False):
    display_height_px: Required[int]
    """The height of the display in pixels."""

    display_width_px: Required[int]
    """The width of the display in pixels."""

    name: Required[Literal["computer"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["computer_20241022"]]

    cache_control: Optional[RequestParamsToolBetaComputerUseTool20241022CacheControl]

    display_number: Optional[int]
    """The X11 display number (e.g. 0, 1) for the display."""


class RequestParamsToolBetaBashTool20241022CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsToolBetaBashTool20241022(TypedDict, total=False):
    name: Required[Literal["bash"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["bash_20241022"]]

    cache_control: Optional[RequestParamsToolBetaBashTool20241022CacheControl]


class RequestParamsToolBetaTextEditor20241022CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsToolBetaTextEditor20241022(TypedDict, total=False):
    name: Required[Literal["str_replace_editor"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["text_editor_20241022"]]

    cache_control: Optional[RequestParamsToolBetaTextEditor20241022CacheControl]


class RequestParamsToolBetaComputerUseTool20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsToolBetaComputerUseTool20250124(TypedDict, total=False):
    display_height_px: Required[int]
    """The height of the display in pixels."""

    display_width_px: Required[int]
    """The width of the display in pixels."""

    name: Required[Literal["computer"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["computer_20250124"]]

    cache_control: Optional[RequestParamsToolBetaComputerUseTool20250124CacheControl]

    display_number: Optional[int]
    """The X11 display number (e.g. 0, 1) for the display."""


class RequestParamsToolBetaBashTool20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsToolBetaBashTool20250124(TypedDict, total=False):
    name: Required[Literal["bash"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["bash_20250124"]]

    cache_control: Optional[RequestParamsToolBetaBashTool20250124CacheControl]


class RequestParamsToolBetaTextEditor20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class RequestParamsToolBetaTextEditor20250124(TypedDict, total=False):
    name: Required[Literal["str_replace_editor"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["text_editor_20250124"]]

    cache_control: Optional[RequestParamsToolBetaTextEditor20250124CacheControl]


RequestParamsTool: TypeAlias = Union[
    RequestParamsToolBetaTool,
    RequestParamsToolBetaComputerUseTool20241022,
    RequestParamsToolBetaBashTool20241022,
    RequestParamsToolBetaTextEditor20241022,
    RequestParamsToolBetaComputerUseTool20250124,
    RequestParamsToolBetaBashTool20250124,
    RequestParamsToolBetaTextEditor20250124,
]


class RequestParams(TypedDict, total=False):
    max_tokens: Required[int]
    """The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter
    only specifies the absolute maximum number of tokens to generate.

    Different models have different maximum values for this parameter. See
    [models](https://docs.anthropic.com/en/docs/models-overview) for details.
    """

    messages: Required[Iterable[RequestParamsMessage]]
    """Input messages.

    Our models are trained to operate on alternating `user` and `assistant`
    conversational turns. When creating a new `Message`, you specify the prior
    conversational turns with the `messages` parameter, and the model then generates
    the next `Message` in the conversation. Consecutive `user` or `assistant` turns
    in your request will be combined into a single turn.

    Each input message must be an object with a `role` and `content`. You can
    specify a single `user`-role message, or you can include multiple `user` and
    `assistant` messages.

    If the final message uses the `assistant` role, the response content will
    continue immediately from the content in that message. This can be used to
    constrain part of the model's response.

    Example with a single `user` message:

    ```json
    [{ "role": "user", "content": "Hello, Claude" }]
    ```

    Example with multiple conversational turns:

    ```json
    [
      { "role": "user", "content": "Hello there." },
      { "role": "assistant", "content": "Hi, I'm Claude. How can I help you?" },
      { "role": "user", "content": "Can you explain LLMs in plain English?" }
    ]
    ```

    Example with a partially-filled response from Claude:

    ```json
    [
      {
        "role": "user",
        "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"
      },
      { "role": "assistant", "content": "The best answer is (" }
    ]
    ```

    Each input message `content` may be either a single `string` or an array of
    content blocks, where each block has a specific `type`. Using a `string` for
    `content` is shorthand for an array of one content block of type `"text"`. The
    following input messages are equivalent:

    ```json
    { "role": "user", "content": "Hello, Claude" }
    ```

    ```json
    { "role": "user", "content": [{ "type": "text", "text": "Hello, Claude" }] }
    ```

    Starting with Claude 3 models, you can also send image content blocks:

    ```json
    {
      "role": "user",
      "content": [
        {
          "type": "image",
          "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": "/9j/4AAQSkZJRg..."
          }
        },
        { "type": "text", "text": "What is in this image?" }
      ]
    }
    ```

    We currently support the `base64` source type for images, and the `image/jpeg`,
    `image/png`, `image/gif`, and `image/webp` media types.

    See [examples](https://docs.anthropic.com/en/api/messages-examples#vision) for
    more input examples.

    Note that if you want to include a
    [system prompt](https://docs.anthropic.com/en/docs/system-prompts), you can use
    the top-level `system` parameter — there is no `"system"` role for input
    messages in the Messages API.
    """

    model: Required[str]
    """The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
    details and options.
    """

    metadata: RequestParamsMetadata
    """An object describing metadata about the request."""

    stop_sequences: List[str]
    """Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn,
    which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of
    text, you can use the `stop_sequences` parameter. If the model encounters one of
    the custom sequences, the response `stop_reason` value will be `"stop_sequence"`
    and the response `stop_sequence` value will contain the matched stop sequence.
    """

    stream: bool
    """Whether to incrementally stream the response using server-sent events.

    See [streaming](https://docs.anthropic.com/en/api/messages-streaming) for
    details.
    """

    system: Union[str, Iterable[RequestParamsSystemUnionMember1]]
    """System prompt.

    A system prompt is a way of providing context and instructions to Claude, such
    as specifying a particular goal or role. See our
    [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).
    """

    temperature: float
    """Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0`
    for analytical / multiple choice, and closer to `1.0` for creative and
    generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully
    deterministic.
    """

    thinking: RequestParamsThinking
    """Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's
    thinking process before the final answer. Requires a minimum budget of 1,024
    tokens and counts towards your `max_tokens` limit.

    See
    [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
    for details.
    """

    tool_choice: RequestParamsToolChoice
    """How the model should use the provided tools.

    The model can use a specific tool, any available tool, decide by itself, or not
    use tools at all.
    """

    tools: Iterable[RequestParamsTool]
    """Definitions of tools that the model may use.

    If you include `tools` in your API request, the model may return `tool_use`
    content blocks that represent the model's use of those tools. You can then run
    those tools using the tool input generated by the model and then optionally
    return results back to the model using `tool_result` content blocks.

    Each tool definition includes:

    - `name`: Name of the tool.
    - `description`: Optional, but strongly-recommended description of the tool.
    - `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the
      tool `input` shape that the model will produce in `tool_use` output content
      blocks.

    For example, if you defined `tools` as:

    ```json
    [
      {
        "name": "get_stock_price",
        "description": "Get the current stock price for a given ticker symbol.",
        "input_schema": {
          "type": "object",
          "properties": {
            "ticker": {
              "type": "string",
              "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
            }
          },
          "required": ["ticker"]
        }
      }
    ]
    ```

    And then asked the model "What's the S&P 500 at today?", the model might produce
    `tool_use` content blocks in the response like this:

    ```json
    [
      {
        "type": "tool_use",
        "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
        "name": "get_stock_price",
        "input": { "ticker": "^GSPC" }
      }
    ]
    ```

    You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an
    input, and return the following back to the model in a subsequent `user`
    message:

    ```json
    [
      {
        "type": "tool_result",
        "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
        "content": "259.75 USD"
      }
    ]
    ```

    Tools can be used for workflows that include running client-side tools and
    functions, or more generally whenever you want the model to produce a particular
    JSON structure of output.

    See our [guide](https://docs.anthropic.com/en/docs/tool-use) for more details.
    """

    top_k: int
    """Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses.
    [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only. You usually only need to use
    `temperature`.
    """

    top_p: float
    """Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options
    for each subsequent token in decreasing probability order and cut it off once it
    reaches a particular probability specified by `top_p`. You should either alter
    `temperature` or `top_p`, but not both.

    Recommended for advanced use cases only. You usually only need to use
    `temperature`.
    """


class Request(TypedDict, total=False):
    custom_id: Required[str]
    """Developer-provided ID created for each request in a Message Batch.

    Useful for matching results to requests, as results may be given out of request
    order.

    Must be unique for each request within the Message Batch.
    """

    params: Required[RequestParams]
    """Messages API creation parameters for the individual request.

    See the [Messages API reference](/en/api/messages) for full documentation on
    available parameters.
    """

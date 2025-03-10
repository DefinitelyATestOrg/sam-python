# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo
from .._models import set_pydantic_config

__all__ = [
    "MessageCountTokensBetaParams",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1BetaRequestTextBlock",
    "MessageContentUnionMember1BetaRequestTextBlockCacheControl",
    "MessageContentUnionMember1BetaRequestTextBlockCitation",
    "MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation",
    "MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation",
    "MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation",
    "MessageContentUnionMember1BetaRequestImageBlock",
    "MessageContentUnionMember1BetaRequestImageBlockSource",
    "MessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource",
    "MessageContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource",
    "MessageContentUnionMember1BetaRequestImageBlockCacheControl",
    "MessageContentUnionMember1BetaRequestToolUseBlock",
    "MessageContentUnionMember1BetaRequestToolUseBlockCacheControl",
    "MessageContentUnionMember1BetaRequestToolResultBlock",
    "MessageContentUnionMember1BetaRequestToolResultBlockCacheControl",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlock",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCacheControl",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitation",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlock",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSource",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource",
    "MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockCacheControl",
    "MessageContentUnionMember1BetaRequestDocumentBlock",
    "MessageContentUnionMember1BetaRequestDocumentBlockSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaPlainTextSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlock",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCacheControl",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitation",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlock",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockCacheControl",
    "MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaUrlpdfSource",
    "MessageContentUnionMember1BetaRequestDocumentBlockCacheControl",
    "MessageContentUnionMember1BetaRequestDocumentBlockCitations",
    "MessageContentUnionMember1BetaRequestThinkingBlock",
    "MessageContentUnionMember1BetaRequestRedactedThinkingBlock",
    "SystemUnionMember1",
    "SystemUnionMember1CacheControl",
    "SystemUnionMember1Citation",
    "SystemUnionMember1CitationBetaRequestCharLocationCitation",
    "SystemUnionMember1CitationBetaRequestPageLocationCitation",
    "SystemUnionMember1CitationBetaRequestContentBlockLocationCitation",
    "Thinking",
    "ThinkingBetaThinkingConfigEnabled",
    "ThinkingBetaThinkingConfigDisabled",
    "ToolChoice",
    "ToolChoiceBetaToolChoiceAuto",
    "ToolChoiceBetaToolChoiceAny",
    "ToolChoiceBetaToolChoiceTool",
    "ToolChoiceBetaToolChoiceNone",
    "Tool",
    "ToolBetaTool",
    "ToolBetaToolInputSchema",
    "ToolBetaToolCacheControl",
    "ToolBetaComputerUseTool20241022",
    "ToolBetaComputerUseTool20241022CacheControl",
    "ToolBetaBashTool20241022",
    "ToolBetaBashTool20241022CacheControl",
    "ToolBetaTextEditor20241022",
    "ToolBetaTextEditor20241022CacheControl",
    "ToolBetaComputerUseTool20250124",
    "ToolBetaComputerUseTool20250124CacheControl",
    "ToolBetaBashTool20250124",
    "ToolBetaBashTool20250124CacheControl",
    "ToolBetaTextEditor20250124",
    "ToolBetaTextEditor20250124CacheControl",
]


class MessageCountTokensBetaParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
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

    system: Union[str, Iterable[SystemUnionMember1]]
    """System prompt.

    A system prompt is a way of providing context and instructions to Claude, such
    as specifying a particular goal or role. See our
    [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).
    """

    thinking: Thinking
    """Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's
    thinking process before the final answer. Requires a minimum budget of 1,024
    tokens and counts towards your `max_tokens` limit.

    See
    [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
    for details.
    """

    tool_choice: ToolChoice
    """How the model should use the provided tools.

    The model can use a specific tool, any available tool, decide by itself, or not
    use tools at all.
    """

    tools: Iterable[Tool]
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


class MessageContentUnionMember1BetaRequestTextBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


MessageContentUnionMember1BetaRequestTextBlockCitation: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation,
    MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation,
    MessageContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation,
]


class MessageContentUnionMember1BetaRequestTextBlock(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[MessageContentUnionMember1BetaRequestTextBlockCacheControl]

    citations: Optional[Iterable[MessageContentUnionMember1BetaRequestTextBlockCitation]]


class MessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource(TypedDict, total=False):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource, {"arbitrary_types_allowed": True}
)


class MessageContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource(TypedDict, total=False):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1BetaRequestImageBlockSource: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    MessageContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource,
]


class MessageContentUnionMember1BetaRequestImageBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestImageBlock(TypedDict, total=False):
    source: Required[MessageContentUnionMember1BetaRequestImageBlockSource]

    type: Required[Literal["image"]]

    cache_control: Optional[MessageContentUnionMember1BetaRequestImageBlockCacheControl]


class MessageContentUnionMember1BetaRequestToolUseBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestToolUseBlock(TypedDict, total=False):
    id: Required[str]

    input: Required[object]

    name: Required[str]

    type: Required[Literal["tool_use"]]

    cache_control: Optional[MessageContentUnionMember1BetaRequestToolUseBlockCacheControl]


class MessageContentUnionMember1BetaRequestToolResultBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitation: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation,
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation,
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation,
]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlock(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[
        MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCacheControl
    ]

    citations: Optional[
        Iterable[MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlockCitation]
    ]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource(
    TypedDict, total=False
):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    {"arbitrary_types_allowed": True},
)


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource(
    TypedDict, total=False
):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSource: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource,
]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlock(
    TypedDict, total=False
):
    source: Required[MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockSource]

    type: Required[Literal["image"]]

    cache_control: Optional[
        MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlockCacheControl
    ]


MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestTextBlock,
    MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1BetaRequestImageBlock,
]


class MessageContentUnionMember1BetaRequestToolResultBlock(TypedDict, total=False):
    tool_use_id: Required[str]

    type: Required[Literal["tool_result"]]

    cache_control: Optional[MessageContentUnionMember1BetaRequestToolResultBlockCacheControl]

    content: Union[str, Iterable[MessageContentUnionMember1BetaRequestToolResultBlockContentUnionMember1]]

    is_error: bool


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource(TypedDict, total=False):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["application/pdf"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource, {"arbitrary_types_allowed": True}
)


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaPlainTextSource(TypedDict, total=False):
    data: Required[str]

    media_type: Required[Literal["text/plain"]]

    type: Required[Literal["text"]]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitation: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestCharLocationCitation,
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestPageLocationCitation,
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitationBetaRequestContentBlockLocationCitation,
]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlock(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[
        MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCacheControl
    ]

    citations: Optional[
        Iterable[
            MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlockCitation
        ]
    ]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource(
    TypedDict, total=False
):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    {"arbitrary_types_allowed": True},
)


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource(
    TypedDict, total=False
):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSource: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaBase64ImageSource,
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSourceBetaURLImageSource,
]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlock(
    TypedDict, total=False
):
    source: Required[
        MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockSource
    ]

    type: Required[Literal["image"]]

    cache_control: Optional[
        MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlockCacheControl
    ]


MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestTextBlock,
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1BetaRequestImageBlock,
]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSource(TypedDict, total=False):
    content: Required[
        Union[
            str,
            Iterable[MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSourceContentUnionMember1],
        ]
    ]

    type: Required[Literal["content"]]


class MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaUrlpdfSource(TypedDict, total=False):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1BetaRequestDocumentBlockSource: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaBase64PdfSource,
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaPlainTextSource,
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaContentBlockSource,
    MessageContentUnionMember1BetaRequestDocumentBlockSourceBetaUrlpdfSource,
]


class MessageContentUnionMember1BetaRequestDocumentBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1BetaRequestDocumentBlockCitations(TypedDict, total=False):
    enabled: bool


class MessageContentUnionMember1BetaRequestDocumentBlock(TypedDict, total=False):
    source: Required[MessageContentUnionMember1BetaRequestDocumentBlockSource]

    type: Required[Literal["document"]]

    cache_control: Optional[MessageContentUnionMember1BetaRequestDocumentBlockCacheControl]

    citations: MessageContentUnionMember1BetaRequestDocumentBlockCitations

    context: Optional[str]

    title: Optional[str]


class MessageContentUnionMember1BetaRequestThinkingBlock(TypedDict, total=False):
    signature: Required[str]

    thinking: Required[str]

    type: Required[Literal["thinking"]]


class MessageContentUnionMember1BetaRequestRedactedThinkingBlock(TypedDict, total=False):
    data: Required[str]

    type: Required[Literal["redacted_thinking"]]


MessageContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1BetaRequestTextBlock,
    MessageContentUnionMember1BetaRequestImageBlock,
    MessageContentUnionMember1BetaRequestToolUseBlock,
    MessageContentUnionMember1BetaRequestToolResultBlock,
    MessageContentUnionMember1BetaRequestDocumentBlock,
    MessageContentUnionMember1BetaRequestThinkingBlock,
    MessageContentUnionMember1BetaRequestRedactedThinkingBlock,
]


class Message(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageContentUnionMember1]]]

    role: Required[Literal["user", "assistant"]]


class SystemUnionMember1CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class SystemUnionMember1CitationBetaRequestCharLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class SystemUnionMember1CitationBetaRequestPageLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class SystemUnionMember1CitationBetaRequestContentBlockLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


SystemUnionMember1Citation: TypeAlias = Union[
    SystemUnionMember1CitationBetaRequestCharLocationCitation,
    SystemUnionMember1CitationBetaRequestPageLocationCitation,
    SystemUnionMember1CitationBetaRequestContentBlockLocationCitation,
]


class SystemUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[SystemUnionMember1CacheControl]

    citations: Optional[Iterable[SystemUnionMember1Citation]]


class ThinkingBetaThinkingConfigEnabled(TypedDict, total=False):
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


class ThinkingBetaThinkingConfigDisabled(TypedDict, total=False):
    type: Required[Literal["disabled"]]


Thinking: TypeAlias = Union[ThinkingBetaThinkingConfigEnabled, ThinkingBetaThinkingConfigDisabled]


class ToolChoiceBetaToolChoiceAuto(TypedDict, total=False):
    type: Required[Literal["auto"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool
    use.
    """


class ToolChoiceBetaToolChoiceAny(TypedDict, total=False):
    type: Required[Literal["any"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool
    use.
    """


class ToolChoiceBetaToolChoiceTool(TypedDict, total=False):
    name: Required[str]
    """The name of the tool to use."""

    type: Required[Literal["tool"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool
    use.
    """


class ToolChoiceBetaToolChoiceNone(TypedDict, total=False):
    type: Required[Literal["none"]]


ToolChoice: TypeAlias = Union[
    ToolChoiceBetaToolChoiceAuto,
    ToolChoiceBetaToolChoiceAny,
    ToolChoiceBetaToolChoiceTool,
    ToolChoiceBetaToolChoiceNone,
]


class ToolBetaToolInputSchemaTyped(TypedDict, total=False):
    type: Required[Literal["object"]]

    properties: Optional[object]


ToolBetaToolInputSchema: TypeAlias = Union[ToolBetaToolInputSchemaTyped, Dict[str, object]]


class ToolBetaToolCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBetaTool(TypedDict, total=False):
    input_schema: Required[ToolBetaToolInputSchema]
    """[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model
    will produce.
    """

    name: Required[str]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    cache_control: Optional[ToolBetaToolCacheControl]

    description: str
    """Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that
    the model has about what the tool is and how to use it, the better it will
    perform. You can use natural language descriptions to reinforce important
    aspects of the tool input JSON schema.
    """

    type: Optional[Literal["custom"]]


class ToolBetaComputerUseTool20241022CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBetaComputerUseTool20241022(TypedDict, total=False):
    display_height_px: Required[int]
    """The height of the display in pixels."""

    display_width_px: Required[int]
    """The width of the display in pixels."""

    name: Required[Literal["computer"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["computer_20241022"]]

    cache_control: Optional[ToolBetaComputerUseTool20241022CacheControl]

    display_number: Optional[int]
    """The X11 display number (e.g. 0, 1) for the display."""


class ToolBetaBashTool20241022CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBetaBashTool20241022(TypedDict, total=False):
    name: Required[Literal["bash"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["bash_20241022"]]

    cache_control: Optional[ToolBetaBashTool20241022CacheControl]


class ToolBetaTextEditor20241022CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBetaTextEditor20241022(TypedDict, total=False):
    name: Required[Literal["str_replace_editor"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["text_editor_20241022"]]

    cache_control: Optional[ToolBetaTextEditor20241022CacheControl]


class ToolBetaComputerUseTool20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBetaComputerUseTool20250124(TypedDict, total=False):
    display_height_px: Required[int]
    """The height of the display in pixels."""

    display_width_px: Required[int]
    """The width of the display in pixels."""

    name: Required[Literal["computer"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["computer_20250124"]]

    cache_control: Optional[ToolBetaComputerUseTool20250124CacheControl]

    display_number: Optional[int]
    """The X11 display number (e.g. 0, 1) for the display."""


class ToolBetaBashTool20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBetaBashTool20250124(TypedDict, total=False):
    name: Required[Literal["bash"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["bash_20250124"]]

    cache_control: Optional[ToolBetaBashTool20250124CacheControl]


class ToolBetaTextEditor20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBetaTextEditor20250124(TypedDict, total=False):
    name: Required[Literal["str_replace_editor"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["text_editor_20250124"]]

    cache_control: Optional[ToolBetaTextEditor20250124CacheControl]


Tool: TypeAlias = Union[
    ToolBetaTool,
    ToolBetaComputerUseTool20241022,
    ToolBetaBashTool20241022,
    ToolBetaTextEditor20241022,
    ToolBetaComputerUseTool20250124,
    ToolBetaBashTool20250124,
    ToolBetaTextEditor20250124,
]

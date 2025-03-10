# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo
from .._models import set_pydantic_config

__all__ = [
    "MessageCreateParams",
    "Message",
    "MessageContentUnionMember1",
    "MessageContentUnionMember1RequestTextBlock",
    "MessageContentUnionMember1RequestTextBlockCacheControl",
    "MessageContentUnionMember1RequestTextBlockCitation",
    "MessageContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation",
    "MessageContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation",
    "MessageContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation",
    "MessageContentUnionMember1RequestImageBlock",
    "MessageContentUnionMember1RequestImageBlockSource",
    "MessageContentUnionMember1RequestImageBlockSourceBase64ImageSource",
    "MessageContentUnionMember1RequestImageBlockSourceURLImageSource",
    "MessageContentUnionMember1RequestImageBlockCacheControl",
    "MessageContentUnionMember1RequestToolUseBlock",
    "MessageContentUnionMember1RequestToolUseBlockCacheControl",
    "MessageContentUnionMember1RequestToolResultBlock",
    "MessageContentUnionMember1RequestToolResultBlockCacheControl",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlock",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCacheControl",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitation",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlock",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSource",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSourceBase64ImageSource",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSourceURLImageSource",
    "MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockCacheControl",
    "MessageContentUnionMember1RequestDocumentBlock",
    "MessageContentUnionMember1RequestDocumentBlockSource",
    "MessageContentUnionMember1RequestDocumentBlockSourceBase64PdfSource",
    "MessageContentUnionMember1RequestDocumentBlockSourcePlainTextSource",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSource",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlock",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCacheControl",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitation",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlock",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSource",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSourceBase64ImageSource",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSourceURLImageSource",
    "MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockCacheControl",
    "MessageContentUnionMember1RequestDocumentBlockSourceUrlpdfSource",
    "MessageContentUnionMember1RequestDocumentBlockCacheControl",
    "MessageContentUnionMember1RequestDocumentBlockCitations",
    "MessageContentUnionMember1RequestThinkingBlock",
    "MessageContentUnionMember1RequestRedactedThinkingBlock",
    "Metadata",
    "SystemUnionMember1",
    "SystemUnionMember1CacheControl",
    "SystemUnionMember1Citation",
    "SystemUnionMember1CitationRequestCharLocationCitation",
    "SystemUnionMember1CitationRequestPageLocationCitation",
    "SystemUnionMember1CitationRequestContentBlockLocationCitation",
    "Thinking",
    "ThinkingThinkingConfigEnabled",
    "ThinkingThinkingConfigDisabled",
    "ToolChoice",
    "ToolChoiceToolChoiceAuto",
    "ToolChoiceToolChoiceAny",
    "ToolChoiceToolChoiceTool",
    "ToolChoiceToolChoiceNone",
    "Tool",
    "ToolTool",
    "ToolToolInputSchema",
    "ToolToolCacheControl",
    "ToolBashTool20250124",
    "ToolBashTool20250124CacheControl",
    "ToolTextEditor20250124",
    "ToolTextEditor20250124CacheControl",
]


class MessageCreateParams(TypedDict, total=False):
    max_tokens: Required[int]
    """The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter
    only specifies the absolute maximum number of tokens to generate.

    Different models have different maximum values for this parameter. See
    [models](https://docs.anthropic.com/en/docs/models-overview) for details.
    """

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

    metadata: Metadata
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

    system: Union[str, Iterable[SystemUnionMember1]]
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


class MessageContentUnionMember1RequestTextBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class MessageContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class MessageContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


MessageContentUnionMember1RequestTextBlockCitation: TypeAlias = Union[
    MessageContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation,
    MessageContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation,
    MessageContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation,
]


class MessageContentUnionMember1RequestTextBlock(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[MessageContentUnionMember1RequestTextBlockCacheControl]

    citations: Optional[Iterable[MessageContentUnionMember1RequestTextBlockCitation]]


class MessageContentUnionMember1RequestImageBlockSourceBase64ImageSource(TypedDict, total=False):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1RequestImageBlockSourceBase64ImageSource, {"arbitrary_types_allowed": True}
)


class MessageContentUnionMember1RequestImageBlockSourceURLImageSource(TypedDict, total=False):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1RequestImageBlockSource: TypeAlias = Union[
    MessageContentUnionMember1RequestImageBlockSourceBase64ImageSource,
    MessageContentUnionMember1RequestImageBlockSourceURLImageSource,
]


class MessageContentUnionMember1RequestImageBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestImageBlock(TypedDict, total=False):
    source: Required[MessageContentUnionMember1RequestImageBlockSource]

    type: Required[Literal["image"]]

    cache_control: Optional[MessageContentUnionMember1RequestImageBlockCacheControl]


class MessageContentUnionMember1RequestToolUseBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestToolUseBlock(TypedDict, total=False):
    id: Required[str]

    input: Required[object]

    name: Required[str]

    type: Required[Literal["tool_use"]]

    cache_control: Optional[MessageContentUnionMember1RequestToolUseBlockCacheControl]


class MessageContentUnionMember1RequestToolResultBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitation: TypeAlias = Union[
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation,
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation,
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation,
]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlock(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[
        MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCacheControl
    ]

    citations: Optional[
        Iterable[MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlockCitation]
    ]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSourceBase64ImageSource(
    TypedDict, total=False
):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSourceBase64ImageSource,
    {"arbitrary_types_allowed": True},
)


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSourceURLImageSource(
    TypedDict, total=False
):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSource: TypeAlias = Union[
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSourceBase64ImageSource,
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSourceURLImageSource,
]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlock(TypedDict, total=False):
    source: Required[MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockSource]

    type: Required[Literal["image"]]

    cache_control: Optional[
        MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlockCacheControl
    ]


MessageContentUnionMember1RequestToolResultBlockContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestTextBlock,
    MessageContentUnionMember1RequestToolResultBlockContentUnionMember1RequestImageBlock,
]


class MessageContentUnionMember1RequestToolResultBlock(TypedDict, total=False):
    tool_use_id: Required[str]

    type: Required[Literal["tool_result"]]

    cache_control: Optional[MessageContentUnionMember1RequestToolResultBlockCacheControl]

    content: Union[str, Iterable[MessageContentUnionMember1RequestToolResultBlockContentUnionMember1]]

    is_error: bool


class MessageContentUnionMember1RequestDocumentBlockSourceBase64PdfSource(TypedDict, total=False):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["application/pdf"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1RequestDocumentBlockSourceBase64PdfSource, {"arbitrary_types_allowed": True}
)


class MessageContentUnionMember1RequestDocumentBlockSourcePlainTextSource(TypedDict, total=False):
    data: Required[str]

    media_type: Required[Literal["text/plain"]]

    type: Required[Literal["text"]]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation(
    TypedDict, total=False
):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitation: TypeAlias = Union[
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestCharLocationCitation,
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestPageLocationCitation,
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitationRequestContentBlockLocationCitation,
]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlock(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[
        MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCacheControl
    ]

    citations: Optional[
        Iterable[
            MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlockCitation
        ]
    ]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSourceBase64ImageSource(
    TypedDict, total=False
):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]

    media_type: Required[Literal["image/jpeg", "image/png", "image/gif", "image/webp"]]

    type: Required[Literal["base64"]]


set_pydantic_config(
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSourceBase64ImageSource,
    {"arbitrary_types_allowed": True},
)


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSourceURLImageSource(
    TypedDict, total=False
):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSource: TypeAlias = Union[
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSourceBase64ImageSource,
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSourceURLImageSource,
]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockCacheControl(
    TypedDict, total=False
):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlock(
    TypedDict, total=False
):
    source: Required[
        MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockSource
    ]

    type: Required[Literal["image"]]

    cache_control: Optional[
        MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlockCacheControl
    ]


MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestTextBlock,
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1RequestImageBlock,
]


class MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSource(TypedDict, total=False):
    content: Required[
        Union[str, Iterable[MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSourceContentUnionMember1]]
    ]

    type: Required[Literal["content"]]


class MessageContentUnionMember1RequestDocumentBlockSourceUrlpdfSource(TypedDict, total=False):
    type: Required[Literal["url"]]

    url: Required[str]


MessageContentUnionMember1RequestDocumentBlockSource: TypeAlias = Union[
    MessageContentUnionMember1RequestDocumentBlockSourceBase64PdfSource,
    MessageContentUnionMember1RequestDocumentBlockSourcePlainTextSource,
    MessageContentUnionMember1RequestDocumentBlockSourceContentBlockSource,
    MessageContentUnionMember1RequestDocumentBlockSourceUrlpdfSource,
]


class MessageContentUnionMember1RequestDocumentBlockCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class MessageContentUnionMember1RequestDocumentBlockCitations(TypedDict, total=False):
    enabled: bool


class MessageContentUnionMember1RequestDocumentBlock(TypedDict, total=False):
    source: Required[MessageContentUnionMember1RequestDocumentBlockSource]

    type: Required[Literal["document"]]

    cache_control: Optional[MessageContentUnionMember1RequestDocumentBlockCacheControl]

    citations: MessageContentUnionMember1RequestDocumentBlockCitations

    context: Optional[str]

    title: Optional[str]


class MessageContentUnionMember1RequestThinkingBlock(TypedDict, total=False):
    signature: Required[str]

    thinking: Required[str]

    type: Required[Literal["thinking"]]


class MessageContentUnionMember1RequestRedactedThinkingBlock(TypedDict, total=False):
    data: Required[str]

    type: Required[Literal["redacted_thinking"]]


MessageContentUnionMember1: TypeAlias = Union[
    MessageContentUnionMember1RequestTextBlock,
    MessageContentUnionMember1RequestImageBlock,
    MessageContentUnionMember1RequestToolUseBlock,
    MessageContentUnionMember1RequestToolResultBlock,
    MessageContentUnionMember1RequestDocumentBlock,
    MessageContentUnionMember1RequestThinkingBlock,
    MessageContentUnionMember1RequestRedactedThinkingBlock,
]


class Message(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageContentUnionMember1]]]

    role: Required[Literal["user", "assistant"]]


class Metadata(TypedDict, total=False):
    user_id: Optional[str]
    """An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use
    this id to help detect abuse. Do not include any identifying information such as
    name, email address, or phone number.
    """


class SystemUnionMember1CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class SystemUnionMember1CitationRequestCharLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_char_index: Required[int]

    start_char_index: Required[int]

    type: Required[Literal["char_location"]]


class SystemUnionMember1CitationRequestPageLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_page_number: Required[int]

    start_page_number: Required[int]

    type: Required[Literal["page_location"]]


class SystemUnionMember1CitationRequestContentBlockLocationCitation(TypedDict, total=False):
    cited_text: Required[str]

    document_index: Required[int]

    document_title: Required[Optional[str]]

    end_block_index: Required[int]

    start_block_index: Required[int]

    type: Required[Literal["content_block_location"]]


SystemUnionMember1Citation: TypeAlias = Union[
    SystemUnionMember1CitationRequestCharLocationCitation,
    SystemUnionMember1CitationRequestPageLocationCitation,
    SystemUnionMember1CitationRequestContentBlockLocationCitation,
]


class SystemUnionMember1(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    cache_control: Optional[SystemUnionMember1CacheControl]

    citations: Optional[Iterable[SystemUnionMember1Citation]]


class ThinkingThinkingConfigEnabled(TypedDict, total=False):
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


class ThinkingThinkingConfigDisabled(TypedDict, total=False):
    type: Required[Literal["disabled"]]


Thinking: TypeAlias = Union[ThinkingThinkingConfigEnabled, ThinkingThinkingConfigDisabled]


class ToolChoiceToolChoiceAuto(TypedDict, total=False):
    type: Required[Literal["auto"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool
    use.
    """


class ToolChoiceToolChoiceAny(TypedDict, total=False):
    type: Required[Literal["any"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool
    use.
    """


class ToolChoiceToolChoiceTool(TypedDict, total=False):
    name: Required[str]
    """The name of the tool to use."""

    type: Required[Literal["tool"]]

    disable_parallel_tool_use: bool
    """Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool
    use.
    """


class ToolChoiceToolChoiceNone(TypedDict, total=False):
    type: Required[Literal["none"]]


ToolChoice: TypeAlias = Union[
    ToolChoiceToolChoiceAuto, ToolChoiceToolChoiceAny, ToolChoiceToolChoiceTool, ToolChoiceToolChoiceNone
]


class ToolToolInputSchemaTyped(TypedDict, total=False):
    type: Required[Literal["object"]]

    properties: Optional[object]


ToolToolInputSchema: TypeAlias = Union[ToolToolInputSchemaTyped, Dict[str, object]]


class ToolToolCacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolTool(TypedDict, total=False):
    input_schema: Required[ToolToolInputSchema]
    """[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model
    will produce.
    """

    name: Required[str]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    cache_control: Optional[ToolToolCacheControl]

    description: str
    """Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that
    the model has about what the tool is and how to use it, the better it will
    perform. You can use natural language descriptions to reinforce important
    aspects of the tool input JSON schema.
    """


class ToolBashTool20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolBashTool20250124(TypedDict, total=False):
    name: Required[Literal["bash"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["bash_20250124"]]

    cache_control: Optional[ToolBashTool20250124CacheControl]


class ToolTextEditor20250124CacheControl(TypedDict, total=False):
    type: Required[Literal["ephemeral"]]


class ToolTextEditor20250124(TypedDict, total=False):
    name: Required[Literal["str_replace_editor"]]
    """Name of the tool.

    This is how the tool will be called by the model and in tool_use blocks.
    """

    type: Required[Literal["text_editor_20250124"]]

    cache_control: Optional[ToolTextEditor20250124CacheControl]


Tool: TypeAlias = Union[ToolTool, ToolBashTool20250124, ToolTextEditor20250124]

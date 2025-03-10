# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable

import httpx

from ...types import message_create_params, message_count_tokens_params, message_count_tokens_beta_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .batches.batches import (
    BatchesResource,
    AsyncBatchesResource,
    BatchesResourceWithRawResponse,
    AsyncBatchesResourceWithRawResponse,
    BatchesResourceWithStreamingResponse,
    AsyncBatchesResourceWithStreamingResponse,
)
from .batches_beta_true import (
    BatchesBetaTrueResource,
    AsyncBatchesBetaTrueResource,
    BatchesBetaTrueResourceWithRawResponse,
    AsyncBatchesBetaTrueResourceWithRawResponse,
    BatchesBetaTrueResourceWithStreamingResponse,
    AsyncBatchesBetaTrueResourceWithStreamingResponse,
)
from ...types.message_create_response import MessageCreateResponse
from ...types.message_count_tokens_response import MessageCountTokensResponse
from ...types.message_count_tokens_beta_response import MessageCountTokensBetaResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def batches(self) -> BatchesResource:
        return BatchesResource(self._client)

    @cached_property
    def batches_beta_true(self) -> BatchesBetaTrueResource:
        return BatchesBetaTrueResource(self._client)

    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
        model: str,
        metadata: message_create_params.Metadata | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        system: Union[str, Iterable[message_create_params.SystemUnionMember1]] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        thinking: message_create_params.Thinking | NotGiven = NOT_GIVEN,
        tool_choice: message_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[message_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCreateResponse:
        """
        Send a structured list of input messages with text and/or image content, and the
        model will generate the next message in the conversation.

        The Messages API can be used for either single queries or stateless multi-turn
        conversations.

        Learn more about the Messages API in our [user guide](/en/docs/initial-setup)

        Args:
          max_tokens: The maximum number of tokens to generate before stopping.

              Note that our models may stop _before_ reaching this maximum. This parameter
              only specifies the absolute maximum number of tokens to generate.

              Different models have different maximum values for this parameter. See
              [models](https://docs.anthropic.com/en/docs/models-overview) for details.

          messages: Input messages.

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

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          metadata: An object describing metadata about the request.

          stop_sequences: Custom text sequences that will cause the model to stop generating.

              Our models will normally stop when they have naturally completed their turn,
              which will result in a response `stop_reason` of `"end_turn"`.

              If you want the model to stop generating when it encounters custom strings of
              text, you can use the `stop_sequences` parameter. If the model encounters one of
              the custom sequences, the response `stop_reason` value will be `"stop_sequence"`
              and the response `stop_sequence` value will contain the matched stop sequence.

          stream: Whether to incrementally stream the response using server-sent events.

              See [streaming](https://docs.anthropic.com/en/api/messages-streaming) for
              details.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).

          temperature: Amount of randomness injected into the response.

              Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0`
              for analytical / multiple choice, and closer to `1.0` for creative and
              generative tasks.

              Note that even with `temperature` of `0.0`, the results will not be fully
              deterministic.

          thinking: Configuration for enabling Claude's extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude's
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

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

          top_k: Only sample from the top K options for each subsequent token.

              Used to remove "long tail" low probability responses.
              [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

              Recommended for advanced use cases only. You usually only need to use
              `temperature`.

          top_p: Use nucleus sampling.

              In nucleus sampling, we compute the cumulative distribution over all the options
              for each subsequent token in decreasing probability order and cut it off once it
              reaches a particular probability specified by `top_p`. You should either alter
              `temperature` or `top_p`, but not both.

              Recommended for advanced use cases only. You usually only need to use
              `temperature`.

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/messages",
            body=maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "metadata": metadata,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "system": system,
                    "temperature": temperature,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    def count_tokens(
        self,
        *,
        messages: Iterable[message_count_tokens_params.Message],
        model: str,
        system: Union[str, Iterable[message_count_tokens_params.SystemUnionMember1]] | NotGiven = NOT_GIVEN,
        thinking: message_count_tokens_params.Thinking | NotGiven = NOT_GIVEN,
        tool_choice: message_count_tokens_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[message_count_tokens_params.Tool] | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCountTokensResponse:
        """
        Count the number of tokens in a Message.

        The Token Count API can be used to count the number of tokens in a Message,
        including tools, images, and documents, without creating it.

        Learn more about token counting in our
        [user guide](/en/docs/build-with-claude/token-counting)

        Args:
          messages: Input messages.

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

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).

          thinking: Configuration for enabling Claude's extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude's
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

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

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/messages/count_tokens",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "system": system,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                message_count_tokens_params.MessageCountTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCountTokensResponse,
        )

    def count_tokens_beta(
        self,
        *,
        messages: Iterable[message_count_tokens_beta_params.Message],
        model: str,
        system: Union[str, Iterable[message_count_tokens_beta_params.SystemUnionMember1]] | NotGiven = NOT_GIVEN,
        thinking: message_count_tokens_beta_params.Thinking | NotGiven = NOT_GIVEN,
        tool_choice: message_count_tokens_beta_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[message_count_tokens_beta_params.Tool] | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCountTokensBetaResponse:
        """
        Count the number of tokens in a Message.

        The Token Count API can be used to count the number of tokens in a Message,
        including tools, images, and documents, without creating it.

        Learn more about token counting in our
        [user guide](/en/docs/build-with-claude/token-counting)

        Args:
          messages: Input messages.

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

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).

          thinking: Configuration for enabling Claude's extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude's
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

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

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/messages/count_tokens?beta=true",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "system": system,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                message_count_tokens_beta_params.MessageCountTokensBetaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCountTokensBetaResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def batches(self) -> AsyncBatchesResource:
        return AsyncBatchesResource(self._client)

    @cached_property
    def batches_beta_true(self) -> AsyncBatchesBetaTrueResource:
        return AsyncBatchesBetaTrueResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        max_tokens: int,
        messages: Iterable[message_create_params.Message],
        model: str,
        metadata: message_create_params.Metadata | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        system: Union[str, Iterable[message_create_params.SystemUnionMember1]] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        thinking: message_create_params.Thinking | NotGiven = NOT_GIVEN,
        tool_choice: message_create_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[message_create_params.Tool] | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCreateResponse:
        """
        Send a structured list of input messages with text and/or image content, and the
        model will generate the next message in the conversation.

        The Messages API can be used for either single queries or stateless multi-turn
        conversations.

        Learn more about the Messages API in our [user guide](/en/docs/initial-setup)

        Args:
          max_tokens: The maximum number of tokens to generate before stopping.

              Note that our models may stop _before_ reaching this maximum. This parameter
              only specifies the absolute maximum number of tokens to generate.

              Different models have different maximum values for this parameter. See
              [models](https://docs.anthropic.com/en/docs/models-overview) for details.

          messages: Input messages.

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

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          metadata: An object describing metadata about the request.

          stop_sequences: Custom text sequences that will cause the model to stop generating.

              Our models will normally stop when they have naturally completed their turn,
              which will result in a response `stop_reason` of `"end_turn"`.

              If you want the model to stop generating when it encounters custom strings of
              text, you can use the `stop_sequences` parameter. If the model encounters one of
              the custom sequences, the response `stop_reason` value will be `"stop_sequence"`
              and the response `stop_sequence` value will contain the matched stop sequence.

          stream: Whether to incrementally stream the response using server-sent events.

              See [streaming](https://docs.anthropic.com/en/api/messages-streaming) for
              details.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).

          temperature: Amount of randomness injected into the response.

              Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0`
              for analytical / multiple choice, and closer to `1.0` for creative and
              generative tasks.

              Note that even with `temperature` of `0.0`, the results will not be fully
              deterministic.

          thinking: Configuration for enabling Claude's extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude's
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

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

          top_k: Only sample from the top K options for each subsequent token.

              Used to remove "long tail" low probability responses.
              [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

              Recommended for advanced use cases only. You usually only need to use
              `temperature`.

          top_p: Use nucleus sampling.

              In nucleus sampling, we compute the cumulative distribution over all the options
              for each subsequent token in decreasing probability order and cut it off once it
              reaches a particular probability specified by `top_p`. You should either alter
              `temperature` or `top_p`, but not both.

              Recommended for advanced use cases only. You usually only need to use
              `temperature`.

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/messages",
            body=await async_maybe_transform(
                {
                    "max_tokens": max_tokens,
                    "messages": messages,
                    "model": model,
                    "metadata": metadata,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "system": system,
                    "temperature": temperature,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                message_create_params.MessageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCreateResponse,
        )

    async def count_tokens(
        self,
        *,
        messages: Iterable[message_count_tokens_params.Message],
        model: str,
        system: Union[str, Iterable[message_count_tokens_params.SystemUnionMember1]] | NotGiven = NOT_GIVEN,
        thinking: message_count_tokens_params.Thinking | NotGiven = NOT_GIVEN,
        tool_choice: message_count_tokens_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[message_count_tokens_params.Tool] | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCountTokensResponse:
        """
        Count the number of tokens in a Message.

        The Token Count API can be used to count the number of tokens in a Message,
        including tools, images, and documents, without creating it.

        Learn more about token counting in our
        [user guide](/en/docs/build-with-claude/token-counting)

        Args:
          messages: Input messages.

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

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).

          thinking: Configuration for enabling Claude's extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude's
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

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

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/messages/count_tokens",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "system": system,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                message_count_tokens_params.MessageCountTokensParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCountTokensResponse,
        )

    async def count_tokens_beta(
        self,
        *,
        messages: Iterable[message_count_tokens_beta_params.Message],
        model: str,
        system: Union[str, Iterable[message_count_tokens_beta_params.SystemUnionMember1]] | NotGiven = NOT_GIVEN,
        thinking: message_count_tokens_beta_params.Thinking | NotGiven = NOT_GIVEN,
        tool_choice: message_count_tokens_beta_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[message_count_tokens_beta_params.Tool] | NotGiven = NOT_GIVEN,
        anthropic_beta: List[str] | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MessageCountTokensBetaResponse:
        """
        Count the number of tokens in a Message.

        The Token Count API can be used to count the number of tokens in a Message,
        including tools, images, and documents, without creating it.

        Learn more about token counting in our
        [user guide](/en/docs/build-with-claude/token-counting)

        Args:
          messages: Input messages.

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

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          system: System prompt.

              A system prompt is a way of providing context and instructions to Claude, such
              as specifying a particular goal or role. See our
              [guide to system prompts](https://docs.anthropic.com/en/docs/system-prompts).

          thinking: Configuration for enabling Claude's extended thinking.

              When enabled, responses include `thinking` content blocks showing Claude's
              thinking process before the final answer. Requires a minimum budget of 1,024
              tokens and counts towards your `max_tokens` limit.

              See
              [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
              for details.

          tool_choice: How the model should use the provided tools. The model can use a specific tool,
              any available tool, decide by itself, or not use tools at all.

          tools: Definitions of tools that the model may use.

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

          anthropic_beta: Optional header to specify the beta version(s) you want to use.

              To use multiple betas, use a comma separated list like `beta1,beta2` or specify
              the header multiple times for each beta.

          anthropic_version: The version of the Anthropic API you want to use.

              Read more about versioning and our version history
              [here](https://docs.anthropic.com/en/api/versioning).

          x_api_key: Your unique API key for authentication.

              This key is required in the header of all API requests, to authenticate your
              account and access Anthropic's services. Get your API key through the
              [Console](https://console.anthropic.com/settings/keys). Each key is scoped to a
              Workspace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "anthropic-beta": ",".join(anthropic_beta) if is_given(anthropic_beta) else NOT_GIVEN,
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/messages/count_tokens?beta=true",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "system": system,
                    "thinking": thinking,
                    "tool_choice": tool_choice,
                    "tools": tools,
                },
                message_count_tokens_beta_params.MessageCountTokensBetaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageCountTokensBetaResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_raw_response_wrapper(
            messages.create,
        )
        self.count_tokens = to_raw_response_wrapper(
            messages.count_tokens,
        )
        self.count_tokens_beta = to_raw_response_wrapper(
            messages.count_tokens_beta,
        )

    @cached_property
    def batches(self) -> BatchesResourceWithRawResponse:
        return BatchesResourceWithRawResponse(self._messages.batches)

    @cached_property
    def batches_beta_true(self) -> BatchesBetaTrueResourceWithRawResponse:
        return BatchesBetaTrueResourceWithRawResponse(self._messages.batches_beta_true)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_raw_response_wrapper(
            messages.create,
        )
        self.count_tokens = async_to_raw_response_wrapper(
            messages.count_tokens,
        )
        self.count_tokens_beta = async_to_raw_response_wrapper(
            messages.count_tokens_beta,
        )

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithRawResponse:
        return AsyncBatchesResourceWithRawResponse(self._messages.batches)

    @cached_property
    def batches_beta_true(self) -> AsyncBatchesBetaTrueResourceWithRawResponse:
        return AsyncBatchesBetaTrueResourceWithRawResponse(self._messages.batches_beta_true)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.create = to_streamed_response_wrapper(
            messages.create,
        )
        self.count_tokens = to_streamed_response_wrapper(
            messages.count_tokens,
        )
        self.count_tokens_beta = to_streamed_response_wrapper(
            messages.count_tokens_beta,
        )

    @cached_property
    def batches(self) -> BatchesResourceWithStreamingResponse:
        return BatchesResourceWithStreamingResponse(self._messages.batches)

    @cached_property
    def batches_beta_true(self) -> BatchesBetaTrueResourceWithStreamingResponse:
        return BatchesBetaTrueResourceWithStreamingResponse(self._messages.batches_beta_true)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.create = async_to_streamed_response_wrapper(
            messages.create,
        )
        self.count_tokens = async_to_streamed_response_wrapper(
            messages.count_tokens,
        )
        self.count_tokens_beta = async_to_streamed_response_wrapper(
            messages.count_tokens_beta,
        )

    @cached_property
    def batches(self) -> AsyncBatchesResourceWithStreamingResponse:
        return AsyncBatchesResourceWithStreamingResponse(self._messages.batches)

    @cached_property
    def batches_beta_true(self) -> AsyncBatchesBetaTrueResourceWithStreamingResponse:
        return AsyncBatchesBetaTrueResourceWithStreamingResponse(self._messages.batches_beta_true)

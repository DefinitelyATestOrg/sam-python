# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import complete_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.complete_create_response import CompleteCreateResponse

__all__ = ["CompleteResource", "AsyncCompleteResource"]


class CompleteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return CompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return CompleteResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        max_tokens_to_sample: int,
        model: str,
        prompt: str,
        metadata: complete_create_params.Metadata | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompleteCreateResponse:
        """[Legacy] Create a Text Completion.

        The Text Completions API is a legacy API.

        We recommend using the
        [Messages API](https://docs.anthropic.com/en/api/messages) going forward.

        Future models and features will not be compatible with Text Completions. See our
        [migration guide](https://docs.anthropic.com/en/api/migrating-from-text-completions-to-messages)
        for guidance in migrating from Text Completions to Messages.

        Args:
          max_tokens_to_sample: The maximum number of tokens to generate before stopping.

              Note that our models may stop _before_ reaching this maximum. This parameter
              only specifies the absolute maximum number of tokens to generate.

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          prompt: The prompt that you want Claude to complete.

              For proper response generation you will need to format your prompt using
              alternating `\n\nHuman:` and `\n\nAssistant:` conversational turns. For example:

              ```
              "\n\nHuman: {userQuestion}\n\nAssistant:"
              ```

              See [prompt validation](https://docs.anthropic.com/en/api/prompt-validation) and
              our guide to
              [prompt design](https://docs.anthropic.com/en/docs/intro-to-prompting) for more
              details.

          metadata: An object describing metadata about the request.

          stop_sequences: Sequences that will cause the model to stop generating.

              Our models stop on `"\n\nHuman:"`, and may include additional built-in stop
              sequences in the future. By providing the stop_sequences parameter, you may
              include additional strings that will cause the model to stop generating.

          stream: Whether to incrementally stream the response using server-sent events.

              See [streaming](https://docs.anthropic.com/en/api/streaming) for details.

          temperature: Amount of randomness injected into the response.

              Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0`
              for analytical / multiple choice, and closer to `1.0` for creative and
              generative tasks.

              Note that even with `temperature` of `0.0`, the results will not be fully
              deterministic.

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
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/complete",
            body=maybe_transform(
                {
                    "max_tokens_to_sample": max_tokens_to_sample,
                    "model": model,
                    "prompt": prompt,
                    "metadata": metadata,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                complete_create_params.CompleteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompleteCreateResponse,
        )


class AsyncCompleteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompleteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompleteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompleteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/DefinitelyATestOrg/sam-python#with_streaming_response
        """
        return AsyncCompleteResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        max_tokens_to_sample: int,
        model: str,
        prompt: str,
        metadata: complete_create_params.Metadata | NotGiven = NOT_GIVEN,
        stop_sequences: List[str] | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_k: int | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        anthropic_version: str | NotGiven = NOT_GIVEN,
        x_api_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompleteCreateResponse:
        """[Legacy] Create a Text Completion.

        The Text Completions API is a legacy API.

        We recommend using the
        [Messages API](https://docs.anthropic.com/en/api/messages) going forward.

        Future models and features will not be compatible with Text Completions. See our
        [migration guide](https://docs.anthropic.com/en/api/migrating-from-text-completions-to-messages)
        for guidance in migrating from Text Completions to Messages.

        Args:
          max_tokens_to_sample: The maximum number of tokens to generate before stopping.

              Note that our models may stop _before_ reaching this maximum. This parameter
              only specifies the absolute maximum number of tokens to generate.

          model: The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional
              details and options.

          prompt: The prompt that you want Claude to complete.

              For proper response generation you will need to format your prompt using
              alternating `\n\nHuman:` and `\n\nAssistant:` conversational turns. For example:

              ```
              "\n\nHuman: {userQuestion}\n\nAssistant:"
              ```

              See [prompt validation](https://docs.anthropic.com/en/api/prompt-validation) and
              our guide to
              [prompt design](https://docs.anthropic.com/en/docs/intro-to-prompting) for more
              details.

          metadata: An object describing metadata about the request.

          stop_sequences: Sequences that will cause the model to stop generating.

              Our models stop on `"\n\nHuman:"`, and may include additional built-in stop
              sequences in the future. By providing the stop_sequences parameter, you may
              include additional strings that will cause the model to stop generating.

          stream: Whether to incrementally stream the response using server-sent events.

              See [streaming](https://docs.anthropic.com/en/api/streaming) for details.

          temperature: Amount of randomness injected into the response.

              Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0`
              for analytical / multiple choice, and closer to `1.0` for creative and
              generative tasks.

              Note that even with `temperature` of `0.0`, the results will not be fully
              deterministic.

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
                    "anthropic-version": anthropic_version,
                    "x-api-key": x_api_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/complete",
            body=await async_maybe_transform(
                {
                    "max_tokens_to_sample": max_tokens_to_sample,
                    "model": model,
                    "prompt": prompt,
                    "metadata": metadata,
                    "stop_sequences": stop_sequences,
                    "stream": stream,
                    "temperature": temperature,
                    "top_k": top_k,
                    "top_p": top_p,
                },
                complete_create_params.CompleteCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompleteCreateResponse,
        )


class CompleteResourceWithRawResponse:
    def __init__(self, complete: CompleteResource) -> None:
        self._complete = complete

        self.create = to_raw_response_wrapper(
            complete.create,
        )


class AsyncCompleteResourceWithRawResponse:
    def __init__(self, complete: AsyncCompleteResource) -> None:
        self._complete = complete

        self.create = async_to_raw_response_wrapper(
            complete.create,
        )


class CompleteResourceWithStreamingResponse:
    def __init__(self, complete: CompleteResource) -> None:
        self._complete = complete

        self.create = to_streamed_response_wrapper(
            complete.create,
        )


class AsyncCompleteResourceWithStreamingResponse:
    def __init__(self, complete: AsyncCompleteResource) -> None:
        self._complete = complete

        self.create = async_to_streamed_response_wrapper(
            complete.create,
        )

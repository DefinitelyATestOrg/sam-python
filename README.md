# Sam Python API library

[![PyPI version](https://img.shields.io/pypi/v/sam.svg)](https://pypi.org/project/sam/)

The Sam Python library provides convenient access to the Sam REST API from any Python 3.7+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The REST API documentation can be found [on docs.sam.com](https://docs.sam.com). The full API of this library can be found in [api.md](https://www.github.com/DefinitelyATestOrg/sam-python/blob/main/api.md).

## Installation

```sh
pip install sam
```

## Usage

The full API of this library can be found in [api.md](https://www.github.com/DefinitelyATestOrg/sam-python/blob/main/api.md).

```python
from sam import Sam

client = Sam()

account_retrieve_response = client.customers.accounts.retrieve(
    "REPLACE_ME",
    customer_id="REPLACE_ME",
)
print(account_retrieve_response.account)
```

## Async usage

Simply import `AsyncSam` instead of `Sam` and use `await` with each API call:

```python
import asyncio
from sam import AsyncSam

client = AsyncSam()


async def main() -> None:
    account_retrieve_response = await client.customers.accounts.retrieve(
        "REPLACE_ME",
        customer_id="REPLACE_ME",
    )
    print(account_retrieve_response.account)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev), which provide helper methods for things like:

- Serializing back into JSON, `model.model_dump_json(indent=2, exclude_unset=True)`
- Converting to a dictionary, `model.model_dump(exclude_unset=True)`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `sam.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `sam.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `sam.APIError`.

```python
import sam
from sam import Sam

client = Sam()

try:
    client.customers.accounts.retrieve(
        "REPLACE_ME",
        customer_id="REPLACE_ME",
    )
except sam.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except sam.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except sam.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from sam import Sam

# Configure the default for all requests:
client = Sam(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).customers.accounts.retrieve(
    "REPLACE_ME",
    customer_id="REPLACE_ME",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from sam import Sam

# Configure the default for all requests:
client = Sam(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Sam(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).customers.accounts.retrieve(
    "REPLACE_ME",
    customer_id="REPLACE_ME",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `SAM_LOG` to `debug`.

```shell
$ export SAM_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call.

```py
from sam import Sam

client = Sam()
response = client.customers.accounts.with_raw_response.retrieve(
    "REPLACE_ME",
    customer_id="REPLACE_ME",
)
print(response.headers.get('X-My-Header'))

account = response.parse()  # get the object that `customers.accounts.retrieve()` would have returned
print(account.account)
```

These methods return an [`APIResponse`](https://github.com/DefinitelyATestOrg/sam-python/tree/main/src/sam/_response.py) object.

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/#client-instances) functionality

```python
import httpx
from sam import Sam

client = Sam(
    # Or use the `SAM_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/DefinitelyATestOrg/sam-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.

# Messages

Types:

```python
from sam.types import (
    MessageCreateResponse,
    MessageCountTokensResponse,
    MessageCountTokensBetaResponse,
)
```

Methods:

- <code title="post /v1/messages">client.messages.<a href="./src/sam/resources/messages/messages.py">create</a>(\*\*<a href="src/sam/types/message_create_params.py">params</a>) -> <a href="./src/sam/types/message_create_response.py">MessageCreateResponse</a></code>
- <code title="post /v1/messages/count_tokens">client.messages.<a href="./src/sam/resources/messages/messages.py">count_tokens</a>(\*\*<a href="src/sam/types/message_count_tokens_params.py">params</a>) -> <a href="./src/sam/types/message_count_tokens_response.py">MessageCountTokensResponse</a></code>
- <code title="post /v1/messages/count_tokens?beta=true">client.messages.<a href="./src/sam/resources/messages/messages.py">count_tokens_beta</a>(\*\*<a href="src/sam/types/message_count_tokens_beta_params.py">params</a>) -> <a href="./src/sam/types/message_count_tokens_beta_response.py">MessageCountTokensBetaResponse</a></code>

## Batches

Types:

```python
from sam.types.messages import (
    BatchCreateResponse,
    BatchRetrieveResponse,
    BatchListResponse,
    BatchDeleteResponse,
    BatchCancelResponse,
    BatchCancelBetaResponse,
    BatchResultsResponse,
    BatchResultsBetaResponse,
)
```

Methods:

- <code title="post /v1/messages/batches">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">create</a>(\*\*<a href="src/sam/types/messages/batch_create_params.py">params</a>) -> <a href="./src/sam/types/messages/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="get /v1/messages/batches/{message_batch_id}">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">retrieve</a>(message_batch_id) -> <a href="./src/sam/types/messages/batch_retrieve_response.py">BatchRetrieveResponse</a></code>
- <code title="get /v1/messages/batches">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">list</a>(\*\*<a href="src/sam/types/messages/batch_list_params.py">params</a>) -> <a href="./src/sam/types/messages/batch_list_response.py">BatchListResponse</a></code>
- <code title="delete /v1/messages/batches/{message_batch_id}">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">delete</a>(message_batch_id) -> <a href="./src/sam/types/messages/batch_delete_response.py">BatchDeleteResponse</a></code>
- <code title="post /v1/messages/batches/{message_batch_id}/cancel">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">cancel</a>(message_batch_id) -> <a href="./src/sam/types/messages/batch_cancel_response.py">BatchCancelResponse</a></code>
- <code title="post /v1/messages/batches/{message_batch_id}/cancel?beta=true">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">cancel_beta</a>(message_batch_id) -> <a href="./src/sam/types/messages/batch_cancel_beta_response.py">BatchCancelBetaResponse</a></code>
- <code title="get /v1/messages/batches/{message_batch_id}/results">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">results</a>(message_batch_id) -> <a href="./src/sam/types/messages/batch_results_response.py">JSONLDecoder[BatchResultsResponse]</a></code>
- <code title="get /v1/messages/batches/{message_batch_id}/results?beta=true">client.messages.batches.<a href="./src/sam/resources/messages/batches/batches.py">results_beta</a>(message_batch_id) -> <a href="./src/sam/types/messages/batch_results_beta_response.py">JSONLDecoder[BatchResultsBetaResponse]</a></code>

### BetaTrue

Types:

```python
from sam.types.messages.batches import BetaTrueRetrieveResponse, BetaTrueDeleteResponse
```

Methods:

- <code title="get /v1/messages/batches/{message_batch_id}?beta=true">client.messages.batches.beta_true.<a href="./src/sam/resources/messages/batches/beta_true.py">retrieve</a>(message_batch_id) -> <a href="./src/sam/types/messages/batches/beta_true_retrieve_response.py">BetaTrueRetrieveResponse</a></code>
- <code title="delete /v1/messages/batches/{message_batch_id}?beta=true">client.messages.batches.beta_true.<a href="./src/sam/resources/messages/batches/beta_true.py">delete</a>(message_batch_id) -> <a href="./src/sam/types/messages/batches/beta_true_delete_response.py">BetaTrueDeleteResponse</a></code>

## BatchesBetaTrue

Types:

```python
from sam.types.messages import BatchesBetaTrueCreateResponse, BatchesBetaTrueListResponse
```

Methods:

- <code title="post /v1/messages/batches?beta=true">client.messages.batches_beta_true.<a href="./src/sam/resources/messages/batches_beta_true.py">create</a>(\*\*<a href="src/sam/types/messages/batches_beta_true_create_params.py">params</a>) -> <a href="./src/sam/types/messages/batches_beta_true_create_response.py">BatchesBetaTrueCreateResponse</a></code>
- <code title="get /v1/messages/batches?beta=true">client.messages.batches_beta_true.<a href="./src/sam/resources/messages/batches_beta_true.py">list</a>(\*\*<a href="src/sam/types/messages/batches_beta_true_list_params.py">params</a>) -> <a href="./src/sam/types/messages/batches_beta_true_list_response.py">BatchesBetaTrueListResponse</a></code>

# Complete

Types:

```python
from sam.types import CompleteCreateResponse
```

Methods:

- <code title="post /v1/complete">client.complete.<a href="./src/sam/resources/complete.py">create</a>(\*\*<a href="src/sam/types/complete_create_params.py">params</a>) -> <a href="./src/sam/types/complete_create_response.py">CompleteCreateResponse</a></code>

# Models

Types:

```python
from sam.types import ModelRetrieveResponse, ModelListResponse, ModelRetrieveBetaResponse
```

Methods:

- <code title="get /v1/models/{model_id}">client.models.<a href="./src/sam/resources/models.py">retrieve</a>(model_id) -> <a href="./src/sam/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="get /v1/models">client.models.<a href="./src/sam/resources/models.py">list</a>(\*\*<a href="src/sam/types/model_list_params.py">params</a>) -> <a href="./src/sam/types/model_list_response.py">ModelListResponse</a></code>
- <code title="get /v1/models/{model_id}?beta=true">client.models.<a href="./src/sam/resources/models.py">retrieve_beta</a>(model_id) -> <a href="./src/sam/types/model_retrieve_beta_response.py">ModelRetrieveBetaResponse</a></code>

# MessagesBetaTrue

Types:

```python
from sam.types import MessagesBetaTrueCreateResponse
```

Methods:

- <code title="post /v1/messages?beta=true">client.messages_beta_true.<a href="./src/sam/resources/messages_beta_true.py">create</a>(\*\*<a href="src/sam/types/messages_beta_true_create_params.py">params</a>) -> <a href="./src/sam/types/messages_beta_true_create_response.py">MessagesBetaTrueCreateResponse</a></code>

# ModelsBetaTrue

Types:

```python
from sam.types import ModelsBetaTrueListResponse
```

Methods:

- <code title="get /v1/models?beta=true">client.models_beta_true.<a href="./src/sam/resources/models_beta_true.py">list</a>(\*\*<a href="src/sam/types/models_beta_true_list_params.py">params</a>) -> <a href="./src/sam/types/models_beta_true_list_response.py">ModelsBetaTrueListResponse</a></code>

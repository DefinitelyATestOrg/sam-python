# Customers

## Accounts

Types:

```python
from sam.types.customers import AccountRetrieveResponse, AccountListResponse
```

Methods:

- <code title="get /v1/customers/{customerId}/accounts/{accountId}">client.customers.accounts.<a href="./src/sam/resources/customers/accounts.py">retrieve</a>(account_id, \*, customer_id) -> <a href="./src/sam/types/customers/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /v1/customers/{customerId}/accounts">client.customers.accounts.<a href="./src/sam/resources/customers/accounts.py">list</a>(customer_id, \*\*<a href="src/sam/types/customers/account_list_params.py">params</a>) -> <a href="./src/sam/types/customers/account_list_response.py">AccountListResponse</a></code>
- <code title="post /v1/customers/{customerId}/accounts/{accountId}/close">client.customers.accounts.<a href="./src/sam/resources/customers/accounts.py">close</a>(account_id, \*, customer_id) -> None</code>

# V1

## Customers

### Accounts

Types:

```python
from sam.types.v1.customers import AccountsResponse, DetailedAccountResponse
```

Methods:

- <code title="get /v1/customers/{customerId}/accounts/{accountId}">client.v1.customers.accounts.<a href="./src/sam/resources/v1/customers/accounts.py">retrieve</a>(account_id, \*, customer_id) -> <a href="./src/sam/types/v1/customers/detailed_account_response.py">DetailedAccountResponse</a></code>
- <code title="get /v1/customers/{customerId}/accounts">client.v1.customers.accounts.<a href="./src/sam/resources/v1/customers/accounts.py">list</a>(customer_id, \*\*<a href="src/sam/types/v1/customers/account_list_params.py">params</a>) -> <a href="./src/sam/types/v1/customers/accounts_response.py">AccountsResponse</a></code>
- <code title="post /v1/customers/{customerId}/accounts/{accountId}/close">client.v1.customers.accounts.<a href="./src/sam/resources/v1/customers/accounts.py">close</a>(account_id, \*, customer_id) -> None</code>

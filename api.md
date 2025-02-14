# Store

Types:

```python
from sam.types import Order
```

## Orders

Methods:

- <code title="get /store/order/{orderId}">client.store.orders.<a href="./src/sam/resources/store/orders.py">retrieve</a>(order_id) -> <a href="./src/sam/types/order.py">Order</a></code>
- <code title="delete /store/order/{orderId}">client.store.orders.<a href="./src/sam/resources/store/orders.py">delete</a>(order_id) -> None</code>

# User

Types:

```python
from sam.types import User, UserLoginResponse
```

Methods:

- <code title="post /user">client.user.<a href="./src/sam/resources/user.py">create</a>(\*\*<a href="src/sam/types/user_create_params.py">params</a>) -> <a href="./src/sam/types/user.py">User</a></code>
- <code title="get /user/{username}">client.user.<a href="./src/sam/resources/user.py">retrieve</a>(username) -> <a href="./src/sam/types/user.py">User</a></code>
- <code title="put /user/{username}">client.user.<a href="./src/sam/resources/user.py">update</a>(path_username, \*\*<a href="src/sam/types/user_update_params.py">params</a>) -> None</code>
- <code title="delete /user/{username}">client.user.<a href="./src/sam/resources/user.py">delete</a>(username) -> None</code>
- <code title="post /user/createWithList">client.user.<a href="./src/sam/resources/user.py">create_list</a>(\*\*<a href="src/sam/types/user_create_list_params.py">params</a>) -> <a href="./src/sam/types/user.py">User</a></code>
- <code title="get /user/login">client.user.<a href="./src/sam/resources/user.py">login</a>(\*\*<a href="src/sam/types/user_login_params.py">params</a>) -> str</code>
- <code title="get /user/logout">client.user.<a href="./src/sam/resources/user.py">logout</a>() -> None</code>

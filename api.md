# Store

## Orders

Types:

```python
from sam.types.store import CoolOrder
```

Methods:

- <code title="get /store/order/{orderId}">client.store.orders.<a href="./src/sam/resources/store/orders.py">retrieve</a>(order_id) -> <a href="./src/sam/types/store/cool_order.py">CoolOrder</a></code>
- <code title="delete /store/order/{orderId}">client.store.orders.<a href="./src/sam/resources/store/orders.py">delete</a>(order_id) -> None</code>

# Users

Types:

```python
from sam.types import User, UserLoginResponse
```

Methods:

- <code title="post /user">client.users.<a href="./src/sam/resources/users.py">create</a>(\*\*<a href="src/sam/types/user_create_params.py">params</a>) -> <a href="./src/sam/types/user.py">User</a></code>
- <code title="get /user/{username}">client.users.<a href="./src/sam/resources/users.py">retrieve</a>(username) -> <a href="./src/sam/types/user.py">User</a></code>
- <code title="put /user/{username}">client.users.<a href="./src/sam/resources/users.py">update</a>(username_1, \*\*<a href="src/sam/types/user_update_params.py">params</a>) -> None</code>
- <code title="delete /user/{username}">client.users.<a href="./src/sam/resources/users.py">delete</a>(username) -> None</code>
- <code title="post /user/createWithList">client.users.<a href="./src/sam/resources/users.py">create_with_list</a>(\*\*<a href="src/sam/types/user_create_with_list_params.py">params</a>) -> <a href="./src/sam/types/user.py">User</a></code>
- <code title="get /user/login">client.users.<a href="./src/sam/resources/users.py">login</a>(\*\*<a href="src/sam/types/user_login_params.py">params</a>) -> str</code>
- <code title="get /user/logout">client.users.<a href="./src/sam/resources/users.py">logout</a>() -> None</code>

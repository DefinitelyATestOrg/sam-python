# Shared Types

```python
from sam_python.types import Order
```

# Pets

Types:

```python
from sam_python.types import APIResponse, Pet, PetFindByStatusResponse, PetFindByTagsResponse
```

Methods:

- <code title="post /pet/{petId}">client.pets.<a href="./src/sam_python/resources/pets.py">create</a>(pet_id, \*\*<a href="src/sam_python/types/pet_create_params.py">params</a>) -> None</code>
- <code title="get /pet/{petId}">client.pets.<a href="./src/sam_python/resources/pets.py">retrieve</a>(pet_id) -> <a href="./src/sam_python/types/pet.py">Pet</a></code>
- <code title="put /pet">client.pets.<a href="./src/sam_python/resources/pets.py">update</a>(\*\*<a href="src/sam_python/types/pet_update_params.py">params</a>) -> <a href="./src/sam_python/types/pet.py">Pet</a></code>
- <code title="delete /pet/{petId}">client.pets.<a href="./src/sam_python/resources/pets.py">delete</a>(pet_id) -> None</code>
- <code title="get /pet/findByStatus">client.pets.<a href="./src/sam_python/resources/pets.py">find_by_status</a>(\*\*<a href="src/sam_python/types/pet_find_by_status_params.py">params</a>) -> <a href="./src/sam_python/types/pet_find_by_status_response.py">PetFindByStatusResponse</a></code>
- <code title="get /pet/findByTags">client.pets.<a href="./src/sam_python/resources/pets.py">find_by_tags</a>(\*\*<a href="src/sam_python/types/pet_find_by_tags_params.py">params</a>) -> <a href="./src/sam_python/types/pet_find_by_tags_response.py">PetFindByTagsResponse</a></code>
- <code title="post /pet/{petId}/uploadImage">client.pets.<a href="./src/sam_python/resources/pets.py">upload_image</a>(pet_id, \*\*<a href="src/sam_python/types/pet_upload_image_params.py">params</a>) -> <a href="./src/sam_python/types/api_response.py">APIResponse</a></code>

# Stores

Types:

```python
from sam_python.types import StoreInventoryResponse
```

Methods:

- <code title="post /store/order">client.stores.<a href="./src/sam_python/resources/stores/stores.py">create_order</a>(\*\*<a href="src/sam_python/types/store_create_order_params.py">params</a>) -> <a href="./src/sam_python/types/shared/order.py">Order</a></code>
- <code title="get /store/inventory">client.stores.<a href="./src/sam_python/resources/stores/stores.py">inventory</a>() -> <a href="./src/sam_python/types/store_inventory_response.py">StoreInventoryResponse</a></code>

# Store

## Orders

Methods:

- <code title="get /store/order/{orderId}">client.store.orders.<a href="./src/sam_python/resources/store/orders.py">retrieve</a>(order_id) -> <a href="./src/sam_python/types/shared/order.py">Order</a></code>
- <code title="delete /store/order/{orderId}">client.store.orders.<a href="./src/sam_python/resources/store/orders.py">delete</a>(order_id) -> None</code>

# Users

Types:

```python
from sam_python.types import User, UserLoginResponse
```

Methods:

- <code title="post /user">client.users.<a href="./src/sam_python/resources/users.py">create</a>(\*\*<a href="src/sam_python/types/user_create_params.py">params</a>) -> None</code>
- <code title="get /user/{username}">client.users.<a href="./src/sam_python/resources/users.py">retrieve</a>(username) -> <a href="./src/sam_python/types/user.py">User</a></code>
- <code title="put /user/{username}">client.users.<a href="./src/sam_python/resources/users.py">update</a>(\*, path_username, \*\*<a href="src/sam_python/types/user_update_params.py">params</a>) -> None</code>
- <code title="delete /user/{username}">client.users.<a href="./src/sam_python/resources/users.py">delete</a>(username) -> None</code>
- <code title="post /user/createWithList">client.users.<a href="./src/sam_python/resources/users.py">create_with_list</a>(\*\*<a href="src/sam_python/types/user_create_with_list_params.py">params</a>) -> <a href="./src/sam_python/types/user.py">User</a></code>
- <code title="get /user/login">client.users.<a href="./src/sam_python/resources/users.py">login</a>(\*\*<a href="src/sam_python/types/user_login_params.py">params</a>) -> str</code>
- <code title="get /user/logout">client.users.<a href="./src/sam_python/resources/users.py">logout</a>() -> None</code>

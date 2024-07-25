# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sam_python import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam_python.types import (
    User,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Sam) -> None:
        user = client.users.create()
        assert user is None

    @parametrize
    def test_method_create_with_all_params(self, client: Sam) -> None:
        user = client.users.create(
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    def test_raw_response_create(self, client: Sam) -> None:
        response = client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_create(self, client: Sam) -> None:
        with client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Sam) -> None:
        user = client.users.retrieve(
            "username",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sam) -> None:
        response = client.users.with_raw_response.retrieve(
            "username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sam) -> None:
        with client.users.with_streaming_response.retrieve(
            "username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Sam) -> None:
        user = client.users.update(
            path_username="username",
        )
        assert user is None

    @parametrize
    def test_method_update_with_all_params(self, client: Sam) -> None:
        user = client.users.update(
            path_username="username",
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            body_username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    def test_raw_response_update(self, client: Sam) -> None:
        response = client.users.with_raw_response.update(
            path_username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_update(self, client: Sam) -> None:
        with client.users.with_streaming_response.update(
            path_username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_username` but received ''"):
            client.users.with_raw_response.update(
                path_username="",
                body_username="",
            )

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        user = client.users.delete(
            "username",
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:
        response = client.users.with_raw_response.delete(
            "username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.users.with_streaming_response.delete(
            "username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.users.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_with_list(self, client: Sam) -> None:
        user = client.users.create_with_list(
            body=[{}, {}, {}],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_create_with_list(self, client: Sam) -> None:
        response = client.users.with_raw_response.create_with_list(
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_create_with_list(self, client: Sam) -> None:
        with client.users.with_streaming_response.create_with_list(
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_login(self, client: Sam) -> None:
        user = client.users.login()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_method_login_with_all_params(self, client: Sam) -> None:
        user = client.users.login(
            password="password",
            username="username",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_raw_response_login(self, client: Sam) -> None:
        response = client.users.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_streaming_response_login(self, client: Sam) -> None:
        with client.users.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_logout(self, client: Sam) -> None:
        user = client.users.logout()
        assert user is None

    @parametrize
    def test_raw_response_logout(self, client: Sam) -> None:
        response = client.users.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_logout(self, client: Sam) -> None:
        with client.users.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSam) -> None:
        user = await async_client.users.create()
        assert user is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSam) -> None:
        user = await async_client.users.create(
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSam) -> None:
        response = await async_client.users.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSam) -> None:
        async with async_client.users.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSam) -> None:
        user = await async_client.users.retrieve(
            "username",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSam) -> None:
        response = await async_client.users.with_raw_response.retrieve(
            "username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSam) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.users.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSam) -> None:
        user = await async_client.users.update(
            path_username="username",
        )
        assert user is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSam) -> None:
        user = await async_client.users.update(
            path_username="username",
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            body_username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSam) -> None:
        response = await async_client.users.with_raw_response.update(
            path_username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSam) -> None:
        async with async_client.users.with_streaming_response.update(
            path_username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_username` but received ''"):
            await async_client.users.with_raw_response.update(
                path_username="",
                body_username="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        user = await async_client.users.delete(
            "username",
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:
        response = await async_client.users.with_raw_response.delete(
            "username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.users.with_streaming_response.delete(
            "username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSam) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.users.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_with_list(self, async_client: AsyncSam) -> None:
        user = await async_client.users.create_with_list(
            body=[{}, {}, {}],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_create_with_list(self, async_client: AsyncSam) -> None:
        response = await async_client.users.with_raw_response.create_with_list(
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_create_with_list(self, async_client: AsyncSam) -> None:
        async with async_client.users.with_streaming_response.create_with_list(
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_login(self, async_client: AsyncSam) -> None:
        user = await async_client.users.login()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncSam) -> None:
        user = await async_client.users.login(
            password="password",
            username="username",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_raw_response_login(self, async_client: AsyncSam) -> None:
        response = await async_client.users.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncSam) -> None:
        async with async_client.users.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_logout(self, async_client: AsyncSam) -> None:
        user = await async_client.users.logout()
        assert user is None

    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncSam) -> None:
        response = await async_client.users.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncSam) -> None:
        async with async_client.users.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

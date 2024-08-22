# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from sam_python import Sam, AsyncSam

from typing import Any, cast

from sam_python.types import Pet, PetFindByStatusResponse, PetFindByTagsResponse, APIResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from sam_python import Sam, AsyncSam
from tests.utils import assert_matches_type
from sam_python.types import pet_create_params
from sam_python.types import pet_update_params
from sam_python.types import pet_find_by_status_params
from sam_python.types import pet_find_by_tags_params
from sam_python.types import pet_upload_image_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestPets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Sam) -> None:
        pet = client.pets.create(
            pet_id=0,
        )
        assert pet is None

    @parametrize
    def test_method_create_with_all_params(self, client: Sam) -> None:
        pet = client.pets.create(
            pet_id=0,
            name="name",
            status="status",
        )
        assert pet is None

    @parametrize
    def test_raw_response_create(self, client: Sam) -> None:

        response = client.pets.with_raw_response.create(
            pet_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = response.parse()
        assert pet is None

    @parametrize
    def test_streaming_response_create(self, client: Sam) -> None:
        with client.pets.with_streaming_response.create(
            pet_id=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Sam) -> None:
        pet = client.pets.retrieve(
            0,
        )
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: Sam) -> None:

        response = client.pets.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = response.parse()
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sam) -> None:
        with client.pets.with_streaming_response.retrieve(
            0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = response.parse()
            assert_matches_type(Pet, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Sam) -> None:
        pet = client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Sam) -> None:
        pet = client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[{
                "id": 0,
                "name": "name",
            }, {
                "id": 0,
                "name": "name",
            }, {
                "id": 0,
                "name": "name",
            }],
        )
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Sam) -> None:

        response = client.pets.with_raw_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = response.parse()
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Sam) -> None:
        with client.pets.with_streaming_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = response.parse()
            assert_matches_type(Pet, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Sam) -> None:
        pet = client.pets.delete(
            pet_id=0,
        )
        assert pet is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Sam) -> None:
        pet = client.pets.delete(
            pet_id=0,
            api_key="api_key",
        )
        assert pet is None

    @parametrize
    def test_raw_response_delete(self, client: Sam) -> None:

        response = client.pets.with_raw_response.delete(
            pet_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = response.parse()
        assert pet is None

    @parametrize
    def test_streaming_response_delete(self, client: Sam) -> None:
        with client.pets.with_streaming_response.delete(
            pet_id=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_find_by_status(self, client: Sam) -> None:
        pet = client.pets.find_by_status()
        assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

    @parametrize
    def test_method_find_by_status_with_all_params(self, client: Sam) -> None:
        pet = client.pets.find_by_status(
            status="available",
        )
        assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

    @parametrize
    def test_raw_response_find_by_status(self, client: Sam) -> None:

        response = client.pets.with_raw_response.find_by_status()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = response.parse()
        assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

    @parametrize
    def test_streaming_response_find_by_status(self, client: Sam) -> None:
        with client.pets.with_streaming_response.find_by_status() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = response.parse()
            assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_find_by_tags(self, client: Sam) -> None:
        pet = client.pets.find_by_tags()
        assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

    @parametrize
    def test_method_find_by_tags_with_all_params(self, client: Sam) -> None:
        pet = client.pets.find_by_tags(
            tags=["string", "string", "string"],
        )
        assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

    @parametrize
    def test_raw_response_find_by_tags(self, client: Sam) -> None:

        response = client.pets.with_raw_response.find_by_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = response.parse()
        assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

    @parametrize
    def test_streaming_response_find_by_tags(self, client: Sam) -> None:
        with client.pets.with_streaming_response.find_by_tags() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = response.parse()
            assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_image(self, client: Sam) -> None:
        pet = client.pets.upload_image(
            pet_id=0,
            body=b'raw file contents',
        )
        assert_matches_type(APIResponse, pet, path=['response'])

    @parametrize
    def test_method_upload_image_with_all_params(self, client: Sam) -> None:
        pet = client.pets.upload_image(
            pet_id=0,
            body=b'raw file contents',
            additional_metadata="additionalMetadata",
        )
        assert_matches_type(APIResponse, pet, path=['response'])

    @parametrize
    def test_raw_response_upload_image(self, client: Sam) -> None:

        response = client.pets.with_raw_response.upload_image(
            pet_id=0,
            body=b'raw file contents',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = response.parse()
        assert_matches_type(APIResponse, pet, path=['response'])

    @parametrize
    def test_streaming_response_upload_image(self, client: Sam) -> None:
        with client.pets.with_streaming_response.upload_image(
            pet_id=0,
            body=b'raw file contents',
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = response.parse()
            assert_matches_type(APIResponse, pet, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncPets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.create(
            pet_id=0,
        )
        assert pet is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.create(
            pet_id=0,
            name="name",
            status="status",
        )
        assert pet is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSam) -> None:

        response = await async_client.pets.with_raw_response.create(
            pet_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = await response.parse()
        assert pet is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSam) -> None:
        async with async_client.pets.with_streaming_response.create(
            pet_id=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = await response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.retrieve(
            0,
        )
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSam) -> None:

        response = await async_client.pets.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSam) -> None:
        async with async_client.pets.with_streaming_response.retrieve(
            0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[{
                "id": 0,
                "name": "name",
            }, {
                "id": 0,
                "name": "name",
            }, {
                "id": 0,
                "name": "name",
            }],
        )
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSam) -> None:

        response = await async_client.pets.with_raw_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSam) -> None:
        async with async_client.pets.with_streaming_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.delete(
            pet_id=0,
        )
        assert pet is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.delete(
            pet_id=0,
            api_key="api_key",
        )
        assert pet is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSam) -> None:

        response = await async_client.pets.with_raw_response.delete(
            pet_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = await response.parse()
        assert pet is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSam) -> None:
        async with async_client.pets.with_streaming_response.delete(
            pet_id=0,
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = await response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_find_by_status(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.find_by_status()
        assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

    @parametrize
    async def test_method_find_by_status_with_all_params(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.find_by_status(
            status="available",
        )
        assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

    @parametrize
    async def test_raw_response_find_by_status(self, async_client: AsyncSam) -> None:

        response = await async_client.pets.with_raw_response.find_by_status()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = await response.parse()
        assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

    @parametrize
    async def test_streaming_response_find_by_status(self, async_client: AsyncSam) -> None:
        async with async_client.pets.with_streaming_response.find_by_status() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = await response.parse()
            assert_matches_type(PetFindByStatusResponse, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_find_by_tags(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.find_by_tags()
        assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

    @parametrize
    async def test_method_find_by_tags_with_all_params(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.find_by_tags(
            tags=["string", "string", "string"],
        )
        assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

    @parametrize
    async def test_raw_response_find_by_tags(self, async_client: AsyncSam) -> None:

        response = await async_client.pets.with_raw_response.find_by_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = await response.parse()
        assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

    @parametrize
    async def test_streaming_response_find_by_tags(self, async_client: AsyncSam) -> None:
        async with async_client.pets.with_streaming_response.find_by_tags() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = await response.parse()
            assert_matches_type(PetFindByTagsResponse, pet, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_image(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.upload_image(
            pet_id=0,
            body=b'raw file contents',
        )
        assert_matches_type(APIResponse, pet, path=['response'])

    @parametrize
    async def test_method_upload_image_with_all_params(self, async_client: AsyncSam) -> None:
        pet = await async_client.pets.upload_image(
            pet_id=0,
            body=b'raw file contents',
            additional_metadata="additionalMetadata",
        )
        assert_matches_type(APIResponse, pet, path=['response'])

    @parametrize
    async def test_raw_response_upload_image(self, async_client: AsyncSam) -> None:

        response = await async_client.pets.with_raw_response.upload_image(
            pet_id=0,
            body=b'raw file contents',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        pet = await response.parse()
        assert_matches_type(APIResponse, pet, path=['response'])

    @parametrize
    async def test_streaming_response_upload_image(self, async_client: AsyncSam) -> None:
        async with async_client.pets.with_streaming_response.upload_image(
            pet_id=0,
            body=b'raw file contents',
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            pet = await response.parse()
            assert_matches_type(APIResponse, pet, path=['response'])

        assert cast(Any, response.is_closed) is True
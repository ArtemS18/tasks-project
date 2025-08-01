from httpx import AsyncClient, Cookies
import pytest_asyncio

new_user = {
    "tg_id": 12121212,
    "name": "test_user_name",
    "login": "test_user_login@test.com",
    "password": "1234567890",
}


@pytest_asyncio.fixture(scope="function")
async def reg_client(client: AsyncClient):
    response = await client.post("/auth/reg", json=new_user)
    assert response.status_code == 200
    data = response.json()
    print(data)
    yield data.get("details")


@pytest_asyncio.fixture(scope="function")
async def auth_client(client: AsyncClient, reg_client) -> Cookies:
    response = await client.post(
        url="/auth/",
        data={"login": new_user["login"], "password": new_user["password"]},
    )
    assert response.status_code == 200
    return response.cookies

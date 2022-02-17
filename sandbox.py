import pytest
import requests


@pytest.fixture
def test_user():
    user_data = {
        "email": "test1@test.test",
        "username": "TestUser1",
        "password": "Test123!@#"
    }

    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/sign_up",
        json=user_data
    )
    assert response.status_code == 200

    yield user_data

    requests.post(
        url="http://31.178.216.240:8855/api/v1/debug/remove_user",
        json={"username": user_data["username"]}
    )


@pytest.fixture
def user_factory():
    users = []

    def factory(user_data):
        requests.post(
            url="http://31.178.216.240:8855/api/v1/sign_up",
            json=user_data
        )
        users.append(user_data)
        return user_data

    yield factory

    for user_data in users:
        requests.post(
            url="http://31.178.216.240:8855/api/v1/debug/remove_user",
            json={"username": user_data["username"]}
        )


def test_users(user_factory):
    user1 = user_factory(
        {
            "email": f"test1@test.test",
            "username": f"TestUser1",
            "password": "Test123!@#"
        }
    )
    user2 = user_factory(
        {
            "email": f"test2@test.test",
            "username": f"TestUser2",
            "password": "Test123!@#"
        }
    )

    x = 2


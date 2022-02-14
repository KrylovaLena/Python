import pytest
import requests


@pytest.fixture
def test_user():
    user_data = {
        "email": "test@test.test2",
        "username": "TestUser2",
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
def test_user_token(test_user):
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/login_web",
        json={
          "username": test_user["username"],
          "password": test_user["password"],
        }
    )

    yield response.json()["token_web"]


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

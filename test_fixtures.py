import requests


def test_create_user():
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/sign_up",
        json={
          "email": "test@test.test2",
          "username": "TestUser2",
          "password": "Test123!@#"
        }
    )

    assert response.status_code == 200

    requests.post(
        url="http://31.178.216.240:8855/api/v1/debug/remove_user",
        json={"username": "TestUser2"}
    )


def test_create_same_user(test_user):
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/sign_up",
        json=test_user,
    )

    assert response.status_code == 409


def test_logged_user(test_user_token):
    assert 1 == 1

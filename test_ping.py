import requests


def test_get_status_code_and_body():
    response = requests.get(
        url="http://31.178.216.240:8855/api/v1/ping",
    )

    resp_body = response.json()
    assert response.status_code == 200
    assert resp_body is True


def test_initial_post():
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json={
          "name": "string",
          "greeting_numbers": 1
        }
    )

    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body == {"greeting": "Hello, String!"}


def test_initial_post_2():
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json={
            "name": "test",
            "greeting_numbers": 1,
            "test_field": "some str"
        }
    )

    assert response.status_code == 400
    resp_body = response.json()
    expected_resp_body = {
        "errors": {
            "greeting_numbers": "'STR' is not of type 'integer'"
        },
        "message": "Input payload validation failed"
    }
    assert resp_body == expected_resp_body


def test_create_usert():
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

import pytest
import requests


def test_get_status_code_and_body():
    response = requests.get(
        url="http://31.178.216.240:8855/api/v1/ping",
    )

    resp_body = response.json()
    assert response.status_code == 200
    assert resp_body is True


def test_initial_post(ping_data_fixture):
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json=ping_data_fixture
    )

    assert response.status_code == 200
    resp_body = response.json()
    assert resp_body == {"greeting": "Hello, String!"}


def test_initial_post_2():
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json={
            "name": "test",
            "greeting_numbers": "1",
        }
    )

    assert response.status_code == 400


def test_initial_post_3():
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json={
            "name": "test",
        }
    )

    assert response.status_code == 400


def test_initial_post_empty_body():
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json={}
    )

    assert response.status_code == 400

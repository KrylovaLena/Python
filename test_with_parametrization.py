import pytest
import requests

from utils.text_utils import check_is_200


@pytest.fixture
def status_code_ok():
    return 200


@pytest.mark.parametrize(
    argnames=["name", "g_number"],
    argvalues=[
        ["name1", 1],
        ["name2", 5],
        ["valid name", 0],
    ],
    ids=["test_1", "using_5", "valid zero"]
)
def test_ping_post__invalid_params__400_response(name, g_number):
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json={
            "name": name,
            "greeting_numbers": g_number,
        }
    )

    assert response.status_code == 200


@pytest.mark.parametrize(
    argnames=["body", "code", "expected_response"],
    argvalues=[
        [{}, 400, {'errors': {'greeting_numbers': "'greeting_numbers' is a required property", 'name': "'name' is a required property"}, 'message': 'Input payload validation failed'}],
        [{"name": "test"}, 400, {'errors': {'greeting_numbers': "'greeting_numbers' is a required property"}, 'message': 'Input payload validation failed'}],
        [{"name": "test", "greeting_numbers": 1}, 200, {"greeting": "Hello, Test!"}]
    ],
    ids=[
        "empty body - 400",
        "missed g_nubers - 400",
        "correct data - 200"
    ]
)
def test_ping_post__invalid_params__400_response2(body, code, expected_response, status_code_ok, test_user_token):
    response = requests.post(
        url="http://31.178.216.240:8855/api/v1/ping",
        json=body,
    )

    if code == 200:
        assert response.status_code == status_code_ok
    else:
        assert response.status_code == code

    assert response.json() == expected_response

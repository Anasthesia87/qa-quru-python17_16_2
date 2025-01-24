import requests
from jsonschema import validate

from schemas import (get_single_user_schema, get_single_resource_schema,
                     create_user_schema, update_post_user_schema,
                     update_patch_user_schema, register_user_schema)


def test_api_list_users_status_code_200():
    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200


def test_api_list_users_response_not_empty():
    response = requests.get("https://reqres.in/api/users?page=2")
    data = response.json()
    assert len(data['data']) > 0


def test_api_single_user_status_code_200():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200


def test_api_single_user_status_code_404():
    response = requests.get("https://reqres.in/api/users/102")
    assert response.status_code == 404


def test_api_single_user_validate_response_schema():
    response = requests.get("https://reqres.in/api/users/2")
    body = response.json()
    validate(body, get_single_user_schema)


def test_api_single_user_not_found_status_code_404():
    response = requests.get("https://reqres.in/api/users/23")
    assert response.status_code == 404


def test_api_single_user_not_found_response_is_empty():
    response = requests.get("https://reqres.in/api/users/23")
    data = response.json()
    assert len(data) == 0


def test_api_list_resource_status_code_200():
    response = requests.get("https://reqres.in/api/unknown")
    assert response.status_code == 200


def test_api_list_resource_response_not_empty():
    response = requests.get("https://reqres.in/api/unknown")
    data = response.json()
    assert len(data['data']) > 0


def test_api_single_resource_status_code_200():
    response = requests.get("https://reqres.in/api/unknown/2")
    assert response.status_code == 200


def test_api_single_resource_response_not_empty():
    response = requests.get("https://reqres.in/api/unknown/2")
    data = response.json()
    assert len(data['data']) > 0


def test_api_single_resource_validate_response_schema():
    response = requests.get("https://reqres.in/api/unknown/2")
    body = response.json()
    validate(body, get_single_resource_schema)


def test_api_single_resource_not_found_status_code_404():
    response = requests.get("https://reqres.in/api/unknown/23")
    assert response.status_code == 404


def test_api_single_resource_response_is_empty():
    response = requests.get("https://reqres.in/api/unknown/23")
    data = response.json()
    assert len(data) == 0


def test_api_delayed_response_status_code_200():
    response = requests.get("https://reqres.in/api/users?delay=3")
    assert response.status_code == 200


def test_api_delayed_response_not_empty():
    response = requests.get("https://reqres.in/api/users?delay=3")
    data = response.json()
    assert len(data['data']) > 0


def test_api_create_user_status_code_200():
    response = requests.post("https://reqres.in/api/users",
                             data={"name": "morpheus", "job": "leader"})
    assert response.status_code == 201


def test_api_create_user_validate_response_schema():
    response = requests.post("https://reqres.in/api/users",
                             data={"name": "morpheus", "job": "leader"})
    body = response.json()
    validate(body, create_user_schema)


def test_api_create_user_attributes_match_expected_values():
    response = requests.post("https://reqres.in/api/users",
                             data={"name": "morpheus", "job": "leader"})
    data = response.json()
    assert data['name'] == 'morpheus'
    assert data['job'] == 'leader'


def test_api_post_update_user_status_code_200():
    response = requests.put("https://reqres.in/api/users/2",
                            data={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200


def test_api_post_update_user_validate_response_schema():
    response = requests.put("https://reqres.in/api/users/2",
                            data={"name": "morpheus", "job": "zion resident"})
    body = response.json()
    validate(body, update_post_user_schema)


def test_api_post_update_user_attribute_match_expected_value():
    response = requests.post("https://reqres.in/api/users/2",
                             data={"name": "morpheus", "job": "zion resident"})
    data = response.json()
    assert data['job'] == 'zion resident'


def test_api_patch_update_user_status_code_200():
    response = requests.patch("https://reqres.in/api/users/2",
                              data={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200


def test_api_patch_update_user_validate_response_schema():
    response = requests.patch("https://reqres.in/api/users/2",
                              data={"name": "morpheus", "job": "zion resident"})
    body = response.json()
    validate(body, update_patch_user_schema)


def test_api_patch_update_user_attribute_match_expected_value():
    response = requests.post("https://reqres.in/api/users/2",
                             data={"name": "morpheus", "job": "zion resident"})
    data = response.json()
    assert data['job'] == 'zion resident'


def test_api_delete_user_status_code_204():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204


def test_api_register_successful_status_code_200():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in", "password": "pistol"})
    assert response.status_code == 200


def test_api_register_successful_validate_response_schema():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in", "password": "pistol"})
    body = response.json()
    validate(body, register_user_schema)


def test_api_register_successful_attributes_match_expected_values():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in", "password": "pistol"})
    data = response.json()
    assert data['id'] == 4
    assert data['token'] == 'QpwL5tke4Pnpja7X4'


def test_api_register_unsuccessful_status_code_400():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "sydney@fife"})
    assert response.status_code == 400


def test_api_register_unsuccessful_response_not_empty():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "sydney@fife"})
    data = response.json()
    assert len(data) > 0


def test_api_login_successful_status_code_200():
    response = requests.post("https://reqres.in/api/login",
                             data={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    assert response.status_code == 200


def test_api_login_successful_attributes_match_expected_values():
    response = requests.post("https://reqres.in/api/login",
                             data={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    data = response.json()
    assert data['token'] == 'QpwL5tke4Pnpja7X4'


def test_api_login_unsuccessful_status_code_400():
    response = requests.post("https://reqres.in/api/login",
                             data={"email": "peter@klaven"})
    assert response.status_code == 400


def test_api_login_unsuccessful_response_not_empty():
    response = requests.post("https://reqres.in/api/login",
                             data={"email": "peter@klaven"})
    data = response.json()
    assert len(data) > 0

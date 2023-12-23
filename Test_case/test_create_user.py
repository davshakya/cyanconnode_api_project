import json
import requests
from DataBag.TestDataBag import TestData
import allure


@allure.severity(severity_level="Critical")
def test_create_user_from_excel_sheet(set_environment_variable):
    endpoint = TestData().get_endpoint_env("stag", 'create_user')
    payload = TestData().get_user_details_from_excel_file()[1]
    header = TestData().header_method()
    payload_json = json.dumps(payload)
    response = requests.request("POST", endpoint, headers=header, data=payload_json) # type: ignore
    res_dict = response.json()
    response_code = response.status_code
    assert response_code == 201, "User already exist"
    assert payload['email'] == res_dict["email"], "User has been created successfully"
    TestData().save_output_in_json_file(res_dict)


@allure.severity(severity_level="Critical")
def test_create_user_with_valid_values(set_environment_variable):
    endpoint = TestData().get_endpoint_env("stag", 'create_user')
    payload = TestData().payload_method()
    header = TestData().header_method()

    payload['id'] = '5818268'
    payload['name'] = 'ra__erma'
    payload['email'] = 'ddrrtyrdd@gmail.com'
    payload['gender'] = 'male'
    payload['status'] = 'active'
    payload_json = json.dumps(payload)
    response = requests.request("POST", endpoint, headers=header, data=payload_json)
    res_dict = response.json()
    response_code = response.status_code
    assert response_code == 201, "User already exist"
    assert payload['email'] == res_dict["email"], "User has been created successfully"
    TestData().save_output_in_json_file(res_dict)


@allure.severity(severity_level="Critical")
def test_create_user_with_invalid_values(set_environment_variable):
    endpoint = TestData().get_endpoint_env("stag", 'create_user')
    payload = TestData().payload_method()
    header = TestData().header_method()

    payload['id'] = '5818268'
    payload['name'] = ''
    payload['email'] = 'davshakya@gmail.com'
    payload['gender'] = 'tiger'
    payload['status'] = ''

    payload_json = json.dumps(payload)
    response = requests.request("POST", endpoint, headers=header, data=payload_json)
    response_code = response.status_code
    res_dict = response.json()
    assert response_code == 201, "Invalid input data"
    massage = res_dict[0]['message']
    assert massage == "can't be blank"
    assert payload['email'] == res_dict["email"], "User has been created successfully"
    TestData().save_output_in_json_file(res_dict)

import json
import requests
import allure
from DataBag.TestDataBag import TestData


@allure.severity(severity_level="Critical")
def test_get_user_with_valid_value_001(set_environment_variable):
    endpoint = TestData().get_endpoint_env("stag", 'get_details')
    payload = TestData().payload_method()
    header = TestData().header_method()
    input_data = {"email": "reev2@gmail.com"}
    payload_json = json.dumps(input_data)
    response = requests.request("GET", endpoint, headers=header, data=payload_json)
    res_dict = response.json()
    response_code = response.status_code
    assert response_code == 200
    assert input_data["email"] == res_dict[0]["email"], "User not available in database"
    TestData().save_output_in_json_file(res_dict)

@allure.severity(severity_level="Normal")
def test_get_user_with_invalid_value_002(set_environment_variable):
    endpoint = TestData().get_endpoint_env("stag", 'get_details')
    payload = TestData().payload_method()
    header = TestData().header_method()
    input_data = {"email": "dttsssev1@gmail.com"}
    payload_json = json.dumps(input_data)
    response = requests.request("GET", endpoint, headers=header, data=payload_json)
    res_dict = response.json()
    response_code = response.status_code
    assert response_code == 200
    assert input_data["email"] == res_dict[0]["email"], "User not available in database"
    TestData().save_output_in_json_file(res_dict)

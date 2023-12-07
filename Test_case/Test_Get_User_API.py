import json
import requests
import allure
from DataBag.TestDataBag import TestData


@allure.severity(severity_level="Critical")
def test_get_user_with_valid_value_001(set_environment_variable):
    env_status=TestData().validate_env("stag")
    assert env_status == True
    endpoint = TestData().endpoint_method()
    payload = TestData().payload_method()
    header = TestData().header_method()
    payload['id'] = ''
    payload['name'] = ''
    payload['email'] = 'davshakya@gmail.com'
    payload['gender'] = ''
    payload['status'] = ''
    payload_json = json.dumps(payload)
    response = requests.request("GET", endpoint, headers=header, data=payload_json)
    print(response.text)
    response_code = response.status_code
    assert response_code == 200


@allure.severity(severity_level="Normal")
def test_get_user_with_invalid_value_002(set_environment_variable):
    endpoint = TestData().endpoint_method()
    payload = TestData().payload_method()
    header = TestData().header_method()
    print("######## Payload #######", payload)
    payload['id'] = '123'
    payload['name'] = ''
    payload['email'] = 'asdf@werty'
    payload['gender'] = ''
    payload['status'] = ''
    payload_json = json.dumps(payload)
    response = requests.request("GET", endpoint, headers=header, data=payload_json)
    print(response.text)
    response_code = response.status_code
    assert response_code == 200

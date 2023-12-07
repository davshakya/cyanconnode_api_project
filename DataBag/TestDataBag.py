import json


class TestData:
    def endpoint_method(self):
        endpoint_file = open("D:\\Dev_Progs\\RestAPI_project1\\Test_endpoints\\endpoint.json", "r").read()
        end_dict = json.loads(endpoint_file)
        url = end_dict['endpoint']
        return url

    def payload_method(self):
        payload_file = open("D:\\Dev_Progs\\RestAPI_Project1\\Test_Payload\\payload_request.json", "r").read()
        payload = json.loads(payload_file)
        return payload

    def header_method(self):
        header_file = open("D:\\Dev_Progs\\RestAPI_Project1\\Test_endpoints\\header_file.json", "r").read()
        header = json.loads(header_file)
        return header

    def validate_env(self,set_environment_variable):
        env_value = set_environment_variable
        print(f"Running tests with environment variable: {env_value}")
        if  env_value in ["stag", "prod"]:
            return  True
        else:
            return False




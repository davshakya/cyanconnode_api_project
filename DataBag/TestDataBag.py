import json
import pandas as pd


class TestData:
    def endpoint_method_stage(self, env, request_method):
        endpoint_file = open("D:/Dev_Progs/cyanconnode_api_project/Test_endpoints/endpoint.json", "r").read()
        if env == "stag" and request_method == "get_details":
            end_dict = json.loads(endpoint_file)
            url = end_dict["endpoint_stage"] + "/" + end_dict["get_user_detail_param"]
            return url

        elif env == "stag" and request_method == "create_user":
            end_dict = json.loads(endpoint_file)
            url = end_dict["endpoint_stage"] + "/" + end_dict["create_user_param"]
            return url

        elif env == "prod" and request_method == "get_details":
            end_dict = json.loads(endpoint_file)
            url = end_dict["endpoint_stage"] + "/" + end_dict["create_user_param"]
            return url

        elif env == "prod" and request_method == "create_user":
            end_dict = json.loads(endpoint_file)
            url = end_dict["endpoint_stage"] + "/" + end_dict["create_user_param"]
            return url

    def payload_method(self):
        payload_file = open("D:/Dev_Progs/cyanconnode_api_project/Test_Payload/payload_request.json", "r").read()
        payload = json.loads(payload_file)
        return payload

    def header_method(self):
        header_file = open("D:\\Dev_Progs\\RestAPI_Project1\\Test_endpoints\\header_file.json", "r").read()
        header = json.loads(header_file)
        return header

    def get_endpoint_env(self, set_environment_variable, request_method):
        env_value = set_environment_variable
        print(f"Running tests with environment variable: {env_value}")
        return self.endpoint_method_stage(env_value, request_method)

    def save_output_in_json_file(self, dict_object):
        with open("my_json.json", 'r+') as json_file:
            file_data = json.load(json_file)
            file_data["user_details"].append(dict_object)
            json_file.seek(0)
            json.dump(file_data, json_file, indent=4)

    def get_user_details_from_excel_file(self):
        excel_data = pd.read_excel("D:/Dev_Progs/cyanconnode_api_project/DataBag/test_xlx.xlsx")
        list_of_dict = excel_data.to_dict(orient="records")
        return list_of_dict

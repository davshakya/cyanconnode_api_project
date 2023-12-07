import pytest
import os
import shutil
import json


@pytest.fixture
def set_environment_variable(request):
    # Get the value from a command-line option or some other source
    env_value = request.config.getoption("--environment")
    # Set the environment variable
    os.environ["MY_ENV_VARIABLE"] = env_value
    # Yield the environment value to the test
    yield env_value
    # Optionally, clean up after the test by unsetting the environment variable
    del os.environ["MY_ENV_VARIABLE"]


# Command-line option to set the environment
def pytest_addoption(parser):
    create_output_json_file()
    remove_unused_files_dir()
    parser.addoption("--environment", action="store", default="stag", help="Specify the test environment")


def remove_unused_files_dir():
    directory_path = 'D:/Dev_Progs/cyanconnode_api_project/report'
    cache_file1 = 'D:/Dev_Progs/cyanconnode_api_project/.pytest_cache'
    cache_file2 = 'D:/Dev_Progs/cyanconnode_api_project/Test_case/.pytest_cache'
    test_cache = 'D:/Dev_Progs/cyanconnode_api_project/Test_case/__pycache__'

    try:
        shutil.rmtree(directory_path)
        shutil.rmtree(cache_file1)
        shutil.rmtree(cache_file2)
        shutil.rmtree(test_cache)
        print(f"The directory {directory_path} has been deleted.")
    except:
        print(f"The directory {directory_path} does not exist.")


def remove_output_file_dir():
    output_file = "D:/Dev_Progs/cyanconnode_api_project/Test_case/my_json.json"
    try:
        os.remove(output_file)
        print(f"The directory {output_file} has been deleted.")
    except:
        print(f"The directory {output_file} does not exist.")


def create_output_json_file():
    # remove_output_file_dir()
    dictionary = {"user_details": [{"id": 5818968, "name": "Dev shakya", "email": "devshakya@hoeger-schiller.test", "gender": "male","status": "active"}]}
    json_object = json.dumps(dictionary, indent=4)
    with open("D:/Dev_Progs/cyanconnode_api_project/Test_case/my_json.json", "w+") as outfile:
        outfile.write(json_object)

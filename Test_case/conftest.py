import pytest
import os
import shutil




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
    remove_unused_files_dir()
    parser.addoption("--environment", action="store", default="stag", help="Specify the test environment")


def remove_unused_files_dir():
    directory_path = 'D:/Dev_Progs/cyanconnode_api_project/report'
    cache_file='D:/Dev_Progs/cyanconnode_api_project/.pytest_cache'
    try:
        shutil.rmtree(directory_path)
        shutil.rmtree(cache_file)
        print(f"The directory {directory_path} has been deleted.")
    except:
        print(f"The directory {directory_path} does not exist.")

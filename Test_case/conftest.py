import pytest
import os


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
    parser.addoption("--environment", action="store", default="stag", help="Specify the test environment")

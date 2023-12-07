# import sys
#
# import pytest
#
#
# @pytest.fixture()
# def setup_env(environment):
#     valid_environments = ["development", "staging", "production"]
#     if environment not in valid_environments:
#         print("Invalid environment. Please choose from:", valid_environments)
#         sys.exit(1)
#     else:
#         print(f"Running tests in {environment} environment")
#
#
#
#
#
#
#
# # Check if a command-line argument is provided for the environment
# # if len(sys.argv) != 2:
# #     print("Usage: python test_script.py <environment>")
# #     sys.exit(1)
#
# # Get the environment from the command-line argument
# # environment = sys.argv[1].lower()
#
# # Validate the environment
# # valid_environments = ["development", "staging", "production"]
# # if environment not in valid_environments:
# #     print("Invalid environment. Please choose from:", valid_environments)
# #     sys.exit(1)
#
# # Run tests with the specified environment
# # perform_tests(environment)
# # set_environment(method,environment)
#
# # @set_environment
# # def testCase(*args):
# #     a=3
# #     return a
#
# # testCase("development")

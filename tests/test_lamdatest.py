import allure

import pytest

from utils.file_utils import read_data_file


@allure.suite("Lambdatest API tests")
@allure.title("JSON to YAML conversion")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-yaml")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    This test case verifies that the API endpoint "Extract Text from JSON" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from JSON via API.
    3. Compare expected and actual text.
""")
@pytest.mark.parametrize("file_name", ["1", "1"])
def test_json_to_yaml_conversion(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_yaml = read_data_file(f"yaml/{file_name}.yml")

    with allure.step("Convert JSON to YAML via API"):
        actual_yaml = lambdatest_service.json_to_yaml(input_json)

    with allure.step("Compare expected and actual YAML"):
        assert actual_yaml == expected_yaml


@allure.suite("Lambdatest API tests")
@allure.title("XML to YAML conversion")
@allure.link("https://www.lambdatest.com/free-online-tools/xml-to-yaml")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    This test case verifies that the API endpoint "Extract Text from XML" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from XML via API.
    3. Compare expected and actual text.
""")
@pytest.mark.parametrize("file_name", ["2", "2"])
def test_xml_to_yaml_conversion(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_xml = read_data_file(f"xml/{file_name}.xml")
        expected_yaml = read_data_file(f"yaml/{file_name}.yml")

    with allure.step("Convert XML to YAML via API"):
        actual_yaml = lambdatest_service.xml_to_yaml(input_xml)

    with allure.step("Compare expected and actual YAML"):
        assert actual_yaml == expected_yaml


@allure.suite("Lambdatest API tests")
@allure.title("YAML to JSON conversion")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-to-json")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    This test case verifies that the API endpoint "Extract Text from YAML" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from YAML via API.
    3. Compare expected and actual text.
""")
@pytest.mark.parametrize("file_name", ["2", "2"])
def test_yaml_to_json_conversion(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yml")
        expected_json = read_data_file(f"json/{file_name}.json")

    with allure.step("Convert YAML to JSON via API"):
        actual_json = lambdatest_service.yaml_to_json(input_yaml)

    with allure.step("Compare expected and actual YAML"):
        assert actual_json == expected_json

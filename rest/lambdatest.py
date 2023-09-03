import allure

import requests

from utils.converters import dict_to_json


class LambdatestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    @allure.step("Send a POST request to {endpoint}")
    def _send_request(self, endpoint, input_key, input_str):
        url = self.BASE_URL + endpoint
        allure.attach(url, "Full URL", allure.attachment_type.TEXT)
        response = requests.post(url, data={input_key: input_str})
        allure.attach(response.text, "Response Text", allure.attachment_type.TEXT)

        return response

    @allure.step("Send a POST request to convert JSON to YAML")
    def json_to_yaml(self, input_str: str) -> str:
        response = self._send_request("json-to-yaml", "json-str", input_str).json()["data"]
        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)
        return response

    @allure.step("Send a POST request to convert XML to YAML")
    def xml_to_yaml(self, input_str: str) -> str:
        response = self._send_request("xml-to-yaml", "xml-str", input_str).json()["data"]
        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response, "Output YAML", allure.attachment_type.YAML)
        return response

    @allure.step("Send a POST request to convert YAML to JSON")
    def yaml_to_json(self, input_str: str) -> str:
        response = self._send_request("yaml-to-json", "yaml-str", input_str).json()["data"]
        output_response = dict_to_json(response)
        allure.attach(input_str, "Input YAML", allure.attachment_type.YAML)
        allure.attach(output_response, "Output JSON", allure.attachment_type.JSON)
        return output_response

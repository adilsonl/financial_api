import unittest
import json
from app import web_app


class TestePoints(unittest.TestCase):
    def setUp(self):
        self.client = web_app.test_client()

    def test_get_status_code_200_ibovespa(self):
        response = self.client.get("/ibovespa")
        self.assertEqual(200, response.status_code)

    def test_get_json_format_ibovespa(self):
        response = self.client.get("/ibovespa")
        self.assertEqual("application/json", response.content_type)

    def test_get_status_code_200_companies(self):
        response = self.client.get("/points/<string:company>")
        self.assertEqual(200, response.status_code)

    def test_get_json_format_companies(self):
        response = self.client.get("/points/<string:company>")
        self.assertEqual("application/json", response.content_type)

    def test_get_error_msg_invalid_company(self):
        response = self.client.get("/points/companyWrong")
        self.assertEqual("Inform a valid company", json.loads(response.data)["error"])

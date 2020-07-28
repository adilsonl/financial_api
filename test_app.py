from unittest import TestCase, mock
import json
from app import web_app


class TestePoints(TestCase):
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

    @mock.patch("app.create_user")
    def test_post_create_user_is_called(self, mock_db):
        user = {"user_name": "Joao", "company": "IBM", "password": "3432"}
        response = self.client.post("/user", json=user)
        mock_db.assert_called()

    @mock.patch("app.create_user")
    def test_post_create_response_json_format(self, mock_db):
        user = {"user_name": "Joao", "company": "IBM", "password": "3432"}
        response = self.client.post("/user", json=user)
        self.assertEqual("application/json", response.content_type)

    @mock.patch("app.create_price")
    def test_post_create_price_is_called(self, mock_db):
        price = {"id_company": 1, "price": 15.3}
        response = self.client.post("/price", json=price)
        mock_db.assert_called()

    @mock.patch("app.create_user")
    def test_post_create_response_json_format(self, mock_db):
        price = {"id_company": 1, "price": 15.3}
        response = self.client.post("/user", json=price)
        self.assertEqual("application/json", response.content_type)

    @mock.patch("app.create_company")
    def test_post_create_company_is_called(self, mock_db):
        company = {"name": "IBM", "symbol": "IBM"}
        response = self.client.post("/company", json=company)
        mock_db.assert_called()

    @mock.patch("app.create_company")
    def test_post_create_response_json_format(self, mock_db):
        company = {"name": "IBM", "symbol": "IBM"}
        response = self.client.post("/company", json=company)
        self.assertEqual("application/json", response.content_type)

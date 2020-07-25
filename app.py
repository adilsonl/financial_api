from flask import Flask, request
from flask_restful import Resource, Api
import requests

web_app = Flask("web_app")
api = Api(web_app)

API_KEY = 'NW84PZQEPS9SN9S7'


class PointsIbovespa(Resource):
    def get(self):
        points = searchCompaniesPoints()
        return points


class CompanyPoints(Resource):
    def get(self, company):
        points = searchCompaniesPoints(company)
        return points


def searchCompaniesPoints(company="BOVA11.SAO"):
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(company, API_KEY)
    callApi = requests.get(url)
    if callApi.status_code == 200:
        response = callApi.json()
        if 'Global Quote' in response and "05. price" in response["Global Quote"]:
            points = {
                "status": callApi.status_code,
                "points": response["Global Quote"]["05. price"]
            }
            return points
        else:
            return {"status": callApi.status_code,
                    'error': 'Inform a valid company'}
    else:
        return {
            "status": callApi.status_code,
            'error': 'Something went wrong'}


api.add_resource(PointsIbovespa, "/ibovespa")
api.add_resource(CompanyPoints, "/points/<string:company>")
if __name__ == "__main__":
    web_app.run(debug=True)

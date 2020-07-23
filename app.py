from flask import Flask,request
from flask_restful import Resource,Api
import requests

app = Flask(__name__)
api = Api(app)

API_KEY='NW84PZQEPS9SN9S7'


class PointsIbovespa(Resource):
    def get(self):
        points = searchCompaniesPoints()
        return points

class CompanyPoints(Resource):
    def get(self,company):
        points = searchCompaniesPoints(company)
        return points

def searchCompaniesPoints(company="BOVA11.SAO"):
    url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}".format(company,API_KEY)
    callApi = requests.get(url)
    response = callApi.json()
    points = {
        "status": callApi.status_code,
        "points": response["Global Quote"]["05. price"]
    }
    return points

api.add_resource(PointsIbovespa,"/points/ibovespa")
api.add_resource(CompanyPoints,"/points/<company>")
if __name__ == "__main__":
    app.run(debug=True)
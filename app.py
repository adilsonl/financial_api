from flask import Flask,request
from flask_restful import Resource,Api
import requests

app = Flask(__name__)
api = Api(app)

API_KEY='NW84PZQEPS9SN9S7'


class PointsIbovespa(Resource):
    def get(self):
        url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=BOVA11.SAO&apikey={}".format(API_KEY)
        callApi = requests.get(url)
        response = callApi.json()
        points ={
            "status":callApi.status_code,
            "points" : response["Global Quote"]["05. price"]
        }
        return points

api.add_resource(PointsIbovespa,"/points/ibovespa")

if __name__ == "__main__":
    app.run(debug=True)
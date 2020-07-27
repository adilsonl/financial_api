from flask import Flask
from flask_restful import Resource, Api
import requests
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


web_app = Flask("web_app")
web_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123Senha@localhost:5432/bank_api"
web_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(web_app)
migrate = Migrate(web_app, db)
CORS(web_app)
api = Api(web_app)

from models import price, company, user
from resources.user_r import  UserAddGetAll,UserRoutes
from resources.company_r import CompanyAddGetAll,CompanyRoutes
from resources.price_r import PriceAddGetAll,PriceRoutes


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
    call_api = requests.get(url)
    if call_api.status_code == 200:
        response = call_api.json()
        if 'Global Quote' in response and "05. price" in response["Global Quote"]:
            points = {
                "status": call_api.status_code,
                "points": response["Global Quote"]["05. price"]
            }
            return points
        else:
            return {"status": call_api.status_code,
                    'error': 'Inform a valid company'}
    else:
        return {
            "status": call_api.status_code,
            'error': 'Something went wrong'}


api.add_resource(PointsIbovespa, "/ibovespa")
api.add_resource(CompanyPoints, "/points/<string:company>")
api.add_resource(UserAddGetAll,"/user")
api.add_resource(UserRoutes,"/user/<int:id>")
api.add_resource(CompanyAddGetAll,"/company")
api.add_resource(CompanyRoutes,"/company/<int:id>")
#api.add_resource(PriceAddGetAll,"/price")
#api.add_resource(PriceRoutes,"/price/<int:id>")
if __name__ == "__main__":
    web_app.run(debug=True)

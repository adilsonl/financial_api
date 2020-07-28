from flask import Flask, request
from flask_restful import Resource, Api
import requests
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

web_app = Flask("web_app")
web_app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:123Senha@localhost:5432/database_api"
web_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(web_app)
migrate = Migrate(web_app, db)
CORS(web_app)
api = Api(web_app)

from models import price, company, user


API_KEY = "NW84PZQEPS9SN9S7"

# ------------Functions----------#


def create_user(data):
    try:
        new_user = user.User(data["user_name"], data["company"], data["password"])
        db.session.add(new_user)
        db.session.commit()
        return {"message": f"user {new_user.user_name} has been created successfully."}
    except Exception as e:
        print(e)
        return {"message": "Error :"}


def create_company(data):
    try:
        new_company = company.Company(data["name"], data["symbol"])
        db.session.add(new_company)
        db.session.commit()
        return {"message": f"Company {new_company.name} has been created successfully."}
    except Exception as e:
        print(e)
        return {"message": "Error :"}


def create_price(data):
    try:
        new_price = price.Price(data["id_company"], data["price"])
        db.session.add(new_price)
        db.session.commit()
        return {"message": f"Price {new_price.price} has been created successfully."}
    except Exception as e:
        print(e)
        return {"message": "Error :"}


def search_companies_points(company="BOVA11.SAO"):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={company}&apikey={API_KEY}"
    call_api = requests.get(url)
    if call_api.status_code == 200:
        response = call_api.json()
        if "Global Quote" in response and "05. price" in response["Global Quote"]:
            points = {
                "status": call_api.status_code,
                "points": response["Global Quote"]["05. price"],
            }
            return points
        else:
            return {"status": call_api.status_code, "error": "Inform a valid company"}
    else:
        return {"status": call_api.status_code, "error": "Something went wrong"}


# ------------Functions----------#

# ---------Classes-------------#
class PointsIbovespa(Resource):
    def get(self):
        points = search_companies_points()
        return points


class CompanyPoints(Resource):
    def get(self, company):
        points = search_companies_points(company)
        return points


class PriceAddGetAll(Resource):
    def post(self):
        data = json.loads(request.data)
        if "id_company" in data and "price" in data:
            response = create_price(data)
            return response
        else:
            return {"message": "error missing arguments"}

    def get(self):
        try:
            prices = price.Price.query.all()
            results = [price_.serialize() for price_ in prices]
            return {"count": len(results), "Prices": results, "message": "success"}
        except Exception as e:
            print(e)
            return {"message": "Error :"}


class PriceRoutes(Resource):
    def get(self, id):
        try:
            price_ = price.Price.query.filter_by(id=id).first()
            return price_.serialize()
        except Exception as e:
            print(e)
            return {"message": "Error "}

    def put(self, id):
        try:
            data = json.loads(request.data)
            price_ = price.Price.query.filter_by(id=id).first()
            price_.id_company = data["id_company"]
            price_.price = data["price"]
            price_.save()
            return {"message": f"Price  {price_.price} successfully updated"}
        except Exception as e:
            print(e)
            return {"message": "Error "}

    def delete(self, id):
        try:
            price_ = price.Price.query.filter_by(id=id).first()
            price_.delete()
            return {"message": f"Price  {price_.price} successfully deleted."}

        except Exception as e:
            print(e)
            return {"message": "Error "}


class CompanyAddGetAll(Resource):
    def post(self):
        data = json.loads(request.data)
        if "name" in data and "symbol" in data:
            response = create_company(data)
            return response
        else:
            return {"message": "error missing arguments"}

    def get(self):
        try:
            companies = company.Company.query.all()
            results = [company_.serialize() for company_ in companies]
            return {"count": len(results), "Companyes": results, "message": "success"}
        except Exception as e:
            print(e)
            return {"message": "Error :"}


class CompanyRoutes(Resource):
    def get(self, id):
        try:
            company_ = company.Company.query.filter_by(id=id).first()
            return company_.serialize()
        except Exception as e:
            print(e)
            return {"message": "Error "}

    def put(self, id):
        try:
            data = json.loads(request.data)
            company_ = company.Company.query.filter_by(id=id).first()
            company_.name = data["name"]
            company_.symbol = data["symbol"]
            company_.save()
            return {"message": f"Company {company_.name} successfully updated"}
        except Exception as e:
            print(e)
            return {"message": "Error "}

    def delete(self, id):
        try:
            company_ = company.Company.query.filter_by(id=id).first()
            company_.delete()
            return {"message": f"Company {company_.name} successfully deleted."}

        except Exception as e:
            print(e)
            return {"message": "Error "}


class UserAddGetAll(Resource):
    def post(self):
        data = json.loads(request.data)
        if "user_name" in data and "company" in data and "password" in data:
            response = create_user(data)
            return response
        else:
            return {"message": "error missing arguments"}

    def get(self):
        try:
            users = user.User.query.all()
            results = [user_.serialize_without_password() for user_ in users]
            return {"count": len(results), "users": results, "message": "success"}
        except Exception as e:
            print(e)
            return {"message": "Error :"}


class UserRoutes(Resource):
    def get(self, id):
        try:
            user_ = user.User.query.filter_by(id=id).first()
            return user_.serialize_without_password()
        except Exception as e:
            print(e)
            return {"message": "Error "}

    def put(self, id):
        try:
            data = json.loads(request.data)
            user_ = user.User.query.filter_by(id=id).first()
            user_.user_name = data["user_name"]
            user_.company = data["company"]
            user_.password = data["password"]
            user_.save()
            return {"message": f"user {user_.user_name} successfully updated"}
        except Exception as e:
            print(e)
            return {"message": "Error "}

    def delete(self, id):
        try:
            user_ = user.User.query.filter_by(id=id).first()
            user_.delete()
            return {"message": f"User {user_.user_name} successfully deleted."}

        except Exception as e:
            print(e)
            return {"message": "Error "}


# ---------Classes-------------#


# ----------- Resources ----------
api.add_resource(PointsIbovespa, "/ibovespa")
api.add_resource(CompanyPoints, "/points/<string:company>")
api.add_resource(UserAddGetAll, "/user")
api.add_resource(UserRoutes, "/user/<int:id>")
api.add_resource(CompanyAddGetAll, "/company")
api.add_resource(CompanyRoutes, "/company/<int:id>")
api.add_resource(PriceAddGetAll, "/price")
api.add_resource(PriceRoutes, "/price/<int:id>")
# ----------- Resources ----------
if __name__ == "__main__":
    web_app.run(debug=True)

from flask_restful import Resource
from flask import request
from models.price import Price
import json
from app import db


class PriceAddGetAll(Resource):
    def post(self):
        try:
            data = json.loads(request.data)
            new_price = Price(data["id_company"], data["price"])
            db.session.add(new_price)
            db.session.commit()
            return {"message": f"Price {new_price.name} has been created successfully."}
        except Exception as e:
            return {"message": "Error :"}

    def get(self):
        prices = Price.query.all()
        results = [price.serialize() for price in prices]
        return {"count": len(results), "Prices": results, "message": "success"}


class PriceRoutes(Resource):
    def get(self, id):
        try:
            price = Price.query.filter_by(id=id).first()
            return price.serialize()
        except Exception as e:
            return {"message": "Error "}

    def put(self, id):
        try:
            data = json.loads(request.data)
            price = Price.query.filter_by(id=id).first()
            price.id_company = data["id_company"]
            price.price = data["price"]
            db.session.commit()
            return {"message": f"Price  {price.price} successfully updated"}
        except Exception as e:
            return {"message": "Error "}

    def delete(self, id):
        try:
            price = Price.query.filter_by(id=id).first()
            db.session.delete(price)
            db.session.commit()
            return {"message": f"Price  {price.price} successfully deleted."}

        except Exception as e:
            return {"message": "Error "}

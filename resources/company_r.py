from flask_restful import Resource
from flask import request
from models.company import Company
import json
from app import db

class CompanyAddGetAll(Resource):
    def post(self):
        try:
            data = json.loads(request.data)
            new_company = Company(data['name'], data['symbol'])
            db.session.add(new_company)
            db.session.commit()
            return {"message": f"Company {new_company.name} has been created successfully."}
        except Exception as e:
            return {"message":"Error :"}

    def get(self):
        companies = Company.query.all()
        results = [company.serialize() for company in companies]
        return {"count": len(results), "Companyes": results, "message": "success"}


class CompanyRoutes(Resource):
    def get(self,id):
        try:
            company = Company.query.filter_by(id=id).first()
            return  company.serialize()
        except Exception as e:
            return {"message": "Error "}

    def put(self,id):
        try:
            data = json.loads(request.data)
            company = Company.query.filter_by(id=id).first()
            company.name = data['name']
            company.symbol = data['symbol']
            db.session.commit()
            return {"message": f"Company {company.name} successfully updated"}
        except Exception as e:
            return {"message": "Error "}

    def delete(self,id):
        try:
            company = Company.query.filter_by(id=id).first()
            db.session.delete(company)
            db.session.commit()
            return {"message": f"Company {company.name} successfully deleted."}

        except Exception as e:
            return {"message": "Error "}
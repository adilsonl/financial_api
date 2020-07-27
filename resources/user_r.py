from flask_restful import Resource
from flask import request
from models.user import User
import json
from app import db


class UserAddGetAll(Resource):
    def post(self):
        try:
            data = json.loads(request.data)
            new_user = User(data['user_name'], data['company'], data['password'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.user_name} has been created successfully."}
        except Exception as e:
            return {"message":"Error :"}

    def get(self):
        users = User.query.all()
        results = [user.serialize_without_password() for user in users]
        return {"count": len(results), "users": results, "message": "success"}


class UserRoutes(Resource):
    def get(self,id):
        try:
            user = User.query.filter_by(id=id).first()
            return  user.serialize_without_password()
        except Exception as e:
            return {"message": "Error "}

    def put(self,id):
        try:
            data = json.loads(request.data)
            user = User.query.filter_by(id=id).first()
            user.user_name = data['user_name']
            user.company = data['company']
            user.password = data['password']
            db.session.commit()
            return {"message": f"user {user.user_name} successfully updated"}
        except Exception as e:
            return {"message": "Error "}

    def delete(self,id):
        try:
            user = User.query.filter_by(id=id).first()
            db.session.delete(user)
            db.session.commit()
            return {"message": f"User {user.user_name} successfully deleted."}

        except Exception as e:
            return {"message": "Error "}




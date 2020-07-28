from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    company = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, user_name, company, password):
        self.user_name = user_name
        self.company = company
        self.password = password

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize_with_password(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "company": self.company,
            "password": self.password,
        }

    def serialize_without_password(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "company": self.company,
        }

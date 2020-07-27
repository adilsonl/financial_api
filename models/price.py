from app import db


class Price(db.Model):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    id_company = db.Column(db.Integer)
    price = db.Column(db.Float())

    def __init__(self,id_company,price):
        self.id_company = id_company
        self.price = price

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'id_company': self.id_company,
            'price': self.price
        }
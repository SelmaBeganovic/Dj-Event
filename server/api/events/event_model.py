from api import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    venue = db.Column(db.String(128))
    address = db.Column(db.String(128))


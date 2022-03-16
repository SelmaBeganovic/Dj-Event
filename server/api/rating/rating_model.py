import datetime
from xmlrpc.client import DateTime
from api import db
import datetime



class Rating(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.datetime.now())
    event_id= db.Column(
        db.Integer, db.ForeignKey("event.id"), index=True, nullable=False
    )
    event = db.relationship("Event", uselist=False, backref=db.backref("rating"))
    user_id= db.Column(
        db.Integer, db.ForeignKey("user.id"), index=True, nullable=False
    )
    user = db.relationship("User", uselist=False, backref=db.backref("rating"))


    @property
    def serialize(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "created_at":self.created_at,
        }
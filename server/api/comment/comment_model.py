import datetime
from xmlrpc.client import DateTime
from api import db
import datetime

class Comment(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    comment = db.Column(db.String(250))
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.datetime.now())
    event_id= db.Column(
        db.Integer, db.ForeignKey("event.id"), index=True, nullable=False
    )
    #comment = db.relationship("Comment", uselist=False, backref=db.backref("event"))
    

    def __str__(self):
        return f"{self.name} {self.date}"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "comment":self.comment,
            "created_at":self.created_at,
        }
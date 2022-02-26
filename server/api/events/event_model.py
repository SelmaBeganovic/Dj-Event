from api import db
from api.events.event_util import create_image_url


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    venue = db.Column(db.String(128))
    address = db.Column(db.String(128))
    slug = db.Column(db.String(128))
    performers = db.Column(db.String(128))
    date = db.Column(db.Date())
    time = db.Column(db.String(20))
    description = db.Column(db.String(250))
    image = db.Column(db.String(250))
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), index=True, nullable=False
    )
    user = db.relationship("User", uselist=False, backref=db.backref("events"))

    def __str__(self):
        return f"{self.name} {self.date}"

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "venue": self.venue,
            "address": self.address,
            "slug": self.slug,
            "performers": self.performers,
            "date": self.date,
            "time": self.time,
            "description": self.description,
            "image": create_image_url(self.image),
        }

from api import db


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

    def __str__(self):
        return f"{self.name} {self.date}"

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'time': self.time,
            'slug': self.slug
        }
